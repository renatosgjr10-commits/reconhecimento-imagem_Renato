# Explicação Linha a Linha - Verificador de Números Primos

## Definição da Função

### Linha 1: Declaração da Função
```python
def eh_primo(numero):
```
- `def` - Palavra-chave para definir uma função em Python
- `eh_primo` - Nome da função
- `numero` - Parâmetro que receberá o número a ser verificado
- `:` - Indica o início do bloco de código da função

### Linhas 2-7: Docstring (Documentação)
```python
    """
    Verifica se um número é primo.
    
    Args:
        numero: Um número inteiro a ser verificado
        
    Returns:
        bool: True se o número é primo, False caso contrário
    """
```
- `"""` - Abre uma string de múltiplas linhas (docstring)
- **Descrição**: Explica o propósito da função
- **Args**: Documenta os parâmetros de entrada
- **Returns**: Documenta o tipo e significado do valor retornado
- `"""` - Fecha a docstring

---

## Corpo da Função

### Linhas 9-10: Verificação de Números Menores que 2
```python
    # Números menores que 2 não são primos
    if numero < 2:
```
- `#` - Inicia um comentário (explicação para o programador)
- `if` - Começa uma estrutura condicional
- `numero < 2` - Condição: verifica se o número é menor que 2
- Números como 0, 1 e negativos não são considerados primos

### Linha 11: Retorno para Números Menores que 2
```python
        return False
```
- `return` - Sai da função e retorna um valor
- `False` - Retorna falso (o número NÃO é primo)
- A indentação de 8 espaços indica que pertence ao bloco `if`

### Linhas 13-14: Verificação do Número 2
```python
    # 2 é o único número par que é primo
    if numero == 2:
```
- `numero == 2` - Verifica igualdade (se o número é exatamente 2)
- O número 2 é um caso especial: é o único número primo que é par

### Linha 15: Retorna True para o Número 2
```python
        return True
```
- Retorna `True` (o número 2 É primo)

### Linhas 17-19: Descarta Números Pares Maiores que 2
```python
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
```
- `%` - Operador módulo (resto da divisão)
- `numero % 2` - Calcula o resto da divisão por 2
- `== 0` - Verifica se o resto é zero (número é par)
- Se for par e não é o 2, não pode ser primo

### Linha 20: Retorna False para Pares
```python
        return False
```
- Retorna `False` (números pares maiores que 2 não são primos)

### Linhas 22-27: Loop de Verificação
```python
    # Verifica divisibilidade até a raiz quadrada do número
    # Se o número tiver um divisor maior que sua raiz quadrada,
    # ele também terá um divisor menor
    for i in range(3, int(numero ** 0.5) + 1, 2):
```
- `for` - Inicia um loop que repete um bloco de código
- `i` - Variável que assume cada valor da sequência
- `range(3, int(numero ** 0.5) + 1, 2)` - Cria uma sequência:
  - `3` - Começa em 3 (já verificamos 2)
  - `numero ** 0.5` - Calcula a raiz quadrada do número
  - `int()` - Converte para número inteiro
  - `+ 1` - Adiciona 1 para incluir a raiz quadrada
  - `, 2` - Incrementa de 2 em 2 (apenas números ímpares)
- **Motivo**: Se um número têm divisor maior que sua raiz, tem outro menor

### Linhas 28-29: Verificação de Divisibilidade
```python
        if numero % i == 0:
            return False
```
- `numero % i` - Calcula o resto da divisão por `i`
- `== 0` - Verifica se o resto é zero (divisão exata)
- Se encontrar um divisor, o número NÃO é primo
- `return False` - Sai da função imediatamente

### Linha 31: Retorno Final
```python
    return True
```
- Se passou por todas as verificações, o número É primo
- Retorna `True`

---

## Programa Principal

### Linhas 34-36: Bloco de Execução Principal
```python
# Exemplos de uso
if __name__ == "__main__":
```
- `if __name__ == "__main__":` - Verifica se o arquivo está sendo executado diretamente
- Permite que o código seja importado sem executar os testes
- `:` - Indica o início do bloco

### Linhas 37-38: Lista de Teste
```python
    # Números para testar
    numeros_teste = [0, 1, 2, 3, 4, 5, 10, 11, 13, 17, 20, 29, 30]
```
- `numeros_teste` - Variável que armazena uma lista
- `[...]` - Sintaxe de lista em Python
- Contém números diversos para testar: pares, ímpares, primos e não-primos

### Linhas 40-41: Imprime Cabeçalho
```python
    print("Verificação de Números Primos:\n")
```
- `print()` - Função que exibe texto na tela
- `"\n"` - Caractere de quebra de linha (espaço em branco)

### Linhas 42-44: Loop sobre a Lista
```python
    for num in numeros_teste:
        resultado = "É primo" if eh_primo(num) else "Não é primo"
        print(f"{num:3d} - {resultado}")
```

#### Linha 42:
- `for num in numeros_teste:` - Loop que repete para cada número da lista
- `num` - Variável recebe cada número, um de cada vez

#### Linha 43:
- `resultado = ... if ... else ...` - Operador ternário (if/else compacto)
- `eh_primo(num)` - Chama a função com o número
- `if eh_primo(num)` - Se retorna `True`
- `"É primo"` - Atribui este texto a `resultado`
- `else` - Se retorna `False`
- `"Não é primo"` - Atribui este texto a `resultado`

#### Linha 44:
- `print(f"...")` - f-string: permite inserir variáveis dentro de strings
- `{num:3d}` - Formata `num` como número inteiro de 3 dígitos
- `{resultado}` - Insere o valor da variável `resultado`
- Exibe algo como: `  2 - É primo`

---

## Resumo do Algoritmo

1. **Rejeita negativos e zero**: Números < 2 não são primos
2. **Caso especial**: O número 2 é primo
3. **Rejeita pares**: Números pares maiores que 2 não são primos
4. **Testa divisibilidade**: Verifica se tem divisores até √n
5. **Retorna resultado**: True se primo, False se não

**Complexidade**: O(√n) - muito eficiente para números grandes
