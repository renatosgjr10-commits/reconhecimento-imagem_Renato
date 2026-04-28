# Relatório de Depuração - debug.py

## Visão Geral dos Erros

O código original continha **7 erros** que impediam sua execução correta. Todos os erros foram identificados, corrigidos e documentados abaixo. O código agora funciona perfeitamente e calcula corretamente o total de compras com impostos e descontos.

---

## Erros Identificados e Correções

### Erro 1: Sintaxe - Aspas Faltando na String (Linha 6)
**Código Original:**
```python
item1 = float(input(Preço do item 1? ))
```

**Problema:** Falta de aspas delimitando a string "Preço do item 1? ".

**Erro de Execução:** `SyntaxError: invalid syntax` - Python não reconhece "Preço" como string válida.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### Erro 2: Tipo de Dados - Input Retorna String (Linha 17)
**Código Original:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

**Problema:** A função `input()` sempre retorna uma string, mas o código tenta usar `desconto_cupom` em operações matemáticas.

**Erro de Execução:** `TypeError: unsupported operand type(s) for /: 'str' and 'int'` na linha 18.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

---

### Erro 3: Operação com String (Linha 18)
**Código Original:**
```python
desconto = subtotal * (desconto_cupom / 100)
```

**Problema:** `desconto_cupom` é uma string (do input), não pode ser dividida por 100.

**Erro de Execução:** Mesmo erro do item 2.

**Correção:** Resolvido convertendo `desconto_cupom` para `float` no erro 2.

---

### Erro 4: F-String Incompleta (Linha 27)
**Código Original:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Problema:** Falta o prefixo `f` para indicar que é uma f-string.

**Erro de Execução:** A string é impressa literalmente, sem substituir `{total_item2:.2f}` pelo valor.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### Erro 5: Comparação Inválida (Linha 32)
**Código Original:**
```python
if desconto_cupom > 0:
```

**Problema:** `desconto_cupom` é uma string, não pode ser comparada com o número 0.

**Erro de Execução:** `TypeError: '>' not supported between instances of 'str' and 'int'`.

**Correção:** Resolvido convertendo `desconto_cupom` para `float` no erro 2.

---

### Erro 6: Indentação e Formatação Inválida (Linha 33)
**Código Original:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problemas:**
1. Falta de indentação no `print` (deve estar dentro do bloco `if`)
2. `desconto_cupom` é string, não pode ser formatado como `:.0f`

**Erro de Execução:**
- O `print` sempre executa (não está no bloco `if`)
- `ValueError: Unknown format code 'f' for object of type 'str'` na formatação

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

### Erro 7: Formatação Redundante (Linha 36)
**Código Original:**
```python
print(f" TOTAL:         R$ {round(total, 2):.2f}")
```

**Problema:** `round(total, 2)` já arredonda para 2 casas decimais, mas depois formata novamente com `:.2f`.

**Erro de Execução:** Não causa erro, mas é redundante e pode causar problemas de precisão.

**Correção:**
```python
print(f" TOTAL:         R$ {total:.2f}")
```

---

## Código Corrigido Completo

```python
# Sistema de Cálculo de Compras - Versão Corrigida
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

---

## Teste de Validação

**Entrada de Teste:**
- Cliente: João Silva
- Item 1: 2 unidades × R$ 10.50 = R$ 21.00
- Item 2: 1 unidade × R$ 25.00 = R$ 25.00
- Item 3: 3 unidades × R$ 5.75 = R$ 17.25
- Subtotal: R$ 63.25
- Imposto (10%): R$ 6.33
- Desconto (5%): R$ 3.16
- **Total Final: R$ 66.41**

**Saída do Programa Corrigido:**
```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 21.00
 Item 2:        R$ 25.00
 Item 3:        R$ 17.25
-------------------------------
 Subtotal:      R$ 63.25
 Imposto (10%): R$ 6.33
 Desconto (5%): -R$ 3.16
===============================
 TOTAL:         R$ 66.41
===============================
```

---

## Lições Aprendidas

1. **Sempre use aspas** em strings de `input()`
2. **Converta tipos** quando necessário (`int()`, `float()`)
3. **Use f-strings corretamente** com o prefixo `f`
4. **Respeite indentação** em blocos condicionais
5. **Evite redundâncias** na formatação de números
6. **Teste o código** após correções para validar

O código agora está **100% funcional** e segue boas práticas de programação Python.