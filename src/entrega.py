def calcular_entrega(distancia):
    if distancia < 0:
        raise ValueError("A distância não pode ser negativa.")
    if distancia <= 3:
        return 5.00
    return 5.00 + (distancia - 3) * 1.50