# Aula Prática - Estruturas Condicionais em Python

# Nesta prática, vamos aplicar os conceitos de estruturas condicionais
# para tomar decisões dentro do código e exibir diferentes saídas.

# Passo 1: Criando uma condição simples com if
# Defina uma variável para armazenar a temperatura e utilize if para verificar se está quente.
temperatura = 30
if temperatura > 25:
    print("Está quente hoje!")

# Passo 2: Utilizando if e else
# Declare uma variável para a idade e verifique se a pessoa é maior de idade.
idade = 16
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

# Passo 3: Utilizando if, elif e else
# Verifique a nota de um aluno e exiba sua classificação.
nota = 85
if nota >= 90:
    print("Excelente!")
elif nota >= 70:
    print("Bom!")
else:
    print("Precisa melhorar.")

# Passo 4: Utilizando condições compostas com and e or
# Verifique se uma pessoa pode dirigir com base na idade e posse de carteira de motorista.
idade = 20
tem_carteira = False
if idade >= 18 and tem_carteira:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

# Passo 5: Criando condições aninhadas
# Verifique se um número é positivo, negativo ou zero.
numero = -5
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Extra: Agora é sua vez!
# 1º) Declare uma variável que armazene uma idade e verifique se a pessoa é criança (0-12 anos), adolescente (13-17 anos) ou adulta (18+ anos).

# Comece aqui...

# 2º) Crie um programa que verifique se um número é par ou ímpar e exiba a resposta.

# Comece aqui...

# 3º) Desenvolva uma lógica que determine se um ano é bissexto (divisível por 4 e não por 100, exceto se for divisível por 400).

# Comece aqui...
