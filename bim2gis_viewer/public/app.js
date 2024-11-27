const viewer = new Cesium.Viewer('cesiumContainer', {
  imageryProvider: new Cesium.WebMapServiceImageryProvider({
    url: 'https://ows.terrestris.de/osm/service', // Cambia por tu servidor WMS si lo tienes
    layers: 'OSM-WMS',
    parameters: {
      service: 'WMS',
      version: '1.1.1',
      request: 'GetMap',
      format: 'image/png',
      transparent: true,
    },
  }),
  terrainProvider: Cesium.createWorldTerrain(),
});

// Configurar cámara inicial
viewer.scene.camera.setView({
  destination: Cesium.Cartesian3.fromDegrees(-58.47, -34.67, 1000), //Larrazabal
});

// Inicializar IFC.js
const ifcLoader = new IfcLoader();
const ifcModels = [];

async function loadIFCModel() {
  // Cargar modelo IFC
  const ifcUrl = './models/MPD-A-MO-ES-07_Puente Larrazabal.ifc'; // Cambia la ruta según tu modelo
  await ifcLoader.ifcManager.setWasmPath('./libs/'); // Ruta del archivo wasm de ifc.js
  const model = await ifcLoader.load(ifcUrl);

  // Convertir a glTF (temporal)
  const gltfUrl = await convertToGLTF(model);
  ifcModels.push(model);

  // Cargar modelo glTF en Cesium
  viewer.scene.primitives.add(Cesium.Model.fromGltf({ url: gltfUrl }));
}

async function convertToGLTF(ifcModel) {
  // Conversión básica de IFC a glTF (temporal)
  const gltfUrl = URL.createObjectURL(new Blob([JSON.stringify(ifcModel)], { type: 'application/json' }));
  return gltfUrl;
}

// Cargar modelo IFC
loadIFCModel().catch(console.error);
