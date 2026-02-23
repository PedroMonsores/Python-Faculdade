nota_um = float (input ("Digite sua primeira nota:"))
nota_dois = float (input ("Digite sua primeira nota:"))

media = (nota_um + nota_dois)/2

if media == 10:
    print("Aprovado com distinção!")
elif media >= 7:
    print("Aprovado")
else :
    print("Reprovado")

