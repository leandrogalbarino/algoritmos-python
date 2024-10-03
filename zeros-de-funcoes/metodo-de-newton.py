import matplotlib.pyplot as plt
import numpy as np
import math

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


def metodo_de_newton():
    x_anterior = pedir_numero_float("Chute inicial:")
    
    interacoes = []  # Lista para armazenar as interações
    interacoes.append((x_anterior, f(x_anterior), f_linha(x_anterior), "--------"))

    while True:
        if f_linha(x_anterior) == 0:
            print("Derivada igual a zero, metodo nao pode continuar.")
            return None, []

        x = x_anterior - f(x_anterior)/ f_linha(x_anterior)
        erro = tolerancia(x, x_anterior)  # Calcula a tolerância
        interacoes.append((x, f(x), f_linha(x), erro))

        if erro < e():
            return x, interacoes
        
        
        if(len(interacoes) > 100):
            print("Metodo de Newton nao convergiu.")
            return None, []

        x_anterior = x


raiz, interacoes = metodo_de_newton()

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

if len(interacoes) > 0:
    # Exibir tabela de interações
    print("\tMÉTODO DE NEWTON | DETERMINAÇÃO DA RAIZ z2")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'xk':>16}{'f(xk)':>16}{'f\'(xk)':>16}{'ERk':>16}")
    for i, (x, fx, f_linha, er) in enumerate(interacoes):
        if isinstance(er, str):
            print(f"{'     '}{i:<6}{x:>16.10f}{fx:>16.10f}{f_linha:>16.10}{er:>16}")  # Exibe a string sem formatação
        else:    
            print(f"{'     '}{i:<6}{x:>16.10f}{fx:>16.10f}{f_linha:>16.10}{er:>16.10f}")
# Exibir o valor final da raiz
if raiz is not None:
    print(f"{'     '}Raiz z2 = {raiz:>16.10f}")

input()