// Coordenadas de Larrazábal y Dellepiane, Buenos Aires
const lat = -34.672546;
const lon = -58.478379;
const height = 300; // Altura en metros para la vista inicial

// Configurar cámara inicial en las coordenadas
viewer.scene.camera.setView({
  destination: Cesium.Cartesian3.fromDegrees(lon, lat, height),
  orientation: {
    heading: 0.0, // Rotación en el plano horizontal (en radianes)
    pitch: -Cesium.Math.toRadians(45), // Inclinación hacia abajo
    roll: 0.0, // Rotación lateral
  },
});

// Agregar un marcador para identificar el lugar
const pinBuilder = new Cesium.PinBuilder();
const pin = viewer.entities.add({
  name: 'Larrazábal y Dellepiane',
  position: Cesium.Cartesian3.fromDegrees(lon, lat),
  billboard: {
    image: pinBuilder.fromColor(Cesium.Color.RED, 48).toDataURL(),
    verticalOrigin: Cesium.VerticalOrigin.BOTTOM,
  },
});
