#Ler 5 valores, calcular e entregar a média aritmética
soma = 0
for x in range (1,5+1,1):
    valores = int(input("Digite um valor: "))
    soma = soma+valores
    media = soma/5
print(f"Média aritmética: {media}")

