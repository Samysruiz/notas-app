import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# =======================
# CONFIGURAÇÃO DO APP
# =======================
st.set_page_config(page_title="Cálculo de Nota – Modo Sábio", page_icon="🧘‍♀️", layout="centered")

st.title("🧘‍♀️ Calculadora de Notas – Modo Sábio")
st.markdown(
    "<p style='font-size:18px; opacity:0.8; font-style:italic;'>"
    "“O caminho se revela para quem caminha.” – Lao Tsé"
    "</p>",
    unsafe_allow_html=True,
)

# =======================
# FRASES SÁBIAS
# =======================
FRASES_SABIAS = [
    "“A água vence pela suavidade.” – Lao Tsé",
    "“Você se torna aquilo que repete.” – Aristóteles",
    "“O progresso é a realização do impossível.” – Marie Curie",
    "“A serenidade é a força dos que persistem.” – Sêneca",
    "“Nada floresce sem disciplina.” – Confúcio",
]
st.caption(random.choice(FRASES_SABIAS))

META_DEFAULT = 70

# =======================
# PESOS OFICIAIS
# =======================
PESOS_FIXOS = {
    "Prova Objetiva": 15,
    "Prova Dissertativa": 30,
    "Projeto Final": 15,
    "Avaliação 360": 2.5,
    "Habilidades Cognitivas": 10,
    "Construção da Escrita": 10,
    "Autogestão": 2.5,
    "Protagonismo": 2.5,
    "Interação": 2.5,
}

# =======================
# NÚMERO DE TRABALHOS
# =======================
st.subheader("📘 Configuração da Disciplina")
qt_trabalhos = st.number_input("Quantos trabalhos existem?", min_value=0, max_value=10, value=3)

PESOS = PESOS_FIXOS.copy()
for i in range(1, qt_trabalhos + 1):
    PESOS[f"Trabalho {i}"] = 10

# =======================
# LANÇAMENTO DE NOTAS
# =======================
st.subheader("✏️ Lançamento de Notas")

notas_lancadas = {}
total = 0
pesos_abertos = {}

for item, peso in PESOS.items():
    usar = st.checkbox(f"Lançar nota de {item}?", key=f"check_{item}")
    if usar:
        nota = st.number_input(
            f"Nota de {item} (0 a 100)",
            min_value=0.0, max_value=100.0, step=1.0, key=f"nota_{item}"
        )
        pontos = (nota / 100) * peso
        notas_lancadas[item] = pontos
        total += pontos
    else:
        pesos_abertos[item] = peso

# =======================
# RESULTADO
# =======================
st.subheader("📊 Sua Nota Atual")
st.write(f"**{total:.2f} pontos**")

# =======================
# GRÁFICO DE PROGRESSO
# =======================
fig, ax = plt.subplots(figsize=(5, 2))
ax.barh(["Progresso"], [min(total, META_DEFAULT)], color="#6699ff")
ax.barh(["Progresso"], [META_DEFAULT], alpha=0.2, color="#cccccc")
ax.set_xlim(0, META_DEFAULT)
ax.set_xlabel("Pontos")
st.pyplot(fig)

# =======================
# SIMULADOR COMPLETO (APENAS)
# =======================
st.subheader("🔁 Simulador Completo de Caminhos Possíveis")

if pesos_abertos:
    falta = max(META_DEFAULT - total, 0)
    st.write(f"Pontos necessários para atingir 70: **{falta:.2f}**")

    st.markdown("### Caminho mínimo (usar só o essencial)")
    pesos_sorted = sorted(pesos_abertos.items(), key=lambda x: x[1], reverse=True)

    restante = falta
    min_require = {}

    for item, peso in pesos_sorted:
        if restante <= 0:
            break
        usar = min(peso, restante)
        min_require[item] = usar
        restante -= usar

    for item, val in min_require.items():
        st.write(f"• {item}: **{val:.2f} pts**")

    if restante > 0:
        st.error("Mesmo no caminho mínimo, não é possível atingir 70.")

    st.markdown("### Caminho ótimo (melhor distribuição)")
    melhor = {}
    total_pesos = sum(pesos_abertos.values())

    if total_pesos > 0:
        for item, peso in pesos_abertos.items():
            proporcao = peso / total_pesos
            melhor[item] = proporcao * falta

        for item, val in melhor.items():
            st.write(f"• {item}: ideal **{val:.2f} pts**")

    st.markdown("### Margem de Segurança")
    sobra = total_pesos - falta
    st.write(f"Você ainda pode somar **{sobra:.2f} pontos** acima do mínimo.")

else:
    st.info("Nenhuma atividade restante disponível para simulação.")

# =======================
# FRASE FINAL
# =======================
st.markdown("---")
st.markdown(
    "<p style='font-size:16px; opacity:0.8; font-style:italic; text-align:center;'>"
    "“A luz se revela a quem permanece.” – Rumi"
    "</p>",
    unsafe_allow_html=True,
)
