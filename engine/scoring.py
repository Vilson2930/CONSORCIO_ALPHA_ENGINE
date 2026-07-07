# ============================================================
# CONSÓRCIO ALPHA ENGINE
# engine/scoring.py
# Motor de Score Institucional
# ============================================================

def calculate_score(
    agio_desagio_pct,
    roi,
    prob_contemplacao,
    tempo_economizado_meses,
    lucro_liquido
):
    """
    Calcula o Score Institucional (0 a 100)
    """

    score = 100

    # =========================================================
    # PREÇO DA COTA
    # =========================================================

    if agio_desagio_pct > 0.30:
        score -= 40

    elif agio_desagio_pct > 0.15:
        score -= 25

    elif agio_desagio_pct > 0:
        score -= 10

    elif agio_desagio_pct < -0.30:
        score += 10

    elif agio_desagio_pct < -0.15:
        score += 5

    # =========================================================
    # ROI
    # =========================================================

    if roi < 0:
        score -= 35

    elif roi < 0.05:
        score -= 20

    elif roi < 0.10:
        score -= 10

    elif roi > 0.20:
        score += 8

    elif roi > 0.15:
        score += 5

    # =========================================================
    # PROBABILIDADE DE CONTEMPLAÇÃO
    # =========================================================

    if prob_contemplacao < 0.40:
        score -= 20

    elif prob_contemplacao < 0.60:
        score -= 10

    elif prob_contemplacao > 0.85:
        score += 8

    elif prob_contemplacao > 0.75:
        score += 5

    # =========================================================
    # TEMPO ECONOMIZADO
    # =========================================================

    if tempo_economizado_meses >= 100:
        score += 10

    elif tempo_economizado_meses >= 60:
        score += 5

    elif tempo_economizado_meses <= 12:
        score -= 10

    # =========================================================
    # LUCRO
    # =========================================================

    if lucro_liquido < 0:
        score -= 40

    elif lucro_liquido > 50000:
        score += 10

    elif lucro_liquido > 20000:
        score += 5

    # =========================================================

    score = max(0, min(100, score))

    return round(score, 1)


# ============================================================
# CLASSIFICAÇÃO DO PREÇO
# ============================================================

def classify_price(agio_desagio_pct):

    if agio_desagio_pct <= -0.30:
        return "DESÁGIO EXCELENTE"

    elif agio_desagio_pct <= -0.15:
        return "DESÁGIO BOM"

    elif agio_desagio_pct <= -0.05:
        return "DESÁGIO PEQUENO"

    elif agio_desagio_pct < 0.05:
        return "PREÇO JUSTO"

    elif agio_desagio_pct < 0.15:
        return "ÁGIO MODERADO"

    elif agio_desagio_pct < 0.30:
        return "ÁGIO ALTO"

    return "ÁGIO EXCESSIVO"


# ============================================================
# DECISÃO FINAL
# ============================================================

def classify_decision(score, lucro_liquido):

    if lucro_liquido <= 0:
        return "NÃO COMPRAR"

    if score >= 90:
        return "COMPRAR IMEDIATAMENTE"

    elif score >= 80:
        return "COMPRAR"

    elif score >= 70:
        return "NEGOCIAR"

    elif score >= 60:
        return "ANALISAR MELHOR"

    return "NÃO COMPRAR"


# ============================================================
# SEMÁFORO
# ============================================================

def traffic_light(score):

    if score >= 80:
        return "🟢 VERDE"

    elif score >= 60:
        return "🟡 AMARELO"

    return "🔴 VERMELHO"


# ============================================================
# GRAU DE CONFIANÇA
# ============================================================

def confidence(score):

    if score >= 90:
        return "MUITO ALTA"

    elif score >= 80:
        return "ALTA"

    elif score >= 70:
        return "BOA"

    elif score >= 60:
        return "MÉDIA"

    return "BAIXA"
