import streamlit as st
# Estilos CSS personalizados
def estilo_add():
    st.markdown("""
        <style>
        .block {
            background-color: #2a2a2a;
            color: white;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 15px;
        }
        .row-flex {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        .scroll-inner {
            max-height: 150px;
            overflow-y: auto;
            padding-right: 10px;
            flex: 2;  /* columna de texto más ancha */
        }
        .image-style {
            flex: 1; /* columna del gráfico más estrecha */
            max-width: 180px;
            max-height: 180px;
            border-radius: 10px;
            margin-left: 20px;
        }
        </style>
    """, unsafe_allow_html=True)