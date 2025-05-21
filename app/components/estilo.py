
import streamlit as st
# Estilos CSS personalizados
def estilo_add():
    st.markdown("""
        <style>
        .block {
            border-radius: 12px;
            padding: 2px;
            margin-bottom: 15px;
            background: linear-gradient(270deg, #ff4b4b, #ffa500, #ffd700, #ffa500, #ff4b4b);
            background-size: 1000% 1000%;
            animation: animateBorder 8s linear infinite;
        }
        .row-flex {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        .scroll-inner {
            border-radius: 10px;
            background-color: #0F111A;
            padding: 20px;
            color: white;
            font-size: 14px;
            line-height: 1.6;   
            max-height: 150px;
            overflow-y: auto;
            padding-right: 10px;
            flex: 2;  /* columna de texto más ancha */
        }
        @keyframes animateBorder {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }
        </style>
    """, unsafe_allow_html=True)

