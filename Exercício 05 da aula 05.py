#Ler 10 valores e escrever quais estão entre 10 e 20 (incluindo ambos)
cont = 0
contfo = 0
for x in range(10,21,1):
    nums = int(input("Digite um número: "))
    if nums >= 10 and nums <= 20:
        cont = cont + 1
    else:
        contfo = contfo +1
print(f"Quantidade de números dentro do intervalo: {cont}")
print(f"Quantidade de números fora do intervalo: {contfo}")
