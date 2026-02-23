numero_um = int (input("Digite o primeiro número:"))
numero_dois = int (input("Digite o segundo número:"))
numero_tres = int (input("Digite o terceiro número:"))

if numero_um >= numero_dois and numero_um >= numero_tres:
    maior_numero = numero_um
elif numero_dois >= numero_um and numero_dois >= numero_tres:
    maior_numero = numero_dois
else :
    maior_numero = numero_tres

print("O maior número é:", maior_numero)