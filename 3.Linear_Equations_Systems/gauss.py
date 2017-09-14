import numpy as np	

'''
	x = eliminacao_gauss(A, b)
	Ax = B
	
	Eliminiacao de Gauss eh realizada em duas fases: eliminacao e substituicao.
	A eliminacao transforma as equacoes na forma Ux = c,
	e a substituicao encontra o valor de cada coeficiente.
	
	@param A: Matriz dos coeficientes
	@param b: Vetor de constantes
'''
def eliminacao_gauss(A, b):
	#  Obtem o numero de linhas
	n = len(b)

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
				A[i, k + 1: n] = A[i, k + 1: n] - fator * A[k, k + 1: n]
				b[i] = b[i] - fator * b[k]

	# Substituicao regressiva de acordo com a definicao
	# Encontra o valor de cada coeficiente
	for k in range(n - 1, -1, -1):
		b[k] = (b[k] - np.dot(A[k, k + 1: n], b[k + 1: n])) / A[k, k]
	return b

# Sistema um
'''
	3x1 - 0.1x2 - 0.2x3 = 7.85
	0.1x1 + 7x2 - 0.3x3 = -19.3
	0.3x1 - 0.2x2 + 10x3 = 71.4
'''
a = np.array([
	[3.0, -0.1, -0.2], 
	[0.1, 7.0, -0.3],
	[0.3, -0.2, 10.0]])
b = np.array([7.85, -19.3, 71.4])

print 'Solucao: ' + str(eliminacao_gauss(a, b))

# Sistema dois
'''
	4x1 - 2x2 + x3 = 11
		3x2 - 1.5x3 = -10.5
				3x3 = 9
'''
c = np.array([
	[4.0, -2.0, 1.0], 
	[-2, 4.0, -2.0],
	[1.0, -2.0, 4.0]])
d = np.array([11.0, -16.0, 17.0])

print 'Solucao: ' + str(eliminacao_gauss(c, d))



