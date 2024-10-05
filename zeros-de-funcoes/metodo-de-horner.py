import matplotlib.pyplot as plt
import numpy as np
import math

coeficientes = [1, -12.0953, 33.6161, 55.4476, -260.915, 119.827]

#coeficientes = [1, 28.3001, 308.576, 1614.77, 4044.8, 3880.73]

#coeficientes = [1, -20.0253, 156.407, -595.207, 1103.49, -797.472]


def f_string():
    return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"
    #return "x** 5 - 20.0253*x** 4 + 156.407*x** 3 - 595.207*x** 2 + 1103.49*x - 797.472"

def f(x):
    return x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827
    #return x** 5 - 20.0253*x** 4 + 156.407*x** 3 - 595.207*x** 2 + 1103.49*x -797.472  

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

        coeficientes_P.append(coeficientes_P_atual)
        coeficientes_P_linha.append(coeficientes_P_linha_atual)
        estimativas.append((x, f(x), f_linha(x), erro))

        if erro < e():
            return x, estimativas, coeficientes_P, coeficientes_P_linha
        

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
    print(f"{'     '}{'k':<6}{'b5k':>20}{'b4k':>20}{'b3k':>20}{'b2k':>20}{'b1k':>20}{'b0k':>20}")
    for i, (b5, b4, b3, b2, b1, b0) in enumerate(coeficientes_P):
        print(f"{'     '}{i:<6}{b5:>20.9e}{b4:>20.9e}{b3:>20.9e}{b2:>20.9e}{b1:>20.9e}{b0:>20.9e}")

print()




if len(coeficientes_P):
    print("\tCoeficientes ci do Polinômio f(x)")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'c5k':>20}{'c4k':>20}{'c3k':>20}{'c2k':>20}{'c1k':>20}")
    for i, (c5, c4, c3, c2, c1) in enumerate(coeficientes_P_linha):
        print(f"{'     '}{i:<6}{c5:>20.9e}{c4:>20.9e}{c3:>20.9e}{c2:>20.9e}{c1:>20.9e}")

print()


if len(estimativas) > 0:
    # Exibir tabela de interações
    print("\tEstimativas")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'xk':>20}{
          'f(xk)':>20}{'f\'(xk)':>20}{'ERk':>20}")
    for i, (x, fx, f_linha, er) in enumerate(estimativas):
        if isinstance(er, str):
            print(f"{'     '}{i:<6}{x:>20.9e}{fx:>20.9e}{f_linha:>20.9e}{
                  er:>20}")  # Exibe a string sem formatação
        else:
            print(f"{'     '}{i:<6}{x:>20.9e}{
                  fx:>20.9e}{f_linha:>20.9e}{er:>20.9e}")
# Exibir o valor final da raiz
if raiz is not None:
    print(f"{'     '}Raiz z5 = {raiz:>20.9e}")

input()
