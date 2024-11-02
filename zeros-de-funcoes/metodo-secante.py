import matplotlib.pyplot as plt
import numpy as np
import math




def aproximar_derivada(x, x_anterior):
    denominador = x - x_anterior
    if abs(denominador) < 1e-12: 
        print("Erro: Divisão por valor muito pequeno na derivada.")
        return None
    f_derivada = (f(x) - f(x_anterior)) / denominador
    return f_derivada


#return "3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x **4 + x**5"
#return 3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x **4 + x**5
#return 4044.8 + 2*1614.77*x + 3*308.576*x**2 + 4*28.3001*x**3 + 5*x**4

def f_string():
    return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"
    #return "3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x **4 + x**5"


def f(x):
    return x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827
    #return 3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x ** 4 + x**5


    

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


def metodo_secante():
    x_anterior2 = pedir_numero_float("Chute inicial 1:")
    x_anterior1 = pedir_numero_float("Chute inicial 2:")

    interacoes = []  # Lista para armazenar as interações
    # Primeira interação
    interacoes.append((x_anterior2, f(x_anterior2), "--------"))
    # Segunda interação
    interacoes.append((x_anterior1, f(x_anterior1), tolerancia(x_anterior1,x_anterior2)))

    while True:
        if abs(f(x_anterior1) - f(x_anterior2)) < 1e-12:
            print("Erro: f(x_n) e f(x_{n-1}) são muito próximos, divisão por valor muito pequeno.")
            return None, []

        derivada_aprox = aproximar_derivada(x_anterior1, x_anterior2)
        if derivada_aprox is None:
            print("Erro ao calcular a derivada!")
            return None, []

        x = x_anterior1 - f(x_anterior1) / derivada_aprox

        erro = tolerancia(x, x_anterior1)  # Calcula a tolerância
        interacoes.append((x, f(x),  erro))

        if erro < e():
            return x, interacoes

        if (len(interacoes) > 100):
            print("Método da secante não convergiu após 100 iterações.")
            return None, []

        x_anterior2 = x_anterior1
        x_anterior1 = x


raiz, interacoes = metodo_secante()

# Preparar dados para o gráfico
x_vals = np.linspace(-3, 7, 1000)  # Intervalo ajustado para incluir a raiz
y_vals = f(x_vals)

# Plotar a função
plt.plot(x_vals, y_vals, label=f_string())
plt.axhline(0, color='purple', linewidth=0.5)  # Linha do eixo x

# Se a raiz foi encontrada, marcá-la no gráfico
if raiz is not None:
    plt.plot(raiz, f(raiz), 'ro', label=f"Raiz = {raiz:.10f}")

# Configurações do gráfico
plt.title('Método da Secante')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
print()

if len(interacoes) > 0:
    # Exibir tabela de interações
    print("\tMÉTODO DA SECANTE | DETERMINAÇÃO DA RAIZ z3")
    # Cabeçalho da tabela
    print(f"{'     '}{'k':<6}{'xk':>20}{'f(xk)':>20}{'ERk':>20}")
    for i, (x, fx, er) in enumerate(interacoes):
        if isinstance(er, str):
            # Exibe a string sem formatação
            print(f"{'     '}{i:<6}{x:>20.9e}{fx:>20.9e}{er:>20}")
        else:
            print(f"{'     '}{i:<6}{x:>20.9e}{fx:>20.9e}{er:>20.9e}")
if raiz is not None:
    print(f"{'     '}Raiz z3 = {raiz:>20.9e}")
input()