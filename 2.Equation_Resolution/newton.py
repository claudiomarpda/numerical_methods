"""
Lista 02. Questao 01.
Metodo de Newton-Raphson para encontrar raizes aproximadas de equacoes com uma aproximacao inicial e uma tolerancia para f(x).
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
    f(x) = 2x + 1/x
'''
def f1_derivada(x):
    return 2 * x + 1 / x

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
        x1 = x0 - (f1(x0) / f1_derivada(x0))
        # f(x)
        f_de_x = f1(x1)

        # se f(x) = 0 ou se a tolerancia for alcancada,
        # x eh uma raiz da equacao
        if(f_de_x == 0.0 or abs(f_de_x) < tolerancia):
            # x eh uma raiz da equacao
            return x1
        else:
            x0 = x1

            if(LOG):
                print 'x = ' + str(x0) + '; f(x) = ' + str(f_de_x)

# Teste com estimativa inicial 0.75 e tolerancia |f(x)| = 0.05
print 'Estivamtiva inicial x0 = 0.75; |f(x)| < 0.05'
print 'Raiz aproximada x = ' + str(newton(0.75, 5e-2)) + '; f(x) = ' + str(f_de_x) + '; ' + str(iteracoes) + ' iteracoes'
