""" WHILE

contador = 1

while contador <= 5:    
    print(contador)
    contador = contador +1
    
print("Fin del contador")

#siempre poner limite en el while para que no se haga infinito,
# si no se pone limite el while se ejecuta infinitamente.

# DO-WHILE

while True:
    pasword = input("Ingrese la contraseña: ")
    if pasword == "1234":
        print("Contraseña correcta")
        break
    


#for

palabra = "Hola mundo"

for letra in palabra:
    print(letra) 
    
    
"""
#For con Break  
for num in range(1,21):
    print(num)
    if num == 16:
        print("Se encontró el elemento. Se finaliza el recorrido")
        break
    