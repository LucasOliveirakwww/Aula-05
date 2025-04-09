#Ler valor e imprimir valores inteiros entre 1 e "N". Considerando que "N" é sempre maior que 0
N = int(input("Digite um número: "))
if N > 0:
    for x in range(1, N + 1, 1):
        print(x, end=" ")
else:
    print("Número inválido")