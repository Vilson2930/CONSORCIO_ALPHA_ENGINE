# ============================================================
# CONSÓRCIO ALPHA ENGINE
# engine/market_intelligence.py
# Inteligência de Mercado
# ============================================================

import pandas as pd


def market_summary(df):
    """
    Gera estatísticas estratégicas sobre as oportunidades analisadas.
    """

    if df.empty:
        return {}

    resumo = {
        "total_oportunidades": len(df),
        "score_medio": round(df["score"].mean(), 2),
        "roi_medio": round(df["roi"].mean() * 100, 2),
        "lucro_medio": round(df["lucro_liquido"].mean(), 2),
        "melhor_score": round(df["score"].max(), 2),
        "melhor_roi": round(df["roi"].max() * 100, 2),
        "maior_lucro": round(df["lucro_liquido"].max(), 2),
    }

    return resumo


def opportunities_by_decision(df):
    """
    Conta quantas oportunidades existem por decisão.
    """

    if df.empty or "decisao" not in df.columns:
        return pd.DataFrame()

    return (
        df.groupby("decisao")
        .size()
        .reset_index(name="quantidade")
        .sort_values("quantidade", ascending=False)
    )


def opportunities_by_administrator(df):
    """
    Mostra quais administradoras aparecem com melhores oportunidades.
    """

    if df.empty or "administradora" not in df.columns:
        return pd.DataFrame()

    return (
        df.groupby("administradora")
        .agg(
            quantidade=("administradora", "count"),
            score_medio=("score", "mean"),
            roi_medio=("roi", "mean"),
            lucro_medio=("lucro_liquido", "mean"),
        )
        .reset_index()
        .sort_values("score_medio", ascending=False)
    )


def best_opportunities(df, top=10):
    """
    Retorna as melhores oportunidades do ranking.
    """

    if df.empty:
        return pd.DataFrame()

    return (
        df.sort_values(
            by=["score", "roi", "lucro_liquido"],
            ascending=[False, False, False],
        )
        .head(top)
        .reset_index(drop=True)
    )


def rejected_opportunities(df):
    """
    Lista oportunidades rejeitadas.
    """

    if df.empty or "decisao" not in df.columns:
        return pd.DataFrame()

    return df[df["decisao"].str.contains("NÃO|EVITAR", na=False)]


def intelligence_report(df):
    """
    Relatório simples de inteligência de mercado.
    """

    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("INTELIGÊNCIA DE MERCADO")
    print("=" * 80)

    if df.empty:
        print("Nenhuma oportunidade analisada.")
        return

    resumo = market_summary(df)

    print(f"Total de oportunidades.......: {resumo['total_oportunidades']}")
    print(f"Score médio..................: {resumo['score_medio']}")
    print(f"ROI médio....................: {resumo['roi_medio']}%")
    print(f"Lucro médio..................: R$ {resumo['lucro_medio']:,.2f}")
    print(f"Melhor score.................: {resumo['melhor_score']}")
    print(f"Melhor ROI...................: {resumo['melhor_roi']}%")
    print(f"Maior lucro..................: R$ {resumo['maior_lucro']:,.2f}")

    print("-" * 80)
    print("TOP 5 OPORTUNIDADES")
    print("-" * 80)

    top = best_opportunities(df, top=5)

    colunas = [
        "ranking",
        "administradora",
        "grupo",
        "score",
        "decisao",
        "roi",
        "lucro_liquido",
        "preco_maximo",
    ]

    colunas_existentes = [c for c in colunas if c in top.columns]

    print(top[colunas_existentes].to_string(index=False))

    print("=" * 80)
