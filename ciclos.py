numero = 0

while numero <= 10:
    print(" El valor actual de la variable es:", numero)
    numero += 1
    if numero == 7:

        break

print(numero)

animales = ['Perro', 'Gato', 'Ave', 'Serpientes']

for animal in animales:
    print("El animal es:" , animal)
    if animal == 'Gato':
        break