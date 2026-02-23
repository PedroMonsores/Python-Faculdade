letra = input("Digite uma letra:").lower()
if len(letra) !=1 or not letra.isalpha():
    print("Digite apenas uma letra!")
elif letra in "aeiou":
    print (("É vogal"))
else:
    print("É consoante")