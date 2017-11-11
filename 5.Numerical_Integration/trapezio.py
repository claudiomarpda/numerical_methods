# Execute com Python3 com o seguinte comando no terminal:
# -------------------------------------------------------
# ~$ python3 trapezio.py
# -------------------------------------------------------
"""
    Considere o calculo por integracao numerica de Integral f(x)dx no intervalo [a,b].
    Considere o intervalo [a,b] dividido em n-subintervalos, i.e, por uma malha de (n+1)
    pontos x0, x1, ..., xn-1, xn, igualmente espacados de h = (b-a)/n.
"""

import math


def trapezio_repetida(f, a, b, t):
    """
    Implementa a regra do Trapezio repetida.

    :param f: a funcao
    :param a: o intervalo inferior
    :param b: o intervalo superior
    :param t: a tabela de pontos
    :return: uma aproximacao da integral da funcao
    """

    # numero de pontos da tabela t
    n = len(t)

    soma = 0
    h = (b - a) / (n - 1)
    print('h: ' + str(h))

    # somatorio de i=0 ateh n-2
    for i in range(0, n - 1):
        soma = soma + (f(t[i]) + f(t[i + 1]))

    return (h / 2.0) * soma


''' ------- funcoes ------- '''


def f1(x):
    return math.sqrt(x)


def f2(x):
    return math.cos(x)


def f3(x):
    return math.sin(x)


''' ------- tabelas ------- '''

tab1 = [1.0, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
tab2 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
tab_q7 = [1.2, 1.3, 1.4, 1.5, 1.6]


''' ------- running ------- '''

print('----- Problema 1 -----', end='\n\n')
print('Integral de raiz(x)dx no intervalo [1, 1.3]')
print('Tabela', end=' ')
print(tab1)
r = trapezio_repetida(f1, 1.0, 1.3, tab1)
print('Integral aproximada:', end=' ')
print(r, end='\n\n\n')

print('----- Problema 2 -----', end='\n\n')
print('Integral de cos(x)dx no intervalo [0, 1]')
print('Tabela', end=' ')
print(tab2)
r = trapezio_repetida(f2, 0.0, 1.0, tab2)
print('Integral aproximada:', end=' ')
print(r, end='\n\n\n')

print('----- Problema 3 -----', end='\n\n')
print('Integral de sen(x)dx no intervalo [1.2, 1.6]')
print('Tabela', end=' ')
print(tab_q7)
r = trapezio_repetida(f3, 1.2, 1.6, tab_q7)
print('Integral aproximada:', end=' ')
print(r, end='\n\n\n')
