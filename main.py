import streamlit as st
import requests

st.set_page_config(page_title="Busca preços de veículos")
st.title("Busca preços de veículos")


marcas = requests.get("http://localhost:5000/lista_marcas").json()
marcas = [marca[0] for marca in marcas[0]]


lista_marcas = st.selectbox("Selecione a Marca", (marcas), index=None, placeholder="Selecione a Marca", label_visibility="hidden")

if lista_marcas != None:

    modelos = requests.get(f"http://localhost:5000/lista_modelos/{lista_marcas}").json()

    lista_modelos = [modelo[0] for modelo in modelos[0]]

    def busca_preco():
        selected_modelo = st.session_state["modelo_selectbox"]
        preco = next((modelo[1] for modelo in modelos[0] if modelo[0] == selected_modelo), None)

        if preco:
            st.session_state.preco = preco
            st.session_state.modelo = selected_modelo

    st.selectbox(
        f"Selecione o Modelo da {lista_marcas}",
        lista_modelos,
        index=None, placeholder="Selecione o Modelo",label_visibility="hidden",key="modelo_selectbox",on_change=busca_preco)
    
    if "preco" in st.session_state:
        texto = f"""
                <style>
                   .valor {{ color: red; font-size: 20px; }}
                </style>

                {st.session_state.modelo} tem o Preço de <span class='valor'>R$ {st.session_state.preco}</span>"""

        st.markdown(texto, unsafe_allow_html=True)