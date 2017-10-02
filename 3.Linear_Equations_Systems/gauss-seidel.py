"""
	Metodo iterativo de Gauss-Seidel para obter valores que satisfacam simultaneamente 
	um conjunto de 3 equacoes de um sistema linear. 
	Em cada iteracao, eh verificado o Erro Relativo e comparado com a tolerancia desejada.
	Eh verificado o determinante, Criterio das Linhas e o de Sassenfeld antes de iniciar as iteracoes.
"""

import numpy as np

"""
	Teorema: Criterio das Linhas para verificar condicao suficiente de convergencia.
	A soma dos valores absolutos de cada linha, exceto o elemento da diagonal principal,
	deve ser menor do que o valor absoluto do elemento da diagonal principal atual (A[i, i]).
	Ex.: A[1, 1], A[2, 2], ...

	@param A: Matriz dos coeficientes
"""
def criterio_linhas(A):
	# Percorre linhas
	for i in range(0, len(A)):
		soma = 0
		# Somatorio dos valores da linha, exceto o valor da diagonal principal
		for j in range(0, len(A)):
			soma = soma + np.abs(A[i][j])
		soma = soma - A[i][i]			
		# Verifica se o valor absoluto do elemento da diagonal principal eh menor do que 
		# o valor absoluto da soma dos elementos da linha
		if(np.abs(A[i][i]) < soma):
			print '[FALHA] Criterio das linhas nao satisfeito'
			return False
	print '[OK] Criterio das linhas satisfeito'
	return True

"""
	Teorema: Criterio de Sassenfeld para verificar condicao suficiente de convergencia.
	A soma do valor absoluto de todos elementos de cada linha, multiplicado pelo fator anterior, exceto o elemento da diagonal principal),
	deve ser menor do que o valor absoluto do elemento da diagonal principal atual (A[i, i]).
	Ex.: A[1, 1], A[2, 2], A[3, 3]...

	@param A: Matriz dos coeficientes
"""
def criterio_sassenfeld(A):
	n = len(A)
	# Inicia array de fatores com valores 1
	fator = np.ones(n)

	# Percorre linhas
	for i in range(0, n):
		soma = 0
		# Soma o valor absoluto de todos os elementos da linha e multiplica pelo fator resultante da linha anterior, 
		# menos do elemento da diagonal principal
		# Percorre colunas
		for j in range(0, n):
			soma = soma + A[i][j] * fator[j]	

		fator[i] = soma / np.abs(A[i][i])

	# Verifica se o valor do maior fator eh menor do que 1
	if(np.max(fator) >= 1):
		print '[FALHA] Criterio de Sassenfeld nao satisfeito'
		return False
	print '[OK] Criterio de Sassenfeld satisfeito'
	return True

"""
	Funcao principal para execucao do metodo de Gauss-Seidel.
	Obtem aproximacoes de raizes para solucao de um sistema linear
	de acordo com parametros informados.

	@param A: Matriz dos coeficientes
	@param tol: Tolerancia para o Erro Relativo das aproximacoes
	@param imax: Maximo numero de iteracoes
"""
def gauss_seidel(A, tol, imax):
	print 'Metodo de Gaus-Seidel para a matriz:'
	print A

	x1 = x2 = x3 = 0
	x1_anterior = x2_anterior = x3_anterior = 0

	# Verifica determinanete != 0
	if(np.linalg.det(A) == 0):
		print '[FALHA] Determinante = 0'
		quit()
	else:
		print '[OK] Determinante != 0'

	if(criterio_linhas(A) == False):
		if(criterio_sassenfeld(A) == False):
			quit()

	'''
		Obtem a primeira aproximacao de cada variavel.
		A primeira iteracao eh feita fora do loop para evitar condicional
		dentro do loop e obter maior desempenho da CPU.
	'''
	x1 = f_aprox_x1(x2, x3)
	x2 = f_aprox_x2(x1, x3)
	x3 = f_aprox_x3(x1, x2)
	x1_anterior = x1
	x2_anterior = x2
	x3_anterior = x3

	# Busca um Erro Relativo inferior a tolerancia
	for i in range(imax):
		x1 = f_aprox_x1(x2, x3)
		x2 = f_aprox_x2(x1, x3)
		x3 = f_aprox_x3(x1, x2)	

		atuais = [x1, x2, x3]
		anteriores = [x1_anterior, x2_anterior, x3_anterior]
		er = erro_relativo(atuais, anteriores)

		if(er < tol):
			break
		
		# Atualiza valores das aproximacoes para a proxima iteracao
		x1_anterior = x1
		x2_anterior = x2
		x3_anterior = x3

	print 'ER = ' + str(er)
	print 'Aproximacoes: ' + str(atuais)
	print 'Iteracoes: ' + str(i)

"""
	Calcula o Erro Relativo com os valores das variaveis atuais e da iteracao anterior

	@param atuais: Array com as aproximacoes atuais
	@param anteriores: Array com as aproximacoes anteriores
"""
def erro_relativo(atuais, anteriores):
	maior = 0
	# Indice do maior valor
	im = 0
	# Percorre todas as variaveis do sistema
	for i in range(len(atuais)):
		# Atualiza o maior valor e guarda seu indice
		if(atuais[i] > maior):
			maior = atuais[i]
			im = i

	# retorna erro relativo
	return np.abs(atuais[im] - anteriores[im]) / np.abs(atuais[im])

# Sistema para teste
'''
	3x1 - 0.1x2 - 0.2x3 = 7.85
	0.1x1 + 7x2 - 0.3x3 = -19.3
	0.3x1 - 0.2x2 + 10x3 = 71.4
'''
"""
	Calcula o valor aproximado de x1 de acordo com x2 e x3 atuais
"""
def f_aprox_x1(x2, x3):
	return (7.5 + 0.1 * x2 + 0.2 * x3) / 3

"""
	Calcula o valor aproximado de x2 de acordo com x1 e x3 atuais
"""
def f_aprox_x2(x1, x3):
	return (-19.3 - 0.1 * x1 + 0.3 * x3) / 7

"""
	Calcula o valor aproximado de x3 de acordo com x1 e x2 atuais
"""
def f_aprox_x3(x1, x2):
	return (71.4 - 0.3 * x1 + 0.2 * x2) / 10

# Matriz dos coeficientes 
A1 = np.array([
	[3.0, -0.1, -0.2],
	[0.1, 7.0, -0.3], 
	[0.3, -0.2, 10.0]])
b1 = np.array([7.85, -19.3, 71.4])

# Executa o metodo
gauss_seidel(A1, 10e-10, 1000)
