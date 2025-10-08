import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { test } from 'node:test';
import assert from 'node:assert/strict';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');

async function loadGeoJSON() {
  const raw = await readFile(join(root, 'beagle.geojson'), 'utf8');
  return JSON.parse(raw);
}

test('las escalas están ordenadas por fecha de inicio', async () => {
  const geojson = await loadGeoJSON();
  const features = geojson.features;
  const dates = features.map((feature) => new Date(feature.properties.fecha_inicio).getTime());

  for (let i = 0; i < dates.length - 1; i += 1) {
    assert.ok(
      dates[i] <= dates[i + 1],
      `La escala ${features[i].properties.nombre} debe ocurrir antes o el mismo día que ${features[i + 1].properties.nombre}`
    );
  }
});

test('cada escala respeta la relación inicio <= fin', async () => {
  const geojson = await loadGeoJSON();
  for (const feature of geojson.features) {
    const start = new Date(feature.properties.fecha_inicio).getTime();
    const end = new Date(feature.properties.fecha_fin).getTime();
    assert.ok(
      start <= end,
      `La escala ${feature.properties.nombre} tiene fecha_inicio posterior a fecha_fin`
    );
  }
});

test('las coordenadas se mantienen en los rangos válidos', async () => {
  const geojson = await loadGeoJSON();
  for (const feature of geojson.features) {
    const [lon, lat] = feature.geometry.coordinates;
    assert.ok(lon >= -180 && lon <= 180, `Longitud fuera de rango en ${feature.properties.nombre}`);
    assert.ok(lat >= -90 && lat <= 90, `Latitud fuera de rango en ${feature.properties.nombre}`);
  }
});
