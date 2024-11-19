import numpy as np
import matplotlib.pyplot as plt
import copy
from scipy.interpolate import interp1d  # para interpolação de exemplo

def interpolacao_polinomial(x, fx):
    N = len(x)
    y = fx[:]
    interacoes = []
    for i in range(1,N):
        for j in range(N - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x[j] - x[j-i])
        interacoes.append(copy.deepcopy(y))
    interacoes.append(copy.deepcopy(y))

    return y, interacoes

def estimar_ponto(ponto, x, valores_x):
    N = len(valores_x)
    interacoes = []
    resultado = valores_x[0]
    interacoes.append((resultado, None))
    err_ant = resultado
    termo = 1
    for i in range(1,N):
        termo*= (ponto - x[i-1])
        resultado+= valores_x[i] * termo
        erro = abs(abs(resultado - err_ant) / resultado)  
        interacoes.append((resultado, erro))
        err_ant = resultado

    return interacoes

def melhor_estimativa(z_interacoes):
    menor_erro = 500
    melhor_estimativa = -1
    # Preenche a tabela com os dados
    for k, (Pk, ERk) in enumerate(z_interacoes):
        if ERk is not None:
            if  k > 1:
                if ERk < menor_erro:
                    menor_erro = ERk
                    melhor_estimativa = k
                else:
                    break
            
    melhor_estimativa_list = [melhor_estimativa, z_interacoes[melhor_estimativa][0]]
    if melhor_estimativa != -1:
        return melhor_estimativa_list
    else:
        return None

def imprimir_interacoes(x, fx, interacoes,z):
    # Define o número de iterações
    N = len(interacoes)
    print(f"Tabela de diferenças divididas | z = {z}")
    # Título das colunas
    header = f"{'x'.center(12)} | {'y'.center(12)} | " + " | ".join([f"DD{i+1}".center(12) for i in range(N - 1)])
    print(header)
    print("-" * len(header))

    # Preenche a tabela com cada linha de valores
    i = 0
    while i < N:
        linha = []
        linha.append(f"{x[i]:<12.6g}")   # Adiciona x[i]
        linha.append(f"{fx[i]:<12.6g}") # Adiciona fx[i]

        # Adiciona valores de interacoes[j][i] para j < i
        linha.extend([f"{interacoes[j][i]:<12.6g}" for j in range(i)])

        # Exibe a linha formatada
        print(" | ".join(linha))
        i += 1



def imprimir_estimativas(estimativas):
    # Títulos das colunas
    print("Estimativas | f(z)")
    header = f"{'k':<5} {'Pk(z)':<15} {'ERk':<15}"
    print(header)
    print("-" * len(header))
    # Preenche a tabela com os dados
    for k, (Pk, ERk) in enumerate(estimativas):
        if ERk is not None:
            print(f"{k:<5} {Pk:<15.6g} {ERk:<15.6g}")
        else:
            print(f"{k:<5} {Pk:<15.6g} {'-':<15}")


def imprimir_melhor_estimativa(fz_interacoes):
    melhor_est = melhor_estimativa(fz_interacoes)
    if melhor_estimativa is not None:
        print(f"Aproximação mais confiável: k = {melhor_est[0]}, Pk(z) = {melhor_est[1]:.6g}")
    else:
        print("Não foi possível determinar a melhor estimativa.")

def plot_grafico(x, fx, diferencas_divididas):
    # Plotando a função estimada para cada Pk(x)
    for k in range(2,10, 2):
        plt.figure(figsize=(10, 6))

        x_vals = np.linspace(min(x), 5, 500)
        Pk_vals = [estimar_ponto(x_val, x, diferencas_divididas)[k][0] for x_val in x_vals]
        plt.plot(x_vals, Pk_vals, label=f'y = P$_{{{k}}}$(x)', linestyle='-')
        
        # Plotando os pontos originais
        plt.scatter(x, fx, color='black')

        # Títulos e legendas
        plt.title("Gráfico")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()

        plt.xlim(0,1.75)
        plt.ylim(-1,6)
        plt.savefig(f'grafico{k}.png')

def ordenar_diferenca(x, z):
    return sorted(x, key=lambda valor: abs(valor - z))




x = [1.07118, 0.87691, 0.740587, 1.3449, 1.40753, 1.49681, 0.54692, 1.67324, 0.338935, 0.199134]
fx = [0.197905, 0.265178, 0.055113, 2.35749, 2.92806, 4.66274, -0.0632531, 4.30248, 1.17692, 2.21001]
z = 1.03


# Meus valores
#x = [0.167264, 0.375744, 0.573337, 0.68687,  0.93012, 1.13454, 1.28866,  1.50625, 1.56189, 1.65422]
#fx = [2.84831, 0.862072, -0.131428, -0.0413058, 0.342375, 0.229793, 1.39694,  3.64033, 3.94954, 5.34887]
#z = 1.5


x = ordenar_diferenca(x, z)

# Metódo da diferenças divididas
diferencas_dividadas, interacoes = interpolacao_polinomial(x, fx)
imprimir_interacoes(x,fx, interacoes, z)

# Estimativas de Z
fz_interacoes = estimar_ponto(z,x, diferencas_dividadas)
imprimir_estimativas(fz_interacoes)
imprimir_melhor_estimativa(fz_interacoes)
melhor_estimativa(fz_interacoes)
plot_grafico(x, fx, diferencas_dividadas)

print()
input()


