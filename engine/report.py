# ============================================================
# CONSÓRCIO ALPHA ENGINE
# engine/report.py
# Relatório Executivo
# ============================================================

from engine.scoring import traffic_light, confidence


def executive_report(resultado):

    print("\n")
    print("=" * 80)
    print("CONSÓRCIO ALPHA ENGINE")
    print("RELATÓRIO EXECUTIVO")
    print("=" * 80)

    print(f"Tipo.......................: {resultado['tipo']}")
    print(f"Administradora............: {resultado['administradora']}")
    print(f"Grupo.....................: {resultado['grupo']}")

    print("-" * 80)

    print(f"Valor da carta............: R$ {resultado['valor_carta']:,.2f}")
    print(f"Parcela atual.............: {resultado['parcela_atual']}")
    print(f"Tempo economizado.........: {resultado['tempo_economizado_meses']} meses")

    print("-" * 80)

    print(f"Valor pedido..............: R$ {resultado['valor_pedido']:,.2f}")
    print(f"Preço ideal...............: R$ {resultado['preco_ideal']:,.2f}")
    print(f"Preço máximo..............: R$ {resultado['preco_maximo']:,.2f}")

    print("-" * 80)

    print(f"Lucro esperado............: R$ {resultado['lucro_liquido']:,.2f}")
    print(f"ROI.......................: {resultado['roi']:.2%}")
    print(f"Custo por R$1............: R$ {resultado['custo_por_1_real_credito']:.2f}")

    print("-" * 80)

    print(f"Classificação preço.......: {resultado['classificacao_preco']}")
    print(f"Score.....................: {resultado['score']}/100")
    print(f"Semáforo.................: {traffic_light(resultado['score'])}")
    print(f"Confiança................: {confidence(resultado['score'])}")

    print("-" * 80)

    print(f"DECISÃO FINAL............: {resultado['decisao']}")

    print("\n")

    print("DIAGNÓSTICO")

    for motivo in resultado["motivos"]:
        print(f"✓ {motivo}")

    print("\n")

    print("REGRA PRÁTICA")

    if resultado["decisao"] == "COMPRAR IMEDIATAMENTE":

        print("Comprar imediatamente.")
        print(f"Não pagar acima de R$ {resultado['preco_maximo']:,.2f}")

    elif resultado["decisao"] == "COMPRAR":

        print("Comprar se conseguir negociar.")
        print(f"Preço ideal: R$ {resultado['preco_ideal']:,.2f}")

    elif resultado["decisao"] == "NEGOCIAR":

        print("Negocie antes de fechar.")
        print(f"Tente comprar próximo de R$ {resultado['preco_ideal']:,.2f}")

    elif resultado["decisao"] == "ANALISAR MELHOR":

        print("Reavalie o negócio antes da compra.")
        print("Atualize os dados do grupo e da carta.")

    else:

        print("Não comprar esta oportunidade.")

    print("=" * 80)
