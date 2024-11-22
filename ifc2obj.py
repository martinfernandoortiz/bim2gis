import os
import subprocess

# Carpeta que contiene los archivos IFC generados
ifc_folder = "salida_por_tipo"
output_folder = "salida_objetos"
os.makedirs(output_folder, exist_ok=True)

# Iterar sobre todos los archivos IFC en la carpeta
for ifc_file in os.listdir(ifc_folder):
    if ifc_file.endswith(".ifc"):
        input_path = os.path.join(ifc_folder, ifc_file)
        output_path = os.path.join(output_folder, ifc_file.replace(".ifc", ".obj"))
        
        # Comando para ejecutar IfcConvert
        command = ["IfcConvert", input_path, output_path]
        
        try:
            # Ejecutar IfcConvert
            subprocess.run(command, check=True)
            print(f"Convertido: {ifc_file} -> {os.path.basename(output_path)}")
        except subprocess.CalledProcessError as e:
            print(f"Error al convertir {ifc_file}: {e}")

print("¡Conversión completada!")
