num = int(input("Por favor digite un número:"))

if num < 0:
    print("Este número es negativo")
    if num > -11:
        print("Este número número se encuentra dentro del rango de -1 al -10")
elif num > 10:
    print("Este número no esta en el rango del 1 al 10")

else:
    print("Este número es positivo")