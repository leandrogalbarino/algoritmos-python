import copy


def erro_relativo(vet_int, vet_int_ant):
    err = []
    if len(vet_int) == 0 or len(vet_int_ant) == 0:
        raise ValueError("Os vetores não podem estar vazios.")
    for i in range(len(vet_int)):
        if vet_int[i] != 0:
            erro_x = abs(vet_int[i] - vet_int_ant[i]) / abs(vet_int[i])
        else:
            erro_x = float('inf')
        err.append(erro_x)
    return max(err) if max(err) != 0 else float('inf'), err


def convergencia_jacobi(mat):
    N = len(mat)
    for i in range(N):
        valor_col = 0
        valor_diag = abs(mat[i][i])
        for j in range(N):
            if i != j:
                valor_col += abs(mat[i][j])
        if valor_col >= valor_diag:
            return False
    return True


def gauss_jacobi(mat, vet_int):
    epsilon = 1e-5
    N = len(mat)
    vet_int_ant = [5] * N
    if not (convergencia_jacobi(mat)):
        print("Método não convergiu!")
        return vet_int
    interacoes = []
    err_int = []
    interacoes.append((copy.deepcopy(vet_int), [1,1,1,1,1,1,1]))
    while (True):
        vet_int_ant = copy.deepcopy(vet_int)
        for i in range(N):
            soma = 0
            for j in range(N):
                if j != i:
                    soma += vet_int_ant[j]*mat[i][j]

            vet_int[i] = (mat[i][N] - soma) / mat[i][i]
        err, err_int = erro_relativo(vet_int, vet_int_ant)
        interacoes.append((copy.deepcopy(vet_int), copy.deepcopy(err_int)))

        if err < epsilon:
            return vet_int, interacoes


def gauss_seidel(mat, vet_int):
    epsilon = 1e-5
    N = len(mat)
    vet_int_ant = [5] * N
    if not (convergencia_jacobi(mat)):
        print("Método não convergiu!")
        return vet_int
    interacoes = []
    err_int = []
    interacoes.append((copy.deepcopy(vet_int), [1,1,1,1,1,1,1]))

    while (True):
        vet_int_ant = copy.deepcopy(vet_int)
        for i in range(N):
            soma = 0
            for j in range(N):
                if j != i:
                    if j < i:
                        soma += vet_int[j]*mat[i][j]
                    else:
                        soma += vet_int_ant[j]*mat[i][j]
            vet_int[i] = (mat[i][N] - soma) / mat[i][i]

        err, err_int = erro_relativo(vet_int, vet_int_ant)
        interacoes.append((copy.deepcopy(vet_int), copy.deepcopy(err_int)))

        if err < epsilon:
            return vet_int, interacoes


def mostrar_solucao(resultado):
    print("\nSOLUÇÃO")
    linha = " | ".join(
        f"{variavel} = {valor:.10g}" for variavel, valor in resultado)
    print(linha)
    print("-" * 50)
    print("\n")


def print_valores(interacoes, vet_solucao, tipo="valor"):
    # Cabeçalho
    print(f"\n{'   '}{'k':<8}", end="")
    for var in vet_solucao:
        print(f"{var:<18}", end="")
    print('\n')

    # Conteúdo das interações
    for i, (vet_int, err) in enumerate(interacoes):
        print(f"{'   '}{i:<8}", end="")  # Número da iteração
        valores = vet_int if tipo == "valor" else err
        for valor in valores:
            # Valores de vet_int ou erro relativo
            print(f"{valor:<18.10g}", end="")
        print()  # Quebra de linha após cada iteração


def mostrar_interacoes(mat, interacoes, vet_solucao, metodo):
    print(f"Método de {metodo}\n")
    print(f"Matriz A:")
    for linha in mat:
        # Exibir todas as colunas até a penúltima
        linha_formatada = " ".join(f"{elem:20.10f}" for elem in linha[:-1])
        # Exibir a última coluna com uma barra separadora
        linha_formatada += "  |  " + f"{linha[-1]:20.10f}"
        print(linha_formatada)
    print("-" * 50)

    print("Iterações dos Valores:")
    print_valores(interacoes, copy.deepcopy(vet_solucao), tipo="valor")
    print("\nIterações dos Erros:")
    print_valores(interacoes, vet_solucao, tipo="erro")

mat = [
    [970, 6, -282, 15, 48, 153, -21, -64],
    [114, 555, -31, 5, - 52, 17, -199, 25],
    [0, 14, -594, 197, 35, 140, 47, 17],
    [257, -21, -20, 571, 136, -48, 5, -23],
    [9, 10, 104, -301, 556, 54, 24, 64],
    [68, -103, 24, -16, 310, -1040, -4, 6],
    [20, -211, -129, 63, -34, 7, 527, 35]
]

## mat Tilles
# mat = [
#     [-822, -84, -17, 26, 8, 64, 213, 2],
#     [- 51, 542, 94, 11, 7, -236, 31, 96],
#     [- 15, 180, 436, 5, 34, 63, -108, -4],
#     [- 6, 64, 10, -494, -225, -22, 108, -39],
#     [- 11, -42, 33, 179, -479, -144, -9, -27],
#     [197, -52, -134, -2, 29, -637, 19, 45],
#     [- 10, -17, 263, 131, -61, 40, 939, 15]]


vet_solucao = ["x1", "x2", "x3", "x4", "x5", "x6", "x7"]
vet_solucao_jacobi = [0] * len(vet_solucao)
vet_solucao_seidel = [0] * len(vet_solucao)

# Metódo de Jacobi
vet_solucao_jacobi, interacoes_jacobi = gauss_jacobi(mat, vet_solucao_jacobi)
resultado_jacobi = list(zip(vet_solucao, vet_solucao_jacobi))
mostrar_interacoes(mat, interacoes_jacobi, vet_solucao, "Jacobi")
mostrar_solucao(resultado_jacobi)

# Metódo de Seidel
vet_solucao_seidel, interacoes_seidel = gauss_seidel(mat, vet_solucao_seidel)
resultado_seidel = list(zip(vet_solucao, vet_solucao_seidel))
mostrar_interacoes(mat, interacoes_seidel, vet_solucao, "Seidel")
mostrar_solucao(resultado_seidel)

input()
