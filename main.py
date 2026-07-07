# ============================================================
# CONSÓRCIO ALPHA ENGINE
# main.py
# Motor Principal
# ============================================================

from engine.validator import validate_opportunity
from engine.calculator import analyze_opportunity
from engine.report import executive_report


# ============================================================
# MOTOR PRINCIPAL
# ============================================================

def run_engine(dados):

    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("MOTOR PRINCIPAL")
    print("=" * 80)

    # --------------------------------------------------------
    # VALIDAÇÃO DOS DADOS
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # EXECUTA O MOTOR
    # --------------------------------------------------------

    resultado = analyze_opportunity(dados)

    # --------------------------------------------------------
    # RELATÓRIO
    # --------------------------------------------------------

    executive_report(resultado)

    print("=" * 80)
    print("PROCESSAMENTO FINALIZADO")
    print("=" * 80)

    return resultado


# ============================================================
# TESTE LOCAL
# ============================================================

if __name__ == "__main__":

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

        "custo_oportunidade": 0.105

    }

    run_engine(oportunidade)
