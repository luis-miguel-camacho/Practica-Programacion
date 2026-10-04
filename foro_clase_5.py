
# Recorrido de lista, deportes disponibles. Hasta encontrar "futbol" y finalizar. 

deportes_disponibles = ["voley", "handball", "lucha", "natacion", "atletismo", "basket", "futbol", "esgrima", "pesca"]

for  deporte in deportes_disponibles:
    if deporte == "futbol":
        print(f"Se encontró {deporte}. Fin de la búsqueda")
        break 
    