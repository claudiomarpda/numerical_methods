"""
    Caso continuo.
    Dada uma funcao f(x), implemente um programa que determina o polinomio de gray n,
    digamos pn(x) = a0 + a1x + ... anx^n, que melhor ajusta o grafico de f pelo metodo
    dos minimos quadrados.
    Entrada: a funcao f e o grau n do polinomio ajuste.
    Saida: os coeficientes a0, a1, ..., an do polinomio ajuste e uma figura
    com o grafico da funcao f dada e o grafico do polinomio ajuste sobrepostos.
"""
# Execute com Python3 com o seguinte comando no terminal:
# -------------------------------------------------------
# ~$ python3 minimos_quadrados_continuo.py
# -------------------------------------------------------


from eliminacao_gauss import f_eliminacao_gauss
from util import *


def f_(x):
    return 4 * (x ** 3)


def a11(x):
    return x


def a12(x):
    return (x ** 2) / 2


def a22(x):
    return (x ** 3) / 3


def b1(x):
    return x ** 4


def b2(x):
    return 4 * (x ** 5) / 5


def minimos_quadrados_continuo(grau, a, b):
    """
    Regressao polinomial pelo metodo dos Minimos Quadrados para um caso especifico.
    A partir de uma funcao e um intervalo de integracao, este metodo encontra um
    sistema de equacoes lineares do tipo Mx = v.
    Entao, resolvemos o sitema pelo metodo da Eliminacao de Gauss.

    :param a: intervalo inferior da integral
    :param b: intervalo superior da integral
    :param grau: grau (ordem) do polinomio desejado
    :return: vetor com o valor dos coeficientes do polinomio encontrado
    """

    # O tamanho da matriz eh de acordo com o grau do polinomio desejado
    m = np.empty([grau + 1, grau + 1])

    print('Grau do polinomio: ' + str(grau))
    print('Intervalo: ', end='')
    print('(a, b) = (', end='')
    print(a, end=', ')
    print(b, end=')\n\n')

    # Preenche a matriz com a integral do produto das g(x)
    # g(x)*g(x)

    # a11
    gg = a11(b) - a11(a)
    m[0][0] = gg

    # a12 = a21
    gg = a12(b) - a12(a)
    # Preenche de forma simetrica
    m[0][1] = gg
    m[1][0] = gg

    # a22
    gg = a22(b) - a22(a)
    m[1][1] = gg

    # O vetor independente v de Mx = v
    v = np.empty([grau + 1])

    v[0] = b1(b) - b1(a)
    v[1] = b2(b) - b1(a)

    print('Matriz simetrica', end='\n\n')
    print(m)
    print()
    print('Vetor independente', end='\n\n')
    print(v)
    print()

    # Temos um sistema do tipo Mx = v
    # Vamos resolve-lo de forma simultanea com Eliminacao de Gauss

    # Obtem o valor dos coeficientes do polinomio
    return f_eliminacao_gauss(m, v)


# ------------------ running ------------------

# Define a precisao decimal do pacote Numpy
np.set_printoptions(precision=4)

print('------- Problema 1 -------', end='\n\n')

# 4x^3
coef_real = np.array([0, 0, 0, 4])
print('Polinomio real')
exibe_polinomio(coef_real)
print()

coef_ajuste = minimos_quadrados_continuo(1, 0, 1)
print('Polinomio ajuste')
exibe_polinomio(coef_ajuste)
print()

k_points = 2
# Inicia array com k intervalos
# linspace(inicio, fim, intervalo)
x = np.linspace(0, 1, num=k_points)
y = np.linspace(0, 1, num=k_points)

plot_poly2(x, y, coef_real)


