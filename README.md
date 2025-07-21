Here’s a visually appealing and well-formatted `README.md` for your **Salary Predictor for AI/ML/Data Science Jobs** project:

---

# 💼 Salary Predictor for AI/ML/Data Science Jobs

A **Streamlit-based web application** that predicts salaries for AI, Machine Learning, and Data Science roles using a `RandomForestRegressor` model. Trained on real-world data (`salaries_complete.csv`) and deployed on **Streamlit Community Cloud**.

🌐 **[Live Demo →](https://salarypredictorkarthik.streamlit.app/)**
📁 **[Source Code →](https://github.com/karthikhv/salary-predictor)**

---

## 📑 Table of Contents

* [✨ Features](#-features)
* [🛠 Installation](#-installation)
* [🚀 Usage](#-usage)
* [📂 File Structure](#-file-structure)
* [☁️ Deployment](#️-deployment-on-streamlit-community-cloud)
* [📝 License](#-license)

---

## ✨ Features

🎯 **Input Parameters:**

* **Work Year**: `2023`, `2024`, `2025`
* **Experience Level**: `EN` (Entry), `MI` (Mid), `SE` (Senior), `EX` (Executive)
* **Employment Type**: `FT`, `PT`, `CT`, `FL`
* **Job Title**: e.g., `Data Scientist`, `AI Engineer`, `ML Architect`
* **Employee Residence**: Country (e.g., `US`, `DE`, `IN`, `GB`, `CA`)
* **Remote Ratio**: 0–100% (Fully On-site to Fully Remote)
* **Company Location**: Country (e.g., `US`, `DE`, `IN`, `GB`, `CA`)
* **Company Size**: `S` (Small), `M` (Medium), `L` (Large)

💰 **Output:**

* **Predicted Salary** in **USD** (formatted, e.g., `$120,000`)

📱 **Interactive Interface:**

* Built with **Streamlit** for an intuitive user experience

---

## 🛠 Installation

To run the app locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/karthikhv/salary-predictor.git
   cd salary-predictor
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate         # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**

   > Ensure `salaries_complete.csv` is present in the project root.

   ```bash
   python train_model.py
   ```

5. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   Visit [http://localhost:8501](http://localhost:8501)

---

## 🚀 Usage

* Select job-related inputs using dropdowns and sliders
* Click **“Predict Salary”**
* View the estimated salary in **USD**

🔗 Try it live here: **[salarypredictorkarthik.streamlit.app](https://salarypredictorkarthik.streamlit.app/)**

---

## 📂 File Structure

```bash
salary-predictor/
│
├── app.py                # Streamlit frontend for salary prediction
├── train_model.py        # Trains RandomForestRegressor & saves model
├── requirements.txt      # Required Python packages
├── salaries_complete.csv # Dataset (must include salary_in_usd, etc.)
├── salary_model.pkl      # Trained ML model (generated)
├── .gitignore            # Excludes venv, __pycache__, etc.
```

---

## ☁️ Deployment on Streamlit Community Cloud

1. Push your project to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo & deploy `app.py`
4. Set any environment secrets (if needed)
5. Your app is now live!

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
