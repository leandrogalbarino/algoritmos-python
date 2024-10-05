
# def ordenar_colunas(mat, N):
    #pivotamente parcial e pivotamento total
 #   for i in range(0, N-1):
  #      for j in range(i + 1, N):



def eliminacao_gaussiana(mat, N):
    #ordenar_colunas(mat)
    for i in range(0, N-1):
        for j in range(i + 1, N):
            mult = mat[j][i] / mat[i][i]
            mat[j][i] = 0.0
            #for k in range(i, N + 1):
            for k in range(i + 1, N + 1):
                mat[j][k] = mat[j][k] - mult*mat[i][k]
    return mat

matriz = [
    [-17, 19, -3,8, 86] ,
    [13,-10,-18,-20, -297] ,
    [-1, 15, -11, 9, 64],
    [-18,2, 18,-7, 6]
]

matriz2 = eliminacao_gaussiana(matriz, 4)
# Exibindo a matriz resultado
for linha in matriz2:
    print(" | ".join(f"{x:>15.10f}" for x in linha))  # Formatação com 2 casas decimais

input()