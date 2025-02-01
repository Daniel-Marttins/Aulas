# Aula Prática - Tipos de Dados em Python

# Nesta prática, vamos explorar os tipos de dados mais comuns em Python
# e aplicar o conhecimento de forma simples e objetiva.

# Passo 1: Declarando variáveis de diferentes tipos de dados
# Aqui, criamos variáveis de diferentes tipos e atribuímos valores a elas
idade = 25  # Tipo inteiro (int), representa valores numéricos sem casas decimais
altura = 1.75  # Tipo ponto flutuante (float), utilizado para números com casas decimais
nome = "Carlos"  # Tipo string (str), usado para representar textos
esta_chovendo = True  # Tipo booleano (bool), usado para valores lógicos (Verdadeiro ou Falso)
lista_de_compras = ["Leite", "Pão", "Café"]  # Tipo lista (list), usada para armazenar múltiplos valores
cadastro = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}  # Tipo dicionário (dict), utilizado para armazenar dados estruturados

# Passo 2: Exibindo os valores armazenados nas variáveis
# Agora, vamos imprimir os valores de cada variável para verificar seu conteúdo
print(f"Idade: {idade} (Tipo: {type(idade)})")
print(f"Altura: {altura} (Tipo: {type(altura)})")
print(f"Nome: {nome} (Tipo: {type(nome)})")
print(f"Está chovendo? {esta_chovendo} (Tipo: {type(esta_chovendo)})")
print(f"Lista de Compras: {lista_de_compras} (Tipo: {type(lista_de_compras)})")
print(f"Cadastro: {cadastro} (Tipo: {type(cadastro)})")

# Passo 3: Modificando valores das variáveis
# Podemos alterar o valor de uma variável após sua criação
idade = 26  # Alterando o valor da variável idade
lista_de_compras.append("Ovos")  # Adicionando um novo item à lista
cadastro["idade"] = 31  # Atualizando a idade no dicionário

print("\nApós a modificação:")
print(f"Nova Idade: {idade}")
print(f"Lista de Compras Atualizada: {lista_de_compras}")
print(f"Cadastro Atualizado: {cadastro}")

# Extra: Agora é sua vez!
# 1º) Declare variáveis para armazenar o preço de um produto (R$ 99.90)
# e mostre o resultado.

# Comece aqui...

# 2º) Crie uma variável que guarde um número de telefone como string
# e exiba na tela.

# Comece aqui...

# 3º) Declare uma lista contendo os nomes de três amigos e exiba um a um.

# Comece aqui...

# 4º) Crie um dicionário representando um carro, contendo marca, modelo e ano.
# Depois, exiba essas informações.

# Comece aqui...
