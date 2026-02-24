sim = 0

input ("Você telefonou pra vítima? ") 
if "sim":
        sim+=1
input ("Esteve no local do crime?")
if "sim":
        sim+=1
input ("Mora perto da vítima?")
if "sim":
        sim+=1
input ("Devia pra vítima?")
if "sim":
        sim+=1
input ("Já trabalhou pra vítima?")
if "sim":
        sim+=1
        
if sim == 2:
        print("Suspeito")

elif sim == 3 or 4:
        print ("Cúmplice")
elif sim == 5:
        print ("Culpado")
else:
        print("Inocente")
        


        