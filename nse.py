from contextlib import closing
import time
import streamlit as st
#import matplotlib.plotly as plt
import datetime
from datetime import datetime, date, time
import pandas as pd
#import seaborn as sns
#import numpy as np
import plotly.express as px
import yfinance as yf

st.set_page_config(
    page_title="Nairobi Stock Exchange Market",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="auto",
)
url=("https://raw.githubusercontent.com/regan-mu/ADS-April-2022/main/Assignments/Assignment%201/data.csv")
df = pd.read_csv(url)
add_name = st.sidebar.subheader("Assignment by:  Charles Livuza")
add_selectbox = st.sidebar.selectbox("Ticker", pd.unique(df["ticker"]))
df = df[df["ticker"] == add_selectbox]

#st.markdown('Data Science is **_really_ cool**.')

add_start_date = st.sidebar.date_input("Start Date")
add_end_date = st.sidebar.date_input("End Date")

#df = df[df["date"] == add_start_date]
#df = df[df["date"] == add_end_date]

#with st.sidebar:
 #   add_radio = st.radio(
 #       "Price",
 #      ("High", "Medium")
 #   )
st.markdown("#### Nairobi Stock Exchange" )
st.write("Date range")

fig = px.line(data_frame=df, y="price", x="date")
#fig.show()
st.write(fig)
#st.line_chart(df.price)

st.write("""
# Stock Prices & Volume

Stock **closing price** and **volume** of Google!
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)
#add_date = st.sidebar.date_input("Date")
#df = df[df["date"] == add_date]
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.write("""
#### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
#### Closing Price
""")
st.line_chart(tickerDf.Close)