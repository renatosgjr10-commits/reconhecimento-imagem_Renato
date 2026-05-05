# Test Assistant Code - Exemplos Python

Este repositório contém exemplos de scripts Python e explicações associadas para aprendizado de lógica, debugging e refatoração.

## Visão Geral

A pasta `test-assistent-code` abriga três scripts principais e arquivos de documentação:

- `num_primos.py` - Verificador de números primos com otimização por raiz quadrada.
- `debug.py` - Sistema de cálculo de compras com entrada de dados, imposto e desconto.
- `refatoracao.py` - Cálculo de estatísticas básicas de uma lista de números.
- `explicacao_num_primo.md` - Explicação linha a linha do verificador de números primos.
- `explicacao_refatoracao.md` - Explicação linha a linha da refatoração de cálculo de estatísticas.
- `explicacao-debug.md` - Relatório de depuração do script de cálculo de compras.

## Scripts

### `num_primos.py`

Verifica se um número inteiro é primo.

Características:
- retorna `False` para números menores que 2
- trata `2` como o único primo par
- descarta pares maiores que 2 imediatamente
- testa divisores ímpares apenas até a raiz quadrada do número

Uso:
```bash
python num_primos.py
```

### `debug.py`

Sistema de cálculo de compras que solicita ao usuário:
- nome do cliente
- quantidade e preço de três itens
- valor do cupom de desconto

Calcula e exibe:
- total de cada item
- subtotal
- imposto de 10%
- desconto aplicado
- valor final

Uso:
```bash
python debug.py
```

### `refatoracao.py`

Calcula estatísticas básicas de uma lista de números:
- soma
- média
- maior valor
- menor valor

Uso:
```bash
python refatoracao.py
```

## Documentação Complementar

Os arquivos `*.md` detalham o funcionamento dos scripts e as correções aplicadas:

- `explicacao_num_primo.md` — descrição passo a passo do algoritmo de primalidade.
- `explicacao_refatoracao.md` — explicação sobre a refatoração do cálculo de estatísticas.
- `explicacao-debug.md` — relatório de erros encontrados e correções realizadas em `debug.py`.

## Como Executar

1. Abra um terminal na pasta `test-assistent-code`.
2. Execute o script desejado com Python 3:

```bash
python num_primos.py
python debug.py
python refatoracao.py
```

## Requisitos

- Python 3.x

## Observações

- Os scripts são exemplos didáticos e podem ser adaptados para suportar outros casos de uso.
- Para leitura detalhada do funcionamento interno, abra os arquivos `explicacao_*.md`.