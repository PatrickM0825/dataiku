import streamlit as st
import requests

# Define your model's endpoint URL
model_endpoint = "http://34.142.210.9:10040/public/api/v1/predict_sentiment/rf_model/predict"

# Create Streamlit input widgets
st.title("Sentiment Prediction Web App")
star_rating = st.number_input("Star Rating:", min_value=1, max_value=5)
review_text = st.text_area("Review Text:", "")

# Create a button to trigger prediction
if st.button("Predict Sentiment"):
    input_data = {
        "features": {
            "stars": star_rating,
            "recommended_label": "",
            "new_reviews": review_text
        }
    }

    try:
        # Make a POST request to the model's endpoint
        response = requests.post(model_endpoint, json=input_data)

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            sentiment = result["result"]
            st.write(f"Predicted Sentiment: {sentiment}")
        else:
            # Handle the error and display details
            st.error(f"Error: Unable to get prediction from the model. Status code: {response.status_code}")
            st.text(f"Response content: {response.content}")

    except Exception as e:
        # Handle exceptions and display details
        st.error(f"Error: {str(e)}")

# Optionally, display a result paragraph
sentiment_output = st.empty()
sentiment_output.text("")

# You can uncomment the above lines if you want to display the result in a paragraph