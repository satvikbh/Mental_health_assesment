# 🎓 Student Mental Health Assessment 🧠💙

An interactive **machine learning-based** web application designed to provide **preliminary mental health assessments** for students. The tool processes raw survey data, trains models for **Depression, Anxiety, and Panic Attacks**, and provides **an easy-to-use interface** with insights and recommendations.

> ⚠️ **Disclaimer:** This tool is NOT a diagnostic application. It is a **screening tool** meant to encourage consultation with mental health professionals.

---

## 📌 Table of Contents

- [🌟 Features](#-features)
- [🚀 Installation](#-installation)
- [🛠️ Usage](#️-usage)
  - [🔄 Data Preprocessing & Model Training](#-data-preprocessing--model-training)
  - [🎭 Running the Streamlit App](#-running-the-streamlit-app)
- [📊 Results & Improvements](#-results--improvements)
- [📜 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 🌟 Features

✅ **Data Preprocessing:** Cleans, encodes, and standardizes raw student mental health data.  
✅ **Machine Learning Models:** Trains **RandomForest classifiers** for predicting mental health conditions.  
✅ **Interactive Web App:** Uses **Streamlit** to provide a user-friendly UI for mental health assessment.  
✅ **Explainability:** Displays **interpretable outputs** and basic reasoning for predictions.  
✅ **Scalability & Modularity:** Well-structured code for **easy maintenance and updates**.  

---
##🚀 Installation
1️⃣ Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/student-mental-health-assessment.git
cd student-mental-health-assessment

2️⃣ (Optional) Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3️⃣ Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt


##🛠️ Usage
🔄 Data Preprocessing & Model Training

1️⃣ Ensure the dataset (student_mental_health.csv) is available in the data/ folder.

2️⃣ Run the preprocessing and training script:

bash
Copy
Edit
python model_preprocessing.py
🔹 This script will:

Load and clean the dataset
Encode categorical features
Train RandomForest models for Depression, Anxiety, and Panic Attacks
Save models, scalers, and training columns

##🎭 Running the Streamlit App
After training the models:

1️⃣ Start the web application:

bash
Copy
Edit
streamlit run app.py

2️⃣ A browser tab will open with the Student Mental Health Assessment tool.

3️⃣ Enter your details (age, gender, CGPA, year of study, etc.).

4️⃣ Receive a preliminary assessment and mental health recommendations.

##📊 Results & Improvements
✅ Model Evaluation
🔹 Depression Model: Well-predicts common cases but faces class imbalance issues.

🔹 Anxiety & Panic Attacks: Similar performance with room for improvement.

🔧 Suggested Enhancements

🔹 Use balanced datasets (oversampling/undersampling).

🔹 Experiment with deep learning models (e.g., Transformers).

🔹 Improve UI/UX for better engagement.

##📜 License
📄 This project is licensed under the MIT License. See the LICENSE file for details.

##🙏 Acknowledgements
💙 Special thanks to contributors, data providers, and the open-source community!
🤝 This project aims to raise awareness about student mental health through AI-driven tools.



