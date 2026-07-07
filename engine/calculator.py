# ============================================================
# CONSÓRCIO ALPHA ENGINE
# engine/calculator.py
# Calcula uma oportunidade individual
# ============================================================

from engine.scoring import classify_price, classify_decision, calculate_score


def safe_div(a, b):
    try:
        if b == 0:
            return 0
        return a / b
    except Exception:
        return 0


def analyze_opportunity(dados):
    """
    Analisa uma proposta de consórcio em andamento.
    Retorna um dicionário com decisão, score, preço justo,
    preço máximo, ROI e diagnóstico.
    """

    valor_carta = float(dados.get("valor_carta", 0))
    prazo_total = int(dados.get("prazo_total", 1))
    parcela_atual = int(dados.get("parcela_atual", 1))
    valor_parcela = float(dados.get("valor_parcela", 0))
    saldo_devedor = float(dados.get("saldo_devedor", 0))
    valor_pedido = float(dados.get("valor_pedido", 0))
    valor_imovel = float(dados.get("valor_imovel", 0))
    valor_revenda = float(dados.get("valor_revenda", 0))

    taxa_transferencia = float(dados.get("taxa_transferencia", 1500))
    custos_operacionais = float(dados.get("custos_operacionais", 17000))
    prob_contemplacao = float(dados.get("prob_contemplacao", 0.75))
    custo_oportunidade = float(dados.get("custo_oportunidade", 0.105))

    # --------------------------------------------------------
    # TEMPO ECONOMIZADO
    # --------------------------------------------------------

    tempo_economizado_meses = max(parcela_atual - 1, 0)
    tempo_economizado_anos = tempo_economizado_meses / 12

    valor_tempo_economizado = (
        valor_pedido
        * custo_oportunidade
        * tempo_economizado_anos
    )

    # --------------------------------------------------------
    # LUCRO DO ATIVO
    # --------------------------------------------------------

    lucro_operacional = (
        valor_revenda
        - valor_imovel
        - custos_operacionais
    )

    valor_probabilistico = lucro_operacional * prob_contemplacao

    # --------------------------------------------------------
    # VALOR ECONÔMICO DA COTA
    # --------------------------------------------------------

    valor_economico_cota = (
        valor_tempo_economizado
        + valor_probabilistico
    )

    preco_ideal = valor_economico_cota * 0.85
    preco_maximo = valor_economico_cota * 0.95

    agio_desagio_valor = valor_pedido - valor_economico_cota
    agio_desagio_pct = safe_div(agio_desagio_valor, valor_economico_cota)

    # --------------------------------------------------------
    # RESULTADO ECONÔMICO
    # --------------------------------------------------------

    custo_entrada = (
        valor_pedido
        + taxa_transferencia
    )

    capital_total = (
        custo_entrada
        + custos_operacionais
    )

    lucro_liquido = (
        valor_economico_cota
        - custo_entrada
    )

    roi = safe_div(lucro_liquido, capital_total)

    custo_por_1_real_credito = safe_div(
        saldo_devedor + custo_entrada,
        valor_carta
    )

    # --------------------------------------------------------
    # SCORE E DECISÃO
    # --------------------------------------------------------

    score = calculate_score(
        agio_desagio_pct=agio_desagio_pct,
        roi=roi,
        prob_contemplacao=prob_contemplacao,
        tempo_economizado_meses=tempo_economizado_meses,
        lucro_liquido=lucro_liquido
    )

    classificacao_preco = classify_price(agio_desagio_pct)
    decisao = classify_decision(score, lucro_liquido)

    # --------------------------------------------------------
    # DIAGNÓSTICO
    # --------------------------------------------------------

    motivos = []

    if lucro_liquido > 0:
        motivos.append("Lucro econômico positivo")
    else:
        motivos.append("Lucro econômico negativo")

    if agio_desagio_pct < 0:
        motivos.append("Cota negociada com deságio")
    else:
        motivos.append("Cota negociada com ágio")

    if roi >= 0.12:
        motivos.append("ROI atrativo")
    elif roi > 0:
        motivos.append("ROI positivo, mas moderado")
    else:
        motivos.append("ROI negativo")

    if custo_por_1_real_credito < 1:
        motivos.append("Custo por R$1 de crédito abaixo de R$1")
    else:
        motivos.append("Custo por R$1 de crédito acima de R$1")

    resultado = {
        "tipo": dados.get("tipo", "IMOVEL"),
        "administradora": dados.get("administradora", ""),
        "grupo": dados.get("grupo", ""),
        "valor_carta": valor_carta,
        "prazo_total": prazo_total,
        "parcela_atual": parcela_atual,
        "tempo_economizado_meses": tempo_economizado_meses,
        "valor_pedido": valor_pedido,
        "valor_economico_cota": valor_economico_cota,
        "preco_ideal": preco_ideal,
        "preco_maximo": preco_maximo,
        "agio_desagio_pct": agio_desagio_pct,
        "classificacao_preco": classificacao_preco,
        "lucro_liquido": lucro_liquido,
        "roi": roi,
        "capital_total": capital_total,
        "custo_por_1_real_credito": custo_por_1_real_credito,
        "score": score,
        "decisao": decisao,
        "motivos": motivos
    }

    return resultado
