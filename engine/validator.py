# ============================================================
# CONSÓRCIO ALPHA ENGINE
# engine/validator.py
# Validação dos dados antes da análise
# ============================================================


def validate_opportunity(dados):
    """
    Valida os dados básicos de uma oportunidade.
    Retorna uma lista de alertas.
    Se a lista estiver vazia, a oportunidade está aprovada para análise.
    """

    alertas = []

    valor_carta = float(dados.get("valor_carta", 0))
    prazo_total = int(dados.get("prazo_total", 0))
    parcela_atual = int(dados.get("parcela_atual", 0))
    valor_parcela = float(dados.get("valor_parcela", 0))
    saldo_devedor = float(dados.get("saldo_devedor", 0))
    valor_pedido = float(dados.get("valor_pedido", 0))
    valor_imovel = float(dados.get("valor_imovel", 0))
    valor_revenda = float(dados.get("valor_revenda", 0))

    if valor_carta <= 0:
        alertas.append("Valor da carta inválido.")

    if prazo_total <= 0:
        alertas.append("Prazo total inválido.")

    if parcela_atual <= 0:
        alertas.append("Parcela atual inválida.")

    if parcela_atual > prazo_total:
        alertas.append("Parcela atual maior que o prazo total.")

    if valor_parcela <= 0:
        alertas.append("Valor da parcela inválido.")

    if saldo_devedor < 0:
        alertas.append("Saldo devedor não pode ser negativo.")

    if valor_pedido < 0:
        alertas.append("Valor pedido pelo vendedor não pode ser negativo.")

    if valor_imovel <= 0:
        alertas.append("Valor do imóvel inválido.")

    if valor_revenda <= 0:
        alertas.append("Valor de revenda inválido.")

    if valor_revenda < valor_imovel:
        alertas.append("Valor de revenda menor que valor de compra estimado.")

    return alertas


def is_valid_opportunity(dados):
    """
    Retorna True se os dados estiverem válidos.
    """

    return len(validate_opportunity(dados)) == 0
