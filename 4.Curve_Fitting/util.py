from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np


def exibe_polinomio(coef_poli):
    """
    Exibe no console de saida o polinomio com seus coeficientes de variaveis

    :param coef_poli:
    :return: vetor com os coeficientes do polinomio
    """

    print('{0:.4f}'.format(coef_poli[0]), end='  ')
    # Cada indice significa um coeficiente e um grau do polinomio
    for i in range(1, len(coef_poli)):
        # Coeficiente negativo
        if coef_poli[i] < 0:
            print(' -', end=' ')
        # Coeficiente positivo
        else:
            print(' +', end=' ')

        print('{0:.4f}'.format(coef_poli[i]), end=' (x^')
        print(i, end=')')
    print(end='\n\n')


def exibe_figura(x, y, a):
    """
    Exibe uma figura com o diagrama de dispersao da tabela e o grafico do polinomio ajuste

    :param x: vetor de pontos x da tabela
    :param y: vetor de pontos y da tabela
    :param a: vetor de pontos resultantes da funcao de ajuste
    :return:
    """

    # TODO: Suavizar as curvas do grafico desenhado

    style.use('ggplot')

    # plota funcao ajuste
    plt.plot(x, a)
    # plota diagrama de dispesao
    plt.scatter(x, y)

    plt.title('Ajuste de curvas')
    plt.ylabel('Eixo Y')
    plt.xlabel('Eixo X')
    plt.show()


def funcao_ajuste(x, coef):
    """
    Calcula f(x) para todos os pontos do vetor x da tabela

    :param x: vetor de pontos x da tabela
    :param coef: coeficientes do polinomio ajuste
    :return: um vetor de pontos resultantes da funcao de ajuste
    """

    # n coeficientes
    n = len(coef)

    ajuste = np.empty([len(x)])

    # Para cara ponto do vetor x
    for i in range(0, len(x)):
        # Para cada coeficiente
        for j in range(0, n):
            ajuste[i] = ajuste[i] + coef[j] * (x[i] ** j)

    return ajuste


def plot_poly(pontos_x, pontos_y, coef):
    """
        Plota funcao de um polinomio com curvas suaves
    """

    m = len(coef)
    x1 = min(pontos_x)
    x2 = max(pontos_x)
    dx = (x2 - x1) / 20.0

    x = np.arange(x1, x2 + dx / 10.0, dx)
    y = np.zeros((len(x))) * 1.0

    for i in range(m):
        y = y + coef[i] * x ** i

    plt.plot(pontos_x, pontos_y, 'o', x, y, '-')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.grid(True)
    plt.show()


def plot_poly2(pontos_x, pontos_y, coef):
    """
        Plota funcao de um polinomio com curvas suaves
    """

    # coef

    m = len(coef)
    x1 = min(pontos_x)
    x2 = max(pontos_x)
    dx = (x2 - x1) / 20.0

    x = np.arange(x1, x2 + dx / 10.0, dx)
    y = np.zeros((len(x))) * 1.0

    for i in range(m):
        y = y + coef[i] * x ** i

    # plota

    plt.plot(pontos_x, pontos_y, x, y, '-')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.grid(True)
    plt.show()
