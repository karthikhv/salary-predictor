import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

try:
    # Load and preprocess data
    df = pd.read_csv('salaries_complete.csv')
except FileNotFoundError:
    print("Error: 'salaries_complete.csv' not found in the project folder.")
    exit(1)

# Verify required columns
required_columns = ['salary_in_usd', 'work_year', 'experience_level', 'employment_type', 
                    'job_title', 'employee_residence', 'remote_ratio', 'company_location', 'company_size']
if not all(col in df.columns for col in required_columns):
    print(f"Error: CSV missing required columns. Found: {df.columns.tolist()}")
    exit(1)

# Clean data
df = df.dropna(subset=['salary_in_usd'])
df = df[df['salary_in_usd'].apply(lambda x: str(x).replace('.', '').isdigit())]  # Handle potential decimal points

# Define features and target
features = required_columns[1:]  # Exclude salary_in_usd
target = 'salary_in_usd'

# Encode categorical features
df_encoded = pd.get_dummies(df[features])
X = df_encoded
y = df[target].astype(float)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model and feature columns
joblib.dump((model, X.columns), 'salary_model.pkl')
print("Model trained and saved as salary_model.pkl")
