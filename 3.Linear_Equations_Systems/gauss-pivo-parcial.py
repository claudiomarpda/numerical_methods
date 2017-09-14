import numpy as np	

'''
	x = eliminacao_gauss(A, b)
	Ax = B
	
	Eliminiacao de Gauss eh realizada em duas fases: eliminacao e substituicao.
	A eliminacao transforma as equacoes na forma Ux = c,
	e a substituicao encontra o valor de cada coeficiente.
	A eliminacao com pivo parcial procura o maior elemento da primeira coluna de todo o sistema
	e utilizada a linha desse elemento como a primeira, o que eh feito trocando a posicao das linhas.
	
	@param A: Matriz dos coeficientes
	@param b: Vetor de constantes
'''
def eliminacao_gauss_pivo_parcial_linha(A, b):
	#  Obtem o numero de linhas
	n = len(b)
	analisa_pivo(A, b)
	# Eliminacao progressiva

	# k: Coluna atual
	for k in range(0, n - 1):
		# i: Linha atual
		# A partir da segunda linha (k + 1)
		for i in range(k + 1, n):
			# Nao executa linha i se Aik for 0
			if A[i, k] != 0.0:
				fator = A[i, k] / A[k, k]
				# A coluna k da linha atual seria substituida por 0, mas aqui nao eh preciso
				# A coluna k eh ignorada, pois seus valores sao irrelevantes para obter a solucao
				# Logo, inicia-se pela coluna 2 (k + 1)
				A[i, k + 1 : n] = A[i, k + 1 : n] - fator * A[k, k + 1 : n]
				b[i] = b[i] - fator * b[k]

	# Substituicao regressiva de acordo com a definicao
	# Encontra o valor de cada coeficiente
	for k in range(n - 1, -1, -1):
		b[k] = (b[k] - np.dot(A[k, k + 1 : n], b[k + 1 : n])) / A[k, k]
	return b

'''
	Troca a primeira linha com a linha de indice i
	@param A: Matriz dos coeficientes
	@param b: Vetor de constantes
	@param i: Linha alvo
'''
def troca_linha(A, b, i):
	# Numero de colunas
	# Troca as linhas da matriz
	c = A.shape[1]
	primeira = A[0, 0:c].copy()
	A[0] = A[i]
	A[i] = primeira

	# Troca as linhas do vetor
	primeira = b[0].copy()
	b[0] = b[i]  
	b[i] = primeira

'''
	Verifica a possibilidade de pivotamento parcial nas linhas.
	@param A: Matriz dos coeficientes
	@param b: Vetor de constantes
'''
def analisa_pivo(A, b):
	maior = A[0, 0]
	linha = 0
	for i in range(0, len(A)):
		if(A[i, 0] > maior):
			maior = A[i, 0]
			linha = i
	troca_linha(A, b, linha)


# Sistema um
'''
	0.1x1 + 7x2 - 0.3x3 = -19.3
	3x1 - 0.1x2 - 0.2x3 = 7.85
	0.3x1 - 0.2x2 + 10x3 = 71.4
'''
e = np.array([
	[0.3, -0.2, 10.0],
	[3.0, -0.1, -0.2], 
	[0.1, 7.0, -0.3]])
f = np.array([-19.3, 7.85, 71.4])

print 'Solucao: ' + str(eliminacao_gauss_pivo_parcial_linha(e, f))
