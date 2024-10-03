import matplotlib.pyplot as plt
import numpy as np
import math

def f_string():
    return "x**3 - 2*x**2 - 4*x + 4"

def f(x):
    return x**3 - 2*x**2 - 4*x + 4


def g(x):
    return (x**3*(1/2) - 2*(x-1))**(1/2)

def e():
    return 0.000001


def tolerancia(x, x_anterior):
    return abs(x - x_anterior)

def pedir_numero_float(mensagem):
    while True:
        try:
            x = float(input(mensagem))
            return x
        except ValueError:
            print("Entrada invalida, tente novamente!")


def metodo_ponto_fixo():
    x_anterior = pedir_numero_float("Chute inicial:")
    
    interacoes = []  # Lista para armazenar as interações
    interacoes.append((x_anterior, f(x_anterior), "--------"))

    while True:
        x = g(x_anterior)
        erro = tolerancia(x, x_anterior)  # Calcula a tolerância

        interacoes.append((x, f(x), erro))
        if erro <= e():
            return x, interacoes
        
        x_anterior = x


raiz, interacoes = metodo_ponto_fixo()

# Preparar dados para o gráfico
x_vals = np.linspace(-2, 5, 1000)  # Intervalo ajustado para incluir a raiz
y_vals = f(x_vals)

# Plotar a função
plt.plot(x_vals, y_vals, label=f_string())
plt.axhline(0, color='black', linewidth=0.5)  # Linha do eixo x

# Se a raiz foi encontrada, marcá-la no gráfico
if raiz is not None:
    plt.plot(raiz, f(raiz), 'ro', label=f"Raiz = {raiz:.6f}")

# Configurações do gráfico
plt.title('Método do Ponto Fixo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Exibir tabela de interações
print("\nInterações do Método do Ponto Fixo:")
# Cabeçalho da tabela
print(f"{'n':<5}{'x':>13}{'f(x)':>13}{'ER':>13}")
for i, (x, fx, er) in enumerate(interacoes):
    if isinstance(er, str):
        print(f"{i+1:<6}{x:>13.6f}{fx:>13.6f}{er:>13}")
    else:
        print(f"{i+1:<6}{x:>13.6f}{fx:>13.6f}{er:>13.6f}")

input()