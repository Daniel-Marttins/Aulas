# Tipos de dados são usados na programação para que nós, como programadores, saibamos o que estamos 
# manipulando e o que vamos fazer com tais tipos, seja para armazenar um grupo de informações, 
# realizar cálculos ou tomar decisões com base em certas condições.

# Por exemplo, no nosso dia a dia, lidamos com diferentes tipos de informações.
# Se vamos ao mercado, trabalhamos com números para contar quantos itens compramos.
# Se mandamos uma mensagem para um amigo, lidamos com texto.
# Se decidimos se levamos um guarda-chuva ou não, estamos lidando com decisões lógicas.

# Em Python, isso se traduz em diferentes tipos de dados:

# Números inteiros (int) - Representam quantidades exatas
idade = 25  # A idade de uma pessoa é um número inteiro
quantidade_de_maçãs = 10  # Quantas maçãs temos na cesta

# Números de ponto flutuante (float) - Representam medidas e valores fracionários
altura = 1.75  # Altura em metros
preco_do_cafe = 4.50  # O preço do café na padaria

# Strings (str) - Representam textos, como palavras ou frases
nome = "Carlos"  # O nome de uma pessoa
mensagem = "Olá, tudo bem?"  # O que falamos no dia a dia

# Booleanos (bool) - Representam verdades e mentiras, útil para tomadas de decisão
esta_chovendo = True  # Se estiver chovendo, levamos um guarda-chuva
tem_dinheiro = False  # Se não tivermos dinheiro, não podemos comprar algo

# Listas (list) - Representam coleções de itens, como uma lista de compras
lista_de_compras = ["Leite", "Pão", "Café"]  # Itens que precisamos comprar

# Dicionários (dict) - Representam informações organizadas por chave-valor, como um cadastro
cadastro = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}  # Informações sobre uma pessoa

# Cada um desses tipos de dados nos ajuda a modelar e representar o mundo real na programação,
# tornando o código mais intuitivo e alinhado com a forma como pensamos no dia a dia.

# Em Python, não precisamos especificar o tipo dos dados, pois ele é uma linguagem de tipagem dinâmica.
# Isso significa que podemos simplesmente escrever `idade = 25` sem dizer que é um número inteiro (int),
# pois o Python entende automaticamente.

# Já em outras linguagens, como Java e C, precisamos deixar isso explícito:
# Em Java:
# int idade = 25;
# double altura = 1.75;
# String nome = "Carlos";

# Em C:
# int idade = 25;
# float altura = 1.75;
# char nome[] = "Carlos";

# Isso acontece porque essas linguagens têm tipagem estática, exigindo que o programador declare os tipos
# explicitamente para que o código seja compilado corretamente.

# Em resumo, Python nos dá mais flexibilidade ao lidar com tipos de dados, enquanto outras linguagens
# exigem uma definição mais rigorosa, o que pode trazer vantagens de desempenho e segurança no código.