# 1. Estrutura de Repetição "for"
# O "for" é usado para iterar sobre uma sequência (como uma lista, tupla, string, ou range) 
# e executar um bloco de código para cada item da sequência.

print("Estrutura de Repetição 'for':\n")

# Vamos criar uma lista de números e imprimir cada um deles.
numeros = [1, 2, 3, 4, 5]

# O "for" vai iterar sobre cada número da lista e imprimir o valor.
for numero in numeros:
    print(f"Número: {numero}")

# Saída:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Número: 5

# Como a lista contém 5 elementos, o loop executa 5 vezes, imprimindo cada número na lista.

print("\n")  # Quebra de linha no final do tópico

# 2. Estrutura de Repetição "while"
# O "while" continua executando um bloco de código enquanto uma condição for verdadeira.
# Ou seja, o loop só termina quando a condição se tornar falsa.

print("Estrutura de Repetição 'while':\n")

# Vamos usar um contador para ilustrar o uso do "while".
contador = 1

# O loop "while" vai continuar enquanto o contador for menor ou igual a 5.
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador em 1 a cada iteração

# Saída:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5

# Neste caso, o loop executa enquanto a condição (contador <= 5) for verdadeira. Quando o contador 
# atingir 6, a condição será falsa, e o loop terminará.

print("\n")  # Quebra de linha no final do tópico


# 3. Laços "for" com intervalo (range)
# O "range" é frequentemente utilizado com a estrutura "for" para gerar uma sequência de números 
# dentro de um intervalo específico.

print("Laço 'for' com intervalo (range):\n")

# O range(1, 6) gera os números de 1 a 5.
for i in range(1, 6):
    print(f"Número gerado pelo range: {i}")

# Saída:
# Número gerado pelo range: 1
# Número gerado pelo range: 2
# Número gerado pelo range: 3
# Número gerado pelo range: 4
# Número gerado pelo range: 5

# O "range" cria uma sequência de números de 1 a 5 (o 6 não é incluído), 
# e o "for" itera sobre essa sequência imprimindo cada número.

print("\n")  # Quebra de linha no final do tópico


# 4. Laços aninhados
# Podemos colocar um laço dentro de outro. Isso é útil quando precisamos repetir uma sequência dentro de outra.

print("Laços aninhados ('for' dentro de 'for'):\n")

# Vamos criar uma tabela de multiplicação.
for i in range(1, 4):  # Laço externo para as linhas
    for j in range(1, 4):  # Laço interno para as colunas
        print(f"{i} x {j} = {i * j}", end="\t")  # Multiplicação e exibição
    print()  # Quebra de linha para separar as linhas da tabela

# Saída:
# 1 x 1 = 1	1 x 2 = 2	1 x 3 = 3	
# 2 x 1 = 2	2 x 2 = 4	2 x 3 = 6	
# 3 x 1 = 3	3 x 2 = 6	3 x 3 = 9	

# O laço externo percorre as linhas (de 1 a 3), e o laço interno percorre as colunas (de 1 a 3),
# gerando uma tabela de multiplicação.

print("\n")  # Quebra de linha no final do tópico


# 5. Controle de fluxo dentro do laço (break, continue)
# Usamos o "break" para sair de um loop antes que a condição termine, e o "continue" para pular a iteração atual e continuar para a próxima.

print("Controle de fluxo no laço ('break' e 'continue'):\n")

# Exemplo com o "break":
for numero in range(1, 10):
    if numero == 6:
        break  # O loop vai parar assim que encontrar o número 6
    print(f"Número: {numero}")

# Saída:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Número: 5

# O loop foi interrompido quando chegou ao número 6 devido ao "break".

# Exemplo com o "continue":
for numero in range(1, 6):
    if numero == 3:
        continue  # Pula a iteração quando o número for 3
    print(f"Número: {numero}")

# Saída:
# Número: 1
# Número: 2
# Número: 4
# Número: 5

# O "continue" fez o loop pular a iteração em que o número é 3, mas continuou com os outros números.

print("\n")  # Quebra de linha no final do tópico
