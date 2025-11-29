import streamlit as st
import pandas as pd
import altair as alt
import random

# -------------------------------------------------------------
# CONFIGURAÇÃO DO APP
# -------------------------------------------------------------
st.set_page_config(page_title="Calculadora de Notas Biopark", page_icon="📘")

st.title("📘 Calculadora de Notas – Modelo Híbrido Biopark")
st.caption("Baseado na estrutura oficial da disciplina.")

st.divider()

# -------------------------------------------------------------
# PESOS
# -------------------------------------------------------------

# Cognitivo - total 70
PESOS_COGNITIVO = {
    "Prova Objetiva": 15,
    "Prova Dissertativa": 30,
    "Trabalho 1": 10/3,
    "Trabalho 2": 10/3,
    "Trabalho 3": 10/3,
    "Entrega Final": 15
}

# Avaliação 360 - total 30 (24 prof, 3 colegas, 3 você)
PESOS_360 = {
    "Nota da Professora (24 pts)": 24,
    "Nota dos Colegas (3 pts)": 3,
    "Autoavaliação (3 pts)": 3
}

# -------------------------------------------------------------
# LANÇAMENTO COGNITIVO
# -------------------------------------------------------------
st.header("🧠 Avaliação Cognitiva (70 pontos)")

total_cog = 0
restantes_cog = {}

for item, peso in PESOS_COGNITIVO.items():
    col1, col2 = st.columns([2, 1])
    with col1:
        usar = st.checkbox(item)
    if usar:
        with col2:
            nota = st.number_input(f"{item} (0–100%)", min_value=0.0, max_value=100.0, step=1.0, key=item)
        pontos = (nota / 100) * peso
        total_cog += pontos
    else:
        restantes_cog[item] = peso

# -------------------------------------------------------------
# LANÇAMENTO 360
# -------------------------------------------------------------
st.divider()
st.header("🔄 Avaliação 360° (30 pontos)")

total_360 = 0
restantes_360 = {}

# PROFESSORA (24 pontos)
if st.checkbox("Nota da Professora (24 pts)"):
    prof = st.number_input("Desempenho avaliado pela professora (0–100%)", 0.0, 100.0, 0.0)
    total_360 += (prof/100)*24
else:
    restantes_360["Professora"] = 24

# COLEGAS (3 pontos)
if st.checkbox("Nota dos Colegas (3 pts)"):
    colegas = st.number_input("Nota dada pelos colegas (0–100%)", 0.0, 100.0, 0.0)
    total_360 += (colegas/100)*3
else:
    restantes_360["Colegas"] = 3

# AUTOAVALIAÇÃO (3 pontos)
if st.checkbox("Autoavaliação (3 pts)"):
    auto = st.number_input("Sua autoavaliação (0–100%)", 0.0, 100.0, 0.0)
    total_360 += (auto/100)*3
else:
    restantes_360["Autoavaliação"] = 3

# -------------------------------------------------------------
# RESULTADO FINAL
# -------------------------------------------------------------
st.divider()
st.header("📊 Resultado Geral")

total_final = total_cog + total_360

st.write(f"### 🔵 Sua pontuação atual: **{total_final:.2f} / 100**")

if total_final >= 70:
    st.success("🎉 Parabéns! Você já atingiu a meta de **70 pontos** e está aprovada!")
else:
    falta = 70 - total_final
    st.warning(f"⚠️ Ainda faltam **{falta:.2f} pontos** para atingir 70.")

# -------------------------------------------------------------
# OPORTUNIDADES RESTANTES
# -------------------------------------------------------------
st.divider()
st.header("📌 Oportunidades Restantes e Pontos Possíveis")

total_restante = sum(restantes_cog.values()) + sum(restantes_360.values())

st.write(f"Você ainda pode ganhar: **{total_restante:.2f} pontos**")

st.subheader("Itens faltantes:")

if len(restantes_cog) == 0 and len(restantes_360) == 0:
    st.info("Você já lançou todas as notas disponíveis.")
else:
    for item, peso in restantes_cog.items():
        st.write(f"- {item}: **{peso:.2f} pts**")
    for item, peso in restantes_360.items():
        st.write(f"- {item}: **{peso:.2f} pts**")

if total_final < 70 and total_restante >= (70 - total_final):
    st.success("💡 É possível atingir os 70 pontos com as atividades restantes!")
elif total_final < 70:
    st.error("❌ Mesmo com tudo, talvez não alcance 70. Avalie conversar com a professora.")

# -------------------------------------------------------------
# GRÁFICO
# -------------------------------------------------------------
st.divider()
st.header("📈 Progresso Visual")

df = pd.DataFrame({
    "Categoria": ["Sua Nota", "Meta (70)"],
    "Pontos": [total_final, 70]
})

chart = (
    alt.Chart(df)
    .mark_bar(size=60)
    .encode(
        x="Categoria:N",
        y="Pontos:Q",
        color="Categoria:N"
    )
)

st.altair_chart(chart, use_container_width=True)

# -------------------------------------------------------------
# FRASE MOTIVACIONAL
# -------------------------------------------------------------
FRASES = [
    "“Cada ponto conquistado é uma pequena vitória sobre o ontem.”",
    "“Você não está longe — só falta o último empurrão.”",
    "“Sua trajetória é maior do que qualquer prova.”",
    "“A constância sempre abre portas que a pressa não vê.”",
    "“Um pouco por dia vira muito no final.”"
]

st.info(random.choice(FRASES))
