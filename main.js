const TAG_ORDER = [
  "inicio",
  "historia",
  "geología",
  "paleontología",
  "biogeografía",
  "botánica",
  "zoología",
  "ecología",
  "sismología",
  "volcanismo",
  "corales",
  "etnografía",
  "fin"
];

const TAG_LABELS = {
  es: {
    inicio: "Inicio",
    fin: "Fin",
    historia: "Historia",
    geología: "Geología",
    paleontología: "Paleontología",
    biogeografía: "Biogeografía",
    botánica: "Botánica",
    zoología: "Zoología",
    ecología: "Ecología",
    sismología: "Sismología",
    volcanismo: "Volcanismo",
    corales: "Corales",
    etnografía: "Etnografía"
  },
  ca: {
    inicio: "Inici",
    fin: "Fi",
    historia: "Història",
    geología: "Geologia",
    paleontología: "Paleontologia",
    biogeografía: "Biogeografia",
    botánica: "Botànica",
    zoología: "Zoologia",
    ecología: "Ecologia",
    sismología: "Sismologia",
    volcanismo: "Vulcanisme",
    corales: "Coralls",
    etnografía: "Etnografia"
  },
  gl: {
    inicio: "Comezo",
    fin: "Fin",
    historia: "Historia",
    geología: "Xeoloxía",
    paleontología: "Paleontoloxía",
    biogeografía: "Biogeografía",
    botánica: "Botánica",
    zoología: "Zooloxía",
    ecología: "Ecoloxía",
    sismología: "Sismoloxía",
    volcanismo: "Vulcanismo",
    corales: "Corais",
    etnografía: "Etnografía"
  },
  eu: {
    inicio: "Hasiera",
    fin: "Amaiera",
    historia: "Historia",
    geología: "Geologia",
    paleontología: "Paleontologia",
    biogeografía: "Biogeografia",
    botánica: "Botanika",
    zoología: "Zoologia",
    ecología: "Ekologia",
    sismología: "Sismologia",
    volcanismo: "Sumendismo",
    corales: "Koralak",
    etnografía: "Etnografia"
  },
  en: {
    inicio: "Departure",
    fin: "Return",
    historia: "History",
    geología: "Geology",
    paleontología: "Palaeontology",
    biogeografía: "Biogeography",
    botánica: "Botany",
    zoología: "Zoology",
    ecología: "Ecology",
    sismología: "Seismology",
    volcanismo: "Volcanism",
    corales: "Corals",
    etnografía: "Ethnography"
  }
};

const LANG_STORAGE_KEY = "viaje-beagle:lang";

const state = {
  lang: "es",
  translations: new Map(),
  data: [],
  markers: new Map(),
  markerLayer: L.layerGroup(),
  route: L.polyline([], {
    color: "#d1495b",
    weight: 3,
    opacity: 0.85
  }),
  baseLayers: null,
  layerControl: null,
  map: null,
  about: null,
  selectedId: null,
  filtered: [],
  chronological: [],
  activeMarkerEl: null
};

const yearRange = document.getElementById("yearRange");
const yearValue = document.getElementById("yearValue");
const searchInput = document.getElementById("searchInput");
const tagList = document.getElementById("tagList");
const statusEl = document.getElementById("status");
const detailContent = document.getElementById("detailContent");
const detailPanel = document.querySelector(".panel-detail");
const languageSwitcher = document.getElementById("languageSwitcher");
const fullRouteBtn = document.getElementById("fullRouteBtn");
const prevStopBtn = document.getElementById("prevStopBtn");
const nextStopBtn = document.getElementById("nextStopBtn");
const darwinButton = document.getElementById("darwinButton");
const aboutButton = document.getElementById("aboutButton");
const aboutModal = document.getElementById("aboutModal");
const closeAbout = document.getElementById("closeAbout");
const aboutVersion = document.getElementById("aboutVersion");
const aboutDataLicense = document.getElementById("aboutDataLicense");
const aboutCodeLicense = document.getElementById("aboutCodeLicense");
const aboutSources = document.getElementById("aboutSources");

let previouslyFocusedElement = null;

function isSupportedLanguage(lang) {
  return Boolean(TAG_LABELS[lang]);
}

function getStorage() {
  try {
    if (typeof window !== "undefined" && "localStorage" in window) {
      return window.localStorage;
    }
  } catch (error) {
    console.warn("No se puede acceder a localStorage", error);
  }
  return null;
}

function getStoredLanguage() {
  const storage = getStorage();
  if (!storage) {
    return null;
  }
  try {
    return storage.getItem(LANG_STORAGE_KEY);
  } catch (error) {
    console.warn("No se pudo leer el idioma almacenado", error);
    return null;
  }
}

function storeLanguage(lang) {
  const storage = getStorage();
  if (!storage) {
    return;
  }
  try {
    storage.setItem(LANG_STORAGE_KEY, lang);
  } catch (error) {
    console.warn("No se pudo guardar el idioma seleccionado", error);
  }
}

function getLocalizedValue(feature, key) {
  const dict = feature.properties?.[`${key}_i18n`];
  if (dict && typeof dict === "object") {
    return (
      dict[state.lang] ||
      dict.es ||
      dict.en ||
      Object.values(dict)[0]
    );
  }
  return feature.properties?.[key];
}

function getLocalizedLinkLabel(link) {
  const dict = link?.label_i18n;
  if (dict && typeof dict === "object") {
    return (
      dict[state.lang] ||
      dict.es ||
      dict.en ||
      Object.values(dict)[0]
    );
  }
  return link?.label;
}

async function init() {
  try {
    const storedLanguage = getStoredLanguage();
    if (storedLanguage && isSupportedLanguage(storedLanguage)) {
      state.lang = storedLanguage;
    }
    document.documentElement.lang = state.lang;
    if (languageSwitcher && isSupportedLanguage(languageSwitcher.value) && languageSwitcher.value !== state.lang) {
      languageSwitcher.value = state.lang;
    }

    await loadTranslations(state.lang);
    applyTranslations();
    updateDetailDefaultMessage();

    state.map = initMap();
    state.markerLayer.addTo(state.map);
    state.route.addTo(state.map);

    const [data, aboutInfo] = await Promise.all([
      fetchJSON("beagle.geojson"),
      fetchJSON("about.json")
    ]);

    state.data = (data.features || []).map((feature) => ({
      ...feature,
      meta: buildMeta(feature)
    }));

    state.chronological = state.data.slice().sort((a, b) => a.meta.start - b.meta.start);
    state.chronological.forEach((feature, index) => {
      feature.meta.position = index + 1;
    });
    state.filtered = state.chronological.slice();

    state.about = aboutInfo;
    populateAbout();

    buildTagFilters();
    buildMarkers();
    applyFilters({ fitBounds: true });

    attachListeners();
  } catch (error) {
    console.error("Error inicializando la aplicación", error);
    showError();
  }
}

document.addEventListener("DOMContentLoaded", init);

function initMap() {
  const map = L.map("map", {
    center: [0, -30],
    zoom: 3,
    keyboard: true
  });

  const osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map);

  const hot = L.tileLayer("https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors, Tiles style by Humanitarian OpenStreetMap Team"
  });

  state.baseLayers = { osm, hot };
  state.layerControl = createLayerControl(map);

  return map;
}

function createLayerControl(map) {
  if (!state.baseLayers) {
    return null;
  }
  const labels = {};
  labels[getTranslation("map.base.osm") || "OpenStreetMap"] = state.baseLayers.osm;
  labels[getTranslation("map.base.hot") || "Humanitarian OSM"] = state.baseLayers.hot;
  return L.control.layers(labels).addTo(map);
}

function updateLayerControlLabels() {
  if (!state.map || !state.baseLayers) {
    return;
  }
  if (state.layerControl) {
    state.layerControl.remove();
  }
  state.layerControl = createLayerControl(state.map);
}

function buildMeta(feature) {
  const start = new Date(feature.properties.fecha_inicio);
  const end = new Date(feature.properties.fecha_fin);
  return {
    start,
    end,
    startYear: start.getUTCFullYear(),
    endYear: end.getUTCFullYear(),
    id: feature.properties.nombre
  };
}

async function fetchJSON(path) {
  const res = await fetch(path);
  if (!res.ok) {
    throw new Error(`Error al cargar ${path}`);
  }
  return res.json();
}

function buildTagFilters() {
  const used = new Set();
  state.data.forEach((feature) => {
    feature.properties.tags.forEach((tag) => used.add(tag));
  });

  tagList.innerHTML = "";
  TAG_ORDER.filter((tag) => used.has(tag)).forEach((tag) => {
    const id = `tag-${tag}`;
    const label = document.createElement("label");
    label.className = "tag-item";

    const input = document.createElement("input");
    input.type = "checkbox";
    input.value = tag;
    input.id = id;
    input.addEventListener("change", () => applyFilters());

    const span = document.createElement("span");
    span.dataset.tagValue = tag;
    span.textContent = getTagLabel(tag);

    label.append(input, span);
    tagList.appendChild(label);
  });
}

function buildMarkers() {
  state.markers.clear();
  state.markerLayer.clearLayers();

  state.data.forEach((feature) => {
    const [lon, lat] = feature.geometry.coordinates;
    const icon = L.divIcon({
      className: "marker-numbered",
      html: `<span>${feature.meta.position}</span>`,
      iconSize: [30, 30],
      iconAnchor: [15, 15]
    });

    const marker = L.marker([lat, lon], { icon });

    marker.bindPopup(buildPopupContent(feature));
    marker.on("click", () => selectFeature(feature, { pan: false }));

    marker.on("add", () => {
      const element = marker.getElement();
      if (element && !element.dataset.keyboardBound) {
        element.setAttribute("tabindex", "0");
        element.setAttribute("role", "button");
        const localizedName = getLocalizedValue(feature, "nombre");
        element.setAttribute("aria-label", `${feature.meta.position}. ${localizedName}`);
        element.dataset.keyboardBound = "true";
        element.addEventListener("keydown", (event) => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            selectFeature(feature);
          }
        });
      }
      if (state.selectedId === feature.meta.id) {
        setActiveMarker(marker);
      }
    });

    state.markers.set(feature.meta.id, marker);
  });
}

function buildPopupContent(feature) {
  const { fecha_inicio, fecha_fin, tags } = feature.properties;
  const nombre = getLocalizedValue(feature, "nombre");
  const interes = getLocalizedValue(feature, "interes");
  const range = formatDateRange(fecha_inicio, fecha_fin);
  const chips = tags
    .map((tag) => `<span class="chip">${getTagLabel(tag)}</span>`)
    .join(" ");

  return `
    <article class="popup">
      <h3>${nombre}</h3>
      <div class="muted">${range}</div>
      <p class="muted">${interes}</p>
      <div class="chips">${chips}</div>
    </article>
  `;
}

function selectFeature(feature, options = {}) {
  state.selectedId = feature.meta.id;

  const marker = state.markers.get(feature.meta.id);
  if (marker) {
    const pan = options.pan !== false;
    const highlight = () => setActiveMarker(marker);

    if (marker._map) {
      marker.openPopup();
    } else {
      marker.once("add", () => marker.openPopup());
    }

    if (pan && state.map) {
      state.map.panTo(marker.getLatLng(), { animate: true });
    }

    const element = marker.getElement();
    if (element) {
      highlight();
    } else {
      marker.once("add", highlight);
    }
  } else {
    setActiveMarker(null);
  }

  renderDetail(feature);
}

function setActiveMarker(marker) {
  if (state.activeMarkerEl) {
    state.activeMarkerEl.classList.remove("is-selected");
    state.activeMarkerEl = null;
  }

  if (!marker) {
    return;
  }

  const element = marker.getElement();
  if (element) {
    element.classList.add("is-selected");
    state.activeMarkerEl = element;
  } else {
    marker.once("add", () => setActiveMarker(marker));
  }
}

function renderDetail(feature) {
  const { fecha_inicio, fecha_fin, enlaces, tags } = feature.properties;
  const nombre = getLocalizedValue(feature, "nombre");
  const interes = getLocalizedValue(feature, "interes");
  const texto = getLocalizedValue(feature, "texto");
  const range = formatDateRange(fecha_inicio, fecha_fin);
  const tagBadges = tags
    .map((tag) => `<span>${getTagLabel(tag)}</span>`)
    .join("");
  const linkList = enlaces && enlaces.length
    ? enlaces
        .map(
          (link) => {
            const label = getLocalizedLinkLabel(link);
            return `<a href="${link.url}" target="_blank" rel="noopener">${label}</a>`;
          }
        )
        .join(" ")
    : "";
  const ordinal = feature.meta.position;
  const displayIndex = ordinal != null ? String(ordinal).padStart(2, "0") : "";
  const headingPrefix = displayIndex ? `<span class="detail-index">#${displayIndex}</span> ` : "";

  detailContent.innerHTML = `
    <article>
      <h3>${headingPrefix}${nombre}</h3>
      <p class="muted">${range} · ${interes}</p>
      <p>${texto}</p>
      <div class="detail-tags">${tagBadges}</div>
      <div class="detail-links">${linkList}</div>
    </article>
  `;
  detailPanel.scrollTop = 0;
}

function resetDetail() {
  state.selectedId = null;
  setActiveMarker(null);
  updateDetailDefaultMessage();
}

function applyFilters(options = {}) {
  const year = parseInt(yearRange.value, 10);
  yearValue.textContent = year;

  const selectedTags = Array.from(
    tagList.querySelectorAll('input[type="checkbox"]:checked'),
    (input) => input.value
  );
  const query = searchInput.value.trim().toLowerCase();

  const filtered = state.data.filter((feature) => {
    const { startYear } = feature.meta;
    if (startYear > year) {
      return false;
    }
    if (selectedTags.length) {
      const tags = feature.properties.tags;
      const matchesAll = selectedTags.every((tag) => tags.includes(tag));
      if (!matchesAll) {
        return false;
      }
    }
    if (query) {
      const localized = (getLocalizedValue(feature, "nombre") || "").toLowerCase();
      if (!localized.includes(query)) {
        return false;
      }
    }
    return true;
  });

  const sorted = filtered.slice().sort((a, b) => a.meta.start - b.meta.start);
  state.filtered = sorted;

  state.markerLayer.clearLayers();

  const points = sorted.map((feature) => {
    const marker = state.markers.get(feature.meta.id);
    if (marker) {
      marker.addTo(state.markerLayer);
    }
    const [lon, lat] = feature.geometry.coordinates;
    return [lat, lon];
  });

  state.route.setLatLngs(points);

  if (points.length && options.fitBounds) {
    state.map.fitBounds(points, { padding: [40, 40] });
  }

  setStepButtonsState();

  updateStatus(sorted.length);

  const visibleIds = new Set(sorted.map((feature) => feature.meta.id));

  if (state.selectedId && !visibleIds.has(state.selectedId)) {
    resetDetail();
  } else if (!state.selectedId && !sorted.length) {
    resetDetail();
  } else if (state.selectedId && visibleIds.has(state.selectedId)) {
    const marker = state.markers.get(state.selectedId);
    if (marker) {
      setActiveMarker(marker);
    }
  }
}

function getActiveDataset() {
  return state.filtered;
}

function stepFeature(direction) {
  const dataset = getActiveDataset();
  if (!dataset.length) {
    return;
  }

  let currentIndex = state.selectedId
    ? dataset.findIndex((feature) => feature.meta.id === state.selectedId)
    : -1;

  if (currentIndex === -1) {
    currentIndex = direction > 0 ? 0 : dataset.length - 1;
  } else {
    currentIndex += direction;
    if (currentIndex >= dataset.length) {
      currentIndex = 0;
    }
    if (currentIndex < 0) {
      currentIndex = dataset.length - 1;
    }
  }

  const target = dataset[currentIndex];
  if (target) {
    selectFeature(target);
  }
}

function setStepButtonsState() {
  const dataset = getActiveDataset();
  const disabled = dataset.length === 0;
  if (prevStopBtn) {
    prevStopBtn.disabled = disabled;
  }
  if (nextStopBtn) {
    nextStopBtn.disabled = disabled;
  }
}

function updateStatus(count) {
  const template = getTranslation("ui.resultados") || "{count} puntos visibles";
  statusEl.textContent = template.replace("{count}", count);
}

function showError() {
  statusEl.textContent = getTranslation("ui.error") || "No se pudieron cargar los datos.";
}

function attachListeners() {
  yearRange.addEventListener("input", () => applyFilters());
  searchInput.addEventListener("input", () => applyFilters());
  fullRouteBtn.addEventListener("click", () => {
    yearRange.value = yearRange.max;
    yearValue.textContent = yearRange.max;
    searchInput.value = "";
    tagList.querySelectorAll('input[type="checkbox"]').forEach((input) => {
      input.checked = false;
    });
    applyFilters({ fitBounds: true });
  });

  prevStopBtn.addEventListener("click", () => stepFeature(-1));
  nextStopBtn.addEventListener("click", () => stepFeature(1));

  if (darwinButton) {
    darwinButton.addEventListener("click", () => openDarwinChat());
  }

  languageSwitcher.addEventListener("change", async () => {
    state.lang = languageSwitcher.value;
    if (!isSupportedLanguage(state.lang)) {
      state.lang = "es";
      languageSwitcher.value = state.lang;
    }
    document.documentElement.lang = state.lang;
    storeLanguage(state.lang);
    await loadTranslations(state.lang);
    applyTranslations();
    refreshTagLabels();
    refreshMarkers();
    updateLayerControlLabels();
    applyFilters();
    if (state.selectedId) {
      const feature = state.data.find((item) => item.meta.id === state.selectedId);
      if (feature) {
        renderDetail(feature);
      }
    } else {
      updateDetailDefaultMessage();
    }
    populateAbout();
  });

  aboutButton.addEventListener("click", () => openAbout());
  closeAbout.addEventListener("click", () => closeAboutModal());
  aboutModal.addEventListener("click", (event) => {
    if (event.target === aboutModal) {
      closeAboutModal();
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !aboutModal.hasAttribute("hidden")) {
      closeAboutModal();
    }
  });
}

function updateDetailDefaultMessage() {
  if (!detailContent || state.selectedId) {
    return;
  }
  const message = getTranslation("ui.detalle.default") || detailContent.textContent;
  detailContent.textContent = message;
}

async function loadTranslations(lang) {
  if (state.translations.has(lang)) {
    return;
  }
  const data = await fetchJSON(`translations/${lang}.json`);
  state.translations.set(lang, data);
}

function applyTranslations() {
  const dict = state.translations.get(state.lang) || {};

  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.dataset.i18n;
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const key = el.dataset.i18nPlaceholder;
    if (dict[key]) {
      el.setAttribute("placeholder", dict[key]);
    }
  });

  document.querySelectorAll("[data-i18n-aria-label]").forEach((el) => {
    const key = el.dataset.i18nAriaLabel;
    if (dict[key]) {
      el.setAttribute("aria-label", dict[key]);
    }
  });
}

function getTranslation(key) {
  const dict = state.translations.get(state.lang) || {};
  return dict[key];
}

function getTagLabel(tag) {
  const labels = TAG_LABELS[state.lang] || TAG_LABELS.es;
  return labels[tag] || tag;
}

function refreshTagLabels() {
  document.querySelectorAll("[data-tag-value]").forEach((el) => {
    const tag = el.dataset.tagValue;
    el.textContent = getTagLabel(tag);
  });
}

function refreshMarkers() {
  state.data.forEach((feature) => {
    const marker = state.markers.get(feature.meta.id);
    if (!marker) {
      return;
    }
    const popup = marker.getPopup();
    if (popup) {
      popup.setContent(buildPopupContent(feature));
    }
    const element = marker.getElement();
    if (element) {
      const localizedName = getLocalizedValue(feature, "nombre");
      element.setAttribute("aria-label", `${feature.meta.position}. ${localizedName}`);
    }
  });
}

function populateAbout() {
  if (!state.about) return;
  aboutVersion.textContent = state.about.version || "–";
  aboutDataLicense.textContent = state.about.licencia_datos || "–";
  aboutCodeLicense.textContent = state.about.licencia_codigo || "–";

  aboutSources.innerHTML = "";
  (state.about.fuentes || []).forEach((source) => {
    const li = document.createElement("li");
    const link = document.createElement("a");
    link.href = source.url;
    link.target = "_blank";
    link.rel = "noopener";
    link.textContent = source.label;
    li.appendChild(link);
    aboutSources.appendChild(li);
  });
}

function openDarwinChat() {
  const url = "https://notebooklm.google.com/notebook/6e7f576b-f7c2-4d5a-868d-edb5067eb626";
  const viewportWidth = window.innerWidth || document.documentElement.clientWidth || (window.screen ? window.screen.width : 960);
  const viewportHeight = window.innerHeight || document.documentElement.clientHeight || (window.screen ? window.screen.height : 700);
  const width = Math.min(960, Math.max(640, viewportWidth - 80));
  const height = Math.min(720, Math.max(480, viewportHeight - 80));
  const screenLeft = typeof window.screenLeft === "number" ? window.screenLeft : (typeof window.screenX === "number" ? window.screenX : 0);
  const screenTop = typeof window.screenTop === "number" ? window.screenTop : (typeof window.screenY === "number" ? window.screenY : 0);
  const left = screenLeft + Math.max(0, (viewportWidth - width) / 2);
  const top = screenTop + Math.max(0, (viewportHeight - height) / 2);
  const features = [
    "popup=yes",
    "resizable=yes",
    "scrollbars=yes",
    "toolbar=no",
    "menubar=no",
    "location=no",
    "status=no",
    `width=${Math.round(width)}`,
    `height=${Math.round(height)}`,
    `left=${Math.round(left)}`,
    `top=${Math.round(top)}`
  ].join(",");
  const newWindow = window.open(url, "darwinNotebook", features);
  if (newWindow && typeof newWindow.focus === "function") {
    newWindow.focus();
  }
}

function openAbout() {
  previouslyFocusedElement = document.activeElement;
  aboutModal.removeAttribute("hidden");
  closeAbout.focus();
}

function closeAboutModal() {
  aboutModal.setAttribute("hidden", "true");
  if (previouslyFocusedElement) {
    previouslyFocusedElement.focus();
  }
}

function formatDateRange(start, end) {
  if (start === end) {
    return formatDate(start);
  }
  return `${formatDate(start)} – ${formatDate(end)}`;
}

function formatDate(value) {
  const date = new Date(value);
  const formatter = new Intl.DateTimeFormat(state.lang, {
    year: "numeric",
    month: "short",
    day: "2-digit"
  });
  return formatter.format(date);
}
