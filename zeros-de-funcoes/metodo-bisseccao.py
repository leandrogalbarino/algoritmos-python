import matplotlib.pyplot as plt
import numpy as np


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


def pedir_numero_float(str):
    while True:
        try:
            x = float(input(str))
            return x
        except ValueError:
            print("Entrada invalida, tente novamente!")


def metodo_bisseccao():
    a = pedir_numero_float("Digite a1:")
    b = pedir_numero_float("Digite b1:")

    if f(a)*f(b) > 0:
        print("Nao existe raiz nesse intervalo ou o intervalo possui mais de uma raiz. Tente outro.")
        return None, []

    x_anterior = None
    interacoes = []  # Lista para armazenar as interações

    while True:
        x = (a + b) / 2
        interacoes.append((a, x, b, f(a), f(x), f(b), tolerancia(
            x, x_anterior) if x_anterior is not None else "--------"))

        if x_anterior is not None and tolerancia(x, x_anterior) <= e():
            return x, interacoes


        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        x_anterior = x


raiz, interacoes = metodo_bisseccao()

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
plt.title('Método da Bisseção')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
print()
# Exibir tabela de iterações
print("\tMÉTODO DA BISSECÇÃO | DETERMINAÇÃO DA RAIZ z1")
print(f"{'     '}{'nk':<6}{'ak':>16}{'xk':>16}{'bk':>16}{'f(ak)':>16}{'f(xk)':>16}{'f(bk)':>16}{'ERk':>16}")
for i, (a, x, b, fa, fx, fb, er) in enumerate(interacoes):
    if isinstance(er, str):
        print(f"{'     '}{i:<6}{a:>16.10f}{x:>16.10f}{b:>16.10f}{fa:>16.10f}{fx:>16.10f}{fb:>16.10f}{er:>16}")
    else:
        print(f"{'     '}{i:<6}{a:>16.10f}{x:>16.10f}{b:>16.10f}{fa:>16.10f}{fx:>16.10f}{fb:>16.10f}{er:>16.10f}")

# Exibir o valor final da raiz
if raiz is not None:
    print(f"{'     '}Raiz z1 = {raiz:>16.10f}")

input()
