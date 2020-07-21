#Saludo al usuario
print("Hola")
name = input("¿Quien eres?")
while name == "":
    print("ingrese su nombre")
    name = input()
print("Hola,", name, "Esta es asistente de calculadora básica")
#Fin del Saludo
#Contador
contador = 0
#Solicitud de números
numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo número:"))
#Lista de opciones
opcionCalculadora = ["Suma", "Resta", "Multiplicación", "División", "Número mayor", "Número menor"]
#Cliclo de la lista
for calculadora in opcionCalculadora:
    contador+=1
    print(contador, "...............", calculadora)
#Entrada del usuaio
print("Seleccione..............:")
seleccion = int(input())
# Codicional de suma
if  seleccion == 1:
    print("El resultado es: ", numero1+numero2)
#Condicional de resta
elif seleccion == 2:
    print("El resultado es: ", numero1-numero2)
#Condicional de multiplicación
elif seleccion == 3:
    print("El resultado es: ", numero1*numero2)
#Condicional de división
elif seleccion == 4:
    print("El resultado es: ", numero1/numero2)
#Condcional de número mayor
elif seleccion == 5:
    #Estrucutura que valida cual es el número mayor por codicionales
    if numero2<numero1:
        print("El número mayor es:", numero1)
    else:
        print("El número mayor es:", numero2)
    #Fin de la estrucutura
#Condicional de número menor
elif seleccion == 6:
    # Estrucutura que valida cual es el número menor por codicionales
    if numero2<numero1:
        print("El número menor es:", numero2)
    else:
        print("El número menor es:", numero1)
    #Fin de la estrucutura