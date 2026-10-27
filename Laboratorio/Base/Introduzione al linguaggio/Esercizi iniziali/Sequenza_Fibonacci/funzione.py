def seq_fibonacci(limite: int) -> None:
    a, b = 0, 1

    while a <= limite:
        # Usando le f-string decidi tu quanti spazi inserire senza l'interferenza della virgola
        print(f"{a}  ", end='')

        # Assegnazione simultanea
        a, b = b, a + b
    print() # Giusto per andare a capo alla fine della sequenza