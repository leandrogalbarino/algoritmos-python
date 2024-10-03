import matplotlib.pyplot as plt
import numpy as np
import math

coeficientes = [1, -12.0953, 33.6161, 55.4476, -260.915, 119.827]

#coeficientes = [1, 28.3001, 308.576, 1614.77, 4044.8, 3880.73]


def f_string():
    return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"
       

def f(x):
    return x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827

def f_linha(x):
    return 5*x**4 - 4*12.0953*x**3 + 3*33.6161*x**2 + 2*55.4476*x - 260.915
    
def e():
    return 0.000001


def tolerancia(x, x_anterior):
    return abs((x - x_anterior) / x)


def pedir_numero_float(mensagem):
    while True:
        try:
            x = float(input(mensagem))
            return x
        except ValueError:
            print("Entrada invalida, tente novamente!")


def horner(coeficientes, x):

    n = len(coeficientes) - 1  # Grau do polinômio
    p = coeficientes[0]  # Primeiro coeficiente (a_N)
    p_linha = 0  # Derivada começa com zero

    coeficientes_P = [p]  # Coeficientes do polinômio
    coeficientes_P_linha = []  # Coeficientes da derivada


    # Aplicando o método de Horner para P(x) e P'(x)
    for i in range(1, n+1):
        p_linha = p_linha * x + p  # Derivada de Horner
        p = p * x + coeficientes[i]  # Polinômio de Horner

        
        coeficientes_P_linha.append(p_linha)  
        coeficientes_P.append(p)  # Coeficiente do polinômio

    return p, p_linha, coeficientes_P, coeficientes_P_linha


def metodo_de_horner():
    x_anterior = pedir_numero_float("Chute inicial:")


    coeficientes_P = []
    coeficientes_P_linha = []
    estimativas = []  # Lista para armazenar as interações
    estimativas.append((x_anterior, f(x_anterior),
                      f_linha(x_anterior), "--------"))

    while True:
        p_xn, pn_linha_xn, coeficientes_P_atual, coeficientes_P_linha_atual = horner(coeficientes, x_anterior)

        # Adiciona os coeficientes da iteração atual às listas

        if pn_linha_xn == 0:
            print("Derivada igual a zero, metodo nao pode continuar.")
            return None, []

        x = x_anterior - p_xn / pn_linha_xn
        erro = tolerancia(x, x_anterior)  # Calcula a tolerância

        if erro < e():
            return x, estimativas, coeficientes_P, coeficientes_P_linha
        
        coeficientes_P.append(coeficientes_P_atual)
        coeficientes_P_linha.append(coeficientes_P_linha_atual)
        estimativas.append((x, f(x), f_linha(x), erro))

        if (len(estimativas) > 100):
            print("Metodo de Horner nao convergiu.")
            return None, []

        x_anterior = x


raiz, estimativas, coeficientes_P, coeficientes_P_linha = metodo_de_horner()

# Preparar dados para o gráfico
x_vals = np.linspace(-3, 7, 1000)  # Intervalo ajustado para incluir a raiz

y_vals = f(x_vals)

# Plotar a função
plt.plot(x_vals, y_vals, label=f_string())
plt.axhline(0, color='black', linewidth=0.5)  # Linha do eixo x

# Se a raiz foi encontrada, marcá-la no gráfico
if raiz is not None:
    plt.plot(raiz, f(raiz), 'ro', label=f"Raiz = {raiz:.10f}")

# Configurações do gráfico
plt.title('Método do Newton')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()


print()
print("\tMÉTODO DE HORNER | DETERMINAÇÃO DA RAÍZ z5")
if len(coeficientes_P):
    print("\tCoeficientes bi do Polinômio f(x)")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'b5k':>16}{'b4k':>16}{'b3k':>16}{'b2k':>16}{'b1k':>16}{'b0k':>16}")
    for i, (b5, b4, b3, b2, b1, b0) in enumerate(coeficientes_P):
        print(f"{'     '}{i:<6}{b5:>16.10f}{b4:>16.10f}{b3:>16.10}{b2:>16.10f}{b1:>16.10f}{b0:>16.10f}")

print()




if len(coeficientes_P):
    print("\tCoeficientes ci do Polinômio f(x)")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'c5k':>16}{'c4k':>16}{'c3k':>16}{'c2k':>16}{'c1k':>16}")
    for i, (c5, c4, c3, c2, c1) in enumerate(coeficientes_P_linha):
        print(f"{'     '}{i:<6}{c5:>16.10f}{c4:>16.10f}{c3:>16.10}{c2:>16.10f}{c1:>16.10f}")

print()


if len(estimativas) > 0:
    # Exibir tabela de interações
    print("\tEstimativas")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'xk':>16}{
          'f(xk)':>16}{'f\'(xk)':>16}{'ERk':>16}")
    for i, (x, fx, f_linha, er) in enumerate(estimativas):
        if isinstance(er, str):
            print(f"{'     '}{i:<6}{x:>16.10f}{fx:>16.10f}{f_linha:>16.10}{
                  er:>16}")  # Exibe a string sem formatação
        else:
            print(f"{'     '}{i:<6}{x:>16.10f}{
                  fx:>16.10f}{f_linha:>16.10}{er:>16.10f}")
# Exibir o valor final da raiz
if raiz is not None:
    print(f"{'     '}Raiz z5 = {raiz:>16.10f}")

input()
