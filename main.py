# ============================================================
# CONSÓRCIO ALPHA ENGINE
# main.py
# Motor Principal
# ============================================================

from engine.calculator import analyze_opportunity
from engine.report import executive_report


def run_engine(dados):

    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("=" * 80)

    # -------------------------------------------------------
    # EXECUTA O MOTOR
    # -------------------------------------------------------

    resultado = analyze_opportunity(dados)

    # -------------------------------------------------------
    # RELATÓRIO
    # -------------------------------------------------------

    executive_report(resultado)

    return resultado


# ============================================================
# TESTE LOCAL
# ============================================================

if __name__ == "__main__":

    oportunidade = {

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

        "valor_revenda": 320000

    }

    run_engine(oportunidade)
