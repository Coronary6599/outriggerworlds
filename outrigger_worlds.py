# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
st.title('Outrigger Worlds')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://github.com/Coronary6599/outriggerworlds/blob/main/tinysample.csv')

@st.cache

def load_data(nrows):
    data = pd.read_csv(DATA_URL, sep = ",")
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

