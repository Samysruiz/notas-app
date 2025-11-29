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
    "Construção da Escrita": 10,
    "Autogestão": 2.5,
    "Protagonismo": 2.5,
    "Interação": 2.5,
}

# Escolher número de trabalhos
qt_trabalhos = st.number_input("Quantos trabalhos existem?", min_value=0, max_value=10, value=3, step=1)

PESOS = PESOS_FIXOS.copy()

for i in range(1, qt_trabalhos + 1):
    PESOS[f"Trabalho {i}"] = 10


# Entradas
total = 0
pesos_abertos = {}
notas_dict = {}

st.subheader("Lançamento das Notas")

for item, peso in PESOS.items():
    usar = st.checkbox(f"Lançar nota de {item}?", key=f"check_{item}")
    
    if usar:
        nota = st.number_input(
            f"Nota de {item} (0 a 100)",
            min_value=0.0, max_value=100.0, step=1.0, key=f"nota_{item}"
        )
        pontos = (nota / 100) * peso
        notas_dict[item] = pontos
        total += pontos
    else:
        pesos_abertos[item] = peso

# Resultado
st.subheader("Resultado Final")
st.write(f"**Sua nota atual:** {total:.2f}")

# Gráfico de Progresso
st.subheader("Progresso até 70")
fig, ax = plt.subplots(figsize=(5, 2))
ax.barh(["Progresso"], [min(total, META)])
ax.barh(["Progresso"], [META], alpha=0.2)
ax.set_xlim(0, META)
ax.set_xlabel("Pontos")
st.pyplot(fig)

if total >= META:
    st.success("🎉 Você atingiu ou ultrapassou a meta de 70! Vitória redonda.")
else:
    falta = META - total
    st.warning(f"Faltam **{falta:.2f} pontos** para atingir 70.")

    st.subheader("Oportunidades restantes")
    for item, valor in pesos_abertos.items():
        st.write(f"• {item}: até **{valor} pontos** possíveis")

    possivel = sum(pesos_abertos.values())
    st.info(f"✨ Total possível ainda para ganhar: **{possivel:.2f} pontos**")

    if possivel >= falta:
        st.success("💡 Ainda dá para passar! Há caminhos abertos para os pontos que faltam.")
    else:
        st.error("⚠ Mesmo com tudo, talvez não alcance 70. Avalie conversar com a professora para atividades extras.")
