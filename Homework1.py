""" Ejercicio 1:
Supongamos que estás desarrollando un programa para un cine
y deseas asegurarte de que los espectadores sean lo suficientemente
mayores para ver una película clasificada como PG-13. 

Debes solicitar la edad del espectador y permitir el acceso
solo si tienen al menos 13 años

print ("Bienvenido al cine")
print ("Clasificación de la película: PG-13")

edad = int(input("que edad tenes?: "))
if edad >= 13:
    print("podes pasar a ver la película")
else:
    print("no puedes pasar, te recominedo otra pelí")

Ejercicio 2:
Imagina que eres un profesor y deseas calcular las calificaciones 
finales de tus estudiantes en función de sus puntajes en un examen.  
La calificación final se asignará de la siguiente manera: 

Si el puntaje…

Es mayor o igual a 90, la calificación es "A".
Está entre 80 y 89, la calificación es "B".
Está entre 70 y 79, la calificación es "C".
Está entre 60 y 69, la calificación es "D".
Es menor que 60, la calificación es "F".

# calificacion = int(input("ingresa la calificacion del examen."))
nota = 50
if nota >= 90:
    print("La calificación 'A'.")
elif nota >= 80 and  nota <= 89:
    print("La calificación 'B'.")
elif nota >= 70 and nota <= 79:
    print("La calificación 'C'.")
elif nota >= 60 and nota <= 69:
    print("La calificación 'D'.")
else:
    print("La calificación 'F'.")

ercicio 3:
Calculadora de descuento

Ahora debes generar un programa calcule el descuento de un producto,
se le solicita al usuario ingresar el precio original de un producto.
Luego, calcula y muestra el precio final después del descuento. 

Tener en cuenta lo siguiente: 

Si se ingresa un precio de producto mayor o igual a $12.999 entonces 
se realizará el descuento del 30%, 
Sino, se realizará el descuento del 20% sobre el total del producto.


Precio_original = float(input("ingrse el precio original:"))

if Precio_original >= 12999:
    Descuento = Precio_original *.30
    print(f"con el descuento del 30% se descaontaron: {Descuento}")
else:
    Descuento = Precio_original *.20
    print(f"con el descuento del 20% se descaontaron: {Descuento}")

print(f"el precio final con el descuento es:{Precio_original - Descuento}")

Ejercicio 4:
Validar dias de la semana

Crea un programa que pida al usuario ingresar un número del 1 al 7
y muestre el día de la semana correspondiente. 
Si ingresa un número fuera de ese rango, 
mostrar el siguiente mensaje de error: "Número de día incorrecto".


  
numero_dia = input("ingrese un número del 1 al 7: ")
if numero_dia == "1":
    print("domingo")
elif numero_dia == "2":
    print("lunes")
elif numero_dia == "3":
    print("martes")
elif numero_dia == "4":
    print("miércoles")
elif numero_dia == "5":
    print("jueves")
elif numero_dia == "6":
    print("viernes")
elif numero_dia == "7":
    print("sábado") 
else: 
    print("día invalido elegir entre el 1 y el 7")
    
"""