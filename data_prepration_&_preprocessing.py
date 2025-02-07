import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

import joblib

# Load data
df = pd.read_csv("student mental health.csv")

# Data Cleaning
# Drop unnecessary columns
df = df.drop(columns=['Timestamp'])

# Clean column names (remove spaces)
df.columns = df.columns.str.strip()

# Handle categorical columns
# Gender encoding (assuming binary for simplicity)
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender'] = df['Gender'].map({'male': 0, 'female': 1, 'm': 0, 'f': 1}).fillna(2)

# Simplify course categories
top_courses = df['course'].value_counts().head(5).index
df['course'] = df['course'].apply(lambda x: x if x in top_courses else 'Other')

# Handle 'year of Study' column
df['year of Study'] = df['year of Study'].astype(str).str.strip()

df['year of Study'] = pd.to_numeric(df['year of Study'], errors='coerce')

mode_value = df['year of Study'].mode()

if not mode_value.empty:
    df['year of Study'].fillna(mode_value[0], inplace=True)
else:
    df['year of Study'].fillna(1, inplace=True)

df['year of Study'] = df['year of Study'].astype(int)



# CGPA cleaning
df['CGPA?'] = df['CGPA?'].str.strip().replace({'3.50 - 4.00': '3.75', '2.50 - 3.49': '3.0', 
                                             '1.50 - 2.49': '2.0', '0.00 - 1.49': '1.0'})
df['CGPA?'] = pd.to_numeric(df['CGPA?'], errors='coerce')

# Marital status encoding
df['Marital status'] = LabelEncoder().fit_transform(df['Marital status'])

df = df.dropna()

targets = ['Depression', 'Anxiety', 'Panic attack']
for t in targets:
    df[t] = df[t].str.strip().map({'Yes': 1, 'No': 0})

# Feature engineering
X = pd.get_dummies(df[['Gender', 'Age', 'course', 'year of Study', 
                      'CGPA?', 'Marital status']])
y = df[targets]
# Save training columns for inference
joblib.dump(X.columns.tolist(), 'train_columns.pkl')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Model Development & Evaluation
# Train separate binary classifiers for each target
models = {}
for idx, target in enumerate(targets):
    print(f"\nTraining model for {target}")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train[target])
    
    
    preds = model.predict(X_test_scaled)
    print(classification_report(y_test[target], preds))
    
    
    models[target] = model

# Save models

joblib.dump(models, 'mental_health_models.pkl')
joblib.dump(scaler, 'scaler.pkl')