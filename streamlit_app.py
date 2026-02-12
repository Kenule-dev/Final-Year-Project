import streamlit as st
import numpy as np
import joblib

model=joblib.load("pollution_model.pkl")
le = joblib.load("label_encoder.pkl")
model
le
