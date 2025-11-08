import pickle
import os
import streamlit as st
from streamlit_option_menu import option_menu
import google.generativeai as genai


api_key = "AIzaSyD0baKxhmFLvA-l9oHou3J_WPWTzQUW0d0"  
genai.configure(api_key=api_key)




@st.cache_data
def load_model(filepath):
    """Loads a saved .sav model. Cached to load once."""
    if not os.path.exists(filepath):
        st.warning(f"⚠️ Model file missing at: {filepath}")
        return None

    try:
        with open(filepath, 'rb') as file_handle:
            model = pickle.load(file_handle)
            return model
    except Exception as e:
        st.error(f"❌ Error loading {filepath}: {e}")
        return None


def get_ai_advice(condition_name, info_string):
    """Uses Gemini API to generate simple, non-medical wellness suggestions."""

    prompt = f"""
    Analyze this health profile for {condition_name}:
    DETAILS: {info_string}
    
    Generate 3-5 lifestyle and wellness recommendations focusing on
    diet, exercise, and monitoring habits. 
    Avoid giving prescription-level advice. Keep it simple and educational.
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        disclaimer = (
            "> **Note:** *These tips are AI-generated for general informational "
            "purposes only. Always consult a certified medical professional for "
            "diagnosis and treatment.*"
        )
        return f"{disclaimer}\n\n" + response.text

    except Exception as e:
        return f"⚠️ AI suggestion generation failed: {e}"


# disease pg

def diabetes_page(model):
    st.title("🩸 Diabetes Risk Assessment")
    st.write("Enter patient data to analyze the likelihood of diabetes.")

    col1, col2 = st.columns(2)
    with col1:
        preg = st.number_input('Pregnancy Count', 0, 20, 0, 1)
        gluc = st.number_input('Glucose Level (mg/dL)', 0.0, format="%.2f")
        bp = st.number_input('Blood Pressure (mm Hg)', 0.0, format="%.2f")
        skin = st.number_input('Skin Thickness (mm)', 0.0, format="%.2f")
    with col2:
        insulin = st.number_input('Insulin Level (mu U/ml)', 0.0, format="%.2f")
        bmi = st.number_input('Body Mass Index (BMI)', 0.0, format="%.2f")
        dpf = st.number_input('Diabetes Pedigree Function', 0.0, format="%.3f")
        age = st.number_input('Age (years)', 0, 120, 25, 1)

    st.divider()

    if st.button('Run Diabetes Analysis'):
        if not model:
            st.error("Model unavailable. Please ensure file is in correct path.")
            return

        features = [preg, gluc, bp, skin, insulin, bmi, dpf, age]
        prediction = model.predict([features])

        if prediction[0] == 1:
            st.error("Prediction: High likelihood of Diabetes.")
            with st.spinner("Generating AI lifestyle tips..."):
                info = f"Preg: {preg}, Glucose: {gluc}, BP: {bp}, BMI: {bmi}, Age: {age}"
                advice = get_ai_advice("Diabetes", info)
                st.subheader("AI Wellness Recommendations:")
                st.markdown(advice)
        else:
            st.success("Prediction: Low likelihood of Diabetes.")


def heart_page(model):
    st.title("❤️ Heart Disease Prediction")
    st.write("Provide the required metrics to assess cardiac risk.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.number_input('Age', 1, 120, 25, 1)
        sex = st.number_input('Sex (1=M, 0=F)', 0, 1, 1, 1)
        cp = st.number_input('Chest Pain Type (0-3)', 0, 3, 0, 1)
    with col2:
        trestbps = st.number_input('Resting BP', 0.0, format="%.2f")
        chol = st.number_input('Cholesterol (mg/dL)', 0.0, format="%.2f")
        fbs = st.number_input('Fasting Sugar > 120 (1/0)', 0, 1, 0, 1)
    with col3:
        restecg = st.number_input('Resting ECG (0-2)', 0, 2, 0, 1)
        thalach = st.number_input('Max Heart Rate', 0.0, format="%.2f")
        exang = st.number_input('Exercise Angina (1/0)', 0, 1, 0, 1)
    with col4:
        oldpeak = st.number_input('ST Depression', 0.0, format="%.2f")
        slope = st.number_input('Slope (0-2)', 0, 2, 0, 1)
        ca = st.number_input('Major Vessels (0-3)', 0, 3, 0, 1)
        thal = st.number_input('Thal (0-2)', 0, 2, 0, 1)

    st.divider()
    if st.button('Run Cardiac Analysis'):
        if not model:
            st.error("Heart model missing. Ensure file is loaded correctly.")
            return

        features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                    exang, oldpeak, slope, ca, thal]
        prediction = model.predict([features])

        if prediction[0] == 1:
            st.error("Prediction: High likelihood of Heart Disease.")
        else:
            st.success("Prediction: Low likelihood of Heart Disease.")


def parkinsons_page(model):
    st.title("🧠 Parkinson’s Vocal Analysis")
    st.info("Input 22 vocal measurement features for Parkinson’s risk assessment.")

    fields = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
        'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
        'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
        'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA',
        'spread1', 'spread2', 'D2', 'PPE'
    ]

    cols = st.columns(5)
    inputs = []
    for i, f in enumerate(fields):
        with cols[i % 5]:
            val = st.number_input(f, format="%.6f", key=f"park_{i}")
            inputs.append(val)

    st.divider()
    if st.button("Run Parkinson’s Analysis"):
        if not model:
            st.error("Parkinson’s model missing. Ensure file is loaded correctly.")
            return

        prediction = model.predict([inputs])
        if prediction[0] == 1:
            st.error("Prediction: High likelihood of Parkinson’s Disease.")
        else:
            st.success("Prediction: Low likelihood of Parkinson’s Disease.")


# Main fn
def main():
    with st.sidebar:
        st.title("🩺 MediPredict")
        selected_page = option_menu(
            "Navigation",
            ['Diabetes', 'Heart Disease', "Parkinson's"],
            icons=['activity', 'heart', 'brain'],
            default_index=0
        )
        st.sidebar.info("⚠️ This app provides informational insights, not medical advice.")

    # model paths
    models = {
    'diabetes': load_model('C:/Users/KIIT0001/Desktop/MultipleDiseasePrediction/diabetes_model.sav'),
    'heart': load_model('C:/Users/KIIT0001/Desktop/MultipleDiseasePrediction/Heart_disease_model.sav'),
    'parkinsons': load_model('C:/Users/KIIT0001/Desktop/MultipleDiseasePrediction/parkinsons_model.sav')
}


    
    if selected_page == 'Diabetes':
        diabetes_page(models['diabetes'])
    elif selected_page == 'Heart Disease':
        heart_page(models['heart'])
    elif selected_page == "Parkinson's":
        parkinsons_page(models['parkinsons'])


if __name__ == "__main__":
    main()
