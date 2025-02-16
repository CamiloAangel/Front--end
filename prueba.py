
print("Primer comentario Camilo.")
print("No, hoy es domingo")
print("Soy Alan y yo Camilo jeje")
print("El mejor fibonacci")

def fibonacci_iterativo(n):
    #Casos base
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    #Si no hay casos base, pasa a generar la sucesión
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci_iterativo(10))