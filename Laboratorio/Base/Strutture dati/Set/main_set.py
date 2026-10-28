# Definizione di un set
my_set = {"apple", "banana", "cherry"}

# Ottenere la lunghezza del set
print(len(my_set))

# Accedere agli elementi del set
for x in my_set:
    print(x)

# Verificare se un elemento e dentro al set
print("banana" in my_set)
print("banana" not in my_set)

# Aggiungere gli elementi dentro al set
my_set.add("orange")

# Aggiungere elementi da un altro set
secondo_set = {"pera", "fragola", "mirtillo"}
my_set.update(secondo_set)