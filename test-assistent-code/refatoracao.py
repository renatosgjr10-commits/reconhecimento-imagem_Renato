def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros: Lista de números
        
    Returns:
        tuple: (soma, media, maximo, minimo)
    """
    if not numeros:
        return 0, 0, None, None
    
    soma = sum(numeros)
    media = soma / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return soma, media, maximo, minimo


# Exemplo de uso
lista = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior, menor = calcular_estatisticas(lista)

print(f"Total: {total}")
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")