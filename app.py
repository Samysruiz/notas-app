import streamlit as st

st.set_page_config(page_title="Notas", page_icon="📘")

st.title("📘 Calculadora de Notas – Versão Estável")

META = 70

PESOS = {
    "Prova Objetiva": 15,
    "Prova Dissertativa": 30,
    "Trabalho 1": 10,
    "Trabalho 2": 10,
    "Trabalho 3": 10,
    "Projeto Final": 15,
    "Avaliação 360": 2.5,
    "Habilidades Cognitivas": 10,
    "Construção da Escrita": 10,
    "Autogestão": 2.5,
    "Protagonismo": 2.5,
    "Interação": 2.5,
}

st.write("Marque cada nota que você quer lançar:")

total = 0
restantes = {}

for item, peso in PESOS.items():
    usar = st.checkbox(item)
    if usar:
        nota = st.number_input(f"Nota de {item} (0 a 100):", 0.0, 100.0, 0.0)
        total += (nota / 100) * peso
    else:
        restantes[item] = peso

st.header("Resultado")
st.write(f"Sua nota atual: **{total:.2f} pontos**")

if total >= META:
    st.success("🎉 Você atingiu a meta de 70!")
else:
    falta = META - total
    st.warning(f"Faltam **{falta:.2f} pontos** para atingir 70.")
    st.write("Atividades restantes e seus pesos:")
    for item, peso in restantes.items():
        st.write(f"- {item}: até **{peso} pontos**")
