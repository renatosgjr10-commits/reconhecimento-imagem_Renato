def eh_primo(numero):
    """
    Verifica se um número é primo.
    
    Args:
        numero: Um número inteiro a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
    # Números menores que 2 não são primos
    if numero < 2:
        return False
    
    # 2 é o único número par que é primo
    if numero == 2:
        return True
    
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False
    
    # Verifica divisibilidade até a raiz quadrada do número
    # Se o número tiver um divisor maior que sua raiz quadrada,
    # ele também terá um divisor menor
    for i in range(3, int(numero ** 0.5) + 1, 2):
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
