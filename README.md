#  House Price Prediction System

Machine Learning based Indian House Price Prediction using Random Forest.

##  Project Overview

This project predicts house prices using real estate data and machine learning.

Features used:

- Total Area
- Bedroom
- Bathroom
- City
- Engineered Features

Workflow:

- Data Cleaning
- EDA
- Feature Engineering
- One Hot Encoding
- Random Forest Model
- FastAPI Backend
- Streamlit Frontend
- Deployment


##  Model Used

Random Forest Regressor

Final Performance:

| Metric | Score |
|----------|------|
| R² Score | 0.75 |
| MAE | 0.356 |
| RMSE | 0.218 |


##  Feature Engineering

Created:

- Area per Bedroom
- Total Rooms
- Luxury Indicator

---

##  Tech Stack

Backend:
- FastAPI

Frontend:
- Streamlit

Libraries:
- Pandas
- NumPy
- Scikit-learn
- Requests


##  Project Structure

HOUSE PRICE PREDICTION

├── Backend  
│ ├── app.py  
│ ├── house_price_model.pkl  
│ └── model_columns.pkl  

├── Frontend  
│ └── app.py  

├── requirements.txt  
└── README.md

---

##  Run Backend

```bash
cd Backend
uvicorn app:app --reload