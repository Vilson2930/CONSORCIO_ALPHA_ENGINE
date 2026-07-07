# ============================================================
# CONSÓRCIO ALPHA ENGINE
# engine/scanner.py
# Scanner de múltiplas oportunidades
# ============================================================

import pandas as pd

from engine.validator import validate_opportunity
from engine.calculator import analyze_opportunity


def scan_opportunities(oportunidades):
    """
    Analisa várias oportunidades e cria um ranking.

    Entrada:
        oportunidades: lista de dicionários

    Saída:
        DataFrame ordenado por score, ROI e lucro.
    """

    resultados = []

    for i, dados in enumerate(oportunidades, start=1):

        alertas = validate_opportunity(dados)

        if len(alertas) > 0:
            resultados.append({
                "ranking": None,
                "id": dados.get("id", f"OPORTUNIDADE_{i}"),
                "tipo": dados.get("tipo", "N/A"),
                "administradora": dados.get("administradora", "N/A"),
                "grupo": dados.get("grupo", "N/A"),
                "score": 0,
                "decisao": "ERRO NOS DADOS",
                "lucro_liquido": 0,
                "roi": 0,
                "preco_maximo": 0,
                "preco_ideal": 0,
                "valor_pedido": dados.get("valor_pedido", 0),
                "alertas": "; ".join(alertas)
            })
            continue

        resultado = analyze_opportunity(dados)

        resultados.append({
            "ranking": None,
            "id": dados.get("id", f"OPORTUNIDADE_{i}"),
            "tipo": resultado["tipo"],
            "administradora": resultado["administradora"],
            "grupo": resultado["grupo"],
            "score": resultado["score"],
            "decisao": resultado["decisao"],
            "lucro_liquido": resultado["lucro_liquido"],
            "roi": resultado["roi"],
            "preco_maximo": resultado["preco_maximo"],
            "preco_ideal": resultado["preco_ideal"],
            "valor_pedido": resultado["valor_pedido"],
            "valor_economico_cota": resultado["valor_economico_cota"],
            "custo_por_1_real_credito": resultado["custo_por_1_real_credito"],
            "classificacao_preco": resultado["classificacao_preco"],
            "alertas": ""
        })

    df = pd.DataFrame(resultados)

    if df.empty:
        return df

    df = (
        df.sort_values(
            by=["score", "roi", "lucro_liquido"],
            ascending=[False, False, False]
        )
        .reset_index(drop=True)
    )

    df["ranking"] = df.index + 1

    return df


def load_opportunities_from_csv(path):
    """
    Carrega oportunidades a partir de um CSV.
    """

    df = pd.read_csv(path)

    oportunidades = df.to_dict(orient="records")

    return oportunidades


def save_ranking(df, path="data/historico.csv"):
    """
    Salva o ranking em CSV.
    """

    df.to_csv(path, index=False, encoding="utf-8-sig")

    return path


# ============================================================
# TESTE LOCAL
# ============================================================

if __name__ == "__main__":

    oportunidades_teste = [
        {
            "id": "COTA_01",
            "tipo": "IMOVEL",
            "administradora": "NAO INFORMADA",
            "grupo": "0001",
            "valor_carta": 300000,
            "prazo_total": 180,
            "parcela_atual": 74,
            "valor_parcela": 2500,
            "saldo_devedor": 210000,
            "valor_pedido": 37000,
            "valor_imovel": 320000,
            "valor_revenda": 320000,
            "taxa_transferencia": 1500,
            "custos_operacionais": 17000,
            "prob_contemplacao": 0.75,
            "custo_oportunidade": 0.105
        },
        {
            "id": "COTA_02",
            "tipo": "IMOVEL",
            "administradora": "NAO INFORMADA",
            "grupo": "0002",
            "valor_carta": 500000,
            "prazo_total": 200,
            "parcela_atual": 95,
            "valor_parcela": 3500,
            "saldo_devedor": 335000,
            "valor_pedido": 62000,
            "valor_imovel": 455000,
            "valor_revenda": 535000,
            "taxa_transferencia": 2000,
            "custos_operacionais": 28000,
            "prob_contemplacao": 0.75,
            "custo_oportunidade": 0.105
        }
    ]

    ranking = scan_opportunities(oportunidades_teste)

    print("=" * 80)
    print("RANKING DAS OPORTUNIDADES")
    print("=" * 80)
    print(ranking)
