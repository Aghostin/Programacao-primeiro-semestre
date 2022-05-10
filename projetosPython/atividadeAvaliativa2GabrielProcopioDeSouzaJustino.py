# Aluno: Gabriel Procópio de Souza Justino
# Sistemas de informação noturno - Quarta-feira
# Se rodar o código ele vai passar de exercício por exercício.

# ------------------------------------EXERCÍCIO 1------------------------------------------------
# 1. Elabore um programa que solicite ao usuário um número real e ao final imprima na tela se o
# número informado é maior que 10 (dez)
print('--Exercício 1--')

# Primeiro solicitamos a entrada do número.
numeroReal = float(input('Digite um número real: '))

# após isso apenas verificamos se ele é maior que 10 ou não.
# (Se não for, nada é imprimido, já que o comando não especificou)
if numeroReal > 10:
    print('O número informado é maior que 10.')
# ------------------------------------EXERCÍCIO 2------------------------------------------------
# 2. Escreva um programa que solicite ao usuário um número real e ao final imprima na tela se
# o número informado é maior ou igual a dez ou menor que 10 (dez)
print('--Exercício 2--')

# Novamente pedimos um input, após isso calculamos se é maior ou igual a dez, ou então menor.
# Em seguida, imprimimos.
numeroReal = float(input('Digite um número real: '))
if numeroReal >= 10:
    print('O número informado é maior ou igual a 10 (dez).')
else:
    print('O número informado é menor que 10 (dez).')
# ------------------------------------EXERCÍCIO 3------------------------------------------------
# 3. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o
# número informado é maior que dez, se é menor que dez, ou se é igual a dez
print('--Exercício 3--')

# Mesma coisa da atividade anterior, só que agora um para cada
numeroReal = float(input('Digite um número real: '))
if numeroReal > 10:
    print('O número informado é maior que 10.')
elif numeroReal == 10:
    print('O número informado é igual a 10.')
else:
    print('O número informado é menor que 10.')

# ------------------------------------EXERCÍCIO 4------------------------------------------------
# 4. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o
# número informado é positivo, negativo ou nulo (zero)
print('--Exercício 4--')

# Pedimos o número
numeroReal = float(input('Digite um número real: '))

# Verificamos
if numeroReal > 0:
    print('O número informado é positivo.')
elif numeroReal == 0:
    print('O número informado é nulo (zero).')
else:
    print('O número informado é negativo.')

# ------------------------------------EXERCÍCIO 5------------------------------------------------
# 5. Elabore um algoritmo que leia um número inteiro e imprima uma das mensagens: é múltiplo
# de 3, ou, não é múltiplo de 3
print('--Exercício 5--')

# Pedimos o número
numeroInteiro = int(input('Digite um número inteiro: '))

# Verificamos se é múltiplo e imprimimos
if numeroInteiro % 3 == 0:
    print('O número informado é múltiplo de 3.')
else:
    print('O número informado não é múltiplo de 3.')

# ------------------------------------EXERCÍCIO 6------------------------------------------------
# 6. Refazer o exercício anterior, solicitando antes o múltiplo a ser testado <- ? Isso quer dizer que é pra testar se
# o número é múltiplo de outro número informado? Vou considerar que sim, já que o comando é meio confuso.
print('--Exercício 6--')

# Pedindo os números
multiploTeste = int(input('-----Teste de múltiplo!-----\nInforme o múltiplo a ser testado: '))
numeroInteiro = int(input('Digite um número inteiro: '))

# Verificando se é múltiplo
if numeroInteiro % multiploTeste == 0:
    print(f'O número informado é múltiplo de {multiploTeste}.')
else:
    print(f'O número informado não é múltiplo de {multiploTeste}.')

# ------------------------------------EXERCÍCIO 7------------------------------------------------
# 7. Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como
# par ou ímpar
print('--Exercício 7--')

# Pedimos o número inteiro.
numeroInteiro = int(input('Digite um número inteiro: '))

# Verificamos e imprimimos. Numero par é aquele que é divisível por 2 com resto 0.
if numeroInteiro % 2 == 0:
    print('O número informado é par.')
# Caso contrário é ímpar.
else:
    print('O número informado é ímpar.')

# ------------------------------------EXERCÍCIO 8------------------------------------------------
# 8. Elabore um algoritmo que leia um número, e se ele for maior do que 20, imprimir a metade
# desse número, caso contrário, imprimir o dobro do número
print('--Exercício 8--')

# Pedimos o número real
numeroReal = float(input('Digite um número: '))

# Verificamos e imprimimos.
if numeroReal > 20:
    print(numeroReal/2)
else:
    print(numeroReal*2)

# ------------------------------------EXERCÍCIO 9------------------------------------------------
# 9. Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado
# seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele
print('--Exercício 9--')

# Pedimos os números
numeroInteiro = int(input('Digite um número inteiro: '))
numeroInteiro2 = int(input('Digite outro número inteiro: '))
# Somamos eles
soma = numeroInteiro + numeroInteiro2
# Verificamos e imprimimos
if soma > 10:
    print(soma**2)
else:
    print(soma/2)

# ------------------------------------EXERCÍCIO 10------------------------------------------------
# 10. O sistema de avaliação de determinada disciplina é composto por três provas. A primeira
# prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Considerando que a
# média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno
# desta disciplina e dizer se o aluno foi aprovado ou não
print('--Exercício 10--')

# Pedimos as notas de cada prova e calculamos a média
prova = float(input('Digite a nota da primeira prova: '))*2
prova2 = float(input('Digite a nota da segunda prova: '))*3
prova3 = float(input('Digite a nota da terceira prova: '))*5
mediaFinal = (prova+prova2+prova3)/10

# Verificamos e imprimimos
if mediaFinal >= 6.0:
    print(f'O aluno foi aprovado com média: {mediaFinal}')
else:
    print(f'O aluno foi reprovado com média: {mediaFinal}')

# ------------------------------------EXERCÍCIO 11------------------------------------------------
# 11. Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da
# pessoa mais pesada
# Dúvida: é possível escrever direto no CMD 'Digite o peso da pessoa: --Area do input--Kg?
print('--Exercício 11--')

# Perguntamos o nome da pessoa e seu peso
pessoa1 = str(input('Digite o nome da primeira pessoa: '))
pesopessoa1 = float(input(f'Digite o peso de {pessoa1} em KG: '))

# Repetimos o processo
pessoa2 = str(input('Digite o nome da segunda pessoa: '))
pesopessoa2 = float(input(f'Digite o peso de {pessoa2} em KG: '))

# Comparamos e imprimimos
if pesopessoa1 > pesopessoa2:
    print(f'{pessoa1} é a pessoa mais pesada.')
elif pesopessoa1 < pesopessoa2:
    print(f'{pessoa2} é a pessoa mais pesada.')
else:
    print('Ambos têm o mesmo peso.')

# ------------------------------------EXERCÍCIO 12------------------------------------------------
# 12. Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e
# 90, ou não
print('--Exercício 12--')

# Pedimos o input do numero
numeroReal = float(input('Digite um número real: '))

# Verificamos se ele está contindo entre 20 e 90, então imprimimos.
if numeroReal in range(20, 91):
    print('O número informado está entre 20 e 90.')
else:
    print('O número informado não está entre 20 e 90.')

# ------------------------------------EXERCÍCIO 13------------------------------------------------
# 13. Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se
# são iguais
print('--Exercício 13--')

# Pedimos os inputs dos números
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

# Verificamos qual é maior ou se são iguais.
if numero1 > numero2:
    print(f'O número {numero1:0.2f} é maior que o número {numero2:0.2f}.')
elif numero1 == numero2:
    print('Os dois números são iguais.')
else:
    print(f'O número {numero2:0.2f} é maior que o número {numero1:0.2f}.')

# ------------------------------------EXERCÍCIO 14------------------------------------------------
# 14. Escreva um programa em linguagem C(?????) que solicite ao usuário a média para aprovação
# em um curso e em seguida solicite ao usuário o nome, sexo e as 03 notas do aluno e ao
# final imprima a frase: "O aluno XXXXX foi aprovado com media YY" considerando o gênero
# do(a) aluno(a) e se foi aprovado(a) ou reprovado(a)
print('--Exercício 14--')

# Primeiro definimos as definições de gênero aceitas como resposta
# (não que isso sejam todas as possíveis. Mas supre o que o programa pede.
masculino = ['HOMEM', 'MASCULINO', 'M']
feminino = ['MULHER', 'FEMININO', 'F']

# Após isso, pedimos a entrada de cada parte solicitada no texto: média, nome, genero e notas
mediaAprovacao = float(input('Qual a média para aprovação da instituição? '))
nomealuno = str(input('Qual o nome do aluno? '))
sexoaluno = str(input('Qual o gênero do aluno (MASCULINO (M)/FEMININO (F)? '))
nota1 = float(input('Digite a nota do aluno na prova 1: '))
nota2 = float(input('Digite a nota do aluno na prova 2: '))
nota3 = float(input('Digite a nota do aluno na prova 3: '))

# Então, calculamos a média final do aluno com base nas notas
resultadofinalaluno = (nota1 + nota2 + nota3) / 3

# Agora verificamos se o aluno passou na instituição ou não e qual seu gênero

# Resultados caso ele/ela tenha sido aprovado(a)
if resultadofinalaluno >= mediaAprovacao and sexoaluno.upper() in masculino:
    print(f'''O aluno {nomealuno} foi aprovado com média {resultadofinalaluno:0.2f}.
    MÉDIA DA INSTITUIÇÃO: {mediaAprovacao} STATUS: APROVADO''')
elif resultadofinalaluno >= mediaAprovacao and sexoaluno.upper() in feminino:
    print(f'''A aluna {nomealuno} foi aprovada com média {resultadofinalaluno:0.2f}.
    MÉDIA DA INSTITUIÇÃO: {mediaAprovacao} STATUS: APROVADA''')

# Resultados caso ele/ela tenha sido reprovado(a)
elif resultadofinalaluno < mediaAprovacao and sexoaluno.upper() in masculino:
    print(f'''O aluno {nomealuno} foi reprovado com média {resultadofinalaluno:0.2f}.
    MÉDIA DA INSTITUIÇÃO: {mediaAprovacao} STATUS: REPROVADO''')
elif resultadofinalaluno < mediaAprovacao and sexoaluno.upper() in feminino:
    print(f'''A aluna {nomealuno} foi reprovada com média {resultadofinalaluno:0.2f}.
    MÉDIA DA INSTITUIÇÃO: {mediaAprovacao} STATUS: REPROVADA''')


# Aluno: Gabriel Procópio de Souza Justino
# Sistemas de informação noturno - Quarta-feira
