# ============================================================
# CONSÓRCIO ALPHA ENGINE
# app.py
# Interface Principal
# ============================================================

import streamlit as st

st.set_page_config(
    page_title="Consórcio Alpha Engine",
    page_icon="🏠",
    layout="wide"
)

# ============================================================
# CABEÇALHO
# ============================================================

st.title("🏠 CONSÓRCIO ALPHA ENGINE")
st.caption("Motor Institucional para Análise de Consórcios")

st.divider()

# ============================================================
# DADOS DA OPORTUNIDADE
# ============================================================

st.subheader("Nova Oportunidade")

col1, col2 = st.columns(2)

with col1:

    tipo = st.selectbox(
        "Tipo",
        [
            "IMÓVEL",
            "VEÍCULO",
            "SERVIÇOS"
        ]
    )

    administradora = st.text_input(
        "Administradora"
    )

    grupo = st.text_input(
        "Grupo"
    )

    valor_carta = st.number_input(
        "Valor da Carta",
        min_value=0.0,
        step=1000.0
    )

    prazo_total = st.number_input(
        "Prazo Total",
        min_value=1,
        step=1
    )

    parcela_atual = st.number_input(
        "Parcela Atual",
        min_value=1,
        step=1
    )

with col2:

    valor_parcela = st.number_input(
        "Valor da Parcela",
        min_value=0.0,
        step=100.0
    )

    saldo_devedor = st.number_input(
        "Saldo Devedor",
        min_value=0.0,
        step=1000.0
    )

    valor_pedido = st.number_input(
        "Valor Pedido pelo Vendedor",
        min_value=0.0,
        step=1000.0
    )

    valor_imovel = st.number_input(
        "Valor Atual do Imóvel",
        min_value=0.0,
        step=1000.0
    )

    valor_revenda = st.number_input(
        "Valor Estimado de Revenda",
        min_value=0.0,
        step=1000.0
    )

st.divider()

# ============================================================
# BOTÃO
# ============================================================

if st.button(
    "ANALISAR OPORTUNIDADE",
    use_container_width=True
):

    st.success("Dados enviados ao motor de análise.")

    st.info(
        "Na próxima etapa o Calculator Engine processará automaticamente esta oportunidade."
    )

st.divider()

st.caption("Consórcio Alpha Engine ©")
