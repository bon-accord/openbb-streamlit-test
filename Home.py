import streamlit as st 
from openbb_terminal.sdk import openbb


def main():

    st.set_page_config(layout="wide")
    st.title('Example Dashboard Using OpenBB & Streamlit')

    st.write('''Wee example app''')

    st.write(f"OpenBB Version : {openbb.__version__}")

main()
