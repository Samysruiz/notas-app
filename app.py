import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tema escuro
st.set_page_config(page_title="Cálculo de Nota", page_icon="📘", layout="centered")

st.title("📘 Calculadora de Notas – Versão Premium Mobile")

META = 70

st.markdown("Escolha o número de trabalhos, preencha as notas recebidas e veja seu progresso.")

# Frases filosóficas discretas
FRASES = [
    "“A coragem é a primeira das qualidades humanas.” – Aristóteles",
    "“A educação é a arma mais poderosa para mudar o mundo.” – Nelson Mandela",
    "“Você se torna aquilo que pensa.” – Buda",
    "“Ninguém liberta ninguém; as pessoas se libertam em comunhão.” – Paulo Freire",
    "“A persistência realiza o impossível.” – Nietzsche",
]

import random
st.caption(random.choice(FRASES))

# Pesos fixos do plano
PESOS_FIXOS = {
    "Prova Objetiva": 15,
    "Prova Dissertativa": 30,
    "Projeto Final": 15,
    "Avaliação 360": 2.5,
    "Habilidades Cognitivas": 10,

