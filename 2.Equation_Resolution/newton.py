"""
Lista 02. Questao 01.
Metodo de Newton-Raphson para encontrar raizes aproximadas de equacoes com uma aproximacao inicial e uma tolerancia para f(x).
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
    f(x) = 2x + 1/x
'''
def f1_derivada(x):
    return 2 * x + 1 / x

'''
    f(x) = x^5 + (-10/9)x^3 + (5/21)x
'''
def f2(x):
    return (x ** 5.0) + ((-10.0 / 9.0) * (x ** 3.0)) + ((5.0 / 21.0) * x)

'''
    f(x) = 5x^4 + (-10/3)x^2 + 5/21
'''
def f2_derivada(x):
    return 5 * x ** 4 + ((-10.0 / 3.0) * (x ** 2.0)) + (5.0 / 21.0)

'''
    f(x) = x^3 - x - 1
'''
def f3(x):
    return x ** 3 - x - 1

'''
    f(x) = 3x^2 -1
'''
def f3_derivada(x):
    return 3 * x ** 2 - 1

'''
    @param aproximacao_inicial
    @param tolerancia: objetivo a ser alcancado
    @return: uma raiz aproximada da equacao
'''
def newton(aproximacao_inicial, tolerancia):
    global iteracoes
    global f_de_x

    iteracoes = 0
    f_de_x = 0
    x0 = aproximacao_inicial

    while True:
        iteracoes += 1
        # formula de newton-raphson: Xk+1 = Xk - (f(x) / f'(x))
        x1 = x0 - (f3(x0) / f3_derivada(x0))
        # f(x)
        f_de_x = f3(x1)

        # se f(x) = 0 ou se a tolerancia for alcancada,
        # x eh uma raiz da equacao
        if(f_de_x == 0.0 or abs(f_de_x) < tolerancia):
            # x eh uma raiz da equacao
            return x1
        else:
            # atualiza aproximacao
            x0 = x1

            if(LOG):
                print 'x = ' + str(x0) + '; f(x) = ' + str(f_de_x)

# Testes
# print 'Raiz aproximada x = ' + str(newton(0.75, 0.05)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
# print 'Raiz aproximada x = ' + str(newton(-0.8, 10e-3)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print 'Raiz aproximada x = ' + str(newton(1.5, 10e-3)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
print