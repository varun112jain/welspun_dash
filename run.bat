@echo off
set PORT=%1
if "%PORT%"=="" set PORT=8501
echo Starting Welspun Streamlit Dashboard on port %PORT%...
start http://localhost:%PORT%
C:\Users\0231304\myenv\Scripts\streamlit.exe run app.py --server.port %PORT%

