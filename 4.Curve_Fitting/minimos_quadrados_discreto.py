"""
    Dada uma tabela com p-pontos(x1, y1), (x2, y2), ..., (xp, yp), implemente um programa
    que determina o polinomio de grau n, com n <= p, digamos pn(x) = a0 + a1x + ... an xn,
    que melhor ajusta a tal tabela de pontos pelo metodo dos minimos quadrados.
    Caso discreto.
"""
# Execute com Python3 com o seguinte comando no terminal:
# -------------------------------------------------------
# ~$ python3 minimos_quadrados_discreto.py
# -------------------------------------------------------


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from eliminacao_gauss import f_eliminacao_gauss


def minimos_quadrados_discreto(grau, n, x, y):
    """
    Regressao polinomial pelo metodo dos Minimos Quadrados.
    A partir de uma tabela de pontos, este metodo encontra um
    sistema de equacoes lineares do tipo Mx = v.
    Entao, resolvemos o sitema pelo metodo da Eliminacao de Gauss.

    :param grau: grau (ordem) do polinomio desejado
    :param n: numero de pontos dos vetores x e y
    :param x: vetor de pontos x da tabela
    :param y: vetor de pontos y da tabela
    :return: vetor com o valor dos coeficientes do polinomio encontrado
    """

    # O tamanho da matriz eh de acordo com o grau do polinomio desejado
    m = np.empty([grau + 1, grau + 1])

    print('Grau do polinomio: ' + str(grau))
    print('Numero de pontos: ' + str(n))
    print('Pontos x: ', end='')
    print(x)
    print('Pontos y: ', end='')
    print(y)
    print()

    # Elemento [0][0] recebe o valor do numero de pontos da tabela
    m[0][0] = n

    # Preenche a matriz com os somatorios das potencias de x: Somatorio(Xi^p)
    for k in range(0, grau):
        for i in range(k, grau + 1):
            soma_pot_i = 0
            # Percorre vetor de pontos x
            for j in range(0, n):
                # Calcula o valor da potencia de x e adiciona ao somatorio
                soma_pot_i = soma_pot_i + x[j - k] ** (i + k)
            # Preenche de forma simetrica
            m[k][i] = soma_pot_i
            m[i][k] = soma_pot_i

    # Elemento extremo da diagonal inferior direita
    soma_ultimo = 0
    # Ex.: Uma matriz 3x3, tomando indice inicial igual a 0, o ultimo elemento eh M[2][2]
    # e e e
    # e e e
    # e e x

    # Percorre vetor de pontos x
    for i in range(0, n):
        # calcula o valor da potencia de x
        soma_ultimo = soma_ultimo + x[i] ** (2 * (grau + 1) - 2)
    m[grau][grau] = soma_ultimo

    # O vetor independente v de Mx = v
    v = np.empty([grau + 1])
    soma_y = 0
    produto_x_y = 0

    # Percorre vetor de pontos y e calcula sua soma
    for i in range(0, n):
        soma_y = soma_y + y[i]
    # O primeiro elemento eh o somatorio do vetor y
    v[0] = soma_y

    # Seja i o indice do vetor e S o somatorio.
    # Vamos calcular S(Xi^i) * S(Yi)

    # Preenche o vetor independente
    for i in range(1, grau + 1):
        # Somatorio do produto entre x e y: S(Xi * Yi)
        soma_x_y = 0
        # Percorre vetor de pontos x e y
        for j in range(0, n):
            # Calcula o produto (Xi^i) * (Yi)
            produto_x_y = (x[j] ** i) * y[j]
            # Adiciona o produto ao somatorio
            soma_x_y = soma_x_y + produto_x_y
        # Adiciona o somatorio ao vetor independente
        v[i] = soma_x_y

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


def exibe_polinomio(coef_poli):
    """
    Exibe no console de saida o polinomio com seus coeficientes de variaveis

    :param coef_poli:
    :return: vetor com os coeficientes do polinomio
    """

    print('Polinomio funcao ajuste', end='\n\n')
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
    plt.plot(x, a, label='fit')
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


def plot_poly(x_data, y_data, coeff, xlab='x', ylab='y'):
    """
        Plota funcao de um polinomio com curvas suaves
    """
    m = len(coeff)
    x1 = min(x_data)
    x2 = max(x_data)
    dx = (x2 - x1) / 20.0
    x = np.arange(x1, x2 + dx / 10.0, dx)
    y = np.zeros((len(x))) * 1.0
    for i in range(m):
        y = y + coeff[i] * x ** i
    plt.plot(x_data, y_data, 'o', x, y, '-')
    plt.xlabel(xlab);
    plt.ylabel(ylab)
    plt.grid(True)
    plt.show()


def exibe_resultados(x, y, coef):
    exibe_polinomio(coef)
    ajuste = funcao_ajuste(x, coef)
    print('Pontos ajustados', end='\n\n')
    print(ajuste)
    # exibe_figura(x, y, ajuste)
    plot_poly(x, y, coef)


# ------------------ running ------------------

# Define a precisao decimal do pacote Numpy
np.set_printoptions(precision=4)

print('Escolha um problema:')
print('1\n2\n3\n')
escolha = input()

if escolha == '1':
    print('------- Problema 1 -------', end='\n\n')
    # Problema 1 (Livro Steven C. Chapra Metodos Numericos para Engenharia 5ed, pag 394)

    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

    coef_poli = minimos_quadrados_discreto(2, 6, x, y)

    exibe_resultados(x, y, coef_poli)

elif escolha == '2':
    print('------- Problema 2 -------', end='\n\n')
    # Problema 2 (Notas Lenimar)

    x = np.array([1.0, 1.5, 2.0, 2.5, 3.0])
    y = np.array([2.4, 4.1, 4.8, 6.0, 6.8])

    coef_poli = minimos_quadrados_discreto(1, 5, x, y)

    exibe_resultados(x, y, coef_poli)

elif escolha == '3':
    print('------- Problema 3 -------', end='\n\n')

    # Problema 3 (Notas Aparecido)
    x = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    y = np.array([2.0, 1.0, 0.5, 2.0, 1.5])

    coef_poli = minimos_quadrados_discreto(1, 5, x, y)

    exibe_resultados(x, y, coef_poli)
