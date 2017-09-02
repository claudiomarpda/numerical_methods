"""
Lista 02. Questao 01.
Metodo da Secante para encontrar raizes aproximadas de equacoes com duas aproximacoes iniciais e uma tolerancia para f(x).
"""

import math

# quando flag ativa, exibe informacoes durante o processo
LOG = True

'''
    f(x) = x^2 + log(x)
'''
def f1(x):
    return x ** 2 + math.log(x)

'''
    f(x) = x + ln(x)
'''
def f2(x):
    return x + math.log(x)

'''
    f(x) = x^3 - x - 1
'''
def f3(x):
    return x ** 3 - x - 1

'''
    @param x0: primeira aproximacao 
    @param x1: segunda aproximacao
    @param tolerancia: objetivo a ser alcancado
    @return: uma raiz aproximada da equacao
'''
def secante(x0, x1, tolerancia):
    global iteracoes
    global f_de_x

    iteracoes = 0
    f_de_x = 0

    while True:
        iteracoes += 1
        # formula do metodo da secante
        x2 = (x0 * f1(x1) - x1 * f1(x0)) / (f1(x1) - f1(x0)) 
        # f(x)
        f_de_x = f1(x2)

        # se f(x) = 0 ou se a tolerancia for alcancada,
        # x eh uma raiz da equacao
        if(f_de_x == 0.0 or abs(f_de_x) < tolerancia):
            # x eh uma raiz da equacao
            return x2
        else:
            x0 = x1
            x1 = x2

            if(LOG):
                print 'x2 = ' + str(x2) + '; f(x) = ' + str(f_de_x)

# Teste com o intervalo [0.5, 1] e tolerancia |f(x)| = 0.05
print 'Estivamtiva inicial x0 = 0.1, x1 = 1; |f(x)| < 0.05'
print 'Raiz aproximada x = ' + str(secante(0.1, 1.0, 5e-2)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
