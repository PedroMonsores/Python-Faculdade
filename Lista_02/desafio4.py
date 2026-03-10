nome = input ("Digite seu nome:")

while True:

    nome = input ("Digite seu nome:")

    if len(nome) < 3:
        print ("Número de caracteres menor")
        continue
    
    idade = int (input ("Digite sua idade:"))

    if 0 < idade > 150:
        print ("Idade inválida!")
        continue
    
    salario = int (input("Digite seu salário:"))

    if salario < 0:
        print ("Salário inválido!")
        continue
    
    genero = input ("Digite seu gênero (f ou m):")
    
    if genero != 'f' or 'm':
        print ("Digite novamente:")
        continue
    
    est_civil = input ("Digite seu estado civil:(s,c,v,d):")
        
    if est_civil != 's' or 'c' or 'v' or 'd':
        print ("Digite novamente:")
        continue

    
        

    
