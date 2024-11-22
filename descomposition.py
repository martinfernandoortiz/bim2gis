import ifcopenshell
import json

# Cargar el archivo IFC
filepath = "MPD-A-MO-ES-07_Puente Larrazabal.ifc"
model = ifcopenshell.open(filepath)

# Extraer todos los objetos y sus tipos
objects = []
for obj in model:
    if hasattr(obj, "is_a"):
        objects.append({
            "oid": obj.id(),
            "type": obj.is_a(),
            "name": getattr(obj, "Name", None)
        })

# Guardar como JSON
with open("output.json", "w") as json_file:
    json.dump(objects, json_file, indent=4)
