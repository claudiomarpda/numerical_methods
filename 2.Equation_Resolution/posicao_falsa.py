import math

'''
    f(x) = x^2 + log(x)
'''
def equacao_um(x):
    return x ** 2 + math.log(x)

'''
	f(x) = ?
'''
def equacao_dois(x):
	# TODO: define and test this equation

'''
	f(x) = ?
'''
def equacao_tres(x):
	# TODO: define and test this equation


'''
    @a: intervalo inferior
    @b: intervalo superior
    @tolerancia: objetivo a ser alcancado
    @return uma raiz aproximada da equacao
'''
def posicao_falsa(a, b, tolerancia):

    # calcula f(a) e f(b)
    resultado_a = equacao_um(a)
    resultado_b = equacao_um(b)

    # verifica se existe raiz neste intervalo
    if((resultado_a > 0 and resultado_b > 0) or (resultado_a < 0 and resultado_b < 0)):
        print 'Nao existe raiz no intervalo dado'
        return
    else:
    	# procura por raiz
        while True:
        	# formula da posicao falsa
            x = (a * equacao_um(b) - b * equacao_um	(a)) / (equacao_um(b) - equacao_um(a))
            # f(x)
            resultado_x = equacao_um(x)
            # se f(x) = 0, x eh uma raiz da equacao ou
            # se a tolerancia for alcancada
            if(resultado_x == 0.0 or abs(resultado_x) < tolerancia):
                # x eh uma raiz da equacao
                return x
            # raiz nao encontrada
            else:
                if(resultado_x > 0):
            		# novo intervalo: [a, x]
                    b = x
                else:
                	# novo intervalo: [x, b]
                    a = x


# Teste com o intervalo [0.5, 1] e tolerancia |f(x)| = 0.05
print 'Raiz aproximada: ' + str(posicao_falsa(0.5, 1.0, 0.05))