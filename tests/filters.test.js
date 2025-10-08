import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { test } from 'node:test';
import assert from 'node:assert/strict';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');

async function loadData() {
  const raw = await readFile(join(root, 'beagle.geojson'), 'utf8');
  const geojson = JSON.parse(raw);
  return geojson.features.map((feature) => ({
    ...feature,
    meta: {
      start: new Date(feature.properties.fecha_inicio),
      end: new Date(feature.properties.fecha_fin),
      startYear: new Date(feature.properties.fecha_inicio).getUTCFullYear()
    }
  }));
}

function filterFeatures(data, { year, tags = [], query = '' }) {
  const q = query.trim().toLowerCase();
  return data
    .filter((feature) => {
      if (typeof year === 'number' && feature.meta.startYear > year) {
        return false;
      }
      if (tags.length) {
        const hasAll = tags.every((tag) => feature.properties.tags.includes(tag));
        if (!hasAll) {
          return false;
        }
      }
      if (q && !feature.properties.nombre.toLowerCase().includes(q)) {
        return false;
      }
      return true;
    })
    .sort((a, b) => a.meta.start - b.meta.start);
}

test('el filtro por año respeta el límite superior', async () => {
  const data = await loadData();
  const result = filterFeatures(data, { year: 1832 });
  assert.ok(result.length > 0, 'Debe haber escalas antes de 1833');
  assert.ok(
    result.every((feature) => feature.meta.startYear <= 1832),
    'No deben aparecer escalas posteriores al año filtrado'
  );
});

test('el filtro combinado de etiquetas encuentra intersecciones correctas', async () => {
  const data = await loadData();
  const result = filterFeatures(data, { tags: ['geología', 'sismología'] });
  const nombres = result.map((feature) => feature.properties.nombre);
  assert.deepEqual(nombres, ['Valparaíso y Cuenca de Santiago (Chile)']);
});

test('los filtros combinados de año y etiqueta devuelven subconjuntos previsibles', async () => {
  const data = await loadData();
  const result = filterFeatures(data, { year: 1835, tags: ['biogeografía'] });
  const nombres = result.map((feature) => feature.properties.nombre);
  assert.deepEqual(nombres, ['Islas Galápagos (Ecuador)']);
});

test('la búsqueda por nombre es insensible a mayúsculas', async () => {
  const data = await loadData();
  const result = filterFeatures(data, { query: 'cocos' });
  const nombres = result.map((feature) => feature.properties.nombre);
  assert.deepEqual(nombres, ['Islas Cocos (Keeling)']);
});
