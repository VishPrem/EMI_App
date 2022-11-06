# Write the code for creating the EMI calculator app
import streamlit as st

def calculate_emi(p, n, r):
  return p * (r / 100) * ((1 + (r / 100)) ** n / ((1 + (r / 100)) ** n - 1))

st.title('EMI Calculator App')
principal = 50000
tenure = 2
roi = 5.05

n = tenure * 12
r = roi / 12

if st.button('Calculate'):
  calculation = calculate_emi(principal, n, r)
  st.write("Emi = ", calculation)