import streamlit as st
import joblib
import pandas as pd
import numpy as np
from transformers import pipeline, set_seed

# Page configuration
st.set_page_config(
    page_title="Student Mental Health Assessment",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .risk-high { color: #ff4b4b; }
    .risk-moderate { color: #ffa500; }
    .risk-low { color: #00cc00; }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for storing results
if 'assessment_done' not in st.session_state:
    st.session_state.assessment_done = False

def load_models():
    """Load all necessary ML models and scalers"""
    try:
        models = joblib.load('mental_health_models.pkl')
        scaler = joblib.load('scaler.pkl')
        train_cols = joblib.load('train_columns.pkl')
        return models, scaler, train_cols
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        return None, None, None

def get_risk_description(probability):
    """Convert probability to risk level description"""
    if probability > 0.7:
        return "High"
    elif probability > 0.5:
        return "Moderate"
    elif probability > 0.3:
        return "Low"
    else:
        return "Minimal"

def get_risk_color(risk_level):
    """Get color code for risk level"""
    colors = {
        "High": "risk-high",
        "Moderate": "risk-moderate",
        "Low": "risk-low",
        "Minimal": "risk-low"
    }
    return colors.get(risk_level, "")

def generate_condition_advice(condition, risk_level):
    """Generate specific advice based on condition and risk level"""
    advice_map = {
        'depression': {
            'High': """You're showing signs that might be related to depression. This could be affecting your daily activities and mood. 
                   While this isn't a diagnosis, it's important to speak with a mental health professional who can provide proper evaluation and support.""",
            'Moderate': """Some symptoms of depression might be present. This is common among students, especially during stressful periods. 
                       Consider talking to a counselor about healthy coping strategies.""",
            'Low': """While some mild depressive symptoms might be present, they appear to be within a manageable range. 
                   Continue practicing self-care and maintaining social connections.""",
            'Minimal': """Your responses suggest minimal signs of depression. Keep up your positive mental health practices!"""
        },
        'anxiety': {
            'High': """Your responses indicate significant anxiety levels that might be impacting your daily life. 
                   This is common among students, but it's important to seek professional support to develop effective coping strategies.""",
            'Moderate': """You're showing moderate levels of anxiety. This is very common in academic settings, 
                       but developing some additional coping strategies could be beneficial.""",
            'Low': """Some mild anxiety is present, which is normal, especially during academic stress. 
                   Consider learning some basic stress management techniques.""",
            'Minimal': """Your anxiety levels appear to be well-managed. Continue your current stress management practices!"""
        },
        'panic attack': {
            'High': """Your responses suggest you might be experiencing symptoms that could lead to panic attacks. 
                   While this can be frightening, there are effective treatments and coping strategies available.""",
            'Moderate': """Some panic-related symptoms are present. Learning specific coping techniques could help you 
                       manage these symptoms effectively.""",
            'Low': """Mild signs of panic-related symptoms are detected. These are manageable with proper support and techniques.""",
            'Minimal': """Your responses suggest minimal risk of panic attacks. Continue your current wellness practices!"""
        }
    }
    return advice_map.get(condition.lower(), {}).get(risk_level, "Assessment unavailable for this condition.")

def generate_recommendations(results, student_info):
    """Generate personalized recommendations based on assessment results and student information"""
    recommendations = []
    
    # Academic recommendations based on CGPA
    if student_info['cgpa'] < 7.0:
        recommendations.extend([
            "Consider creating a structured study schedule",
            "Visit your academic advisor to discuss study strategies",
            "Make use of campus tutoring services",
            "Join study groups for collaborative learning"
        ])
    
    # Mental health recommendations based on highest risk factor
    highest_risk = max(results.items(), key=lambda x: x[1]['probability'])[0]
    risk_level = get_risk_description(max(r['probability'] for r in results.values()))
    
    if risk_level in ["High", "Moderate"]:
        recommendations.extend([
            "Schedule an appointment with the campus counseling center",
            "Practice daily relaxation techniques",
            "Maintain a regular sleep schedule",
            "Exercise regularly to reduce stress"
        ])
    
    # General wellness recommendations
    recommendations.extend([
        "Stay connected with friends and family",
        "Take regular breaks during study sessions",
        "Practice mindfulness or meditation",
        "Maintain a balanced diet and stay hydrated"
    ])
    
    return recommendations

def main():
    st.title("Student Mental Health Assessment")
    st.markdown("""
    This tool provides a preliminary assessment of common mental health concerns among students.
    Please note that this is not a diagnostic tool and should not replace professional medical advice.
    """)
    
    # Load models
    models, scaler, train_cols = load_models()
    if not all([models, scaler, train_cols]):
        st.error("Unable to load necessary models. Please contact support.")
        return

    # Create input form
    with st.form("assessment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.selectbox("Gender", ['Male', 'Female'])
            age = st.number_input("Age", min_value=16, max_value=60, value=20)
            course = st.selectbox("Course", ['Engineering', 'IT', 'Business', 'Arts', 'Science', 'Other'])
        
        with col2:
            year = st.slider("Year of Study", 1, 6, 1)
            cgpa = st.select_slider("CGPA", options=[float(i)/10 for i in range(40, 101, 5)], value=7.0)
            marital = st.selectbox("Marital Status", ['Single', 'Married'])
        
        submit_button = st.form_submit_button("Begin Assessment")

    if submit_button:
        # Prepare input data
        input_data = {
            'Gender': 0 if gender == 'Male' else 1,
            'Age': age,
            'course': course,
            'year of Study': year,
            'CGPA?': cgpa,
            'Marital status': 0 if marital == 'Single' else 1
        }
        
        # Make predictions
        processed = pd.get_dummies(pd.DataFrame([input_data])).reindex(columns=train_cols, fill_value=0)
        scaled = scaler.transform(processed)
        
        results = {}
        for target, model in models.items():
            proba = model.predict_proba(scaled)[0][1]
            results[target] = {
                'prediction': model.predict(scaled)[0],
                'probability': round(proba, 2)
            }
        
        # Display results
        st.markdown("---")
        st.subheader("Assessment Results")
        
        # Create three columns for results display
        col1, col2, col3 = st.columns([2, 2, 3])
        
        with col1:
            st.markdown("### Risk Levels")
            for condition, data in results.items():
                risk_level = get_risk_description(data['probability'])
                color = get_risk_color(risk_level)
                st.markdown(f"**{condition}**: <span class='{color}'>{risk_level}</span> ({data['probability']:.0%})", 
                          unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Support Resources")
            st.write("🏫 **Campus Counseling**")
            st.write("📞 **24/7 Helpline - 1800-9300-8528**")
            st.write("👥 **Peer Support**")
            st.write("📚 **Academic Services**")
        
        with col3:
            st.markdown("### Key Recommendations")
            recommendations = generate_recommendations(results, {'cgpa': cgpa})
            for i, rec in enumerate(recommendations[:5], 1):
                st.write(f"{i}. {rec}")
        
        # Detailed Analysis
        st.markdown("---")
        st.subheader("Detailed Analysis")
        
        for condition, data in results.items():
            risk_level = get_risk_description(data['probability'])
            with st.expander(f"{condition} - Detailed Information"):
                st.markdown(generate_condition_advice(condition, risk_level))
        
        # Final recommendations
        st.markdown("---")
        st.subheader("Next Steps")
        st.markdown("""
        1. Review the detailed analysis for each area of concern
        2. Consider discussing these results with a mental health professional
        3. Implement the suggested recommendations that feel most relevant to you
        4. Remember that seeking help is a sign of strength, not weakness
        """)
        
        # Disclaimer
        st.markdown("---")
        st.markdown("""
        *Disclaimer: This assessment is for screening purposes only and is not a diagnostic tool. 
        The results should be discussed with qualified mental health professionals for proper evaluation. 
        If you're experiencing severe distress, please seek immediate professional help.*
        """)

if __name__ == "__main__":
    main()