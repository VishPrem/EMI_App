import streamlit as st

def calculate_emi(p, n, r):
  return p * (r / 100) * ((1 + (r / 100)) ** n / ((1 + (r / 100)) ** n - 1))

def calculate_outstanding_balance(p, n, r, m):
  return (p * (1 + r / 100) ** n - (1 + r / 100) ** m) / ((1 + r / 100) ** n - 1)

st.title('Improvised EMI Calculator App')

m = 4
principal = 50000
tenure = 2
roi = 5.05
n = tenure * 12
r = roi / 12

if st.button('Calculate EMI'):
  calculation = calculate_emi(principal, n, r)
  st.write("Emi = ", calculation)

if st.button('Calculate Outstanding Balance'):
  calculation = calculate_outstanding_balance(principal, n, r, m)
  st.write("Outstanding Balance = ", calculation)