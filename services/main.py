import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt         
import streamlit as st
import base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:1.jpg;base64,%s");
    background-position: center;
    background-size: cover;
    }
 input[type="text"] {
     
     opacity: 0.6;
          
 }
  </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('bg1.jpg')


st.markdown("<h1 style='text-align: justify;'>Vehicle Service Recommendation</h1>", unsafe_allow_html=True)
    
print("============================= data load =======================================")

df = pd.read_csv('vehicle_maintenance_data.csv')
print(df.head())
df.info()
print(df.isnull().sum())




vehicle=df['Vehicle_Model']
maintain=df['Maintenance_History']
fuel=df['Fuel_Type']
transmission=df['Transmission_Type']
service=df['Last_Service_Date']
expiry=df['Warranty_Expiry_Date']
owner=df['Owner_Type']
tire=df['Tire_Condition']
brake=df['Brake_Condition']
battery=df['Battery_Status']

print()    
print("============================= label encoding ===================================")
print()    

from sklearn.preprocessing import LabelEncoder
ll = LabelEncoder()
df[['Vehicle_Model', 'Maintenance_History', 'Fuel_Type','Transmission_Type','Last_Service_Date','Warranty_Expiry_Date','Owner_Type','Tire_Condition','Brake_Condition','Battery_Status']] = df[['Vehicle_Model', 'Maintenance_History', 'Fuel_Type','Transmission_Type','Last_Service_Date','Warranty_Expiry_Date','Owner_Type','Tire_Condition','Brake_Condition','Battery_Status']].apply(LabelEncoder().fit_transform)
df.info()

print()    
print("================================ data split =====================================")
print()    

dd = df.fillna(0)
from sklearn.model_selection import train_test_split
 



X = dd[['Mileage','Engine_Size','Odometer_Reading']]
y = dd.iloc[:, -1]



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)
print(X_train, X_test, y_train, y_test)



print()    
print("=====================================  DT =========================================")
print()    

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report



DT = DecisionTreeClassifier()
DT.fit(X_train, y_train)
y_pred = DT.predict(X_test)
print(classification_report(y_test, y_pred))
accuracy = accuracy_score(y_test, y_pred)*100
print("Accuracy:", accuracy)



vehicle = st.selectbox('Vehicle_Model',('Bus','Car','Motorcycle','Truck','Van'))
mileage = st.number_input("Mileage", key="type")
maintain = st.selectbox('Maintenance_History',('Average','Good','Poor'))
fuel = st.selectbox('Fuel_Type',('Disel','Electrc','Petrol'))
transmission = st.selectbox('Transmission_Type',('Automatic','Manual'))
engine = st.number_input("Engine-size", key="typee")
odometer = st.number_input("Odometer_Reading", key="type1")
service = st.date_input('Last_Service_Date',value=None)
expiry = st.date_input('Warranty_Expiry_Date',value=None)
owner = st.selectbox('Owner_Type',('First','Second','Third'))
tire = st.selectbox('Tire_Condition',('Good','New','Worn Out'))
brake = st.selectbox('Brake_Condition',('Good','New','Weak'))
battery = st.selectbox('Battery_Status',('Good','New','Weak'))




pree=([mileage,engine,odometer])

pree=([51376,2500,149060])
predict=np.array([pree]).reshape(1, -1) 
pre=DT.predict(predict)

print(pre)
st.text(pre) 
if pre==0:
    st.text("Need Maintanence") 
else:
    st.text("No Need Maintanence") 


