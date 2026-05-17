import streamlit as st
import requests

st.title('House Price Prediction')

total_area = st.number_input(
    'Total Area',
    min_value = 500
)

bedroom = st.selectbox(
    'Bedroom',
    [1,2,3,4,5,6]
)

bathroom = st.selectbox(
    'Bathroom',
    [1,2,3,4,5,6,7]
)

city = st.selectbox(
    'City',
    [
        'Delhi',
        'Gurgaon',
        'Noida',
        'Ghaziabad',
        'Faridabad'
    ]
)

if st.button('Predict'):
    if total_area < bedroom * 200:
        st.error(
            'Total area too small for selected bedrooms'
        )

    elif bathroom > bedroom + 2:
        st.error(
            'Bathrooms look unrealistic'
        )     

    else:

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
                    result['Predicted Price']
                    .replace('₹', '')
                )

                crore = price / 10000000

                st.success(
                    f"Predicted Price: ₹ {crore:.2f} Crore"
                )
            else:

                st.error(
                    'Prediction Failed'
                )    
        except:

            st.error(
                'Backend not running. Start FastAPI server.'
            )        
