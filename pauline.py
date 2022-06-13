import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import datetime

# App title
st.markdown('''
# Stock Price App
Shown are the stock price data for query companies!
**Credits**

''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2020, 10, 16))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/regan-mu/ADS-April-2022/main/Assignments/Assignment%201/data.csv')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

#string_name = tickerData.info['longName']
#st.header('**%s**' % string_name)

#string_summary = tickerData.info['longBusinessSummary']
#st.info(string_summary)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf= px.line(tickerDf,title='First Quant Figure')
#fig = qf.iplot(asFigure=True)
st.plotly_chart(qf);

####
#st.write('---')
#st.write(tickerData.info)