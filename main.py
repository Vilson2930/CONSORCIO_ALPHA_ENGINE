# ============================================================
# CONSÓRCIO ALPHA ENGINE
# main.py
# Motor Principal
# ============================================================

from engine.validator import validate_opportunity
from engine.calculator import analyze_opportunity
from engine.report import executive_report
from engine.scanner import (
    scan_opportunities,
    load_opportunities_from_csv,
    save_ranking,
)
from engine.dashboard import show_dashboard
from engine.market_intelligence import intelligence_report


# ============================================================
# ANÁLISE DE UMA ÚNICA OPORTUNIDADE
# ============================================================

def run_engine(dados):

    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("ANÁLISE INDIVIDUAL")
    print("=" * 80)

    alertas = validate_opportunity(dados)

    if len(alertas) > 0:
        print()
        print("ERROS ENCONTRADOS")
        print("-" * 80)

        for alerta in alertas:
            print(f"• {alerta}")

        print()
        print("ANÁLISE CANCELADA")
        print("=" * 80)

        return None

    print("Validação..................: OK")

    resultado = analyze_opportunity(dados)

    executive_report(resultado)

    print("=" * 80)
    print("PROCESSAMENTO FINALIZADO")
    print("=" * 80)

    return resultado


# ============================================================
# SCANNER DE VÁRIAS OPORTUNIDADES
# ============================================================

def run_scanner(
    input_path="data/oportunidades.csv",
    output_path="data/ranking.csv"
):

    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("SCANNER DE OPORTUNIDADES")
    print("=" * 80)

    oportunidades = load_opportunities_from_csv(input_path)

    ranking = scan_opportunities(oportunidades)

    if ranking.empty:
        print("Nenhuma oportunidade válida encontrada.")
        return ranking

    save_ranking(ranking, output_path)

    show_dashboard(ranking)

    intelligence_report(ranking)

    print()
    print(f"Ranking salvo em.............: {output_path}")
    print("=" * 80)
    print("SCANNER FINALIZADO")
    print("=" * 80)

    return ranking


# ============================================================
# TESTE LOCAL
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # 1. TESTE INDIVIDUAL
    # --------------------------------------------------------

    oportunidade = {
        "tipo": "IMOVEL",
        "administradora": "NAO INFORMADA",
        "grupo": "0001",
        "valor_carta": 300000.00,
        "prazo_total": 180,
        "parcela_atual": 74,
        "valor_parcela": 2500.00,
        "saldo_devedor": 210000.00,
        "valor_pedido": 37000.00,
        "valor_imovel": 320000.00,
        "valor_revenda": 320000.00,
        "taxa_transferencia": 1500.00,
        "custos_operacionais": 17000.00,
        "prob_contemplacao": 0.75,
        "custo_oportunidade": 0.105,
    }

    run_engine(oportunidade)

    # --------------------------------------------------------
    # 2. TESTE DO SCANNER
    # --------------------------------------------------------

    run_scanner()
