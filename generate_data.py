import json
from datetime import datetime

features = [
    {
        "nombre": "Plymouth (zarpe)",
        "fecha_inicio": "1831-12-27",
        "fecha_fin": "1831-12-27",
        "interes": "Inicio del viaje y calibración de instrumentos.",
        "texto": "Darwin embarca en el HMS Beagle y acompaña al capitán FitzRoy en la verificación de sextantes, cronómetros y barómetros antes de dejar el puerto. Observa cómo los naturalistas anteriores dejaron notas sobre mareas y las compara con mediciones propias. Concluye que el grado de precisión alcanzado permitirá traducir observaciones locales en teorías globales sobre cambios geológicos y distribución de especies.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?pageseq=3&itemID=F1916"}
        ],
        "tags": ["inicio", "historia"],
        "coordinates": [-4.143, 50.371],
    },
    {
        "nombre": "Porto Praya, Santiago (Cabo Verde)",
        "fecha_inicio": "1832-01-16",
        "fecha_fin": "1832-01-25",
        "interes": "Estratos volcánicos escalonados y nivel marino fósil.",
        "texto": "En los acantilados de Porto Praya distingue colchones de lava negra superpuestos a bancos de conchas cementadas que se elevan varios metros sobre el mar actual. Interpreta las terrazas como evidencia de hundimientos lentos seguidos de levantamientos sucesivos, descartando las erupciones únicas como explicación completa. Comprende que la historia volcánica puede leerse como una cronología gradual, idea clave para su geología comparada.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&viewtype=side&pageseq=46"}
        ],
        "tags": ["geología", "volcanismo"],
        "coordinates": [-23.508, 14.919],
    },
    {
        "nombre": "Salvador de Bahía (Brasil)",
        "fecha_inicio": "1832-02-28",
        "fecha_fin": "1832-03-18",
        "interes": "Bosque tropical como laboratorio de adaptación.",
        "texto": "Recorre la mata atlántica y documenta lianas, epífitas y manglares que ocupan nichos superpuestos en distintos estratos de luz. Anota cómo la profusión de insectos polinizadores se corresponde con flores especializadas y compara la distribución de raíces aéreas con suelos encharcados. Deduce que la competencia por recursos moldea morfologías convergentes y que los trópicos ofrecen pruebas vivas de la selección natural incipiente.",
        "enlaces": [
            {"label": "Carta a Henslow", "url": "https://darwin-online.org.uk/content/frameset?pageseq=45&itemID=F1460"}
        ],
        "tags": ["zoología", "ecología"],
        "coordinates": [-38.501, -12.973],
    },
    {
        "nombre": "Río de Janeiro (Brasil)",
        "fecha_inicio": "1832-04-04",
        "fecha_fin": "1832-07-05",
        "interes": "Muestreo sistemático de fauna y flora de la mata.",
        "texto": "Instala estaciones de muestreo en diferentes altitudes del bosque carioca y compara escarabajos, aves y bromelias entre claros y sombra cerrada. Observa que pequeños cambios en humedad generan reemplazos rápidos de especies y reflexiona sobre la ventaja de caracteres que facilitan la partición del hábitat. Concluye que la diversidad tropical se explica por variaciones graduales y no por creaciones independientes, reforzando su visión sobre la unidad de tipo.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?pageseq=75&itemID=F1936"}
        ],
        "tags": ["botánica", "zoología"],
        "coordinates": [-43.1729, -22.9068],
    },
    {
        "nombre": "Montevideo (Uruguay)",
        "fecha_inicio": "1832-07-26",
        "fecha_fin": "1834-08-24",
        "interes": "Base para expediciones paleontológicas en la pampa.",
        "texto": "Desde Montevideo organiza salidas hacia el interior pampeano y establece correspondencia logística con naturalistas británicos. Documenta cómo los estancieros hallan huesos gigantes en barrancas fluviales y planifica su extracción cuidadosa con moldes de yeso. Reconoce que la proximidad entre restos fósiles y fauna actual sugiere reemplazos graduales, clave para cuestionar la extinción cataclísmica inmediata.",
        "enlaces": [
            {"label": "Catálogo de fósiles", "url": "https://darwin-online.org.uk/content/frameset?itemID=F272&pageseq=19"}
        ],
        "tags": ["paleontología", "historia"],
        "coordinates": [-56.1645, -34.9011],
    },
    {
        "nombre": "Punta Alta y Bahía Blanca (Argentina)",
        "fecha_inicio": "1832-09-22",
        "fecha_fin": "1832-10-15",
        "interes": "Megafauna pleistocena en estratos marinos.",
        "texto": "Excava dientes y caparazones de gliptodontes junto a maderas semicarbonizadas en acantilados costeros. Nota que las capas fósiles se alternan con depósitos marinos recientes, implicando que los gigantes terrestres vivieron hasta tiempos muy cercanos. Deduce que la extinción pudo relacionarse con cambios ambientales graduales y no con diluvios puntuales, apoyando la mutabilidad lenta de los ecosistemas.",
        "enlaces": [
            {"label": "Notas geológicas", "url": "https://darwin-online.org.uk/content/frameset?itemID=F271&pageseq=67"}
        ],
        "tags": ["paleontología", "geología"],
        "coordinates": [-62.083, -38.72],
    },
    {
        "nombre": "Canal Beagle y Tierra del Fuego", 
        "fecha_inicio": "1833-01-12",
        "fecha_fin": "1833-02-20",
        "interes": "Observación etnográfica y adaptación al frío extremo.",
        "texto": "Convive con yámanas reembarcados por FitzRoy y registra cómo su vestimenta mínima contrasta con la eficacia de sus canoas en aguas heladas. Analiza la distribución de musgos y líquenes sobre rocas graníticas expuestas al viento y relaciona la escasa flora con las estrategias de subsistencia fueguina. Concluye que cultura y biología coevolucionan con el clima, evidencia empírica contra la idea de razas fijas e inmutables.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=211"}
        ],
        "tags": ["etnografía", "historia"],
        "coordinates": [-68.628, -54.865],
    },
    {
        "nombre": "Islas Malvinas (Port Louis)",
        "fecha_inicio": "1833-03-01",
        "fecha_fin": "1833-03-18",
        "interes": "Relevamiento de rocas pizarrosas y aves endémicas.",
        "texto": "Compara capas de pizarra con cuarcitas intruidas por diques de diabasa y registra huellas de temperaturas altas en su metamorfismo. Estudia pingüinos y caranchos que conviven en colonias densas, anotando su flexibilidad alimentaria tras la introducción ganadera. Infere que los ambientes insulares moldean conjuntos mixtos de especies nativas y oportunistas, resaltando la dinámica ecológica frente a ocupaciones humanas recientes.",
        "enlaces": [
            {"label": "Aves de Malvinas", "url": "https://darwin-online.org.uk/content/frameset?itemID=F2181&pageseq=15"}
        ],
        "tags": ["geología", "zoología"],
        "coordinates": [-58.95, -51.7],
    },
    {
        "nombre": "Bahía de San Julián (Argentina)",
        "fecha_inicio": "1833-04-01",
        "fecha_fin": "1833-05-05",
        "interes": "Sedimentos patagónicos y experimentos de mareas.",
        "texto": "Realiza taladros en terrazas marinas para medir fósiles en distintos niveles y determina que el litoral ascendió lentamente tras periodos de hundimiento. Observa cómo guanacos y zorros se concentran en vegas salobres, señalando la influencia de recursos hídricos escasos en la distribución animal. Deduce que paisaje y fauna evolucionan juntos, reforzando su convicción de gradualismo ecológico.",
        "enlaces": [
            {"label": "Geología patagónica", "url": "https://darwin-online.org.uk/content/frameset?itemID=F273&pageseq=111"}
        ],
        "tags": ["geología", "ecología"],
        "coordinates": [-67.725, -49.306],
    },
    {
        "nombre": "Isla Chiloé (Chile)",
        "fecha_inicio": "1834-01-11",
        "fecha_fin": "1834-02-20",
        "interes": "Bosques templados lluviosos y actividad volcánica.",
        "texto": "Recorre los bosques valdivianos saturados de humedad y describe coigües cubiertos de epífitas mientras registra erupciones recientes del volcán Osorno. Notifica cómo deslizamientos remueven troncos y crean claros donde se suceden helechos gigantes y aves insectívoras. Concluye que la interacción entre volcanismo y sucesión vegetal ofrece un modelo acelerado de renovación paisajística.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1936&pageseq=185"}
        ],
        "tags": ["volcanismo", "botánica"],
        "coordinates": [-73.766, -42.48],
    },
    {
        "nombre": "Valparaíso y Cuenca de Santiago (Chile)",
        "fecha_inicio": "1834-03-04",
        "fecha_fin": "1834-08-14",
        "interes": "Elevación costera tras el terremoto de 1822.",
        "texto": "Inspecciona con nivel los bloques coralinos elevados que quedaron tierra adentro después del sismo de 1822 y mide cuántos centímetros superan la línea de marea viva. Entrevista a residentes que recuerdan peces quedando atrapados, usando los relatos como evidencia cronológica. Concluye que los terremotos actúan como pulsos en un proceso continuo de ascenso andino, alineado con el gradualismo de Lyell.",
        "enlaces": [
            {"label": "Observaciones geológicas", "url": "https://darwin-online.org.uk/content/frameset?itemID=F272&pageseq=141"}
        ],
        "tags": ["geología", "sismología"],
        "coordinates": [-71.612, -33.047],
    },
    {
        "nombre": "Cordillera de los Andes (Cruce Uspallata)",
        "fecha_inicio": "1834-04-18",
        "fecha_fin": "1834-05-08",
        "interes": "Fósiles marinos a gran altitud.",
        "texto": "Durante la travesía recoge fragmentos de ammonites y conchas incrustadas en calizas situadas a más de tres mil metros de altitud. Compara la inclinación de los estratos con fallas visibles que desplazan capas enteras y calcula tasas de levantamiento usando edades relativas. Confirma que cadenas montañosas pueden ser antiguas plataformas marinas elevadas lentamente, demostrando el poder acumulativo del tiempo geológico.",
        "enlaces": [
            {"label": "Notas andinas", "url": "https://darwin-online.org.uk/content/frameset?itemID=F272&pageseq=221"}
        ],
        "tags": ["geología", "paleontología"],
        "coordinates": [-69.730, -32.823],
    },
    {
        "nombre": "Lima y Callao (Perú)",
        "fecha_inicio": "1835-07-19",
        "fecha_fin": "1835-09-07",
        "interes": "Preparativos para Galápagos y estudio de costas levantadas.",
        "texto": "Mientras espera reparaciones del Beagle, examina depósitos marinos elevados cerca de Callao y mide capas de conchas trituradas a varios kilómetros tierra adentro. Visita el gabinete de historia natural de Lima para comparar sus propios especímenes con colecciones coloniales. Deduce que las costas del Pacífico experimentan levantamientos episódicos similares a Chile, lo que anticipa condiciones idóneas para observar variación insular en el siguiente tramo.",
        "enlaces": [
            {"label": "Carta a Henslow", "url": "https://darwin-online.org.uk/content/frameset?pageseq=339&itemID=F1461"}
        ],
        "tags": ["geología", "historia"],
        "coordinates": [-77.154, -12.06],
    },
    {
        "nombre": "Islas Galápagos (Ecuador)",
        "fecha_inicio": "1835-09-15",
        "fecha_fin": "1835-10-20",
        "interes": "Variación entre islas y especiación incipiente.",
        "texto": "Reúne pinzones, sinsontes y tortugas identificando cada ejemplar con la isla donde fue capturado, tras notar diferencias en picos y caparazones. Observa volcanes escoriáceos activos y campos de lava recientes que limitan la vegetación, creando microhábitats aislados. Concluye que el aislamiento insular permite diversificación a partir de ancestros comunes, idea germinal de su teoría sobre la selección natural y el origen de especies.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=403"},
            {"label": "Pinzones", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1975&pageseq=7"}
        ],
        "tags": ["biogeografía", "zoología"],
        "coordinates": [-90.438, -0.953],
    },
    {
        "nombre": "Tahití y Moorea (Polinesia Francesa)",
        "fecha_inicio": "1835-11-15",
        "fecha_fin": "1835-12-05",
        "interes": "Sociedades polinesias y arrecifes en crecimiento.",
        "texto": "Estudia los arrecifes franjeantes que rodean Tahití y observa cómo las plataformas coralinas se elevan sobre lagunas de agua tranquila. Dialoga con sacerdotes protestantes y tahitianos sobre prácticas agrícolas compartidas y toma nota de la introducción de nuevas especies comestibles. Infere que la organización social y el coral prosperan gracias a un equilibrio entre aporte humano y crecimiento natural, anticipando su teoría de atolones.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=427"}
        ],
        "tags": ["etnografía", "corales"],
        "coordinates": [-149.563, -17.537],
    },
    {
        "nombre": "Bahía de las Islas (Nueva Zelanda)",
        "fecha_inicio": "1835-12-21",
        "fecha_fin": "1836-01-04",
        "interes": "Paisajes volcánicos templados y contacto maorí.",
        "texto": "Visita misiones anglicanas y asentamientos maoríes, observando cómo cultivos de kumara conviven con bosques de kauri en suelos volcánicos drenados. Registra la rápida erosión de colinas deforestadas y su impacto en estuarios ricos en moluscos. Concluye que la introducción europea altera ciclos ecológicos frágiles, mostrando cómo la modificación cultural acelera transformaciones ambientales.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=441"}
        ],
        "tags": ["etnografía", "ecología"],
        "coordinates": [174.05, -35.22],
    },
    {
        "nombre": "Sídney (Australia)",
        "fecha_inicio": "1836-01-12",
        "fecha_fin": "1836-01-30",
        "interes": "Colonización británica y fauna marsupial.",
        "texto": "Revisa colecciones del Museo Australiano y compara marsupiales con mamíferos placentarios, destacando convergencias funcionales entre lobos y dingos. Observa el trazado geométrico de la colonia y la rapidez con que el suelo arcilloso se degrada bajo pastoreo intensivo. Deduce que la historia natural australiana exige explicar divergencias profundas a partir de un ancestro común adaptado a ambientes aislados.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=457"}
        ],
        "tags": ["zoología", "historia"],
        "coordinates": [151.209, -33.865],
    },
    {
        "nombre": "Hobart, isla de Tasmania", 
        "fecha_inicio": "1836-02-05",
        "fecha_fin": "1836-02-17",
        "interes": "Bosques templados y especies relictas.",
        "texto": "Explora bosques de eucaliptos gigantes alternados con matorrales densos donde registra monotremas y marsupiales nocturnos cazados por colonos. Observa tocones quemados y compara la regeneración vegetal tras incendios controlados por pueblos palawa con prácticas europeas. Concluye que las perturbaciones periódicas pueden sostener diversidad si respetan los ritmos ecológicos locales.",
        "enlaces": [
            {"label": "Notas de Tasmania", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1936&pageseq=251"}
        ],
        "tags": ["botánica", "ecología"],
        "coordinates": [147.327, -42.882],
    },
    {
        "nombre": "King George Sound (Australia Occidental)",
        "fecha_inicio": "1836-03-06",
        "fecha_fin": "1836-03-14",
        "interes": "Flora mediterránea austral y endemismos.",
        "texto": "Cataloga plantas con hojas duras y flores tubulares adaptadas a suelos pobres en fósforo, mientras identifica insectos polinizadores muy especializados. Observa cómo el fuego natural abre espacio a bancos de semillas persistentes y genera mosaicos de vegetación en pocos años. Entiende que el aislamiento prolongado del suroeste australiano favorece linajes únicos, reforzando el concepto de regiones biogeográficas.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=469"}
        ],
        "tags": ["botánica", "biogeografía"],
        "coordinates": [117.883, -35.023],
    },
    {
        "nombre": "Islas Cocos (Keeling)",
        "fecha_inicio": "1836-04-01",
        "fecha_fin": "1836-04-12",
        "interes": "Formación de atolones por subsidencia oceánica.",
        "texto": "Mide profundidades desde la goleta y registra cómo el arrecife coralino crece hacia arriba mientras el fondo volcánico se hunde. Analiza la granulometría de las playas para entender el ritmo de erosión y deposición que alimenta las islas bajas. Concluye que los atolones nacen de volcanes sumergidos y que la biología constructora de corales puede seguir al hundimiento, hipótesis que publicará en 1842.",
        "enlaces": [
            {"label": "Estructura de atolones", "url": "https://darwin-online.org.uk/content/frameset?itemID=F271&pageseq=279"}
        ],
        "tags": ["corales", "geología"],
        "coordinates": [96.83, -12.16],
    },
    {
        "nombre": "Mauricio (Puerto de Port Louis)",
        "fecha_inicio": "1836-04-29",
        "fecha_fin": "1836-05-09",
        "interes": "Montes basálticos y jardines botánicos.",
        "texto": "Documenta la morfología en herradura del cráter de Trou aux Cerfs y contrasta sus lavas con los basaltos de Cabo Verde, buscando patrones universales. Visita el Jardín Botánico de Pamplemousses para comparar especies antillanas naturalizadas con endemismos mauricianos. Infere que las islas volcánicas comparten procesos iniciales, pero la colonización vegetal depende de corrientes y vientos dominantes.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=483"}
        ],
        "tags": ["volcanismo", "botánica"],
        "coordinates": [57.505, -20.160],
    },
    {
        "nombre": "Ciudad del Cabo (Sudáfrica)",
        "fecha_inicio": "1836-05-31",
        "fecha_fin": "1836-06-18",
        "interes": "Reino floral del Cabo y convergencias ecológicas.",
        "texto": "Recorre el Jardín de Kirstenbosch y describe proteas, ericas y restios que ocupan nichos similares a plantas sudamericanas aunque no estén emparentadas. Observa la erosión en laderas arenosas tras la tala de bosques nativos para cultivar viñedos. Concluye que diferentes continentes generan soluciones botánicas comparables ante presiones ambientales parecidas, reforzando la noción de convergencia adaptativa.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=491"}
        ],
        "tags": ["botánica", "ecología"],
        "coordinates": [18.49, -34.35],
    },
    {
        "nombre": "Santa Elena (Atlántico sur)",
        "fecha_inicio": "1836-07-08",
        "fecha_fin": "1836-07-14",
        "interes": "Isla oceánica antigua con flora endémica.",
        "texto": "Examina columnas de basalto erosionadas y compara su mineralogía con la de lavas más jóvenes observadas en otros puertos. Recorre plantaciones reforestadas por los británicos y evalúa cómo especies exóticas desplazan a la vegetación endémica de zonas húmedas. Concluye que la larga historia aislada de la isla generó organismos exclusivos, vulnerables a la intervención humana acelerada.",
        "enlaces": [
            {"label": "Notas de Santa Elena", "url": "https://darwin-online.org.uk/content/frameset?itemID=F271&pageseq=313"}
        ],
        "tags": ["geología", "biogeografía"],
        "coordinates": [-5.7, -15.95],
    },
    {
        "nombre": "Isla Ascensión", 
        "fecha_inicio": "1836-07-19",
        "fecha_fin": "1836-07-23",
        "interes": "Colonización biológica en suelos volcánicos jóvenes.",
        "texto": "Analiza conos de escoria recientes y registra cómo musgos y líquenes colonizan grietas protegidas, seguidos por gramíneas llevadas por guarniciones británicas. Observa fragatas y trópicos que nidifican en acantilados expuestos al viento, ajustando sus ciclos al recurso marino. Infere que la dispersión a larga distancia basta para poblar islas remotas si existen microhábitats disponibles.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=499"}
        ],
        "tags": ["ecología", "volcanismo"],
        "coordinates": [-14.37, -7.93],
    },
    {
        "nombre": "Falmouth (regreso)",
        "fecha_inicio": "1836-10-02",
        "fecha_fin": "1836-10-02",
        "interes": "Cierre de la circunnavegación y recopilación científica.",
        "texto": "Desembarca en Falmouth con 12 cuadernos de campo, 1 529 especímenes en alcohol y centenares de rocas etiquetadas por origen. Revisa los instrumentos de medición para verificar su deriva tras casi cinco años y anota correcciones que permitirán interpretar los datos con rigor. Comprende que la síntesis de estas colecciones transformará la historia natural británica y abre la puerta a nuevas teorías evolutivas.",
        "enlaces": [
            {"label": "Diario", "url": "https://darwin-online.org.uk/content/frameset?itemID=F1909&pageseq=511"}
        ],
        "tags": ["fin", "historia"],
        "coordinates": [-5.071, 50.154],
    },
]

allowed_tags = {"geología", "paleontología", "biogeografía", "botánica", "zoología", "ecología", "sismología", "volcanismo", "corales", "etnografía", "historia", "fin", "inicio"}

converted_features = []
for original in features:
    texto = " ".join(original["texto"].split())
    length = len(texto)
    if not (300 <= length <= 600):
        raise ValueError(f"Texto fuera de rango para {original['nombre']}: {length} caracteres")
    fecha_inicio = datetime.strptime(original["fecha_inicio"], "%Y-%m-%d")
    fecha_fin = datetime.strptime(original["fecha_fin"], "%Y-%m-%d")
    if fecha_inicio > fecha_fin:
        raise ValueError(f"Fechas fuera de orden en {original['nombre']}")
    for tag in original["tags"]:
        if tag not in allowed_tags:
            raise ValueError(f"Tag no permitido {tag} en {original['nombre']}")
    lon, lat = original["coordinates"]
    if not (-180 <= lon <= 180 and -90 <= lat <= 90):
        raise ValueError(f"Coordenadas fuera de rango en {original['nombre']}")
    feature = {
        "type": "Feature",
        "properties": {
            "nombre": original["nombre"],
            "fecha_inicio": original["fecha_inicio"],
            "fecha_fin": original["fecha_fin"],
            "interes": original["interes"],
            "texto": texto,
            "enlaces": original.get("enlaces", []),
            "tags": original["tags"],
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat],
        },
    }
    converted_features.append(feature)

collection = {"type": "FeatureCollection", "features": converted_features}

with open("beagle.geojson", "w", encoding="utf-8") as fh:
    json.dump(collection, fh, ensure_ascii=False, indent=2)
