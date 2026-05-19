import streamlit as st
st.title("Geeso Locadora - Alugue já!")
st.sidebar.title("Escolha seu modelo")
st.sidebar.image("logo.png")

carros = ["BMW X5","Audi R8","Ford Mustang","VW Polo","Fiat Toro"]

opcao = st.sidebar.selectbox("Escolha o carro que foi alugado", carros)

st.image(f"{opcao}.png")
st.markdown(f"## Você alugou o modelo: {opcao}")
st.markdown("---")

dias = st.text_input(f"Por quantos dias o {opcao} foi alugado ?")
km = st.text_input(f"Quantos km você rodou com o {opcao} ?")