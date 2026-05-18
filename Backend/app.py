from fastapi import FastAPI
from enum import Enum
import pandas as pd
import numpy as np
import pickle

# LOAD MODEL & COLUMNS

model = pickle.load(open("house_price_model (3).pkl", "rb"))
model_columns = pickle.load(open("model_columns (3).pkl", "rb"))

# FASTAPI APP

app = FastAPI(
    title="House Price Prediction API",
    description="ML API for predicting Indian house prices",
    version="1.0"
)

# ENUMS (Dropdown Options)

class CityEnum(str, Enum):
    Delhi = "Delhi"
    Gurgaon = "Gurgaon"
    Noida = "Noida"
    Ghaziabad = "Ghaziabad"
    Faridabad = "Faridabad"


# HOME ROUTE

@app.get("/")
def home():
    return {
        "message": "House Price Prediction API Running Successfully"
    }



# PREDICTION ROUTE

@app.post("/predict")
def predict_price(
    total_area: float,
    bedroom: int,
    bathroom: int,
    city: CityEnum
):

    
    # FEATURE ENGINEERING
    

    area_per_bedroom = total_area / bedroom
    bathroom_per_bedroom = bathroom / bedroom
    total_rooms = bedroom + bathroom + 2
    room_density = (bedroom/bathroom) / total_area
    bathroom_bonus = bedroom * bathroom
    luxury_home = int(
        (total_area > 3000) and (bathroom >= 4)
    )
    

    
    # CREATE INPUT 

    input_dict = {col: 0 for col in model_columns}

    # Numerical Features
    input_dict["total_area"] = total_area
    input_dict["bedroom"] = bedroom
    input_dict["bathroom"] = bathroom
    input_dict["area_per_bedroom"] = area_per_bedroom
    input_dict['bathroom_per_bedroom'] = bathroom_per_bedroom
    input_dict["total_rooms"] = total_rooms
    input_dict['room_density'] = room_density
    input_dict['bathroom_bonus'] = bathroom_bonus
    input_dict['luxury_home'] = luxury_home
    


    # ONE HOT ENCODING


    city_col = f"city_{city.value}"

    if city_col in input_dict:
        input_dict[city_col] = 1

    
    # CONVERT TO DATAFRAME


    input_df = pd.DataFrame([input_dict])


    # PREDICTION


    prediction = model.predict(input_df)[0]

    # Reverse log transform

    final_price = np.expm1(prediction)

    # RETURN RESPONSE

    return {
        "Predicted Price": f"₹ {round(final_price, 2)}"
    }



