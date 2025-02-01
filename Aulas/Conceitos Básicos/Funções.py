# Funções em Python
# Funções são usadas para agrupar blocos de código e executar tarefas específicas. 
# Podemos reutilizar o código da função sempre que necessário.

# 1. Definindo uma função simples
print("Definindo uma função simples:\n")

# Vamos definir uma função chamada "saudar" que imprime uma saudação.
def saudar():
    print("Olá, seja bem-vindo ao aprendizado de Python!")

# Agora, chamamos a função saudar.
saudar()

# Saída: "Olá, seja bem-vindo ao aprendizado de Python!"
# A função "saudar" foi definida e, em seguida, chamada para ser executada.

print("\n")  # Quebra de linha no final do tópico


# 2. Funções com parâmetros
# Podemos passar informações para a função usando parâmetros. Isso torna a função mais flexível.

print("Funções com parâmetros:\n")

# Vamos criar uma função chamada "saudar_com_nome" que recebe um parâmetro, "nome".
def saudar_com_nome(nome):
    print(f"Olá, {nome}! Como você está?")

# Chamando a função passando um argumento.
saudar_com_nome("Carlos")

# Saída: "Olá, Carlos! Como você está?"
# A função recebeu o parâmetro "Carlos" e o usou para imprimir a mensagem.

# Também podemos passar outros nomes para a função:
saudar_com_nome("Maria")
saudar_com_nome("João")

# Saída:
# "Olá, Maria! Como você está?"
# "Olá, João! Como você está?"

print("\n")  # Quebra de linha no final do tópico


# 3. Funções com valores de retorno
# As funções podem retornar valores. Isso permite que possamos usar o resultado da função em outro lugar no código.

print("Funções com valores de retorno:\n")

# Vamos criar uma função que soma dois números e retorna o resultado.
def somar(a, b):
    return a + b

# Chamando a função e armazenando o resultado.
resultado = somar(10, 5)
print(f"A soma de 10 e 5 é: {resultado}")

# Saída: "A soma de 10 e 5 é: 15"
# A função "somar" retorna o valor da soma e o armazena na variável "resultado".

# Podemos fazer mais cálculos chamando a função novamente.
resultado2 = somar(20, 30)
print(f"A soma de 20 e 30 é: {resultado2}")

# Saída: "A soma de 20 e 30 é: 50"

print("\n")  # Quebra de linha no final do tópico


# 4. Funções com parâmetros opcionais
# Podemos definir parâmetros com valores padrão, assim a função pode ser chamada sem que seja necessário passar um valor para o parâmetro.

print("Funções com parâmetros opcionais:\n")

# Vamos criar uma função que exibe uma saudação com um nome, mas tem um valor padrão para o nome.
def saudar_opcional(nome="Visitante"):
    print(f"Olá, {nome}! Bem-vindo!")

# Se não passarmos um nome, o valor padrão "Visitante" será usado.
saudar_opcional()  # Sem passar argumento, usa "Visitante".
saudar_opcional("Ana")  # Passando um argumento, usa "Ana".

# Saída:
# "Olá, Visitante! Bem-vindo!"
# "Olá, Ana! Bem-vindo!"

print("\n")  # Quebra de linha no final do tópico


# 5. Funções com múltiplos parâmetros e retorno
# Podemos passar vários parâmetros e retornar mais de um valor, utilizando estruturas como tuplas.

print("Funções com múltiplos parâmetros e retorno:\n")

# Vamos criar uma função que retorna o produto e o quociente de dois números.
def calcular_produto_quotiente(a, b):
    produto = a * b
    if b != 0:
        quociente = a / b
    else:
        quociente = "Não é possível dividir por zero!"
    return produto, quociente  # Retorna uma tupla com dois valores.

# Chamando a função e armazenando o resultado.
produto, quociente = calcular_produto_quotiente(10, 2)

# Exibindo os resultados.
print(f"Produto: {produto}, Quociente: {quociente}")

# Saída: "Produto: 20, Quociente: 5.0"

# Podemos também tratar a divisão por zero:
produto, quociente = calcular_produto_quotiente(10, 0)
print(f"Produto: {produto}, Quociente: {quociente}")

# Saída: "Produto: 0, Quociente: Não é possível dividir por zero!"

print("\n")  # Quebra de linha no final do tópico


# 6. Funções Recursivas
# Funções recursivas são aquelas que chamam a si mesmas. Elas são úteis para resolver problemas repetitivos e de divisão.

print("Funções Recursivas:\n")

# Vamos criar uma função recursiva para calcular o fatorial de um número.
def fatorial(n):
    if n == 1:  # Caso base: o fatorial de 1 é 1.
        return 1
    else:
        return n * fatorial(n - 1)  # Chama a função novamente com (n - 1).

# Chamando a função para calcular o fatorial de 5.
resultado_fatorial = fatorial(5)
print(f"O fatorial de 5 é: {resultado_fatorial}")

# Saída: "O fatorial de 5 é: 120"
# O fatorial de 5 é calculado como: 5 * 4 * 3 * 2 * 1 = 120

print("\n")  # Quebra de linha no final do tópico
