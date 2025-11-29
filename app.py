import streamlit as st

st.set_page_config(page_title="Cálculo de Nota", page_icon="📘")

st.title("📘 Calculadora de Notas – Versão Mobile")
st.markdown("Preencha somente as notas que você já recebeu. Marque a caixa antes de digitar a nota.")

META = 70

# Pesos oficiais
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

notas = {}
total = 0
pesos_abertos = {}

st.subheader("Lançamento de Notas")

for item, peso in PESOS.items():
    usar = st.checkbox(f"Lançar nota de {item}?", key=f"check_{item}")

    if usar:
        nota = st.number_input(
            f"Nota de {item} (0 a 100)",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key=f"nota_{item}"
        )
        pontos = (nota / 100) * peso
        notas[item] = pontos
        total += pontos
    else:
        pesos_abertos[item] = peso


st.subheader("Resultado")

st.write(f"**Sua nota atual:** {total:.2f}")

if total >= META:
    st.success("🎉 Você já atingiu a meta para aprovação!")
else:
    falta = META - total
    st.warning(f"Faltam **{falta:.2f} pontos** para atingir 70.")

    st.subheader("Oportunidades restantes")
    for item, valor in pesos_abertos.items():
        st.write(f"• {item}: até **{valor} pontos** possíveis")

    possivel = sum(pesos_abertos.values())
    st.info(f"✨ Total ainda possível: **{possivel} pontos**")

    if possivel >= falta:
        st.success("💡 Ainda dá para passar! Continue preenchendo o que falta.")
    else:
        st.error("⚠ Mesmo com tudo, talvez não alcance 70. Consulte a professora para atividades extras.")
