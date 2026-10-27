import Modulo_Esercizio

def main():
    voti = [7, 5, 8, 6, 7]

    media = Modulo_Esercizio.calcola_media(voti)
    risultato = Modulo_Esercizio.esito(media)

    print("Voti:", voti)
    print("Media:", media)
    print("Esito:", risultato)

if __name__ == "__main__":
    main()