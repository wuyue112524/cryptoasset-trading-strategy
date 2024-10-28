import streamlit as st
import pandas as pd
from utils.charts import create_plot
st.set_page_config(layout="wide")


## load data
path = 'data/'
price = pd.read_excel(path+'LINK_USDT-1h.xlsx')
value_flow = pd.read_excel(path+"link链上转入转出.xlsx")

st.title('LINK Value Flow Analysis')
fig1 = create_plot(value_flow, price)
st.write('### Section 1: Data overview')
st.plotly_chart(fig1,use_container_width=True)