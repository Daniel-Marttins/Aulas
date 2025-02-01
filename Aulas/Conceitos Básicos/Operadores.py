# Em Python, usamos operadores para realizar operações matemáticas, 
# comparar valores e tomar decisões lógicas. Vamos aprender sobre os operadores mais comuns.

# 1. Operadores Aritméticos (Matemáticos)
# Usamos operadores aritméticos para realizar operações matemáticas, como somar, subtrair, etc.

print('Operadores Aritméticos (Matemáticos)\n')

# Soma
numero1 = 10
numero2 = 5
resultado_soma = numero1 + numero2  # Soma os dois números
print(f"Soma: {numero1} + {numero2} = {resultado_soma}")

# Subtração
resultado_subtracao = numero1 - numero2  # Subtrai numero2 de numero1
print(f"Subtração: {numero1} - {numero2} = {resultado_subtracao}")

# Multiplicação
resultado_multiplicacao = numero1 * numero2  # Multiplica os dois números
print(f"Multiplicação: {numero1} * {numero2} = {resultado_multiplicacao}")

# Divisão
resultado_divisao = numero1 / numero2  # Divide numero1 por numero2
print(f"Divisão: {numero1} / {numero2} = {resultado_divisao}")

# Divisão inteira (sem casas decimais)
resultado_divisao_inteira = numero1 // numero2  # Resultado da divisão, arredondado para baixo
print(f"Divisão inteira: {numero1} // {numero2} = {resultado_divisao_inteira}")

# Resto da divisão (módulo)
resultado_modulo = numero1 % numero2  # Retorna o resto da divisão
print(f"Resto da divisão: {numero1} % {numero2} = {resultado_modulo}")

# Potência
resultado_potencia = numero1 ** numero2  # Numero1 elevado à potencia de numero2
print(f"Potência: {numero1} ** {numero2} = {resultado_potencia}")
print('\n')


# 2. Operadores de Comparação
# Usamos operadores de comparação para comparar dois valores e retornar True ou False.

print('Operadores de Comparação\n')

# Igualdade
igualdade = numero1 == numero2  # Verifica se numero1 é igual a numero2
print(f"igualdade: {numero1} == {numero2} -> {igualdade}")

# Diferença
diferenca = numero1 != numero2  # Verifica se numero1 é diferente de numero2
print(f"Diferença: {numero1} != {numero2} -> {diferenca}")

# Maior que
maior_que = numero1 > numero2  # Verifica se numero1 é maior que numero2
print(f"Maior que: {numero1} > {numero2} -> {maior_que}")

# Menor que
menor_que = numero1 < numero2  # Verifica se numero1 é menor que numero2
print(f"Menor que: {numero1} < {numero2} -> {menor_que}")

# Maior ou igual
maior_igual = numero1 >= numero2  # Verifica se numero1 é maior ou igual a numero2
print(f"Maior ou igual: {numero1} >= {numero2} -> {maior_igual}")

# Menor ou igual
menor_igual = numero1 <= numero2  # Verifica se numero1 é menor ou igual a numero2
print(f"Menor ou igual: {numero1} <= {numero2} -> {menor_igual}")
print('\n')


# 3. Operadores Lógicos
# Usamos operadores lógicos para realizar comparações entre expressões booleanas (verdadeiro ou falso).

print('Operadores Lógicos\n')

# AND (E)
condicao1 = True
condicao2 = False
resultado_and = condicao1 and condicao2  # Só é True se ambas as condições forem True
print(f"AND (E): {condicao1} and {condicao2} -> {resultado_and}")

# OR (OU)
resultado_or = condicao1 or condicao2  # Só é False se ambas as condições forem False
print(f"OR (OU): {condicao1} or {condicao2} -> {resultado_or}")

# NOT (NÃO)
resultado_not = not condicao1  # Inverte o valor da condição
print(f"NOT (NÃO): not {condicao1} -> {resultado_not}")
print('\n')


# 4. Operadores de Atribuição
# Usamos operadores de atribuição para atribuir valores a variáveis de forma mais compacta.

print('Operadores de Atribuição\n')

# Atribuição simples
numero3 = 20  # Atribui 20 a numero3
print(f"Atribuição simples: numero3 = {numero3}")

# Atribuição com soma
numero3 += 5  # Equivalente a numero3 = numero3 + 5
print(f"Atribuição com soma: numero3 += 5 -> {numero3}")

# Atribuição com multiplicação
numero3 *= 2  # Equivalente a numero3 = numero3 * 2
print(f"Atribuição com multiplicação: numero3 *= 2 -> {numero3}")
print('\n')
