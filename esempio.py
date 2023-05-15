base_folder ="C://"
counter = 45
nome_file = f"{base_folder}/photo_{counter:03d}.jpg" #f-string
print(nome_file)

a = 4
b = 10
print(f"la somma di {a} e {b} è {a+b}")


tupla = (1,2,3,4,5)
#le tuple sono immutabili
#tupla[0] = 100
print(tupla)


#lista = [0,1,2,3,4]
#le liste sono modificabili
#lista[0] = 9
#print(lista)

lista = [0,1,"ciao",2,3,4,True, False]
print(lista[2:5:2])
print(lista[-1:1:-1]) #slicing da 2 escluso a 5 escluso

#for elemento in lista:
    #print(elemento)

stringa = "ciao"
for c in stringa:
    print (c)

print(stringa[-1])