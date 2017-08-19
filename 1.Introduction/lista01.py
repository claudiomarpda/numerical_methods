'''
1. Introducao aos metodos numericos
	Representacao de numeros em maquinas
	Truncamento, arredondamento e erros
	Propagacao de erros
'''

import math

def questao_15():
	i = 1
	soma = 0
	
	for i in range(1, 1001):
		soma = soma + (i * (i + 1))/2

	print 'A soma da serie eh ' + str(soma)

# subprograma da questao 16
def fatorial(n):
	resultado = 1
	#Multiplica o valor contido em 'resultado' de 1 ate n vezes
	for i in range(1, n+1):
		resultado = resultado * i
	#Retorna o valor do fatorial para quem a chamou
	return resultado

# parametro x eh o valor exponencial de Euler (e^x)
def question_16(x):
	e = 1 + x
	for i in range(2, 25):
		#fatorial(i) eh o valor obtido no retorno do subprograma fatorial(n), com o n variando de 2 a 25
		#O operador '**' representa o numero elevado ao expoente. No caso abaixo, o valor de x elevado ao expoente i
		e = e + (x ** i) / fatorial(i)
	print 'Valor de (e ^ ' + str(x) + ') eh ' + str(e)

def questao_17():
    soma = 0
    print '(k, S(k))'
    for k in range(1, 11):
        soma = soma + (math.cos(3 * math.pi * k / 4.0) * (2.0 / (k ** 2)))
        print str(k) + ', ' + str(soma)

def questao_18():
	raio = 4.0 # raio de 4 metros
	volume = (4.0 / 3) * math.pi * (raio ** 3)
	print 'Volume para um raio de 4 metros com acrescimo de 40% sobre seu volume: ' + str(volume * 1.4)

def questao_20():
	n = 10000
	soma_exata = (math.pi ** 4) / 90.0

	# ordem crescente
	soma_aproximada = 0
	for k in range(1, n + 1):
	 	soma_aproximada += 1.0 / (k ** 4)

 	erro_absoluto = soma_exata - soma_aproximada
	erro_relativo = erro_absoluto / soma_exata
	print 'Erro relativo percentual na ordem crescente: ' + str(erro_relativo * 100) + ' %'

	# ordem decrescente
	soma_aproximada = 0
	for k in range(n, 0, -1):
		soma_aproximada += 1.0 / (k ** 4)

	erro_absoluto = soma_exata - soma_aproximada
	erro_relativo = erro_absoluto / soma_exata
	print 'Erro relativo percentual na ordem decrescente: ' + str(erro_relativo * 100) + ' %'


print 'Questao 15'
questao_15()
# Saida
# A soma da serie eh 167167000

print '\nQuestao 16'
question_16(-0.15)
# Saida
# Valor (e ^ -0.15) eh 0.860707976425
question_16(1/	0.15)
# Saida
# Valor (e ^ 6.66666666667) eh 785.771960035

print '\nQuestao 17'
questao_17()
# Saida
'''
(k, S(k))
1, -1.41421356237
2, -1.41421356237
3, -1.25707872211
4, -1.38207872211
5, -1.32551017961
6, -1.32551017961
7, -1.35437168089
8, -1.32312168089
9, -1.34058110758
10, -1.34058110758
'''

print '\nQuestao 18'
questao_18()
# Saida
# Volume para um raio de 4 metros com acrescimo de 40% sobre seu volume: 375.315602349

print '\nQuestao 20'
questao_20()
# Saida
# Erro relativo percentual na ordem crescente: 2.55828955452e-11 %
# Erro relativo percentual na ordem decrescente: 3.07733306478e-11 %
