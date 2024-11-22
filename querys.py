import ifcopenshell
import json
import os

# Archivo IFC de entrada
input_ifc = "MPD-A-MO-ES-07_Puente Larrazabal.ifc"

# Carpeta para guardar las salidas
output_folder = "salida_por_tipo"
os.makedirs(output_folder, exist_ok=True)

# Leer el modelo IFC
model = ifcopenshell.open(input_ifc)

# Lista de tipos deseados
desired_types = ["05632d911b", "IFCBEAM", "IFCBUILDINGELEMENTPROXY", "IFCSLAB"]

# Diccionario para almacenar los datos por tipo
data_by_type = {type_: [] for type_ in desired_types}

# Filtrar los elementos según su tipo
for element in model:
    if element.is_a() in desired_types:
        # Guardar datos en el diccionario
        data_by_type[element.is_a()].append({
            "oid": element.id(),
            "name": getattr(element, "Name", "Sin nombre"),
        })

        # Crear un nuevo modelo con solo este elemento
        new_model = ifcopenshell.file(schema=model.schema)
        new_element = new_model.add(element)
        new_model.write(f"{output_folder}/{element.is_a()}_{element.id()}.ifc")

# Guardar los datos de cada tipo en archivos JSON
for type_, elements in data_by_type.items():
    with open(f"{output_folder}/{type_}.json", "w") as json_file:
        json.dump(elements, json_file, indent=4)

print("¡Archivos generados con éxito!")
