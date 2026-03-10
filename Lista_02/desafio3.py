quantidade = int(input("Quantos números deseja colocar?:"))

numeros = []

for i in range (quantidade):
    while True:
         n = float(input("Digite um número:"))
         if 0 <= n <=1000:
             numeros.append(n)
             break
         else:
             print ("Valor inválido! digite um número entre 0 e 1000.")
        

print ("menor:\n", min(numeros))
print ("maior:\n", max(numeros))
print ("Soma:\n", sum(numeros))

