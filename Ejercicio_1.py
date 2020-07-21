#Primera linea de Codigo
#Saludo al usuario
print("Hola")
nombre = input("¿Quien eres?:")
print("Hola", nombre)
#Fin de Saludo
#Inicio de solicitud de números
print("Ingrese el primer número")
n1 = int(input())
print("Ingrese el segundo número:")
n2 = float(input())
#Fin de solicitud al usuario

#Suma de 2 números
print("La suma de los 2 números ingresado son:", n1+n2)
#Resta de 2 números
print("La resta de los 2 números es:", n1-n2)
#Multiplicación
print("La multiplicación de los 2 números es:",n1*n2)
#La división de 2 números
print("La división de los 2 números es:", n1/n2)
# Fin de la calculadora básica

print("¿El número uno es mayor?", n1>n2)
print("¿El número dos es mayor?", n2>n1)

#Tipos de datos ingresados

print("El primer número es de tipo:", type(n1))
print("El segundo número es de tipo:", type(n2))
print("El nombre es de tipo", type(nombre))