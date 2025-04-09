#Ler 10 valores e escrever quantos são negativos
neg = 0
for x in range(1,11,1):
    nums = int(input("Digite o valor: "))
    if nums < 0:
        neg = neg+1
print(f"Existem {neg} valor(es) negativo(s)")