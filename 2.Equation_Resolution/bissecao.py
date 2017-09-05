"""
Questao 01 da lista 02.
Metodo da bissecao para encontrar raizes aproximadas de equacoes com um intervalo inicial e uma tolerancia para f(x).
"""

import math

# quando flag ativa, exibe informacoes durante o processo
LOG = True
# evita loop infinito
MAX_ITERACAO = 9999

'''
    f(x) = x^2 + ln(x)
'''
def f1(x):
    return x ** 2 + math.log(x)

'''
    f(x) = x^5 - (10/9)x^3 + (5/21)x
'''
def f2(x):
    return (x ** 5.0) + ((-10.0 / 9.0) * (x ** 3.0)) + ((5.0 / 21.0) * x)

'''
    f(x) = x^3 - x - 1
'''
def f3(x):
    return x ** 3 - x - 1

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
    f_de_a = f3(a)
    f_de_b = f3(b)

    # verifica se existe raiz neste intervalo
    if((f_de_a > 0 and f_de_b > 0) or (f_de_a < 0 and f_de_b < 0)):
        print 'Nao existe raiz no intervalo dado'
        return
    else:
        # procura por raiz
        while True:
            if(iteracoes > MAX_ITERACAO):
                print 'AVISO: Limite de iteracoes alcancado'
                return 0
            else:
                iteracoes += 1
            # formula da bissecao: ponto medio de [a, b]
            x = (a + b) / 2.0
            # f(x)
            f_de_x = f3(x)

            if(LOG):
                print 'x = ' + str(x) + '; f(x) = ' + str(f_de_x) + '; i = ' + str(iteracoes) 

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
                    print 'Novo intervalo: [' + str(a) + ', ' + str(b) + '];'

# Testes
# print 'Raiz aproximada x = ' + str(bissecao(0.5, 1.0, 0.05)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
# print 'Raiz aproximada x = ' + str(bissecao(-1, 0.25, 10e-3)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print 'Raiz aproximada x = ' + str(bissecao(1, 2, 10e-3)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print
