# BIM2GIS
All the scripts are base on this paper IFC to 3D Tiles: An Integrated Open-Source Solution for Visualising BIMs on Cesium

Check https://github.com/Erfan-Shooraj/ifc2b3dm?tab=readme-ov-file


## Requirements
'''
sudo apt-get install git
sudo apt install python3-pip
pip install requests pyifc
pip install ifcopenshell
'''

## Descargar IFC Convert (esta en descargas)
## Agregar al path
'''
sudo nano  ~./bashrc
export PATH=$PATH:/home/ausa/ifcconvert/
guardar los cambios y salir
source ~./bashrc
'''
'''
sudo apt-get install nodejs
sudo apt install npm
npm install -g obj2gltf
npm install 3d-tiles-tools

npm install 3d-tiles-validator
'''


BIM SERVER

Descargar java desde https://www.oracle.com/java/technologies/downloads/?er=221886

'''
sudo dpkg -i jdk-23_linux-x64_bin.deb 
'''

Descargar 
bimserverjar-1.5.186.jar: Run on your desktop (just double click)
https://github.com/opensourceBIM/BIMserver/releases


Copiar el archivo en la carpeta BIMServer (creada en algun lugar que elijamos)

java -version (para chequear que este instalado java)

'''
java -jar bimserverjar-1.5.186.jar 
'''


http://localhost:8082/

'''
sudo git clone https://github.com/Erfan-Shooraj/ifc2b3dm.git

cd ifc2b3dm/IFC2GLTFs/
'''



## Pipeline
