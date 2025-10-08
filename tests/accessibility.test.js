import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { JSDOM } from 'jsdom';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');

async function loadDOM() {
  const html = await readFile(join(root, 'index.html'), 'utf8');
  const dom = new JSDOM(html);
  return dom.window.document;
}

test('existen ayudas básicas de accesibilidad', async () => {
  const document = await loadDOM();
  const skipLink = document.querySelector('.skip-link');
  assert.ok(skipLink, 'Debe existir un enlace para saltar al contenido');
  assert.strictEqual(skipLink.getAttribute('href'), '#map');

  const map = document.getElementById('map');
  assert.ok(map, 'Debe existir el contenedor del mapa');
  assert.strictEqual(map.getAttribute('role'), 'application');
});

test('los controles principales tienen etiquetas accesibles', async () => {
  const document = await loadDOM();
  const yearRange = document.getElementById('yearRange');
  assert.ok(yearRange, 'Debe existir el deslizador de año');
  assert.ok(yearRange.getAttribute('aria-label'), 'El deslizador necesita aria-label');

  const yearLabel = document.querySelector('label[for="yearRange"]');
  assert.ok(yearLabel, 'El deslizador debe tener etiqueta asociada');

  const searchInput = document.getElementById('searchInput');
  assert.ok(searchInput.getAttribute('aria-label'), 'El buscador necesita aria-label');

  const status = document.getElementById('status');
  assert.strictEqual(status.getAttribute('role'), 'status');
  assert.strictEqual(status.getAttribute('aria-live'), 'polite');

  const stepControls = document.querySelector('.step-controls');
  assert.ok(stepControls, 'Debe existir el control de navegación secuencial');
  assert.strictEqual(stepControls.getAttribute('role'), 'group');

  const prevButton = document.getElementById('prevStopBtn');
  const nextButton = document.getElementById('nextStopBtn');
  assert.ok(prevButton, 'Debe existir el botón de punto anterior');
  assert.ok(nextButton, 'Debe existir el botón de punto siguiente');
  assert.ok(prevButton.getAttribute('aria-label'), 'El botón anterior necesita aria-label');
  assert.ok(nextButton.getAttribute('aria-label'), 'El botón siguiente necesita aria-label');
});

test('el modal de acerca de es operable', async () => {
  const document = await loadDOM();
  const aboutModal = document.getElementById('aboutModal');
  assert.ok(aboutModal, 'Debe existir el modal');
  assert.strictEqual(aboutModal.getAttribute('role'), 'dialog');
  assert.strictEqual(aboutModal.getAttribute('aria-modal'), 'true');

  const closeButton = document.getElementById('closeAbout');
  assert.ok(closeButton, 'El modal debe tener botón de cierre');
  assert.ok(closeButton.getAttribute('aria-label'), 'El botón de cierre debe anunciar su función');
});
