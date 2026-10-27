"""
Chiedere una frase e mandare a video:
- Numero di caratteri
- Primo e ultimo carattere
- Frase in maiuscolo e minuscolo
- Contare quante volte c'e la 'a'
- Sostituire gli spazi con '-'
"""
frase = input("Inserisci una frase: ")
print(len(frase))
print(frase[0])
print(frase[-1])
print(frase.upper())
print(frase.lower())
print(frase.count('a'))
print(frase.replace(" ", "-"))