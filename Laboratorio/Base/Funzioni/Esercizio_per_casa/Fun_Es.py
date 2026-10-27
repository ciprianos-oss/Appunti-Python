# 1. Definizione delle 4 funzioni per le operazioni
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return None  # Gestione divisione per zero
    return a / b

# 2. Tupla contenente i simboli delle operazioni valide
OPERAZIONI_VALIDE = ("+", "-", "*", "/")

# 3. Funzione principale che riceve operandi e operatore
def calcola_numeri(num1, num2, operatore):
    # Controllo validità dell'operatore tramite la tupla
    if operatore not in OPERAZIONI_VALIDE:
        err = True
        return None, err
    
    err = False
    
    # Invocazione della funzione corrispondente
    match operatore:
        case "+":
            risultato = somma(num1, num2)
        case "-":
            risultato = sottrazione(num1, num2)
        case "*":
            risultato = moltiplicazione(num1, num2)
        case "/":
            risultato = divisione(num1, num2)
            if risultato is None:  # Caso divisione per zero
                err = True

    return risultato, err