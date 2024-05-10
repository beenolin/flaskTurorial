import streamlit as st
import pandas as pd
import numpy as np

st.title('user picks in NYC')

DATE_COLUMN="date/time"
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    print(data)
    lowercase = lambda x:str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
data_load_state=st.text("데이터 읽는중")
data= load_data(10000)
data_load_state.text("(using st cache)완료됨")
if st.checkbox('raw 데이터 보여줘'):
    st.subheader('raw data')
    st.write(data)
st.subheader('시간당 가져온 곗수')
hist_values=np.histogram(data[DATE_COLUMN].dt.hour,bins=24,range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour',0,23,17)
filtered_data = data[data[DATE_COLUMN].dt.hour==hour_to_filter]
st.subheader('%s:00에 가져온 모든 데이터 map' % hour_to_filter)
st.map(filtered_data)
