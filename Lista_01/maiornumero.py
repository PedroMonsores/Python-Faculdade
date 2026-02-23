numero1 = int (input("Digite um número:"))

numero2 = int (input("Digite um número:"))

if numero1 == numero2:
    print("Os números são iguais!")
elif numero1 > numero2:
    print(f"{numero1} é o número maior")
else:
    print(f"{numero2} é o número maior")