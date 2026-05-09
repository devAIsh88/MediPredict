MediPredict is a multiple disease prediction model using machine learning

  This project predicts the chances of three diseases – Diabetes, Heart Disease, and Parkinson’s Disease – using machine learning models.
  It is developed in Python with Streamlit as the frontend to make it easy to use.
  The idea behind this project is to create a simple tool that helps people get an idea about possible health risks based on basic medical details.
  I have trained three different machine learning models, one for each disease, and then combined them into a single web application.

About the Project:
    The system uses user input such as medical test results to make predictions using pre-trained models.
    Each model is built on separate datasets and is saved as a .sav file.
    The Streamlit interface allows users to select which disease they want to check and then enter the required details.

Models used:
  Diabetes Prediction: Support Vector Machine (SVM)
  Heart Disease Prediction: Logistic Regression
  Parkinson’s Prediction: Support Vector Machine (SVM)
  Google Generative AI (Gemini) is used to generate a small health-related suggestion after the prediction.

Technologies Used:
    Python
    Scikit-learn
    Streamlit
    Pandas
    NumPy
    Google Generative AI API

How It Works?
    The user opens the Streamlit app.
    Selects a disease from the sidebar menu.
    Enters the medical data in the input fields.
    The saved machine learning model loads and makes a prediction.
    The app displays the result and an optional AI-based suggestion.

How to Run the Project

Step 1: Clone the repository
    git clone https://github.com/devAIsh88/Multiple_Disease_Prediction.git

Step 2: Open the project folder
    cd Multiple_Disease_Prediction

Step 3: Install the dependencies
    pip install -r requirements.txt

Step 4: Run the Streamlit app
    streamlit run app.py
    After running the command, the web app will open automatically in your default browser, usually at http://localhost:8501

Project Structure
          Multiple_Disease_Prediction
          │
          ├── app.py – main Streamlit app
          ├── diabetes_model.sav – trained model for diabetes
          ├── heart_model.sav – trained model for heart disease
          ├── parkinsons_model.sav – trained model for Parkinson’s disease
          ├── requirements.txt – project dependencies
          └── README.txt – documentation

Future Improvements:
    Add more disease models.
    Improve the dataset quality and accuracy.
    Deploy the application online for easier access.

Author:
Devashish
Developed this project as part of my machine learning learning journey.
I wanted to create something practical that combines AI, health data, and user interaction in one place.
