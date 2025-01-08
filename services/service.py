


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


st.markdown("<h1 style='text-align: justify;'>Garage Management System</h1>", unsafe_allow_html=True)
service = st.selectbox('Services', (' Air Conditioning',' Upholstery', 'Paintwork', 'Auto Management','reparing tyres '))


Requirement = st.text_area("Enter Requirement:", value="")

if st.button('Recommend'):
    st.write(' The cost for a tire rotation is usually around $20 to $30, but it can vary based on tyre range')

