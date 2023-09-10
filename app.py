import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('./NBClassifier.pkl', 'rb'))

def index():
    return "Hello world"

def predict():

    st.title("Crop Suggestion")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Find the Crop that suits You!! </h2>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    nitrogen = st.number_input('nitrogen')
    phosphorous = st.number_input('phosphorous')
    potassium = st.number_input('potassium')
    temp = st.number_input('temperature')
    humidity = st.number_input('humidity')
    ph = st.number_input('ph')
    rainfall = st.number_input('rainfall')

    result = ""
    ans = ""
    if st.button("Predict"):
        input_query = np.array(
            [[nitrogen, phosphorous, potassium, temp, humidity, ph, rainfall]])
        result = model.predict(input_query)
        ans = result[0]

    st.success('Crop : {}'.format(ans))


if __name__ == '__main__':
    predict()