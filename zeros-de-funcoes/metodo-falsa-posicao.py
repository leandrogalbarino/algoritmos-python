import matplotlib.pyplot as plt
import numpy as np


def f_string():
    # return "x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827"
    return "3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x **4 + x**5"


def f(x):
    # return x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827
    return 3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x ** 4 + x**5


def f_linha(x):
    #return 5*x**4 - 4*12.0953*x**3 + 3*33.6161*x**2 + 2*55.4476*x - 260.915
    return 4044.8 + 2*1614.77*x + 3*308.576*x**2 + 4*28.3001*x**3 + 5*x**4
    

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


def metodo_falsa_posicao():
    a = pedir_numero_float("Digite a1:")
    b = pedir_numero_float("Digite b1:")
    print()

    if f(a)*f(b) > 0:
        print("Nao existe raiz nesse intervalo ou o intervalo possui mais de uma raiz. Tente outro.")
        return None, []
    
    x_anterior = None
    interacoes = []  # Lista para armazenar as interações

    for _ in range(100):
        x = a - (b - a)/(f(b) - f(a))*f(a)

        interacoes.append((a, x, b, f(x), tolerancia(x, x_anterior) if x_anterior is not None else "--------"))

        if x_anterior is not None and tolerancia(x, x_anterior) <= e():
            return x, interacoes

        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
        x_anterior = x

    print("O método não convergiu dentro do número máximo de iterações.")
    return None, []


raiz, interacoes = metodo_falsa_posicao()
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
plt.title('Método da Falsa Posicao')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
print()
# Exibir tabela de interações
print("\tMÉTODO DA FALSA POSIÇÃO | DETERMINAÇÃO DA RAIZ z4")
# Cabeçalho da tabela
print(f"{'     '}{'k':<6}{'ak':>20}{'xk':>20}{'bk':>20}{'f(xk)':>20}{'ERk':>20}")
for i, (a, x, b, fx, er) in enumerate(interacoes):
    if isinstance(er, str):
        print(f"{'     '}{i:<6}{a:>20.9e}{x:>20.9e}{b:>20.9e}{fx:>20.9e}{er:>20}")
    else:
        print(f"{'     '}{i:<6}{a:>20.9e}{x:>20.9e}{b:>20.9e}{fx:>20.9e}{er:>20.9e}")
if raiz is not None:
    print(f"{'     '}Raiz z4 = {raiz:>20.9e}")
input()
