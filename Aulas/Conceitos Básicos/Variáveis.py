# Vamos imaginar, primeiramente, variáveis como uma série de caixas de sapatos 
# vazias e aleatórias amontoadas em um quarto. Por enquanto, essas caixas não 
# contêm nada, estão desorganizadas e sem propósito definido.

# No mundo real, se precisássemos usar essas caixas para armazenar algo, 
# o que faríamos primeiro? Provavelmente, começaríamos organizando-as, separando 
# por cores (caso tivessem), etiquetando ou dando nomes para identificar o conteúdo. 
# Perceba que esse processo de organização já segue uma lógica semelhante a um algoritmo, 
# antes mesmo de falarmos diretamente sobre programação.

# Agora, voltando às nossas caixas, vamos organizá-las e dar nomes a elas, 
# associando cada uma a um tipo específico de item. Podemos armazenar desde objetos 
# pequenos, como lápis e canetas, até algo mais importante, como documentos.

# Vamos nomear nossa primeira caixa e guardar alguns lápis nela:

caixa_lapis = 'Lápis azul, Lápis amarelo, Lápis vermelho'

# Com essa simples atribuição, criamos nossa primeira variável.  
# Da mesma forma que organizamos uma caixa no mundo real, também estamos organizando
# nosso código, dando significado a um conjunto de informações.

# Agora, podemos replicar essa lógica para outras caixas:

caixa_roupas = 'Calça preta, Blusa jeans, Cueca box, Terno preto, Meia colorida'

# Agora temos duas caixas armazenando diferentes tipos de itens. Se quisermos 
# acessar os objetos dentro delas, basta "abrir" e verificar o conteúdo. 
# No código, podemos fazer isso exibindo a variável na tela:

print('Antes da organização:\n')  # Quebra de linha para melhor visualização

print(caixa_lapis)

# Quando executarmos o código (pressionando F5 no editor), a saída será:
# 'Lápis azul, Lápis amarelo, Lápis vermelho'

# Se quisermos ver o que tem na caixa de roupas, basta utilizar o mesmo comando (print),
# mas agora referindo-se à variável correspondente:

print(caixa_roupas)
print('\n')  # Adicionamos uma quebra de linha para espaçamento

# Assim, ao executar o código, veremos a saída:
# 'Calça preta, Blusa jeans, Cueca box, Terno preto, Meia colorida'

# Para tornar nossa saída mais organizada e legível, podemos adicionar mensagens explicativas:

print('Depois da organização:\n')  # Melhorando a visualização das saídas

print('Caixa de Lápis:', caixa_lapis)
print('Caixa de Roupas:', caixa_roupas)
print('\n')

# Como percebemos, os resultados aparecem muito juntos, dificultando a leitura.  
# Para resolver isso, usamos o comando (print('\n')), que insere quebras de linha  
# e melhora a formatação da saída no terminal.

# Com este exemplo, aprendemos como funcionam as variáveis e como elas nos ajudam  
# a organizar informações dentro do código. No futuro, usaremos variáveis para 
# armazenar dados mais complexos, realizar operações matemáticas, comparações lógicas 
# e diversas outras funcionalidades essenciais para a programação.
