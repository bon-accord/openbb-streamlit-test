# Imports
import streamlit as st
import pandas as pd
import numpy as np
from openbb_terminal.sdk import openbb

# -----------------------------------------------------------------------------
# Add app title
# -----------------------------------------------------------------------------
st.title('Stocks')

# -----------------------------------------------------------------------------
# Fetch some data
# -----------------------------------------------------------------------------

data = openbb.stocks.load("SPY", weekly = True)

st.write(data)

data = openbb.ta.atr_chart(data, symbol = "SPY")

st.write(data)
