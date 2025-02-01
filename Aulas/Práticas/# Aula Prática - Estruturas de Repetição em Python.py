# Aula Prática - Estruturas de Repetição em Python

# 1. Estrutura de Repetição "for"
# O "for" é usado para iterar sobre uma sequência (como uma lista, tupla, string, ou range) 
# e executar um bloco de código para cada item da sequência.

print("Estrutura de Repetição 'for':\n")

# Criando uma lista de números e imprimindo cada um deles.
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"Número: {numero}")

print("\n")  # Quebra de linha

# 2. Estrutura de Repetição "while"
print("Estrutura de Repetição 'while':\n")

contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Incremento

print("\n")  # Quebra de linha

# 3. Laços "for" com intervalo (range)
print("Laço 'for' com intervalo (range):\n")

for i in range(1, 6):
    print(f"Número gerado pelo range: {i}")

print("\n")  # Quebra de linha

# 4. Laços aninhados
print("Laços aninhados ('for' dentro de 'for'):\n")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()

print("\n")  # Quebra de linha

# 5. Controle de fluxo dentro do laço (break, continue)
print("Controle de fluxo no laço ('break' e 'continue'):\n")

# Exemplo com o "break":
for numero in range(1, 10):
    if numero == 6:
        break
    print(f"Número: {numero}")

print("\n")

# Exemplo com o "continue":
for numero in range(1, 6):
    if numero == 3:
        continue
    print(f"Número: {numero}")

print("\n")  # Quebra de linha

# Exercícios práticos:
# 1º) Crie um loop "for" que imprima os números de 10 a 1 em ordem decrescente.
# 2º) Utilize um loop "while" para contar de 0 a 20 apenas com números pares.
# 3º) Crie um laço aninhado que gere uma matriz 3x3 com números sequenciais.
# 4º) Modifique o exemplo do "break" para que ele pare quando encontrar o número 8.
# 5º) Modifique o exemplo do "continue" para pular os números 2 e 4.
