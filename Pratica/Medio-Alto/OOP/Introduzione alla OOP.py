# ------------------------------------------------------------------------------
# 1. CREAZIONE DI UNA CLASSE
# ------------------------------------------------------------------------------
# Si utilizza la parola chiave class; la riga class termina con i due punti (:)
# e le istruzioni della classe devono essere indentate.

class MyClass:
    x = 5


# Creazione di oggetti multipli della stessa classe
# Sintassi: nome_oggetto = nome_classe()
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

# print() su un oggetto mostra la classe e l'indirizzo di memoria,
# mentre per leggere l'attributo si usa la notazione oggetto.attributo
print(p1)
print(p2)
print(p3)
print(p1.x)


# ------------------------------------------------------------------------------
# 2. METODO __init__() DELLA CLASSE
# ------------------------------------------------------------------------------
# __init__() viene eseguito automaticamente ogni volta che si crea un oggetto
# e assegna i valori alle proprieta' dell'oggetto.
# Il parametro Age ha un valore predefinito (18), quindi puo' essere omesso.

class Person:
    def __init__(self, Name, Surname, Age=18):
        self.Name = Name
        self.Surname = Surname
        self.Age = Age

    def saluta(self):
        print(f"{self.Name} {self.Surname} {self.Age}")


# Oggetto con tutti i parametri
p1 = Person("Luca", "Rossi", 20)
p1.saluta()

# Oggetto che usa il valore predefinito di Age
p2 = Person("Mario", "Rossi")
p2.saluta()


# ------------------------------------------------------------------------------
# 3. PARAMETRO self
# ------------------------------------------------------------------------------
# self e' il riferimento all'istanza corrente e deve essere il primo parametro
# di ogni metodo. Permette di accedere sia alle proprieta' sia ai metodi.

# EX 1: accesso alle proprieta' tramite self
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}") # Accesso alle proprietà


car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


# EX 2: accesso ad un metodo tramite self
class PersonWelcome:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our app.")


p1 = PersonWelcome("Tobias")
p1.welcome() # Accesso al metodo della classe