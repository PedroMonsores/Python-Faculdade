turno = (input("Digite o turno que vc estuda\n - M (maturino)\n - V (vespertino)\n - N (noturno)")).lower()

match turno:

    case "m":
        print ("Bom Dia!")
    case "v":
        print  ("Boa Tarde!")
    case "n":
        print ("Boa Noite")
    case _:
        print ("Valor inválido!")

