def eh_primo(numero):
    """Verifica se um número é primo.

    Args:
        numero (int): Número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    # Números menores que 2 não atendem à definição de primo
    if numero < 2:
        return False

    # 2 é o único primo par, então podemos tratar esse caso de forma específica
    if numero == 2:
        return True

    # elimina todos os pares maiores que 2 de uma vez
    if numero % 2 == 0:
        return False

    # apenas testamos divisores ímpares até a raiz quadrada para melhorar eficiência
    limite = int(numero ** 0.5) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False

    return True


# Exemplos de uso
if __name__ == "__main__":
    # Números para testar
    numeros_teste = [0, 1, 2, 3, 4, 5, 10, 11, 13, 17, 20, 29, 30]

    print("Verificação de Números Primos:\n")
    for num in numeros_teste:
        resultado = "É primo" if eh_primo(num) else "Não é primo"
        print(f"{num:3d} - {resultado}")
