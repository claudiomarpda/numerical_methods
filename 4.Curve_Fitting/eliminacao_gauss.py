import numpy as np


def f_eliminacao_gauss(a, b):
    """
    Eliminiacao de Gauss eh realizada em duas fases: eliminacao e substituicao.
    A eliminacao transforma as equacoes na forma Ux = c,
    e a substituicao encontra o valor de cada coeficiente.

    :param a: Matriz dos coeficientes
    :param b: Vetor(independente) de constantes
    :return: Vetor de coeficientes
    """

    # Obtem o numero de linhas
    n = len(b)

    # Eliminacao progressiva

    # k: Coluna atual
    for k in range(0, n - 1):
        # i: Linha atual
        # A partir da segunda linha (k + 1)
        for i in range(k + 1, n):
            # Nao executa linha i se Aik for 0
            if a[i, k] != 0.0:
                fator = a[i, k] / a[k, k]
                # A coluna k da linha atual seria substituida por 0, mas aqui nao eh preciso
                # A coluna k eh ignorada, pois seus valores sao irrelevantes para obter a solucao
                # Logo, inicia-se pela coluna 2 (k + 1)
                a[i, k + 1: n] = a[i, k + 1: n] - fator * a[k, k + 1: n]
                b[i] = b[i] - fator * b[k]

    # Substituicao regressiva de acordo com a definicao
    # Encontra o valor de cada coeficiente
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1: n], b[k + 1: n])) / a[k, k]
    return b
