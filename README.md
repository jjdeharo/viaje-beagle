# Viaje del HMS Beagle

Aplicación web basada en Leaflet y OpenStreetMap que muestra las escalas del segundo viaje del HMS *Beagle* con notas histórico-científicas, control temporal y filtros temáticos.

## Contenidos

- `beagle.geojson`: datos GeoJSON validados (WGS84) ordenados cronológicamente.
- `schema.json`: esquema JSON Schema (draft 2020-12) utilizado en las pruebas automáticas.
- `about.json`: metadatos de fuentes y licencias.
- `index.html`, `styles.css`, `main.js`: visor web con controles de filtros, búsqueda, detalle lateral, selector de idioma (es/en) y modal de licencias.
- `translations/`: diccionarios de UI (`es.json`, `en.json`).
- `tests/`: pruebas automatizadas con el runner nativo de Node.

## Requisitos

- Node.js >= 18

Instala dependencias la primera vez:

```bash
npm install
```

## Ejecutar pruebas

```bash
npm test
```

Las pruebas cubren:

- Validación del GeoJSON contra `schema.json` (Ajv 2020).
- Orden cronológico, rangos de fechas y coordenadas.
- Comportamiento de filtros por año, etiquetas y búsqueda.
- Presencia de ayudas básicas de accesibilidad en `index.html`.

## Servir la aplicación

El visor funciona con cualquier servidor estático. Por ejemplo, con Python:

```bash
python3 -m http.server
```

Luego visita `http://localhost:8000/` y abre `index.html`.

## Actualizar datos

El script `generate_data.py` recompone `beagle.geojson` asegurando longitudes de texto, uso del vocabulario controlado y validaciones básicas.

## Licencias

- Datos: CC BY-SA 4.0
- Código: AGPL-3.0-or-later

Consulta el modal “Acerca de” dentro de la aplicación para ver las fuentes primarias y versiones.
