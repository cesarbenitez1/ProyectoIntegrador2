#------------------- PARTE 1 PROYECTO INTEGRADOR------------------------

print ("Bienvenido!, por favor ingresa tu nombre por teclado")

# solictar el nombre del jugador por teclado
nombre_jugador = input("Por favor, ingrese su nombre: ")

#Imprimir el nombre del jugador ingresado con mensaje de bievendida
print("Bienvenido" + " " + nombre_jugador  + ", " + "es hora de jugar!")

#-------------------- PARTE 2 PROYECTO INTEGRADOR ----------------------

import readchar

while True:
    tecla = readchar.readkey()
    print("Tecla presionada:", tecla)

    if tecla == readchar.key.UP:
        print("Usted presionó la tecla de flecha hacia arriba ↑, saliendo del juego")
        break

