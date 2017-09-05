"""
Lista 02. Questao 01.
Metodo da Secante para encontrar raizes aproximadas de equacoes com duas aproximacoes iniciais e uma tolerancia para f(x).
"""

import math

# quando flag ativa, exibe informacoes durante o processo
LOG = True

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
        x2 = (x0 * f2(x1) - x1 * f2(x0)) / (f2(x1) - f2(x0)) 
        # f(x)
        f_de_x = f2(x2)

        # se f(x) = 0 ou se a tolerancia for alcancada,
        # x eh uma raiz da equacao
        if(f_de_x == 0.0 or abs(f_de_x) < tolerancia):
            # x eh uma raiz da equacao
            return x2
        else:
            # atualiza aproximacoes
            x0 = x1
            x1 = x2

            if(LOG):
                print 'x2 = ' + str(x2) + '; f(x) = ' + str(f_de_x) + '; i = ' + str(iteracoes) 

# Testes
# print 'Raiz aproximada x = ' + str(secante(0.5, 1.0, 0.05)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
# print 'Raiz aproximada x = ' + str(secante(0.8, 1.0, 10e-3)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print 'Raiz aproximada x = ' + str(secante(1, 2, 10e-3)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print