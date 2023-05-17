import streamlit as st
import pandas as pd
import gal
import pedro
import leandro
import leone
import os


def call_gal():
    gal.generate_csv()
    load()
def call_pedro():
    pedro.generate_csv()
    load()
def call_leandro():
    leandro.generate_csv()
    load()
def call_leone():
    leone.generate_csv()
    load()
def call_all():
    gal.generate_csv()
    pedro.generate_csv()
    leandro.generate_csv()
    leone.generate_csv()
    load()
def delete():
    os.remove("house_data.csv")
def load():
    st.title("Dados gerados JUDEUS")
    df = pd.read_csv("house_data.csv", encoding = "ISO-8859-1")
    st.write(df)

st.button("Generate CSV (gal)",  on_click=call_gal)
st.button("Generate CSV (pedro)",  on_click=call_pedro)
st.button("Generate CSV (leandro)",  on_click=call_leandro)
st.button("Generate CSV (leone)",  on_click=call_leone)
st.button("Generate CSV (all)",  on_click=call_all)
st.button("RESET", on_click=delete)