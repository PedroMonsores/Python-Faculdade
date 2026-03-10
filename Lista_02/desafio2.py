quantidade = int(input("Quantos números deseja colocar?:"))

numeros = []

for i in range (quantidade):
    n = float(input("Digite um número:"))
    numeros.append(n)

print ("menor:\n", min(numeros))
print ("maior:\n", max(numeros))
print ("Soma:\n", sum(numeros))

