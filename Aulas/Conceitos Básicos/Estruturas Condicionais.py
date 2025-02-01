# Estruturas Condicionais em Python (if, elif, else)
# As estruturas condicionais permitem que o programa tome decisões 
# com base em condições, executando diferentes blocos de código dependendo 
# de um valor verdadeiro (True) ou falso (False).

# 1. Estrutura Condicional Simples (if)
# A estrutura "if" é usada quando queremos testar uma condição. 
# Se a condição for verdadeira, o código dentro do bloco "if" será executado.

print('Estrutura Condicional Simples (if): \n')

idade = 18  # A idade de uma pessoa

if idade >= 18:  # Se a idade for maior ou igual a 18
    print("Você é maior de idade!")  # Mensagem será exibida se a condição for verdadeira

# Saída: "Você é maior de idade!"
# Como idade é 18, a condição (idade >= 18) é verdadeira, então o código dentro do "if" é executado.

print('\n')

# 2. Estrutura Condicional com else
# O "else" é usado quando queremos especificar o que fazer quando a condição do "if" não for verdadeira.
# Ou seja, se a condição no "if" for falsa, o bloco de código do "else" será executado.

print('Estrutura Condicional com else: \n')

idade = 15  # A idade agora é 15

if idade >= 18:  # Verifica se a pessoa é maior ou igual a 18 anos
    print("Você é maior de idade!")  # Será executado se a condição for verdadeira
else:
    print("Você é menor de idade!")  # Será executado se a condição for falsa

# Saída: "Você é menor de idade!"
# Como idade é 15, a condição (idade >= 18) é falsa, então o código dentro do "else" é executado.

print('\n')

# 3. Estrutura Condicional com elif
# O "elif" (else if) é usado quando temos múltiplas condições a serem testadas. 
# Ele permite testar mais de uma condição e escolher qual delas é verdadeira.

print('Estrutura Condicional com elif: \n')

idade = 20  # A idade agora é 20

if idade >= 18:  # Primeira condição
    print("Você é maior de idade!")
elif idade == 17:  # Se a idade for 17
    print("Você tem 17 anos!")
else:
    print("Você é menor de idade!")

# Saída: "Você é maior de idade!"
# A primeira condição (idade >= 18) é verdadeira, então o código dentro do "if" é executado. 
# O "elif" e o "else" são ignorados.

# Se colocássemos a idade como 17, o programa mostraria: "Você tem 17 anos!"

print('\n')

# 4. Condições Compostas
# Podemos testar várias condições ao mesmo tempo, usando operadores lógicos como "and" e "or".

print('Condições Compostas: \n')

idade = 25
tem_documento = True  # A pessoa tem documento?

# Se a pessoa for maior de 18 anos e tiver documento, pode votar
if idade >= 18 and tem_documento:
    print("Você pode votar!")
else:
    print("Você não pode votar!")

# Saída: "Você pode votar!"
# A condição (idade >= 18 and tem_documento) é verdadeira, então o código dentro do "if" é executado.

print('\n')

# 5. Condições Aninhadas
# Podemos ter uma estrutura condicional dentro de outra. Isso é útil para verificar múltiplas condições mais complexas.

print('Condições Aninhadas: \n')

idade = 22
tem_voto = False

if idade >= 18:
    if tem_voto:  # Se a pessoa tem direito a votar
        print("Você pode votar!")
    else:
        print("Você não tem direito a votar.")
else:
    print("Você é menor de idade!")

# Saída: "Você não tem direito a votar."
# Primeiro, a condição (idade >= 18) é verificada, depois, dentro do bloco do "if", verificamos se a pessoa tem direito a voto.

print('\n')