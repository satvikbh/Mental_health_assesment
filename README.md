# 🎓 Student Mental Health Assessment Tool 🧠💙  

A **Streamlit-based web application** designed to **assess student mental health** by predicting the risk levels of **depression, anxiety, and panic attacks** using machine learning. The app provides **personalized recommendations and mental health resources** to support students.  

> ⚠️ **Disclaimer:** This tool is not a substitute for professional medical advice. Please consult a mental health professional if needed.

---

## 📌 Features  

✅ **User-Friendly Interface** – Simple form for students to input their details.  
✅ **Risk Assessment** – Predicts the risk levels for **depression, anxiety, and panic attacks**.  
✅ **Personalized Recommendations** – Provides tailored advice based on assessment results.  
✅ **Resource Links** – Connects students to **campus counseling, helplines, and academic support**.  
✅ **Detailed Analysis** – Offers in-depth insights into mental health conditions.  

---

## ⚙️ Installation  

### 📋 Prerequisites  

- **Python 3.7 or higher**  
- **pip (Python package installer)**  

### 📥 Steps  

1. **Clone the Repository**  
   ```markdown
   git clone https://github.com/your-username/student-mental-health-assessment.git
   cd student-mental-health-assessment
   ```

2. **Create a Virtual Environment**  
   ```markdown
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**  
   ```markdown
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   ```markdown
   streamlit run app.py
   ```

5. **Access the Application**  
   🌐 Open your web browser and go to **[http://localhost:8501](http://localhost:8501)**.  

---

## 🎭 Usage  

1. **Input Student Details** – Fill in details such as **gender, age, course, year of study, CGPA, and marital status**.  
2. **Begin Assessment** – Click **"Begin Assessment"** to evaluate your mental health.  
3. **View Results** – See risk levels for **depression, anxiety, and panic attacks** along with **personalized recommendations**.  
4. **Detailed Analysis** – Expand each section to view in-depth advice and insights.  
5. **Next Steps** – Follow **suggested steps** and consider discussing your results with a professional.  

---

## 📂 Project Structure  

```markdown
student-mental-health-assessment/
│
├── app.py                   # 🎭 Main Streamlit application file
├── data_preprocessing.py    # 🛠️ Data preprocessing & model training script
├── models/
│   ├── mental_health_models.pkl  # 🧠 Trained machine learning models
│   ├── scaler.pkl               # 🔄 Scaler for data normalization
│   ├── train_columns.pkl        # 🔠 Columns used during training
├── requirements.txt         # 📌 Python dependencies
├── README.md                # 📖 Project documentation (this file)
└── data/student_mental_health.csv  # 📊 Training dataset (not included in repo)
```

---

## 🛠️ Data Preprocessing  

- **Load Data** – Reads student mental health dataset.  
- **Data Cleaning** – Drops unnecessary columns, handles missing values.  
- **Feature Engineering** – Encodes categorical variables, simplifies course categories.  
- **Model Training** – Trains **RandomForest classifiers** for **depression, anxiety, and panic attacks**.  
- **Model Saving** – Stores trained models and scaler for **real-time predictions** in the app.  

---

## 📊 Model Evaluation  

The models were evaluated using **classification reports (precision, recall, F1-score):**  

| Condition       | Precision | Recall | F1-score |
|----------------|----------|--------|----------|
| **Depression** | 🟢 0.90  | 🟢 1.00 | 🟢 0.95 |
| **Anxiety**    | 🟡 0.80  | 🟡 1.00 | 🟡 0.89 |
| **Panic Attack** | 🔴 0.56  | 🔴 0.83 | 🔴 0.67 |

🛠️ **Planned Improvements:**  
- Balance the dataset using **oversampling/undersampling**.  
- Explore **deep learning models (e.g., Transformers)** for better performance.  
- Enhance **UI/UX** for better engagement.  

---

## 🤝 Contributing  

💡 **Want to improve this project? Follow these steps:**  

1. **Fork the repository**.  
2. **Create a new branch**:  
   ```markdown
   git checkout -b feature/YourFeatureName
   ```
3. **Commit your changes**:  
   ```markdown
   git commit -m "Add new feature"
   ```
4. **Push to your branch**:  
   ```markdown
   git push origin feature/YourFeatureName
   ```
5. **Submit a pull request** 🚀  

---

## 📜 License  

📄 This project is licensed under the **MIT License**. See the **LICENSE** file for details.  

---

## 🙏 Acknowledgments  

💙 Special thanks to:  
- **Streamlit** – for making it easy to build and share interactive data apps.  
- **scikit-learn community** – for providing powerful machine learning tools.  

📢 *Mental health matters! Let’s use AI to support well-being!* 💙🚀  

---

## 📬 Contact  

📧 **For questions or feedback, reach out at:**  
📩 **satvikbhardwaj2003@gmail.com**  

---

🔥 *If you find this project helpful, give it a ⭐ on GitHub!* 🚀🎉  

