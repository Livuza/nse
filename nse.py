from contextlib import closing
import time

import matplotlib
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
add_name = st.sidebar.subheader("Submitted by:  Charles Livuza")
ticker_options = df["ticker"].unique().tolist()
ticker = st.sidebar.selectbox("Ticker", ticker_options)
df = df[df["ticker"] == ticker]

add_start_date = st.sidebar.date_input("Start Date")
add_end_date = st.sidebar.date_input("End Date")
a_date = st.sidebar.date_input("Pick a date", (add_start_date, add_end_date))
#df = df[df["date"] == a_date]

st.markdown("#### Nairobi Stock Exchange" )
fig = px.line(data_frame=df, y="price", x="date")
st.write(fig)

st.write("""
# Stock Prices & Volume

Stock **closing price** and **volume** of Google!
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.write("""
#### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
#### Closing Price
""")
st.line_chart(tickerDf.Close)

st.file_uploader("Upload your dataset file")