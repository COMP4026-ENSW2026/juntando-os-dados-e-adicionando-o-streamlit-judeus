import streamlit as st
import pandas as pd
import gal
import os


def call():
    gal.generate_csv()

def delete():
    os.remove("house_data.csv")

st.title("mario")
st.button("Generate CSV (gal)",  on_click=call())
st.button("RESET", on_click=delete())