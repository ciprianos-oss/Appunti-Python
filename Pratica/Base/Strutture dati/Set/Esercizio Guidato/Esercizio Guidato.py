# Definizione dei set
calcio = {"Marco", "Luca", "Giulia", "Marco", "Sara", "Luca"}
basket = {"Sara", "Elena", "Luca", "Paolo", "Elena"}
teatro = {"Giulia", "Elena", "Davide", "Sara"}

print("Calcio:", calcio, f"({len(calcio)} iscritti)")
print("Basket:", basket, f"({len(basket)} iscritti)")
print("Teatro:", teatro, f"({len(teatro)} iscritti)")

# Appartenenza
nome = input("Inserisci un nome: ")
if nome in calcio:
    print(nome, "fa calcio")
if nome in basket:
    print(nome, "fa basket")
if nome in teatro:
    print(nome, "fa teatro")
if nome not in calcio | basket | teatro:
    print(nome, "non è iscritto a nessuna attività")

# Operazioni sui set
print("Tutti gli studenti:", calcio | basket | teatro)
print("Calcio e basket:", calcio & basket)
print("Calcio ma non teatro:", calcio - teatro)
print("Basket o teatro (non entrambi):", basket ^ teatro)


teatro.add("Chiara")
basket.discard("Paolo")
print("Teatro:", teatro)
print("Basket:", basket)