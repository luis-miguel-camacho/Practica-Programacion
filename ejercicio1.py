"""# INGRESO DE DATOS POR USUARIO
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

#Suma los dos numeros
suma = numero1 + numero2

#Muestra el resultado de la suma
print(f"La suma de {numero1} y {numero2} es: {suma}")

edad = 15 
if edad >= 18:
    print("Eres mayor de edad.")
else: 
    print("Eres menor de edad.")
    
numero = 0 #cambiar el valor de la variable numero para probar diferentes casos

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    
# ejemplo de esturctura anidada en Python
# definir variabe edad

edad = 7 
# comenzar estructura de decisión anidada

if edad < 0:
    print("Edad no válida.")
else:
    if edad < 18:
        print("Eres menor de edad.")
    elif edad < 65:
        print("Eres adulto.")
    else:
        print("Eres adulto mayor.")   
        
dia_semana = int(input("Ingrese un número del 1 al 7 que represente un día"))

if dia_semana == 1:
    print("lunes")
elif dia_semana == 2:
    print("martes")
elif dia_semana == 3:
    print("miércoles")
elif dia_semana == 4:
    print("jueves")
elif dia_semana == 5:
    print("viernes")
elif dia_semana == 6:
    print("sábado")
elif dia_semana == 7:
    print("domingo")


# operador and

x=5
Y=10
if x > 0 and y > 0:
    print("Ambos números son positivos.")
    
#operador or

edad = 25
if edad < 18 or edad > 65:
    print("tiene un super descuento")

# operador not

x= 5
if not x == 0:
    print("x no es igual a cero.")
    
   
# en el En el primero, se evalúa la variable edad para verificar si es mayor o igual a 18 y menor a 65. Además, mediante el operador lógico OR, se valida si la edad es mayor o igual a 65 y menor a 70 años.

if (edad >= 18 and edad < 65) or (edad >= 65 and edad < 70):
    print("puede votar")

# se valida la variable número para comprobar si es mayor que cero y menor que cien. Asimismo, utilizando el operador lógico OR, se permite que el número sea menor que cero.

edad= 90

if (edad > 0 and edad < 100) or (edad < 0):
    print("El numero es positivo y menor que 100 o es negativo.")    
    
    
# Ejemplo de valor de IMC a evaluar
imc = 10.2

# Estructura de clasificación con if-elif-else
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25.0:
    categoria = "Peso normal (Adecuado)"
elif imc < 30.0:
    categoria = "Sobrepeso"
elif imc < 35.0:
    categoria = "Obesidad Grado I"
elif imc < 40.0:
    categoria = "Obesidad Grado II"
else:
    categoria = "Obesidad Grado III (Mórbida)"

print(f"Para un IMC de {imc}, la categoría es: {categoria}") 

"""   