import numpy as np
import copy
from sympy import symbols, Eq, solve

# pivotamento total


# Escolhe a linha que tem o maior valor absoluto na coluna a ser zerada, e muda linha que seria usada para zeras as outras. 
def pivotamento_parcial(mat, i, N):
    linha_maior = i

    for j in range(i + 1, N):
        if np.abs(mat[j][i]) > np.abs(mat[linha_maior][i]):
            linha_maior = j
    if linha_maior != i:
        mat[i], mat[linha_maior] = mat[linha_maior], mat[i]
    return linha_maior
        


def eliminacao_gaussiana_parcial(mat):
    N = len(mat)
    interacoes = []
    matriz_original = f"Matriz Original"
    interacoes.append((copy.deepcopy(mat), matriz_original))

    for i in range(N-1):
        lin = pivotamento_parcial(mat, i, N)
        if lin != i:
            alteracao_pivo = f"Trocando pivô: linha {i} com linha {lin}"
        else:
            alteracao_pivo = f"Nao foi realizada troca de pivo"
        interacoes.append((copy.deepcopy(mat), alteracao_pivo))    
        for j in range(i + 1, N):
            if mat[i][i] == 0:
                raise ValueError(
                    "Divisão por zero detectada, pivotamento pode ter falhado.")
            mult = mat[j][i] / mat[i][i]

            for k in range(i, N + 1):
                mat[j][k] = mat[j][k] - mult*mat[i][k]
                alteracao = f"matriz[{j}][{i}] <- matriz[{j}][{i}] - ({mult}) * matriz[{i}][{i}]"
            interacoes.append((copy.deepcopy(mat), alteracao))  

    return mat, interacoes

# Determinar o elemento de maior valor absoluto em todo matriz, exceto na ultima coluna, e o coloca na posição de pivô via troca de linhas e de colunas. Quando mudamos as colunas o vetor solução também muda, pois o valor adquirido pela retrosubstição será do elemento da coluna em sua posição original.
def pivotamento_total(mat, i, vet_solucao, N):
    lin_maior, col_maior = i, i
    maior = np.abs(mat[i][i])

    for j in range(i, N):
        for k in range(i, N):
            if np.abs(mat[j][k]) > maior:
                maior = np.abs(mat[j][k])
                lin_maior, col_maior = j, k

    if lin_maior != i:
        mat[i], mat[lin_maior] = mat[lin_maior], mat[i]

    if col_maior != i:
        for lin in range(N):
            mat[lin][i], mat[lin][col_maior] = mat[lin][col_maior], mat[lin][i]
        vet_solucao[i], vet_solucao[col_maior] = vet_solucao[col_maior], vet_solucao[i]
    return lin_maior, col_maior  
    


def eliminacao_gaussiana_total(mat, vet_solucao):
    N = len(mat)
    interacoes = []
    matriz_original = f"Matriz Original"
    interacoes.append((copy.deepcopy(mat), matriz_original))

    for i in range(0, N-1):
        lin, col = pivotamento_total(mat, i, vet_solucao, N)
        if lin != i or col != i:
            alteracao_pivo = f"Trocando pivô: linha {i} com linha {lin}, coluna {i} com coluna {col}"
        else:
            alteracao_pivo = f"Nao foi realizada troca de pivo"
        interacoes.append((copy.deepcopy(mat), alteracao_pivo))
        for j in range(i + 1, N):
            if mat[i][i] == 0:
                raise ValueError(
                    "Divisão por zero detectada, pivotamento pode ter falhado.")

            mult = mat[j][i] / mat[i][i]
            for k in range(i, N + 1):
                mat[j][k] -= mult*mat[i][k]
                alteracao = f"matriz[{j}][{i}] <- matriz[{j}][{i}] - ({mult}) * matriz[{i}][{i}]"
                interacoes.append((copy.deepcopy(mat), alteracao))  

    return mat, vet_solucao, interacoes


def resolver_equacao(mat, vet):
    N = len(mat)
    vet_solucao = vet.copy()
    for i in range(N-1, -1, -1):
        vet_solucao[i] = mat[i][N]
        for j in range(i+1, N):
            vet_solucao[i] -= vet_solucao[j]*mat[i][j]
        vet_solucao[i] /= mat[i][i]
    return vet_solucao


def mostrar_solucao(resultado):
    print("SOLUÇÃO | RETROSUBSTITUIÇÃO")
    for variavel, valor in resultado:
        print(f"{variavel} = {valor:.10g}")
    print("-" * 50)

def mostrar_interacoes(interacoes):
    print("Histórico das Interações da Eliminação Gaussiana:")
    print("=" * 50)
    
    for idx, (mat, alteracao) in enumerate(interacoes):
        print(f"Iteração {idx + 1}:")
        print(f"Alteração: {alteracao}")
            
        print("Matriz Atual:")
        
        for i, linha in enumerate(mat):
            print("    " + " ".join(f"{elem:20.9f}" for elem in linha))
        print("-" * 50)



mat = [
    [83, 61, -6, -55, 9, -35, -61, -70],
    [-24, 87, -5, -38, 19, 53, 26, 73],
    [-28, -97, -13, -66, 70, -5, 52, -51],
    [69, -9, -82, -100, 58, -52, 55, -32],
    [79, 42, -81, 62, -81, 6, -16, -68],
    [-5, 98, -10, 67, 95, -9, -1, -29],
    [59, 63, -56, -90, 0, -29, -64, 2],
]

# mat = [
#     [970, 6, -282, 15, 48, 153, -21, -64],
#     [114, 555, -31, 5, - 52, 17, -199, 25],
#     [0, 14, -594, 197, 35, 140, 47, 17],
#     [257, -21, -20, 571, 136, -48, 5, -23],
#     [9, 10, 104, -301, 556, 54, 24, 64],
#     [68, -103, 24, -16, 310, -1040, -4, 6],
#     [20, -211, -129, 63, -34, 7, 527, 35]
# ]


vet_solucao_parc = ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]
mat_final_parc, interacoes_parc = eliminacao_gaussiana_parcial(mat)
vet_solucao_res_parc = resolver_equacao(mat_final_parc, vet_solucao_parc)
resultado_parc = list(zip(vet_solucao_parc, vet_solucao_res_parc))
mostrar_interacoes(interacoes_parc)
mostrar_solucao(resultado_parc)


# vet_solucao_tot = ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]
# mat_final_tot, vet_solucao_tot, interacoes_tot = eliminacao_gaussiana_total(mat, vet_solucao_tot)
# vet_solucao_tot_res = resolver_equacao(mat_final_tot, vet_solucao_tot)
# resultado_tot = list(zip(vet_solucao_tot, vet_solucao_tot_res))
# mostrar_interacoes(interacoes_tot)
# mostrar_solucao(resultado_tot)


input()
