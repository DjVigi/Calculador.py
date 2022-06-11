#Pequeño juego en el cual debes intentar adivinar el numero en el cual esta pensando el ordenador,acumulas puntos por cada acierto y al final te muestra los puntos conseguidos
import random
puntos=0
for i in range(3):
    x = random.randint(1,10)
    z = int(input("Intenta adivinar el numero que estoy pensando,del 1 al 10"))
    if x == z:
        print("Has introducido el numero",z)
        print("El numero que estoy pensando es",x)
        print("Enhorabuena,has acertado")
        puntos=puntos+1
    else:
        print("El numero que has introducido es",z)
        print("El numero que estoy pensando es",x)
        print("Lo siento,has fallado,sigue intentandolo")
print("Has obtenido",puntos,"puntos")