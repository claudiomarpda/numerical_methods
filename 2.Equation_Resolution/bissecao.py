"""
Questao 01 da lista 02.
Metodo da bissecao para encontrar raizes aproximadas de equacoes com um intervalo inicial e uma tolerancia para f(x).
"""

import math

# quando flag ativa, exibe informacoes durante o processo
LOG = True

'''
    f(x) = x^2 + log(x)
'''
def equacao_um(x):
    return x ** 2 + math.log(x)

'''
    f(x) = x + ln(x)
'''
def equacao_dois(x):
    return x + math.log(x)

'''
    f(x) = ?
'''
def equacao_tres(x):
    # TODO: define and test this equation
    return 0

'''
    @param a: intervalo inferior
    @param b: intervalo superior
    @param tolerancia: objetivo a ser alcancado
    @return: uma raiz aproximada da equacao
'''
def bissecao(a, b, tolerancia):
    global iteracoes
    global f_de_x
    
    iteracoes = 0
    f_de_x = 0

    # calcula f(a) e f(b)
    f_de_a = equacao_um(a)
    f_de_b = equacao_um(b)

    # verifica se existe raiz neste intervalo
    if((f_de_a > 0 and f_de_b > 0) or (f_de_a < 0 and f_de_b < 0)):
        print 'Nao existe raiz no intervalo dado'
        return
    else:
        # procura por raiz
        while True:
            iteracoes += 1
            # formula da bissecao: ponto medio de [a, b]
            x = (a + b) / 2.0
            # f(x)
            f_de_x = equacao_um(x)

            if(LOG):
                print 'x = ' + str(x) + '; f(x) = ' + str(f_de_x)

            # se f(x) = 0 ou se a tolerancia for alcancada,
            # x eh uma raiz da equacao
            if(f_de_x == 0.0 or abs(f_de_x) < tolerancia):
                # x eh uma raiz aceitavel da equacao
                return x
            # raiz nao encontrada
            else:
                if(f_de_x > 0):
            		# novo intervalo: [a, x]
                    b = x
                else:
                	# novo intervalo: [x, b]
                    a = x
                if(LOG):
                    print 'Novo intervalo: [' + str(a) + ', ' + str(b) + ']'

# Teste com o intervalo [0.5, 1] e tolerancia |f(x)| = 0.05
print 'Intervalo [0.5, 1]; |f(x)| < 0.05'
print 'Raiz aproximada x = ' + str(bissecao(0.5, 1.0, 0.05)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print
