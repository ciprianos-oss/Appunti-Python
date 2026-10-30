#Commento di linea
'''
Commento multi linea
'''

# Stampare dei valori iniziali facendo il casting di tipo
a = 5
print("Ciao " + str(a)) #Casting di tipo

#Controllo della classe
a = int(input("In che classe sei?: "))
print(f"Sei in {str(a)}")

#Controllo condizionale
if a == 5:
    print("Allora avete ", end='')
    print("finito")
else:
    print("Non avete finito ancora le superiori")
    print(f"L'anno prossimo sarete in {a + 1}")