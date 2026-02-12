import streamlit as st

import jobliib

model=joblib.load("pollution_model.pkl")
le = joblib.load("label_encoder.pkl")
