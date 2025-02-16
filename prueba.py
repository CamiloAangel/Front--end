
print("Primer comentario Camilo.")
print("No, hoy es domingo")
print("Soy Alan y yo Camilo jeje")

def fibonacci_iterativo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(1, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci_iterativo(10))
