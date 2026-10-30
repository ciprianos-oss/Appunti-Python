#Definizione di un lista
my_list = ["tizio", 3, "sempronio"]

#Mando a video il contenuto della lista, il tipo ed un valore ad un determinato indice
print(my_list)
print(type(my_list))
print(my_list[0])

#Mando a video gli elementi di una lista tramite un ciclo for
for i in range(len(my_list)):
    print(my_list[i])

#Dichiarazione di una lista vuota con aggiunta di elementi
list_2 = []
list_2.append(5)
print(list_2)