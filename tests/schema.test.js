import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { test } from 'node:test';
import assert from 'node:assert/strict';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');

async function loadJSON(relativePath) {
  const path = join(root, relativePath);
  const raw = await readFile(path, 'utf8');
  return JSON.parse(raw);
}

test('el GeoJSON cumple el esquema', async () => {
  const [geojson, schema] = await Promise.all([
    loadJSON('beagle.geojson'),
    loadJSON('schema.json')
  ]);

  const ajv = new Ajv2020({ allErrors: true, strict: false });
  addFormats(ajv);
  const validate = ajv.compile(schema);
  const valid = validate(geojson);

  if (!valid) {
    console.error(validate.errors);
  }

  assert.ok(valid, 'El archivo beagle.geojson debe cumplir el esquema definido');
});
