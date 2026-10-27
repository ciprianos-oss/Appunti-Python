"""
Chiedere una frase in input e mandare a video:
- Frase al contrario
- Dire se e palondroma
- Contare vocali e consonanti
- Visualizzare i primi 3 e gli ultimi 3 caratteri
- Visualizzare la frase senza il primo e l'ultimo carattere
"""
def analizza_frase(frase) -> None:
    # Inversione della frase
    frase_inversa = frase[::-1]
    
    # Controllo palindroma
    frase_pulita = "".join(c.lower() for c in frase if c.isalnum())
    e_palindroma = frase_pulita == frase_pulita[::-1]
    
    # Conteggio vocali e consonanti
    vocali = set("aeiouàèéìòù")
    num_vocali = sum(1 for c in frase.lower() if c in vocali)
    num_consonanti = sum(1 for c in frase.lower() if c.isalpha() and c not in vocali)
    
    # Estratti (primi/ultimi 3 e senza estremi)
    primi_3 = frase[:3]
    ultimi_3 = frase[-3:] if len(frase) >= 3 else frase
    senza_estremi = frase[1:-1] if len(frase) > 2 else ""
    
    # Mando a video i risultati
    print("\n--- RISULTATI ANALISI ---")
    print(f"Frase al contrario: {frase_inversa}")
    print(f"È palindroma?: {'Sì' if e_palindroma else 'No'}")
    print(f"Conteggio: {num_vocali} vocali, {num_consonanti} consonanti")
    print(f"Primi 3 caratteri: '{primi_3}' | Ultimi 3 caratteri: '{ultimi_3}'")
    print(f"Senza primo e ultimo carattere: '{senza_estremi}'")