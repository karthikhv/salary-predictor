import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
try:
    model, feature_columns = joblib.load('salary_model.pkl')
except FileNotFoundError:
    st.error("Model file 'salary_model.pkl' not found. Please run train_model.py first.")
    st.stop()

# Set page configuration
st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Predictor for AI/ML/Data Science Jobs")

# User inputs
st.header("Enter Job Details")
work_year = st.selectbox("Work Year", [2023, 2024, 2025], help="Select the year of employment")
experience_level = st.selectbox("Experience Level", ['EN', 'MI', 'SE', 'EX'], 
                               help="EN: Entry-level, MI: Mid-level, SE: Senior-level, EX: Executive")
employment_type = st.selectbox("Employment Type", ['FT', 'PT', 'CT', 'FL'], 
                              help="FT: Full-time, PT: Part-time, CT: Contract, FL: Freelance")
job_title = st.selectbox("Job Title", ['Data Scientist', 'Machine Learning Engineer', 'AI Architect', 'Data Analyst'],
                        help="Select the job role")
employee_residence = st.selectbox("Employee Residence", ['US', 'DE', 'GB', 'IN', 'CA'],
                                help="Select the employee's country of residence")
remote_ratio = st.slider("Remote Ratio (%)", 0, 100, 100, help="Percentage of remote work")
company_location = st.selectbox("Company Location", ['US', 'DE', 'GB', 'IN', 'CA'],
                              help="Select the company's country")
company_size = st.selectbox("Company Size", ['S', 'M', 'L'], 
                           help="S: Small (<50 employees), M: Medium (50-250), L: Large (>250)")

# Combine inputs into a DataFrame
input_dict = {
    'work_year': work_year,
    'experience_level': experience_level,
    'employment_type': employment_type,
    'job_title': job_title,
    'employee_residence': employee_residence,
    'remote_ratio': remote_ratio,
    'company_location': company_location,
    'company_size': company_size
}
input_df = pd.DataFrame([input_dict])

# Encode input data
input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

# Predict salary
if st.button("Predict Salary"):
    try:
        salary = model.predict(input_encoded)[0]
        st.success(f"💰 Estimated Salary (USD): ${int(salary):,}")
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")