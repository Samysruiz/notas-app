import streamlit as st
import altair as alt
import pandas as pd

# -------------------------------------------------------------------
# CONFIGURAÇÃO GERAL DO APP
# -------------------------------------------------------------------
st.set_page_config(page_title="Calculadora de Notas Biopark", page_icon="📘", layout="centered")

st.title("📘 Calculadora de Notas – Modelo Biopark")
st.caption("Versão híbrida, detalhada e alinhada com as categorias oficiais.")

st.divider()

# -------------------------------------------------------------------
# PESOS EXATOS DA DISCIPLINA
# -------------------------------------------------------------------
st.header("📌 Estrutura Oficial das Notas")

st.write("""
Baseado no modelo CHA (Conhecimentos, Habilidades e Atitudes):

### 🎓 Conhecimentos – 70%
- Prova Objetiva – **15 pontos**
- Unidades / Trabalhos (Comunicação Oral e Escrita) – **10 pontos**
- Prova Dissertativa (Projeto) – **30 pontos**
- Entrega Final – **15 pontos**

### 🧠 Habilidades – 20%
- Comunicação Oral e Escrita – já incluída nos **10 pontos**
- Cognitivo – **10 pontos**

### 🤝 Atitudes – 10%
- Autogestão – 2.5  
- Autonomia – 2.5  
- Protagonismo – 2.5  
- Interação – 2.5  

### 🔄 Avaliação 360
- Autoavaliação: 3%
- Equipe: 3%
- Professor: 24%
""")

st.divider()

# -------------------------------------------------------------------
# FORMULÁRIO DE NOTAS
# -------------------------------------------------------------------
st.header("📝 Lançamento das Notas")

PESOS = {
    "Prova Objetiva": 15,
    "Prova Dissertativa": 30,
    "Trabalho 1": 10/3,
    "Trabalho 2": 10/3,
    "Trabalho 3": 10/3,
    "Entrega Final": 15,

    # Habilidades
    "Cognitivo": 10,

    # Atitudes
    "Autogestão": 2.5,
    "Autonomia": 2.5,
    "Protagonismo": 2.5,
    "Interação": 2.5,

    # Avaliação 360
    "Autoavaliação": 3,
    "Equipe (360)": 3,
    "Professor (360)": 24,
}

notas = {}
total = 0
restantes = {}

st.write("Marque apenas o que você já recebeu nota:")

for item, peso in PESOS.items():
    col1, col2 = st.columns([2, 1])
    with col1:
        incluir = st.checkbox(item)
    if incluir:
        with col2:
            nota = st.number_input(f"{item} (0-100%)", min_value=0.0, max_value=100.0, step=1.0, key=item)
        pontos = (nota / 100) * peso
        notas[item] = pontos
        total += pontos
    else:
        restantes[item] = peso

# -------------------------------------------------------------------
# RESULTADO
# -------------------------------------------------------------------
st.divider()
st.header("📊 Resultado Final")

st.write(f"### Sua pontuação atual: **{total:.2f} / 100**")

if total >= 70:
    st.success("🎉 Você atingiu a meta de **70 pontos**! Aprovada!")
else:
    falta = 70 - total
    st.warning(f"⚠ Ainda faltam **{falta:.2f} pontos** para chegar a 70.")

# --------------------------------
