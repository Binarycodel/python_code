import pandas as pd
import streamlit as st 
import numpy as np 
import time


data = pd.read_csv('medic.csv')

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = np.array([[1,4,6], [5,7,8]])

dic = {
    "name" : ['aadm', 'bola', 'jide'],
    "age": [12,15,89]
}

st.dataframe(data)
# st.table(data)

@st.cache
def run_time(delay=8):
    time.sleep(delay)
    return time.time()

if st.checkbox('1'):
    st.write(run_time())

if st.checkbox('2'):
    st.write(run_time())