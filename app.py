# ============================================================
# CONSÓRCIO ALPHA ENGINE
# app.py
# Interface Streamlit
# ============================================================

import streamlit as st
from engine.calculator import analyze_opportunity
from engine.report import executive_report
from engine.validator import validate_opportunity


st.set_page_config(
    page_title="Consórcio Alpha Engine",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Consórcio Alpha Engine")
st.caption("Analisador prático de cotas de consórcio em andamento")

st.divider()

col1, col2 = st.columns(2)

with col1:
    tipo = st.selectbox("Tipo", ["IMOVEL", "VEICULO", "SERVICOS"])
    administradora = st.text_input("Administradora", "NAO INFORMADA")
    grupo = st.text_input("Grupo", "0001")
    valor_carta = st.number_input("Valor da carta", min_value=0.0, value=300000.0, step=1000.0)
    prazo_total = st.number_input("Prazo total", min_value=1, value=180, step=1)
    parcela_atual = st.number_input("Parcela atual", min_value=1, value=74, step=1)
    valor_parcela = st.number_input("Valor da parcela", min_value=0.0, value=2500.0, step=100.0)

with col2:
    saldo_devedor = st.number_input("Saldo devedor", min_value=0.0, value=210000.0, step=1000.0)
    valor_pedido = st.number_input("Valor pedido pelo vendedor", min_value=0.0, value=37000.0, step=1000.0)
    valor_imovel = st.number_input("Valor estimado do imóvel", min_value=0.0, value=320000.0, step=1000.0)
    valor_revenda = st.number_input("Valor estimado de revenda", min_value=0.0, value=320000.0, step=1000.0)
    taxa_transferencia = st.number_input("Taxa de transferência", min_value=0.0, value=1500.0, step=100.0)
    custos_operacionais = st.number_input("Custos operacionais", min_value=0.0, value=17000.0, step=500.0)
    prob_contemplacao = st.slider("Probabilidade estimada de contemplação", 0.0, 1.0, 0.75, 0.01)

custo_oportunidade = st.slider(
    "Custo de oportunidade anual",
    0.0,
    0.30,
    0.105,
    0.005
)

st.divider()

if st.button("ANALISAR OPORTUNIDADE", use_container_width=True):

    dados = {
        "tipo": tipo,
        "administradora": administradora,
        "grupo": grupo,
        "valor_carta": valor_carta,
        "prazo_total": prazo_total,
        "parcela_atual": parcela_atual,
        "valor_parcela": valor_parcela,
        "saldo_devedor": saldo_devedor,
        "valor_pedido": valor_pedido,
        "valor_imovel": valor_imovel,
        "valor_revenda": valor_revenda,
        "taxa_transferencia": taxa_transferencia,
        "custos_operacionais": custos_operacionais,
        "prob_contemplacao": prob_contemplacao,
        "custo_oportunidade": custo_oportunidade,
    }

    alertas = validate_opportunity(dados)

    if alertas:
        st.error("Corrija os dados antes de analisar.")
        for alerta in alertas:
            st.warning(alerta)
    else:
        resultado = analyze_opportunity(dados)

        st.subheader("Resultado da Análise")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Decisão", resultado["decisao"])
        c2.metric("Score", f"{resultado['score']}/100")
        c3.metric("ROI", f"{resultado['roi']:.2%}")
        c4.metric("Lucro estimado", f"R$ {resultado['lucro_liquido']:,.2f}")

        st.divider()

        c5, c6, c7 = st.columns(3)

        c5.metric("Preço ideal", f"R$ {resultado['preco_ideal']:,.2f}")
        c6.metric("Preço máximo", f"R$ {resultado['preco_maximo']:,.2f}")
        c7.metric("Valor pedido", f"R$ {resultado['valor_pedido']:,.2f}")

        st.divider()

        st.write("### Diagnóstico")
        for motivo in resultado["motivos"]:
            st.write(f"✅ {motivo}")

        st.write("### Regra prática")

        if resultado["decisao"] in ["COMPRAR IMEDIATAMENTE", "COMPRAR"]:
            st.success(
                f"Comprar somente se pagar até R$ {resultado['preco_maximo']:,.2f}."
            )
        elif resultado["decisao"] == "NEGOCIAR":
            st.warning(
                f"Negociar. Tente comprar próximo de R$ {resultado['preco_ideal']:,.2f}."
            )
        else:
            st.error("Não comprar esta oportunidade nas condições atuais.")
