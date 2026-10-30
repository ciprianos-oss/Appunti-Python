'''
2. CREAZIONE DI UN ARRAY ED ACCESSO AI SUOI ELEMENTI
--------------------------------------------------------------------------------
'''
# Creazione di un Array di elementi misti
array = [1, False, "Ciao", 1.6, "Mondo"]

# Accesso agli elementi dell'Array
x = array[0]       # Assegnazione di un elemento di un'Array ad una variabile
array[2] = "CIAO"  # Modifica di un valore dell'Array

'''
3. OPERAZIONI CHE SI POSSONO ESEGUIRE SUGLI ARRAY
--------------------------------------------------------------------------------
'''
# Aggiunta di un elemento nell'Array
array.append("Stringa inserita in fondo all'Array") # Inserisce in fondo all'Array la seguente stringa
array.append(5)                                     # Inserisce in fondo all'Array il seguente numero
array.insert(1, True)                               # Inserisce in seconda posizione il valore True

# Rimozione degli elementi
array.pop(0)          # Rimuove il primo elemento dell'Array
array.remove("Ciao")  # Rimuove dall'Array la stringa "Ciao"

# Contare gli elementi di un'Array
conta_lunghezza = len(array)           # Restituisce il numero totale di elementi
conta_elemento  = array.count("Ciao")  # Conta quante volte c'è all'interno il valore indicato

# Ordinare l'Array
array.sort()

'''
4. ITERARE SUGLI ELEMENTI
'''
for i in array: # Ciclo che stampa i valori dell'Array
    print(i)