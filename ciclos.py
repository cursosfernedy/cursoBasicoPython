print("Hola")
name = input("¿Quien eres?")
while name == "":
    print("ingrese su nombre")
    name = input()

print("Hola", name)
contador = 0
opcionOrden = ["Desayuno", "Almuerzo", "Onces"]

for Orden in opcionOrden:
    contador+=1
    print(contador, "...........", Orden)
