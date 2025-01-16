import streamlit as st
import requests

# Configuração da página
st.set_page_config(layout="wide")

# Título da página
st.title("Plataforma de Aluguel Descentralizada")

# Função para carregar propriedades disponíveis
def carregar_propriedades():
    # Simulação de carregamento de propriedades (substitua com uma chamada real à API)
    propriedades = [
        {"endereco": "Rua Exemplo, 123", "valorAluguel": 1000},
        {"endereco": "Avenida Teste, 456", "valorAluguel": 2000}
    ]
    return propriedades

# Carregar propriedades disponíveis
propriedades = carregar_propriedades()

# Seção para visualizar propriedades
st.header("Propriedades Disponíveis")
col1, col2 = st.columns(2)
with col1:
    st.write("Endereço")
with col2:
    st.write("Valor do Aluguel")

for propriedade in propriedades:
    col1, col2 = st.columns(2)
    with col1:
        st.write(propriedade["endereco"])
    with col2:
        st.write(propriedade["valorAluguel"])

# Seção para reservar propriedade
st.header("Reservar Propriedade")
endereco_reserva = st.text_input("Endereço da Propriedade para Reservar")
if st.button("Reservar"):
    # Simulação de reserva (substitua com uma chamada real à API)
    st.success("Propriedade reservada com sucesso!")

# Seção para realizar pagamento
st.header("Realizar Pagamento")
endereco_pagamento = st.text_input("Endereço da Propriedade para Pagar")
valor_pagamento = st.number_input("Valor do Pagamento")
if st.button("Pagar"):
    # Simulação de pagamento (substitua com uma chamada real à API)
    st.success("Pagamento realizado com sucesso!")
