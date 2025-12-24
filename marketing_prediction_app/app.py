import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title='Marketing Prediction', page_icon='📈', layout='wide')

st.title('📊 Marketing Prediction')
st.write('A Machine Learning Model made for Educational Purpose')

df = pd.read_csv("../data/new/Clean_data.csv")


st.subheader("Dataset Preview")
st.dataframe(df, use_container_width=True)

le = LabelEncoder()
df = pd.get_dummies(df, columns=['Device'])
df['Location'] = le.fit_transform(df['Location'])

X = df[['Device_Desktop', 'Device_Mobile', 'Device_Tablet', 'Clicks', 'Impressions', 'Leads', 'Conversions', 'Location', 'Cost']]
y = df['Sale_Amount']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

st.divider()
st.subheader('📌 Enter the following Details')

device = st.selectbox("Select Targeted Device", ['Desktop', 'Mobile', 'Tablet'])
clicks = st.number_input('Enter number of clicks', min_value=0, value=100)
impression = st.number_input('Enter number of impressions', min_value=0, value=100)
leads = st.number_input('Enter number of leads', min_value=0, value=50)
conversion = st.number_input('Enter number of conversions', min_value=0, value=20)
location = st.selectbox("Select Location", le.classes_.tolist())
cost = st.number_input('Enter Campaign Cost', min_value=0, value=500)

dl_sel = 1 if device == 'Desktop' else 0
ml_sel = 1 if device == 'Mobile' else 0
tb_sel = 1 if device == 'Tablet' else 0

location_encoded = le.transform([location])[0]

if st.button("Predict Sale Amount"):
    user_data = [[
        dl_sel,
        ml_sel,
        tb_sel,
        clicks,
        impression,
        leads,
        conversion,
        location_encoded,
        cost
    ]]

    user_data_scaled = scaler.transform(user_data)
    prediction = model.predict(user_data_scaled)

    st.success(f"Estimated Sale Amount: **${prediction[0]:,.0f}**")

st.markdown('---')
st.caption('Made by Vansh Chandan 🎓')