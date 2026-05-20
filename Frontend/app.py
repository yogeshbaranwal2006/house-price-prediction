import streamlit as st
import requests

# PAGE SETTINGS

st.set_page_config(
    page_title="House Price Prediction",
    layout="centered"
)

st.title("House Price Prediction")

with st.expander("About this Project"):

    st.markdown(""" 
    Predict estimated house prices using a machine learning model.
            
    **Feature used:**
    - Total Area (sqft)
    - Bedrooms
    - Bathrooms
    - City
                
    Model Used: 
    -XGBoost Regressor
            
    Tech Stack: 
    -Python
    -FastAPI
    -Streamlit                                                                              
    """)




# INPUTS

total_area = st.number_input(
    "Total Area (In sqft)",
    min_value=500,
    max_value=10000,
    value=1000
)

bedroom = st.selectbox(
    "Bedroom",
    [1,2,3,4,5,6]
)

bathroom = st.selectbox(
    "Bathroom",
    [1,2,3,4,5,6,7]
)

city = st.selectbox(
    "City",
    [
        "Delhi",
        "Gurgaon",
        "Noida",
        "Ghaziabad",
        "Faridabad"
    ]
)

# PREDICT BUTTON

if st.button("Predict"):

    # Validation

    if total_area < bedroom * 200:

        st.error(
            "Total area too small for selected bedrooms"
        )

    elif bathroom > bedroom + 2:

        st.error(
            "Bathrooms look unrealistic"
        )

    else:

        # Render URL 

        url = "https://house-price-prediction-skbh.onrender.com/predict"

        params = {
            "total_area": total_area,
            "bedroom": bedroom,
            "bathroom": bathroom,
            "city": city
        }

        try:

            response = requests.post(
                url,
                params=params
            )

            if response.status_code == 200:

                result = response.json()

                price = float(
                    result["Predicted Price"]
                    .replace("₹", "")
                    .replace(",", "")
                    .strip()
                )

                # Dynamic display

                if price >= 10000000:

                    crore = price / 10000000

                    display_price = (
                        f"₹ {crore:.2f} Crore"
                    )

                else:

                    lakh = price / 100000

                    display_price = (
                        f"₹ {lakh:.2f} Lakh"
                    )

                st.success(
                    f"Predicted Price: {display_price}"
                )

            else:

                st.error(
                    f"Prediction failed ({response.status_code})"
                )

        except Exception as e:

            st.error(
                f"Backend not running: {e}"
            )