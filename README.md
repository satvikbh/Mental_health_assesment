Student Mental Health Assessment Tool
Overview
This project is a Streamlit-based web application designed to assess the mental health of students. It uses machine learning models to predict the risk levels of depression, anxiety, and panic attacks based on student input data. The application provides personalized recommendations and resources to help students manage their mental health.

Features
User-Friendly Interface: Easy-to-use form for students to input their details.

Risk Assessment: Predicts the risk levels for depression, anxiety, and panic attacks.

Personalized Recommendations: Provides tailored advice based on the assessment results.

Resource Links: Directs students to campus counseling, helplines, and academic services.

Detailed Analysis: Offers in-depth information and advice for each mental health condition.

Installation
Prerequisites
Python 3.7 or higher

pip (Python package installer)

Steps
Clone the Repository

bash
Copy
git clone https://github.com/your-username/student-mental-health-assessment.git
cd student-mental-health-assessment
Create a Virtual Environment

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy
pip install -r requirements.txt
Run the Application

bash
Copy
streamlit run app.py
Access the Application

Open your web browser and go to http://localhost:8501.

Usage
Input Student Details: Fill in the form with the required details such as gender, age, course, year of study, CGPA, and marital status.

Begin Assessment: Click on the "Begin Assessment" button to start the evaluation.

View Results: The application will display the risk levels for depression, anxiety, and panic attacks along with personalized recommendations.

Detailed Analysis: Expand each section to view detailed advice and information about each condition.

Next Steps: Follow the suggested next steps and consider discussing the results with a mental health professional.

Project Structure
Copy
student-mental-health-assessment/
│
├── app.py                  # Main Streamlit application file
├── data_preprocessing.py   # Script for data preprocessing and model training
├── mental_health_models.pkl# Trained machine learning models
├── scaler.pkl              # Scaler used for data normalization
├── train_columns.pkl       # Columns used during model training
├── requirements.txt        # List of dependencies
├── README.md               # This file
└── student mental health.csv # Dataset used for training (not included in the repository)
Data Preprocessing
The data preprocessing script (data_preprocessing.py) performs the following steps:

Load Data: Reads the student mental health dataset.

Data Cleaning: Drops unnecessary columns, cleans column names, and handles missing values.

Feature Engineering: Encodes categorical variables, simplifies course categories, and handles the 'year of Study' column.

Model Training: Trains separate Random Forest classifiers for depression, anxiety, and panic attacks.

Model Saving: Saves the trained models and scaler for use in the Streamlit application.

Model Evaluation
The models are evaluated using classification reports which include precision, recall, and F1-score. The evaluation results are as follows:

Depression:

Precision: 0.90

Recall: 1.00

F1-score: 0.95

Anxiety:

Precision: 0.80

Recall: 1.00

F1-score: 0.89

Panic Attack:

Precision: 0.56

Recall: 0.83

F1-score: 0.67

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the creators of Streamlit for making it easy to build and share data apps.

Thanks to the scikit-learn community for providing robust machine learning tools.

Contact
For any questions or feedback, please reach out to satvikbhardwaj2003@gmail.com

