#Importo il modulo delle funzioni dell'esercizio
import funzioni_es

#Funzione principale
def main():
    num = int(input("Inserisci il numero in cui stampare la tavola pitagorica: "))
    funzioni_es.tavola_pitagorica(num)

#Lancio la funzione principale
if __name__ == "__main__":
    main()