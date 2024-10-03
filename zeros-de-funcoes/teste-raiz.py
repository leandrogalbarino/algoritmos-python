def f(x):
    return x**5 - 12.0953*x**4 + 33.6161*x**3 + 55.4476*x**2 - 260.915*x + 119.827

# Tolerância de erro
erro_tolerancia = 0.000001

# Valor de teste
x_teste = 4.6980854235
# Calcular o valor de f(0)
valor_f_0 = f(4.6980854235)

# Imprimir o resultado com 10 casas decimais de precisão

# Verificação da aproximação da raiz
if abs(f(x_teste)) <= erro_tolerancia:  # Verifica se o valor está dentro da tolerância
    print("FUNCIONOU")  # Aproximação válida

else:
    print("Nao FUNCIONOU")  # Aproximação não válida
    
print(f"f(0) = {valor_f_0:.10f}")

input()


#return "3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x **4 + x**5"
#return 3880.73 + 4044.8*x + 1614.77*x**2 + 308.576*x**3 + 28.3001*x **4 + x**5
#return 4044.8 + 2*1614.77*x + 3*308.576*x**2 + 4*28.3001*x**3 + 5*x**4
