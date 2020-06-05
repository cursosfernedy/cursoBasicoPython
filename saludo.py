saludo = input("Por favor ingrese su nombre: ")

while saludo == "":
    print("Digite su nombre: ")
    saludo = input()
    if saludo != "":
        break
print("Hola", saludo)