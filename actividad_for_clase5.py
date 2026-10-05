# De todos los deportes disponibles, vamos a mostrar los deportesque se listaron solo hasta futbol. 
print("Deportes en el polideportivo")

deportes_disponibles = ["basket", "tenis", "esgrima", "natacion", "futbol", "voley", "atletismo"]

for deporte in deportes_disponibles:
    if deporte == "tenis": 
        print(f"{deporte}") 
        break 
    print(deporte)
