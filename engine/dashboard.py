# ============================================================
# CONSÓRCIO ALPHA ENGINE
# dashboard.py
# Painel Executivo
# ============================================================

import pandas as pd


def show_dashboard(df):

    print()
    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("DASHBOARD EXECUTIVO")
    print("=" * 80)

    if df.empty:

        print("Nenhuma oportunidade encontrada.")
        return

    total = len(df)

    comprar = len(df[df["decisao"].str.contains("COMPRAR", na=False)])

    negociar = len(df[df["decisao"].str.contains("NEGOCIAR", na=False)])

    analisar = len(df[df["decisao"].str.contains("ANALISAR", na=False)])

    evitar = total - comprar - negociar - analisar

    print(f"Oportunidades analisadas.....: {total}")
    print(f"Comprar......................: {comprar}")
    print(f"Negociar.....................: {negociar}")
    print(f"Analisar melhor..............: {analisar}")
    print(f"Evitar.......................: {evitar}")

    print("-" * 80)

    melhor = df.iloc[0]

    print("MELHOR OPORTUNIDADE")

    print(f"ID...........................: {melhor['id']}")
    print(f"Tipo.........................: {melhor['tipo']}")
    print(f"Grupo........................: {melhor['grupo']}")
    print(f"Administradora...............: {melhor['administradora']}")
    print(f"Score........................: {melhor['score']}")
    print(f"Decisão......................: {melhor['decisao']}")
    print(f"ROI..........................: {melhor['roi']:.2%}")
    print(f"Lucro estimado...............: R$ {melhor['lucro_liquido']:,.2f}")

    print("-" * 80)

    print("TOP 5 OPORTUNIDADES")

    colunas = [
        "ranking",
        "id",
        "score",
        "decisao",
        "roi",
        "lucro_liquido"
    ]

    print(df[colunas].head(5).to_string(index=False))

    print("=" * 80)
