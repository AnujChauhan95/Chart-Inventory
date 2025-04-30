
import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('saved_model.pkl')

# App title
st.title('Linear Regression Prediction App')

# Sidebar for user input features
st.sidebar.header('User Input Parameters')

def user_input_features():
    # Example inputs - adjust based on your model features
    feature1 = st.sidebar.number_input('Feature 1', min_value=0.0, value=0.0)
    feature2 = st.sidebar.number_input('Feature 2', min_value=0.0, value=0.0)
    feature3 = st.sidebar.number_input('Feature 3', min_value=0.0, value=0.0)
    # Add more features if needed

    data = {
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Main panel
st.subheader('User Input parameters')
st.write(input_df)

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_df)
    st.subheader('Prediction')
    st.write(prediction[0])
