print("Hola")
name = input("¿Quien eres?")
print("Hola", name)

print("Seleccione su orden")
print("1.......Desayuno")
print("2.......Almuerzo")
print("3.......Onces")

opcion = int(input())

if opcion == 1:
    print("Seleccione su desayuno")
    print("1........Manzana")
    print("2........Huevos")
    print("3........Jugo")
    print("4.......Todas las anteriores")
    opcionDesayuno = int(input())
    if opcionDesayuno == 1:
        print("Su desayuno esta listo, reclame su manzana")
    elif opcionDesayuno == 2:
        print("Su desayuno esta listo, reclame sus huevos")
    elif opcionDesayuno == 3:
        print("Su desayuno esta listo, reclame su jugo")
    else:
        print("Su desayuno esta listo, reclame su Manzana, su Jugo y sus Huevos")
elif opcion == 2:
    print("Su almuerzo esta listo")

else:
    print("Sus Onces estan listas!!")
