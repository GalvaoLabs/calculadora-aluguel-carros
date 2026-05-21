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

if opcao == "BMW X5":
    diaria = 750
elif opcao == "Audi R8":
    diaria = 900
elif opcao == "Ford Mustang":
    diaria = 800
elif opcao == "VW Polo":
    diaria = 650
elif opcao == "Fiat Toro":
    diaria = 700

if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f"Você alugou {opcao} por {dias} dias e rodou {km}Km o valor total a pagar é {aluguel_total:.2f}")