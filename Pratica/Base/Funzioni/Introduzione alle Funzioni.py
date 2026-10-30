# Definizione di funzione
def my_function():
    return "Ciao mondo"

print(my_function())

# Funzione che ritorna n parametri
def somma_sott(p1, p2):
    r1 = p1 + p2
    r2 = p2 - p1

    return r1, r2

a1 = 5
a2 = 10
a, b = somma_sott(a1, a2)
print(a, b)

# Funzioni a cui vengono passati n parametri
def n_parametri(*args):
    print(args)

n_parametri("Ciao", 1, "Mondo")