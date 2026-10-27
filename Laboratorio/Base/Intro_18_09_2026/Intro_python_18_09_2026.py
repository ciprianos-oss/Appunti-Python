#Commento di linea
'''
Commento multi linea
'''

a = 5
print("Ciao " + str(a)) #Casting di tipo

#Funzione per il controllo della classe
def controllo_classe() -> None:
    a = int(input("In che classe sei?: "))
    print(f"Sei in {str(a)}")

    #Controllo condizionale
    if a == 5:
        print("Allora avete ", end='')
        print("finito")
    else:
        print("Non avete finito ancora le superiori")
        print(f"L'anno prossimo sarete in {a + 1}")

#Funzione principale
def main():
    controllo_classe()

#Lancio della funzione principale
if __name__ == "__main__":
    main()