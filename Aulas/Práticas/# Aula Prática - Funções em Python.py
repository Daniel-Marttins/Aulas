# Aula Prática - Funções em Python

# Passo 1: Criando uma função simples
# Vamos criar uma função simples para imprimir uma saudação.

def saudar():
    print("Olá, seja bem-vindo ao aprendizado de Python!")

# Chamando a função para exibir a saudação
saudar()

# Passo 2: Funções com parâmetros
# Agora, vamos criar uma função que recebe um parâmetro, o nome de uma pessoa,
# e imprime uma saudação personalizada.

def saudar_com_nome(nome):
    print(f"Olá, {nome}! Como você está?")

# Chamando a função com diferentes argumentos
saudar_com_nome("Carlos")
saudar_com_nome("Maria")
saudar_com_nome("João")

# Passo 3: Funções com valores de retorno
# Vamos criar uma função que soma dois números e retorna o resultado.

def somar(a, b):
    return a + b

# Chamando a função e armazenando o resultado
resultado = somar(10, 5)
print(f"A soma de 10 e 5 é: {resultado}")

# Passo 4: Funções com parâmetros opcionais
# Agora, vamos criar uma função que recebe um parâmetro opcional.
# Caso não passe o valor, ela usará o valor padrão.

def saudar_opcional(nome="Visitante"):
    print(f"Olá, {nome}! Bem-vindo!")

# Chamando a função sem e com argumento
saudar_opcional()  # Sem passar argumento, usa "Visitante".
saudar_opcional("Ana")  # Passando um argumento, usa "Ana".

# Passo 5: Funções com múltiplos parâmetros e retorno
# Vamos criar uma função que retorna o produto e o quociente de dois números.

def calcular_produto_quotiente(a, b):
    produto = a * b
    if b != 0:
        quociente = a / b
    else:
        quociente = "Não é possível dividir por zero!"
    return produto, quociente  # Retorna uma tupla com dois valores.

# Chamando a função e armazenando o resultado
produto, quociente = calcular_produto_quotiente(10, 2)
print(f"Produto: {produto}, Quociente: {quociente}")

# Passo 6: Funções Recursivas
# Vamos criar uma função recursiva para calcular o fatorial de um número.

def fatorial(n):
    if n == 1:  # Caso base: o fatorial de 1 é 1.
        return 1
    else:
        return n * fatorial(n - 1)  # Chama a função novamente com (n - 1).

# Chamando a função para calcular o fatorial de 5.
resultado_fatorial = fatorial(5)
print(f"O fatorial de 5 é: {resultado_fatorial}")

# Exercícios:
# 1) Declare uma variável que armazene uma idade e verifique se a pessoa é criança (0-12 anos), adolescente (13-17 anos) ou adulta (18+ anos).
# 2) Crie um programa que verifique se um número é par ou ímpar e exiba a resposta.
# 3) Desenvolva uma lógica que determine se um ano é bissexto (divisível por 4 e não por 100, exceto se for divisível por 400).