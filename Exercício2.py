def numero_fibonacci(numero):
    x, y = 0, 1
    while x < numero:
        x, y = y, x + y
    return x == numero


numero_informado = int(input("Qual número deseja verificar se pertence à sequência de Fibonacci: "))

if numero_fibonacci(numero_informado):
    print(f"{numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_informado} não pertence à sequência de Fibonacci.")