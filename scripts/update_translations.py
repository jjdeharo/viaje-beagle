import json
from pathlib import Path


def normalize_text(value):
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        return {k: normalize_text(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize_text(v) for v in value]
    return value


def merge_with_spanish(spanish_value, extras):
    merged = {"es": spanish_value or ""}
    merged.update(extras)
    return normalize_text(merged)


translations = {
    "Plymouth (zarpe)": {
        "nombre": {
            "ca": "Plymouth (salpada)",
            "gl": "Plymouth (saída)",
            "eu": "Plymouth (irteera)",
            "en": "Plymouth (departure)"
        },
        "interes": {
            "ca": "Inici del viatge i calibratge dels instruments.",
            "gl": "Inicio da viaxe e calibración dos instrumentos.",
            "eu": "Bidaiaren hasiera eta tresnen kalibrazioa.",
            "en": "Start of the voyage and instrument calibration."
        },
        "texto": {
            "ca": "Darwin s'embarca a l'HMS Beagle i acompanya el capità FitzRoy en la verificació de sextants, cronòmetres i baròmetres abans d'abandonar el port. Observa com els naturalistes anteriors van deixar anotacions sobre les marees i les compara amb les seves pròpies mesures. Conclou que el grau de precisió assolit permetrà convertir observacions locals en teories globals sobre canvis geològics i distribució d'espècies.",
            "gl": "Darwin embarca no HMS Beagle e acompaña ao capitán FitzRoy na verificación de sextantes, cronómetros e barómetros antes de deixar o porto. Observa como os naturalistas anteriores deixaron notas sobre as mareas e compáraas coas súas propias medicións. Conclúe que o grao de precisión acadado permitirá converter observacións locais en teorías globais sobre cambios xeolóxicos e distribución das especies.",
            "eu": "Darwin HMS Beagle ontzian ontziratu eta FitzRoy kapitainarekin batera portua utzi aurretik sextanteak, kronometroak eta barometroak egiaztatzen ditu. Aurreko naturalistek mareei buruz utzitako oharrak ikusten ditu eta bere neurketekin alderatzen ditu. Ondorioztatzen du lortutako zehaztasunak tokiko behaketak aldaketa geologikoei eta espezieen banaketari buruzko teoria orokorretan bihurtzea ahalbidetuko duela.",
            "en": "Darwin boards HMS Beagle and joins Captain FitzRoy in checking sextants, chronometers, and barometers before the ship leaves port. He notes how earlier naturalists left records of the tides and compares them with his own measurements. He concludes that the precision achieved will allow local observations to be turned into global theories about geological change and species distribution."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol I",
                    "gl": "Diario, capítulo I",
                    "eu": "Egunkaria, I. kapitulua",
                    "en": "Journal, Chapter I"
                }
            }
        ]
    },
    "Porto Praya, Santiago (Cabo Verde)": {
        "nombre": {
            "ca": "Porto Praya, Santiago (Cap Verd)",
            "gl": "Porto Praya, Santiago (Cabo Verde)",
            "eu": "Porto Praya, Santiago (Cabo Verde)",
            "en": "Porto Praya, Santiago (Cape Verde)"
        },
        "interes": {
            "ca": "Estrats volcànics escalonats i nivell marí fòssil.",
            "gl": "Estratos volcánicos escalonados e nivel mariño fósil.",
            "eu": "Mailakatutako estratu bolkanikoak eta itsas maila fosila.",
            "en": "Stepped volcanic strata and fossil shoreline."
        },
        "texto": {
            "ca": "Als penya-segats de Porto Praya distingeix coixins de lava negra superposats a bancs de conquilles cimentades que s'eleven diversos metres per sobre del mar actual. Interpreta les terrasses com a evidència d'enfonsaments lents seguits d'aixecaments successius, descartant les erupcions aïllades com a explicació completa. Comprèn que la història volcànica es pot llegir com una cronologia gradual, idea clau per a la seva geologia comparada.",
            "gl": "Nos cantís de Porto Praya distingue almofadas de lava negra superpostas a bancos de cunchas cementadas que se elevan varios metros sobre o mar actual. Interpreta as terrazas como evidencia de afundimentos lentos seguidos de levantamentos sucesivos, descartando as erupcións illadas como explicación completa. Comprende que a historia volcánica pode lerse como unha cronoloxía gradual, idea clave para a súa xeoloxía comparada.",
            "eu": "Porto Prayako haitzarteetan, itsas maila aktuala baino metro batzuk gorago altxatzen diren maskor zementatuen gainean pilatutako lava beltzeko oheak bereizten ditu. Terrazak hondoratze geldoen eta ondorengo altxaldi jarraien ebidentzia gisa interpretatzen ditu, eta erupzio bakarrek ezin dutela guztia azaldu ondorioztatzen du. Ulertzen du historia bolkanikoa kronologia gradual gisa irakur daitekeela, eta hori bere geologia konparaturako ideia giltzarria dela.",
            "en": "Along the cliffs of Porto Praya he distinguishes pillows of black lava resting on cemented shell banks that rise several metres above the present sea. He interprets the terraces as evidence of slow subsidences followed by successive uplifts, ruling out single eruptions as a full explanation. He understands that volcanic history can be read as a gradual chronology, a key idea for his comparative geology."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol I",
                    "gl": "Diario, capítulo I",
                    "eu": "Egunkaria, I. kapitulua",
                    "en": "Journal, Chapter I"
                }
            }
        ]
    },
    "Salvador de Bahía (Brasil)": {
        "nombre": {
            "ca": "Salvador de Bahia (Brasil)",
            "gl": "Salvador de Baía (Brasil)",
            "eu": "Salvador de Bahía (Brasil)",
            "en": "Salvador da Bahia (Brazil)"
        },
        "interes": {
            "ca": "Bosc tropical com a laboratori d'adaptació.",
            "gl": "Bosque tropical como laboratorio de adaptación.",
            "eu": "Oihan tropikala moldaketaren laborategi gisa.",
            "en": "Tropical forest as an adaptation laboratory."
        },
        "texto": {
            "ca": "Recorre la mata atlàntica i documenta lianes, epífites i manglars que ocupen nínxols superposats en diferents estrats de llum. Anota com la profusió d'insectes pol·linitzadors es correspon amb flors especialitzades i compara la distribució d'arrels aèries amb sòls entollats. Dedueix que la competència pels recursos modela morfologies convergents i que els tròpics ofereixen proves vives d'una selecció natural incipient.",
            "gl": "Percorre a mata atlántica e documenta lianas, epífitas e manglares que ocupan nichos superpostos en distintos estratos de luz. Anota como a profusión de insectos polinizadores corresponde con flores especializadas e compara a distribución de raíces aéreas con solos enchoupados. Deduce que a competencia polos recursos modela morfoloxías converxentes e que os trópicos ofrecen probas vivas dunha selección natural incipiente.",
            "eu": "Atlantikoko oihana zeharkatzen du eta hainbat argi geruzatan gainjarritako habitata betetzen duten lianak, epifitoak eta mangladiak dokumentatzen ditu. Polinizatzaile ugaritasunak lore espezializatuekin duen lotura zehatza idazten du eta sustrai airetako banaketa lur bustiekin alderatzen du. Ondorioztatzen du baliabideekiko lehiak morfologia konbergenteak moldatzen dituela eta tropikoek hautespen natural hasiberriaren froga biziak eskaintzen dituztela.",
            "en": "He traverses the Atlantic forest and records lianas, epiphytes, and mangroves occupying stacked niches across different layers of light. He notes how the profusion of pollinating insects matches specialised flowers and compares the distribution of aerial roots with waterlogged soils. He deduces that competition for resources shapes convergent morphologies and that the tropics provide living evidence of nascent natural selection."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol I",
                    "gl": "Diario, capítulo I",
                    "eu": "Egunkaria, I. kapitulua",
                    "en": "Journal, Chapter I"
                }
            }
        ]
    },
    "Río de Janeiro (Brasil)": {
        "nombre": {
            "ca": "Rio de Janeiro (Brasil)",
            "gl": "Río de Xaneiro (Brasil)",
            "eu": "Rio de Janeiro (Brasil)",
            "en": "Rio de Janeiro (Brazil)"
        },
        "interes": {
            "ca": "Mostreig sistemàtic de la fauna i la flora de la mata.",
            "gl": "Mostraxe sistemática da fauna e flora da mata.",
            "eu": "Fauna eta floraren laginketa sistematikoa mata atlantikoan.",
            "en": "Systematic sampling of forest fauna and flora."
        },
        "texto": {
            "ca": "Instal·la estacions de mostreig a diferents altituds del bosc carioca i compara escarabats, ocells i bromèlies entre clarianes i ombra tancada. Observa que petits canvis d'humitat generen reemplaços ràpids d'espècies i reflexiona sobre l'avantatge de caràcters que faciliten la partició de l'hàbitat. Conclou que la diversitat tropical s'explica per variacions graduals i no per creacions independents, reforçant la seva visió sobre la unitat de tipus.",
            "gl": "Instala estacións de mostraxe en diferentes alturas do bosque carioca e compara escaravellos, aves e bromelias entre claros e sombra pechada. Observa que pequenos cambios de humidade xeran substitucións rápidas de especies e reflexiona sobre a vantaxe de caracteres que facilitan a partición do hábitat. Conclúe que a diversidade tropical se explica por variacións graduais e non por creacións independentes, reforzando a súa visión sobre a unidade de tipo.",
            "eu": "Basoko altuera desberdinetan laginketa estazioak ezartzen ditu eta bareal, txori eta bromelia laginak alderatzen ditu argi guneen eta itzal trinkoaren artean. Hezetasuneko aldaketa txikiek espezieen ordezkapen azkarrak sortzen dituztela ikusten du eta habitataren banaketa errazten duten ezaugarrien abantailaz hausnartzen du. Ondorioztatzen du dibertsitate tropikala aldaketa gradualen emaitza dela eta ez sormen independenteena, eta horrek bere unitate motaren ikuspegia sendotzen du.",
            "en": "He sets up sampling stations at different elevations of the Carioca forest and compares beetles, birds, and bromeliads in clearings versus closed shade. He observes that slight shifts in humidity trigger rapid species turnover and reflects on the advantage of traits that ease habitat partitioning. He concludes that tropical diversity is explained by gradual variations rather than separate creations, reinforcing his view of a unity of type."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol II",
                    "gl": "Diario, capítulo II",
                    "eu": "Egunkaria, II. kapitulua",
                    "en": "Journal, Chapter II"
                }
            }
        ]
    },
    "Montevideo (Uruguay)": {
        "nombre": {
            "ca": "Montevideo (Uruguai)",
            "gl": "Montevideo (Uruguai)",
            "eu": "Montevideo (Uruguai)",
            "en": "Montevideo (Uruguay)"
        },
        "interes": {
            "ca": "Base per a expedicions paleontològiques a la pampa.",
            "gl": "Base para expedicións paleontolóxicas na pampa.",
            "eu": "Pampa aldeko espedizio paleontologikoetarako basea.",
            "en": "Base for palaeontological expeditions in the Pampas."
        },
        "texto": {
            "ca": "Des de Montevideo organitza sortides cap a l'interior pampeà i estableix correspondència logística amb naturalistes britànics. Documenta com els estancers troben ossos gegants a barrancs fluvials i planifica la seva extracció acurada amb motlles de guix. Reconeix que la proximitat entre restes fòssils i fauna actual suggereix reemplaços graduals, clau per qüestionar l'extinció cataclísmica immediata.",
            "gl": "Desde Montevideo organiza saídas cara ao interior pampeano e establece correspondencia loxística con naturalistas británicos. Documenta como os estancieiros atopan ósos xigantes en barrancos fluviais e planifica a súa extracción coidadosa con moldes de xeso. Recoñece que a proximidade entre restos fósiles e fauna actual suxire substitucións graduais, clave para cuestionar a extinción cataclísmica inmediata.",
            "eu": "Montevidiotik pampako barnealdera espedizioak antolatzen ditu eta natur zientzialari britainiarrekin koordinazio logistikoa ezartzen du. Estantzieroek ibaiertzeko labarretan aurkitzen dituzten hezur erraldoiak dokumentatzen ditu eta haien ateratze arretatsua igeltsuzko moldeekin planifikatzen du. Fosil arrastoen eta gaur egungo faunaren arteko hurbiltasunak ordezkapen gradualak iradokitzen dituela onartzen du, berehalako hondamendiaren ideia zalantzan jartzeko funtsezkoa.",
            "en": "From Montevideo he organises journeys into the Pampas interior and establishes logistic correspondence with British naturalists. He records how ranchers uncover giant bones in riverbank cliffs and plans their careful extraction using plaster casts. He recognises that the closeness of fossil remains to living fauna suggests gradual replacements, a key argument against sudden cataclysmic extinction."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol III",
                    "gl": "Diario, capítulo III",
                    "eu": "Egunkaria, III. kapitulua",
                    "en": "Journal, Chapter III"
                }
            }
        ]
    },
    "Punta Alta y Bahía Blanca (Argentina)": {
        "nombre": {
            "ca": "Punta Alta i Bahía Blanca (Argentina)",
            "gl": "Punta Alta e Bahía Blanca (Arxentina)",
            "eu": "Punta Alta eta Bahía Blanca (Argentina)",
            "en": "Punta Alta and Bahía Blanca (Argentina)"
        },
        "interes": {
            "ca": "Megafauna plistocena en estrats marins.",
            "gl": "Megafauna pleistocena en estratos mariños.",
            "eu": "Pleistozenoko megafauna geruza itsastarretan.",
            "en": "Pleistocene megafauna in marine strata."
        },
        "texto": {
            "ca": "Excava dents i closques de gliptodonts al costat de fustes semicabonitzades en penya-segats costaners. Nota que les capes fòssils s'alternen amb dipòsits marins recents, fet que implica que els gegants terrestres van viure fins a temps molt pròxims. Dedueix que l'extinció podria estar relacionada amb canvis ambientals graduals i no amb diluvis puntuals, recolzant la mutabilitat lenta dels ecosistemes.",
            "gl": "Escava dentes e caparazóns de gliptodontes xunto a madeiras semicabonizadas en cantís costeiros. Nota que as capas fósiles se alternan con depósitos mariños recentes, o que implica que os xigantes terrestres viviron ata tempos moi próximos. Deduce que a extinción puido relacionarse con cambios ambientais graduais e non con diluvios puntuais, apoiando a mutabilidade lenta dos ecosistemas.",
            "eu": "Gliptodontoen hortzak eta oskolak erdi erretako egur zatiekin batera ateratzen ditu kostaldeko labarretan. Fosilen geruzak itsas metakin berriekin txandakatzen direla ohartzen da, lurreko erraldoiak oso garai hurbilera arte bizi izan zirela adieraziz. Ondorioztatzen du desagerpena ingurumen aldaketa gradualekin lotuta egon zitekeela eta ez uholde bakarrekin, ekosistemen aldakortasun motelea babestuz.",
            "en": "He excavates glyptodont teeth and carapaces alongside half-charred woods in coastal cliffs. He notes that the fossil beds alternate with recent marine deposits, implying that the land giants lived until very recent times. He deduces that their extinction was tied to gradual environmental shifts rather than sudden deluges, supporting the slow mutability of ecosystems."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol IV",
                    "gl": "Diario, capítulo IV",
                    "eu": "Egunkaria, IV. kapitulua",
                    "en": "Journal, Chapter IV"
                }
            }
        ]
    },
    "Canal Beagle y Tierra del Fuego": {
        "nombre": {
            "ca": "Canal Beagle i Terra del Foc",
            "gl": "Canle Beagle e Terra do Lume",
            "eu": "Beagle kanala eta Suaren Lurra",
            "en": "Beagle Channel and Tierra del Fuego"
        },
        "interes": {
            "ca": "Observació etnogràfica i adaptació al fred extrem.",
            "gl": "Observación etnográfica e adaptación ao frío extremo.",
            "eu": "Etnografia behaketa eta hotz muturrean egokitzapena.",
            "en": "Ethnographic observation and adaptation to extreme cold."
        },
        "texto": {
            "ca": "Conviu amb yamans reembarcats per FitzRoy i registra com la seva vestimenta mínima contrasta amb l'eficàcia de les seves canoes en aigües gelades. Analitza la distribució de molses i líquens sobre roques granítiques exposades al vent i relaciona l'escassa flora amb les estratègies de subsistència fuegina. Conclou que cultura i biologia coevolucionen amb el clima, una evidència empírica contra la idea de races fixes i immutables.",
            "gl": "Convive con yámanas reembarcados por FitzRoy e rexistra como a súa vestimenta mínima contrasta coa eficacia das súas canoas en augas xeadas. Analiza a distribución de musgos e líquenes sobre rochas graníticas expostas ao vento e relaciona a escasa flora coas estratexias de subsistencia fueguinas. Conclúe que cultura e bioloxía coevolucionan co clima, evidencia empírica contra a idea de razas fixas e inmutables.",
            "eu": "FitzRoyalek berriro ontziratutako yámanaekin bizi da eta euren jantzi xumeak nola kontrastatzen duten ur izoztuetako kanoen eraginkortasunarekin jasotzen du. Haizearen menpe dauden granitozko arroketan goroldio eta likenen banaketa aztertzen du eta landaredi urria fuegianoko biziraupen estrategiekin lotzen du. Ondorioztatzen du kultura eta biologia klimarekin batera eboluzionatzen dutela, arraza finko eta aldaezinen ideiaren aurkako ebidentzia enpirikoa.",
            "en": "He lives alongside Yaghan people re-embarked by FitzRoy and records how their minimal clothing contrasts with the efficiency of their canoes in freezing waters. He analyses the spread of mosses and lichens on wind-exposed granite rocks and links the sparse flora to Fuegian subsistence strategies. He concludes that culture and biology co-evolve with climate, empirical evidence against the notion of fixed immutable races."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol X",
                    "gl": "Diario, capítulo X",
                    "eu": "Egunkaria, X. kapitulua",
                    "en": "Journal, Chapter X"
                }
            }
        ]
    },
    "Islas Malvinas (Port Louis)": {
        "nombre": {
            "ca": "Illes Malvines (Port Louis)",
            "gl": "Illas Malvinas (Port Louis)",
            "eu": "Malvinak uharteak (Port Louis)",
            "en": "Falkland Islands (Port Louis)"
        },
        "interes": {
            "ca": "Reconeixement de roques pissarroses i aus endèmiques.",
            "gl": "Levantamento de rochas lousentas e aves endémicas.",
            "eu": "Arbel harrien azterketa eta bertako hegaztiak.",
            "en": "Survey of slate rocks and endemic birds."
        },
        "texto": {
            "ca": "Compara capes de pissarra amb quarsites intruïdes per diques de diabases i registra senyals de temperatures elevades en el seu metamorfisme. Estudia pingüins i caranchos que conviuen en colònies denses, i anota la seva flexibilitat alimentària després de la introducció ramadera. Infereix que els ambients insulars modelen conjunts mixtes d'espècies natives i oportunistes, ressaltant la dinàmica ecològica davant d'ocupacions humanes recents.",
            "gl": "Compara capas de lousa con cuarcitas intruídas por diques de diabasa e rexistra sinais de altas temperaturas no seu metamorfismo. Estuda pingüíns e caranchos que conviven en colonias densas, anotando a súa flexibilidade alimentaria tras a introdución gandeira. Infire que os ambientes insulares moldean conxuntos mixtos de especies nativas e oportunistas, salientando a dinámica ecolóxica fronte a ocupacións humanas recentes.",
            "eu": "Arbel geruzak diabasaz egindako diqueek zeharkatutako kuartzitekin alderatzen ditu eta metamorfismoan tenperatura handien aztarnak erregistratzen ditu. Pinguinoak eta karanxoak kolonia trinkoetan nola bizi diren aztertzen du, eta abeltzaintzaren sarreraren ondoren duten elikadura malgutasuna idazten du. Ondorioztatzen du uharte inguruneek espezie autoktonen eta oportunisten nahasketa moldatzen dutela, gizakiaren azken okupazioen aurrean dinamika ekologikoa azpimarratuz.",
            "en": "He compares slate beds with quartzites cut by diabase dykes and notes traces of high temperatures in their metamorphism. He studies penguins and caranchos sharing dense colonies, recording their dietary flexibility after livestock was introduced. He infers that island environments shape mixed assemblies of native and opportunistic species, highlighting ecological dynamics in the face of recent human occupations."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol IX",
                    "gl": "Diario, capítulo IX",
                    "eu": "Egunkaria, IX. kapitulua",
                    "en": "Journal, Chapter IX"
                }
            }
        ]
    },
    "Bahía de San Julián (Argentina)": {
        "nombre": {
            "ca": "Badia de San Julián (Argentina)",
            "gl": "Baía de San Julián (Arxentina)",
            "eu": "San Julián badia (Argentina)",
            "en": "San Julián Bay (Argentina)"
        },
        "interes": {
            "ca": "Sediments patagònics i experiments de marees.",
            "gl": "Sedimentos patagónicos e experimentos de mareas.",
            "eu": "Patagoniako sedimentuak eta mareen esperimentuak.",
            "en": "Patagonian sediments and tide experiments."
        },
        "texto": {
            "ca": "Realitza perforacions a terrasses marines per mesurar fòssils a diferents nivells i determina que el litoral va ascendir lentament després de períodes d'enfonsament. Observa com guanacs i guineus es concentren en pradells salobrosos, indicant la influència dels escassos recursos hídrics en la distribució animal. Dedueix que paisatge i fauna evolucionen plegats, reforçant la seva convicció en el gradualisme ecològic.",
            "gl": "Realiza perforacións en terrazas mariñas para medir fósiles en distintos niveis e determina que o litoral ascendeu lentamente tras períodos de afundimento. Observa como guanacos e raposos se concentran en veigas salobres, sinalando a influencia dos escasos recursos hídricos na distribución animal. Deduce que paisaxe e fauna evolucionan xuntos, reforzando a súa convicción no gradualismo ecolóxico.",
            "eu": "Kostaldeko terrazetan zulaketak egiten ditu maila desberdinetan dauden fosilak neurtzeko eta hondoratze aldien ondoren kostaldea poliki igo dela ondorioztatzen du. Guanakoek eta azeriek zelai gazietan pilatzen direla ikusten du, baliabide hidriko urriek animalien banaketan duten eragina azpimarratuz. Ondorioztatzen du paisaia eta fauna elkarrekin eboluzionatzen dutela, gradualismo ekologikoaren konbikzioa sendotuz.",
            "en": "He drills marine terraces to measure fossils at different levels and determines that the shoreline rose slowly after periods of subsidence. He notices guanacos and foxes clustering in salty meadows, highlighting the influence of scarce water resources on animal distribution. He concludes that landscape and fauna evolve together, reinforcing his commitment to ecological gradualism."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol VIII",
                    "gl": "Diario, capítulo VIII",
                    "eu": "Egunkaria, VIII. kapitulua",
                    "en": "Journal, Chapter VIII"
                }
            }
        ]
    },
    "Isla Chiloé (Chile)": {
        "nombre": {
            "ca": "Illa de Chiloé (Xile)",
            "gl": "Illa de Chiloé (Chile)",
            "eu": "Chiloé uhartea (Txile)",
            "en": "Chiloé Island (Chile)"
        },
        "interes": {
            "ca": "Boscos temperats plujosos i activitat volcànica.",
            "gl": "Bosques temperados chuviosos e actividade volcánica.",
            "eu": "Oihan epel euritsuak eta jarduera bolkanikoa.",
            "en": "Rainy temperate forests and volcanic activity."
        },
        "texto": {
            "ca": "Registra tales extensives per construir esglésies de fusta amb tècniques missionals i avalua com l'extracció altera aiguamolls torbosos. Descriu la cendra recent dipositada després d'erupcions andines i el seu impacte en els conreus insulars. Conclou que els habitants depenen d'una gestió acurada del bosc per equilibrar economia i resiliència ecològica.",
            "gl": "Rexistra tallas extensivas para construír igrexas de madeira con técnicas misionais e avalía como a extracción altera humidais turbosos. Describe a cinza recente depositada tras erupcións andinas e o seu impacto nos cultivos insulares. Conclúe que os habitantes dependen dunha xestión coidadosa do bosque para equilibrar economía e resiliencia ecolóxica.",
            "eu": "Egurrezko elizak eraikitzeko misiolarien teknikekin egindako zuhaitz mozketak jasotzen ditu eta erauzketak zingira turbak nola aldatzen dituen baloratzen du. Andeetako erupzioen ondoren eroritako errautsa eta uharteetako laboreetan duen eragina deskribatzen du. Ondorioztatzen du bertakoek basoaren kudeaketa arduratsuaren mende daudela ekonomia eta erresilientzia ekologikoa orekatzeko.",
            "en": "He records extensive logging to build wooden churches with missionary techniques and assesses how timber extraction alters peat wetlands. He describes the fresh ash deposited after Andean eruptions and its impact on island crops. He concludes that the inhabitants rely on careful forest management to balance the economy with ecological resilience."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XIII",
                    "gl": "Diario, capítulo XIII",
                    "eu": "Egunkaria, XIII. kapitulua",
                    "en": "Journal, Chapter XIII"
                }
            }
        ]
    },
    "Valparaíso y Cuenca de Santiago (Chile)": {
        "nombre": {
            "ca": "Valparaíso i conca de Santiago (Xile)",
            "gl": "Valparaíso e conca de Santiago (Chile)",
            "eu": "Valparaíso eta Santiagoko arroa (Txile)",
            "en": "Valparaíso and Santiago Basin (Chile)"
        },
        "interes": {
            "ca": "Cronologia de terratrèmols i aixecaments costaners.",
            "gl": "Cronoloxía de terremotos e levantamentos costeiros.",
            "eu": "Lurrikaren eta kostaldeko gorakadaren kronologia.",
            "en": "Chronology of earthquakes and coastal uplifts."
        },
        "texto": {
            "ca": "Recull testimonis dels sismes de 1822 i 1835, comparant els nivells dels murs portuaris abans i després de cada esdeveniment. Observa platges elevades acabades d'exposar i les cartografia juntament amb blocs coral·lins ara emergits. Proposa que els terratrèmols actuen per polsos, elevant trams de costa en successions graduals, cosa que reforça la seva teoria d'un aixecament andí continuat.",
            "gl": "Recopila testemuños dos sismos de 1822 e 1835, comparando os niveis dos muros portuarios antes e despois de cada evento. Observa praias elevadas recentemente expostas e cartografíaas xunto con bloques coralinos agora en seco. Propón que os terremotos actúan por pulsos, elevando tramos de costa en sucesións graduais, o que avala a súa teoría dun levantamento andino continuo.",
            "eu": "1822 eta 1835eko lurrikaren testigantzak biltzen ditu eta portuko hormen mailak konparatzen ditu gertaera bakoitzaren aurretik eta ondoren. Azalera berrian agertutako hondartza altxatuak ikusten ditu eta gaur egun lehorrera ateratako koralezko blokeekin batera mapatzen ditu. Proposatzen du lurrikarak pultsu bidez jarduten dutela, kostalde zatien gorakada gradualak eraginez eta horrek Andeetako etengabeko altxaldiaren teoria sendotzen du.",
            "en": "He gathers accounts of the 1822 and 1835 earthquakes, comparing the levels of harbour walls before and after each event. He observes freshly exposed raised beaches and maps them alongside coral blocks now stranded on land. He proposes that earthquakes work in pulses, lifting stretches of coast in gradual sequences, supporting his theory of continuous Andean uplift."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XII",
                    "gl": "Diario, capítulo XII",
                    "eu": "Egunkaria, XII. kapitulua",
                    "en": "Journal, Chapter XII"
                }
            }
        ]
    },
    "Cordillera de los Andes (Cruce Uspallata)": {
        "nombre": {
            "ca": "Serralada dels Andes (pas d'Uspallata)",
            "gl": "Cordilleira dos Andes (Paso Uspallata)",
            "eu": "Andeetako mendikatea (Uspallata igarobidea)",
            "en": "Andes Range (Uspallata crossing)"
        },
        "interes": {
            "ca": "Estrats marins elevats i fòssils andins.",
            "gl": "Estratos mariños elevados e fósiles andinos.",
            "eu": "Goratutako itsas geruzak eta Andeetako fosilak.",
            "en": "Raised marine strata and Andean fossils."
        },
        "texto": {
            "ca": "Creua la serralada en ple estiu austral i recol·lecta ammonits a més de 3 000 metres, demostrant antics fons marins. Analitza vetes de guix i sal en capes plegades, inferint pressions tectòniques sostingudes durant llargs intervals. Conclou que les muntanyes s'han elevat lentament mentre conservaven signes del seu origen oceànic.",
            "gl": "Atraviesa a cordilleira en pleno verán austral e recolle ammonites a máis de 3 000 metros, demostrando antigos fondos mariños. Analiza vetas de xeso e sal en capas pregadas, inferindo presións tectónicas mantidas durante longos intervalos. Conclúe que as montañas se elevaron lentamente mentres conservaban sinais da súa orixe oceánica.",
            "eu": "Hego hemisferioko udan mendikatea zeharkatzen du eta 3 000 metro baino gorago ammoniteak biltzen ditu, antzinako itsas hondoak agerian utziz. Igeltso eta gatz betetako zainak aztertzen ditu geruza tolestuetan, luzaroan iraun duten presio tektonikoak ondorioztatuz. Ondorioztatzen du mendiak poliki goratu direla jatorri ozeanikoko aztarnak mantenduz.",
            "en": "He crosses the range in the southern summer and collects ammonites above 3,000 metres, proof of ancient sea floors. He analyses veins of gypsum and salt in folded beds, inferring tectonic pressures sustained over long intervals. He concludes that the mountains rose slowly while preserving traces of their oceanic origin."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XV",
                    "gl": "Diario, capítulo XV",
                    "eu": "Egunkaria, XV. kapitulua",
                    "en": "Journal, Chapter XV"
                }
            }
        ]
    },
    "Lima y Callao (Perú)": {
        "nombre": {
            "ca": "Lima i Callao (Perú)",
            "gl": "Lima e Callao (Perú)",
            "eu": "Lima eta Callao (Peru)",
            "en": "Lima and Callao (Peru)"
        },
        "interes": {
            "ca": "Corrents oceàniques fredes i deserts costaners.",
            "gl": "Correntes oceánicas frías e desertos costeiros.",
            "eu": "Itsas korronte hotzak eta kostaldeko basamortuak.",
            "en": "Cold ocean currents and coastal deserts."
        },
        "texto": {
            "ca": "Descriu l'efecte de l'anticicló del Pacífic Sud que refreda el litoral i crea boires que limiten l'agricultura en sòls àrids. Registra com el guano sosté fertilitzants per als valls interiors i calcula l'impacte econòmic de l'exportació. Conclou que el clima costaner peruà depèn d'equilibris atmosfèrics fràgils capaços d'alterar tant els ecosistemes marins com els humans.",
            "gl": "Describe o efecto do anticiclón do Pacífico Sur que arrefría o litoral, creando brétemas que limitan a agricultura en solos áridos. Rexistra como o guano sustenta fertilizantes para vales interiores e calcula o impacto económico da súa exportación. Conclúe que o clima costeiro peruano depende de equilibrios atmosféricos fráxiles capaces de alterar tanto os ecosistemas mariños como os humanos.",
            "eu": "Hego Pazifikoko antisikloiak kostaldea nola hozten duen azaltzen du, lur lehorrak laino hezeekin estaliz eta nekazaritza mugatuz. Ganoak barne haranetarako ongarriak nola hornitzen dituen jasotzen du eta esportazioaren eragin ekonomikoa kalkulatzen du. Ondorioztatzen du Peruko kostaldeko klima oreka atmosferiko ahulen mende dagoela, eta horiek itsas zein gizaki ekosistemak alda ditzaketela.",
            "en": "He describes how the South Pacific anticyclone cools the coast, creating fogs that limit agriculture on arid soils. He records how guano sustains fertilisers for inland valleys and estimates the economic impact of its export. He concludes that Peru’s coastal climate depends on fragile atmospheric balances capable of altering both marine and human ecosystems."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XVI",
                    "gl": "Diario, capítulo XVI",
                    "eu": "Egunkaria, XVI. kapitulua",
                    "en": "Journal, Chapter XVI"
                }
            }
        ]
    },
    "Islas Galápagos (Ecuador)": {
        "nombre": {
            "ca": "Illes Galápagos (Equador)",
            "gl": "Illas Galápagos (Ecuador)",
            "eu": "Galapago uharteak (Ekuador)",
            "en": "Galápagos Islands (Ecuador)"
        },
        "interes": {
            "ca": "Variació entre illes i dinàmica de colonització.",
            "gl": "Variación entre illas e dinámica de colonización.",
            "eu": "Uharteen arteko aldakortasuna eta kolonizazio dinamika.",
            "en": "Variation among islands and colonisation dynamics."
        },
        "texto": {
            "ca": "Compara pinsans, tortugues i cactus d'illes veïnes i descobreix diferències subtils associades als microhàbitats. Etiqueta els espècimens per illa i anota com cada població explota recursos diferents, des de fruits espinosos fins a llavors dures. Posa les bases de la seva teoria de la divergència adaptativa a partir de colonitzacions seqüencials.",
            "gl": "Compara pimpíns, tartarugas e cactus de illas veciñas e descobre diferenzas sutís asociadas a microhábitats. Etiqueta os espécimes por illa e anota como cada poboación explota recursos distintos, desde froitos espiñosos ata sementes duras. Senta as bases da súa teoría da diverxencia adaptativa a partir de colonizacións secuenciais.",
            "eu": "Aldamioetako uharteetako pinzoiak, dortokak eta kaktusak alderatzen ditu eta mikrohabitatekin lotutako alde sotilak aurkitzen ditu. Espezie bakoitza uhartearen arabera etiketatzen du eta nola populazioek baliabide ezberdinak ustiatzen dituzten ohartarazten du, fruitu arantzadunetatik hazi gogorretaraino. Kolonizazio sekuentzialetan oinarritutako dibergentzia moldakorraren teoriaren oinarriak ezartzen ditu.",
            "en": "He compares finches, tortoises, and cacti from neighbouring islands and uncovers subtle differences tied to microhabitats. He labels specimens by island and notes how each population exploits different resources, from spiny fruits to hard seeds. He lays the groundwork for his theory of adaptive divergence driven by sequential colonisations."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XVII",
                    "gl": "Diario, capítulo XVII",
                    "eu": "Egunkaria, XVII. kapitulua",
                    "en": "Journal, Chapter XVII"
                }
            }
        ]
    },
    "Tahití y Moorea (Polinesia Francesa)": {
        "nombre": {
            "ca": "Tahiti i Moorea (Polinèsia Francesa)",
            "gl": "Tahití e Moorea (Polinesia Francesa)",
            "eu": "Tahiti eta Moorea (Polinesia Frantsesa)",
            "en": "Tahiti and Moorea (French Polynesia)"
        },
        "interes": {
            "ca": "Esculls franja i societats polinèsies.",
            "gl": "Arrecifes franjeantes e sociedades polinesias.",
            "eu": "Koralezko franja arrezifeak eta Polinesiako gizarteak.",
            "en": "Fringing reefs and Polynesian societies."
        },
        "texto": {
            "ca": "Examina com els esculls voregen les illes volcàniques i mesuren la seva edat relativa segons l'alçada de les muntanyes ombrejades. Observa sistemes agrícoles basats en el taro i l'arbre del pa, lligats a calendaris rituals que regulen la pesca comunitària. Intueix que la relació entre geologia coral·lina i organització social és inseparable per sostenir poblacions en atols aïllats.",
            "gl": "Examina como os arrecifes rodean as illas volcánicas e miden a súa idade relativa segundo a altura das montañas sombreadas. Observa sistemas agrícolas baseados en taro e árbore do pan, ligados a calendarios rituais que regulan a pesca comunitaria. Intúe que a relación entre xeoloxía coralina e organización social é inseparable para sosteren poboacións en atolóns illados.",
            "eu": "Arrezifeek uharte bolkanikoak nola inguratzen dituzten aztertzen du eta mendi itzaltsuen altueraren arabera adin erlatiboa neurtzen du. Taroan eta ogi-arbolean oinarritutako nekazaritza sistemak ikusten ditu, arrantza komunitarioa erregulatzen duten egutegi erritualekin lotuta. Antzematen du koralezko geologiaren eta gizarte antolaketaren arteko lotura banaezina dela atoloi isolatuetan biztanleria eusteko.",
            "en": "He examines how reefs girdle volcanic islands and gauges their relative age by the height of the shaded mountains. He observes farming systems based on taro and breadfruit, tied to ritual calendars that regulate communal fishing. He senses that the interplay between coral geology and social organisation is inseparable for sustaining populations on isolated atolls."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XVIII",
                    "gl": "Diario, capítulo XVIII",
                    "eu": "Egunkaria, XVIII. kapitulua",
                    "en": "Journal, Chapter XVIII"
                }
            }
        ]
    },
    "Bahía de las Islas (Nueva Zelanda)": {
        "nombre": {
            "ca": "Badia de les Illes (Nova Zelanda)",
            "gl": "Baía das Illas (Nova Zelandia)",
            "eu": "Uharteen badia (Zeelanda Berria)",
            "en": "Bay of Islands (New Zealand)"
        },
        "interes": {
            "ca": "Intercanvi botànic i contacte missioner.",
            "gl": "Intercambio botánico e contacto misioneiro.",
            "eu": "Botanikako trukea eta misiolarien harremana.",
            "en": "Botanical exchange and missionary contact."
        },
        "texto": {
            "ca": "Visita plantacions maorís mixtes amb espècies introduïdes britàniques i anota empelts de pomeres en sòls volcànics. Observa com les missions tradueixen conceptes científics a l'idioma local per explicar el calendari agrícola occidental. Conclou que l'intercanvi botànic va lligat a transformacions culturals profundes.",
            "gl": "Visita plantacións maorís mixtas con especies introducidas británicas e anota enxertos de maceiras en solos volcánicos. Observa como as misións traducen conceptos científicos á lingua local para explicar o calendario agrícola occidental. Conclúe que o intercambio botánico vai unido a transformacións culturais profundas.",
            "eu": "Maorien landaketa mistoak bisitatzen ditu, britainiarrek ekarritako espezieekin nahasita, eta sagarrondoen injertoak erregistratzen ditu lur bolkanikoetan. Misioek kontzeptu zientifikoak tokiko hizkuntzara nola itzultzen dituzten ikusten du mendebaldeko nekazaritza egutegia azaltzeko. Ondorioztatzen du botanikako trukeak kultura eraldaketa sakonekin lotuta doala.",
            "en": "He visits mixed Māori plantations that include British-introduced species and records apple grafts thriving in volcanic soils. He observes missions translating scientific concepts into the local language to explain the Western agricultural calendar. He concludes that botanical exchange is bound up with deep cultural transformation."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XVIII",
                    "gl": "Diario, capítulo XVIII",
                    "eu": "Egunkaria, XVIII. kapitulua",
                    "en": "Journal, Chapter XVIII"
                }
            }
        ]
    },
    "Sídney (Australia)": {
        "nombre": {
            "ca": "Sydney (Austràlia)",
            "gl": "Sidney (Australia)",
            "eu": "Sydney (Australia)",
            "en": "Sydney (Australia)"
        },
        "interes": {
            "ca": "Ciutats colonials i biogeografia marsupial.",
            "gl": "Cidades coloniais e bi xeografía marsupial.",
            "eu": "Hiri kolonialak eta marsupialen biogeografia.",
            "en": "Colonial cities and marsupial biogeography."
        },
        "texto": {
            "ca": "Analitza el traçat geomètric de la ciutat i com se superposa amb antics campaments gadigal. Visita reserves on cangurs i ornitorincs conviuen sota protecció estatal i compara la seva distribució amb els mamífers placentaris europeus introduïts. Argumenta que la singularitat australiana demostra històries evolutives separades modelades per l'aïllament continental.",
            "gl": "Analiza o trazado xeométrico da cidade e como se superpón con antigos campamentos gadigal. Visita reservas onde canguros e ornitorrincos conviven baixo protección estatal e compara a súa distribución cos mamíferos placentarios europeos introducidos. Argumenta que a singularidade australiana proba historias evolutivas separadas moldeadas polo illamento continental.",
            "eu": "Hiriaren trazadura geometrikoa aztertzen du eta nola gainezartzen den gadigal herriaren antzinako kanpamentuekin. Estatu babespean dauden kanguru eta ornitorrinkoen erreserbak bisitatzen ditu eta haien banaketa Europatik ekarritako ugaztun plazentariekin alderatzen du. Argudiatzen du Australiaren berezitasunak isolamendu kontinentalak moldatutako bilakaera historia bereiziak frogatzen dituela.",
            "en": "He analyses the city’s geometric grid and how it overlaps former Gadigal camps. He visits reserves where kangaroos and platypuses live under state protection and compares their ranges with those of introduced European placental mammals. He argues that Australia’s uniqueness demonstrates separate evolutionary histories shaped by continental isolation."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XIX",
                    "gl": "Diario, capítulo XIX",
                    "eu": "Egunkaria, XIX. kapitulua",
                    "en": "Journal, Chapter XIX"
                }
            }
        ]
    },
    "Hobart, isla de Tasmania": {
        "nombre": {
            "ca": "Hobart, illa de Tasmània",
            "gl": "Hobart, illa de Tasmania",
            "eu": "Hobart, Tasmania uhartea",
            "en": "Hobart, island of Tasmania"
        },
        "interes": {
            "ca": "Boscos temperats i espècies relictes.",
            "gl": "Bosques temperados e especies relictas.",
            "eu": "Baso epelak eta erlikia espezieak.",
            "en": "Temperate forests and relict species."
        },
        "texto": {
            "ca": "Explora boscos d'eucaliptus gegants alternats amb matollars densos on registra monotremes i marsupials nocturns caçats pels colons. Observa soques cremades i compara la regeneració vegetal després d'incendis controlats pels pobles palawa amb les pràctiques europees. Conclou que les pertorbacions periòdiques poden sostenir la diversitat si respecten els ritmes ecològics locals.",
            "gl": "Explora bosques de eucaliptos xigantes alternados con matogueiras densas onde rexistra monotremas e marsupiais nocturnos cazados por colonos. Observa tocos queimados e compara a rexeneración vexetal tras incendios controlados polos pobos palawa coas prácticas europeas. Conclúe que as perturbacións periódicas poden soster a diversidade se respectan os ritmos ecolóxicos locais.",
            "eu": "Eukaliptu erraldoien basoak eta zuhaixka trinkoak txandakatzen diren eremuak aztertzen ditu eta kolonizatzaileek ehizatutako monotremo eta marsupial gauztiak erregistratzen ditu. Enbor erreak ikusten ditu eta palawa herriek kontrolatutako suteen ondorengo landaretzaren birsorkuntza praktika europarrekin alderatzen du. Ondorioztatzen du aldizkako asaldurek dibertsitatea eutsi dezaketela tokiko erritmo ekologikoak errespetatzen badituzte.",
            "en": "He explores forests of giant eucalypts alternating with dense scrub where he records monotremes and nocturnal marsupials hunted by settlers. He observes burnt stumps and compares vegetation recovery after fires managed by Palawa communities with European practices. He concludes that periodic disturbances can sustain diversity when they respect local ecological rhythms."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XIX",
                    "gl": "Diario, capítulo XIX",
                    "eu": "Egunkaria, XIX. kapitulua",
                    "en": "Journal, Chapter XIX"
                }
            }
        ]
    },
    "King George Sound (Australia Occidental)": {
        "nombre": {
            "ca": "King George Sound (Austràlia Occidental)",
            "gl": "King George Sound (Australia Occidental)",
            "eu": "King George Sound (Australiako Mendebaldea)",
            "en": "King George Sound (Western Australia)"
        },
        "interes": {
            "ca": "Flora mediterrània austral i endemismes.",
            "gl": "Flora mediterránea austral e endemismos.",
            "eu": "Hego mediterraneoko flora eta endemismoak.",
            "en": "Southern Mediterranean-type flora and endemism."
        },
        "texto": {
            "ca": "Cataloga plantes de fulla dura i flors tubulars adaptades a sòls pobres en fòsfor mentre identifica insectes pol·linitzadors molt especialitzats. Observa com el foc natural obre espai a bancs de llavors persistents i genera mosaics de vegetació en pocs anys. Entén que l'aïllament prolongat del sud-oest australià afavoreix llinatges únics, reforçant el concepte de regions biogeogràfiques.",
            "gl": "Cataloga plantas con follas duras e flores tubulares adaptadas a solos pobres en fósforo, mentres identifica insectos polinizadores moi especializados. Observa como o lume natural abre espazo a bancos de sementes persistentes e xera mosaicos de vexetación en poucos anos. Entende que o illamento prolongado do suroeste australiano favorece liñaxes únicos, reforzando o concepto de rexións biogeográficas.",
            "eu": "Fosforo gutxiko lurretan egokitutako hosto gogorreko eta lore hodi itxurako landareak katalogatzen ditu, eta aldi berean oso espezializatutako intsektu polinizatzaileak identifikatzen ditu. Su naturalek hazitegi iraunkorretarako espazioa nola irekitzen duten eta urte gutxitan landaredi mosaikoak sortzen dituzten behatzen du. Ulertzen du Australiako hego mendebaldeko isolamendu luzeak leinu bereziak sustatzen dituela, eskualde biogeografikoen kontzeptua sendotuz.",
            "en": "He catalogues hard-leaved plants with tubular flowers adapted to phosphorus-poor soils while identifying highly specialised pollinating insects. He observes how natural fire opens space for persistent seed banks and creates vegetation mosaics within a few years. He realises that the long isolation of southwestern Australia favours unique lineages, reinforcing the concept of biogeographic regions."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XIX",
                    "gl": "Diario, capítulo XIX",
                    "eu": "Egunkaria, XIX. kapitulua",
                    "en": "Journal, Chapter XIX"
                }
            }
        ]
    },
    "Islas Cocos (Keeling)": {
        "nombre": {
            "ca": "Illes Cocos (Keeling)",
            "gl": "Illas Cocos (Keeling)",
            "eu": "Cocos uharteak (Keeling)",
            "en": "Cocos (Keeling) Islands"
        },
        "interes": {
            "ca": "Formació d'atols per subsidència oceànica.",
            "gl": "Formación de atolóns por subsidencia oceánica.",
            "eu": "Itsas hondoratze bidezko atolen sorrera.",
            "en": "Atoll formation through oceanic subsidence."
        },
        "texto": {
            "ca": "Mesura profunditats des de la goleta i registra com l'escull coral·lí creix cap amunt mentre el fons volcànic s'enfonsa. Analitza la granulometria de les platges per entendre el ritme d'erosió i deposició que alimenta les illes baixes. Conclou que els atols neixen de volcans submergits i que la biologia constructora dels coralls pot seguir el subsident, hipòtesi que publicarà el 1842.",
            "gl": "Realiza medicións de profundidade desde a goleta e rexistra como o arrecife coralino medra cara arriba mentres o fondo volcánico se afunde. Analiza a granulometría das praias para entender o ritmo de erosión e deposición que alimenta as illas baixas. Conclúe que os atolóns nacen de volcáns somerxidos e que a bioloxía construtora dos corais pode seguir ao afundimento, hipótese que publicará en 1842.",
            "eu": "Goletatik sakonerak neurtzen ditu eta koralezko arrezifeak gora hazten direla erregistratzen du, oinarri bolkanikoa hondoratzen den bitartean. Hondartzen ale tamaina aztertzen du uharte baxuak elikatzen dituen higadura eta metaketa erritmoa ulertzeko. Ondorioztatzen du atoloiek urpeko sumendietatik sortzen direla eta koralen eraikuntza biologiak hondoratzea jarraitu dezakeela; hipotesi hori 1842an argitaratuko du.",
            "en": "He measures depths from the schooner and records how the coral reef grows upward while the volcanic base sinks. He analyses the grain size of the beaches to understand the pace of erosion and deposition that feeds the low islands. He concludes that atolls arise from drowned volcanoes and that reef-building biology can keep pace with subsidence, a hypothesis he will publish in 1842."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XX",
                    "gl": "Diario, capítulo XX",
                    "eu": "Egunkaria, XX. kapitulua",
                    "en": "Journal, Chapter XX"
                }
            }
        ]
    },
    "Mauricio (Puerto de Port Louis)": {
        "nombre": {
            "ca": "Maurici (port de Port Louis)",
            "gl": "Mauricio (porto de Port Louis)",
            "eu": "Maurizio (Port Louis portua)",
            "en": "Mauritius (Port Louis harbour)"
        },
        "interes": {
            "ca": "Muntanyes basàltiques i jardins botànics.",
            "gl": "Montes basálticos e xardíns botánicos.",
            "eu": "Basaltozko mendiak eta lorategi botanikoak.",
            "en": "Basaltic mountains and botanical gardens."
        },
        "texto": {
            "ca": "Documenta la morfologia en ferradura del cràter de Trou aux Cerfs i contrasta les seves laves amb els basaltes de Cap Verd, cercant patrons universals. Visita el Jardí Botànic de Pamplemousses per comparar espècies antillanes naturalitzades amb endemismes mauricians. Infereix que les illes volcàniques comparteixen processos inicials, però que la colonització vegetal depèn de corrents i vents dominants.",
            "gl": "Documenta a morfoloxía en ferradura do cráter de Trou aux Cerfs e contrasta as súas lavas cos basaltos de Cabo Verde, buscando patróns universais. Visita o Xardín Botánico de Pamplemousses para comparar especies antillanas naturalizadas con endemismos mauricianos. Infire que as illas volcánicas comparten procesos iniciais, pero a colonización vexetal depende de correntes e ventos dominantes.",
            "eu": "Trou aux Cerfs krateraren ferra formako morfologia dokumentatzen du eta bere labak Cabo Verdeko basaltoekin alderatzen ditu, eredu unibertsalak bilatuz. Pamplemousses lorategi botanikoa bisitatzen du naturalizatutako Antilletako espezieak eta Maurizioko endemikoak alderatzeko. Ondorioztatzen du uharte bolkanikoek hasierako prozesu komunak partekatzen dituztela, baina landare kolonizazioa korronte eta haize nagusien mende dagoela.",
            "en": "He documents the horseshoe shape of the Trou aux Cerfs crater and contrasts its lavas with those of Cape Verde in search of universal patterns. He visits the Pamplemousses Botanic Garden to compare naturalised Antillean species with Mauritian endemics. He infers that volcanic islands share initial processes, but plant colonisation depends on prevailing currents and winds."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XXI",
                    "gl": "Diario, capítulo XXI",
                    "eu": "Egunkaria, XXI. kapitulua",
                    "en": "Journal, Chapter XXI"
                }
            }
        ]
    },
    "Ciudad del Cabo (Sudáfrica)": {
        "nombre": {
            "ca": "Ciutat del Cap (Sud-àfrica)",
            "gl": "Cidade do Cabo (Sudáfrica)",
            "eu": "Cape Town (Hegoafrika)",
            "en": "Cape Town (South Africa)"
        },
        "interes": {
            "ca": "Regne floral del Cap i convergències ecològiques.",
            "gl": "Reino floral do Cabo e converxencias ecolóxicas.",
            "eu": "Cape floraren erreinua eta konbergentzia ekologikoak.",
            "en": "Cape floristic kingdom and ecological convergence."
        },
        "texto": {
            "ca": "Recorre el Jardí de Kirstenbosch i descriu protees, èriques i restios que ocupen nínxols similars a plantes sud-americanes tot i no estar emparentades. Observa l'erosió a vessants sorrencs després de la tala de boscos natius per cultivar vinyes. Conclou que diferents continents generen solucions botàniques comparables davant pressions ambientals semblants, reforçant la noció de convergència adaptativa.",
            "gl": "Percorre o Xardín de Kirstenbosch e describe proteas, ericas e restios que ocupan nichos semellantes a plantas sudamericanas aínda que non estean emparentadas. Observa a erosión en ladeiras areosas tras a tala de bosques nativos para cultivar viñedos. Conclúe que diferentes continentes xeran solucións botánicas comparables ante presións ambientais semellantes, reforzando a noción de converxencia adaptativa.",
            "eu": "Kirstenbosch lorategia zeharkatzen du eta proteak, erikak eta restioak deskribatzen ditu, hego Amerikako landareekin ahaidetasunik izan gabe antzeko habitata betetzen dutela ikusiz. Baso autoktonoak mahastiak jartzeko moztu ondoren malda hareatsuetan agertzen den higadura behatzen du. Ondorioztatzen du kontinente desberdinek ingurumen presio antzekoen aurrean soluzio botaniko parekoak sortzen dituztela, konbergentzia moldakorraren ideia sendotuz.",
            "en": "He walks through Kirstenbosch Garden and describes proteas, ericas, and restios filling niches similar to South American plants despite lacking kinship. He observes erosion on sandy slopes after native forests were cleared to plant vineyards. He concludes that different continents deliver comparable botanical solutions under similar environmental pressures, reinforcing the notion of adaptive convergence."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XXI",
                    "gl": "Diario, capítulo XXI",
                    "eu": "Egunkaria, XXI. kapitulua",
                    "en": "Journal, Chapter XXI"
                }
            }
        ]
    },
    "Santa Elena (Atlántico sur)": {
        "nombre": {
            "ca": "Santa Helena (Atlàntic sud)",
            "gl": "Santa Helena (Atlántico sur)",
            "eu": "Santa Helena (Hego Atlantikoa)",
            "en": "Saint Helena (South Atlantic)"
        },
        "interes": {
            "ca": "Illa oceànica antiga amb flora endèmica.",
            "gl": "Illa oceánica antiga con flora endémica.",
            "eu": "Itsaso erdiko uharte zaharra flora endemikoarekin.",
            "en": "Ancient oceanic island with endemic flora."
        },
        "texto": {
            "ca": "Examina columnes de basalt erosionades i compara la seva mineralogia amb la de laves més joves observades en altres ports. Recorre plantacions reforestades pels britànics i avalua com les espècies exòtiques desplacen la vegetació endèmica de les zones humides. Conclou que la llarga història aïllada de l'illa va generar organismes exclusius, vulnerables a la intervenció humana accelerada.",
            "gl": "Examina columnas de basalto erosionadas e compara a súa mineraloxía coa de lavas máis novas observadas noutros portos. Recorre plantacións reforestadas polos británicos e avalía como especies exóticas desprazan a vexetación endémica das zonas húmidas. Conclúe que a longa historia illada da illa xerou organismos exclusivos, vulnerables á intervención humana acelerada.",
            "eu": "Basalto zutabe higatuak aztertzen ditu eta haien mineralogia beste portu batzuetan ikusitako laba gazteagoekin alderatzen du. Britainiarrek berreskuratutako landaketak bisitatzen ditu eta espezie exotikoek hezeguneko landaredi endemikoa nola ordezkatzen duten baloratzen du. Ondorioztatzen du uhartearen historia isolatu luzeak organismo bereziak sortu dituela, giza esku hartze azeleratuaren aurrean kalteberak.",
            "en": "He examines eroded basalt columns and compares their mineralogy with that of younger lavas seen at other ports. He surveys plantations reforested by the British and assesses how exotic species displace endemic vegetation in wet zones. He concludes that the island’s long isolated history produced unique organisms now vulnerable to accelerated human interference."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XXI",
                    "gl": "Diario, capítulo XXI",
                    "eu": "Egunkaria, XXI. kapitulua",
                    "en": "Journal, Chapter XXI"
                }
            }
        ]
    },
    "Isla Ascensión": {
        "nombre": {
            "ca": "Illa de l'Ascensió",
            "gl": "Illa Ascensión",
            "eu": "Ascensión uhartea",
            "en": "Ascension Island"
        },
        "interes": {
            "ca": "Colonització biològica en sòls volcànics joves.",
            "gl": "Colonización biolóxica en solos volcánicos novos.",
            "eu": "Lur bolkaniko gazteen kolonizazio biologikoa.",
            "en": "Biological colonisation on young volcanic soils."
        },
        "texto": {
            "ca": "Analitza cons d'escòria recents i registra com els molses i líquens colonitzen esquerdes protegides, seguits per gramínies aportades per les guarnicions britàniques. Observa fragates i ocells tròpics que nidifiquen en penya-segats exposats al vent, ajustant els seus cicles al recurs marí. Infereix que la dispersió a llarga distància basta per poblar illes remotes si hi ha microhàbitats disponibles.",
            "gl": "Analiza conos de escoura recentes e rexistra como musgos e líquenes colonizan gretas protexidas, seguidos por gramíneas achegadas polas guarnicións británicas. Observa fregatas e aves tropicais que nidifican en cantís expostos ao vento, axustando os seus ciclos ao recurso mariño. Infire que a dispersión a longa distancia abonda para poboar illas remotas se existen microhábitats dispoñibles.",
            "eu": "Eskoria kono berriak aztertzen ditu eta goroldio eta likenek babestutako pitzadurak nola kolonizatzen dituzten erregistratzen du, ondoren britainiar garnizioek ekarritako belarrek jarraituta. Fragatak eta tropiko hegaztiak ikuskatzen ditu haizearen menpeko labarretan habiak egiten, eta beren zikloak itsas baliabidera doitzen dituztela ohartzen da. Ondorioztatzen du distantzia luzeko hedapenak nahikoa dela uharte urrunak populatzeko mikrohabitat egokiak badaude.",
            "en": "He analyses recent scoria cones and records how mosses and lichens occupy sheltered cracks, followed by grasses brought by British garrisons. He observes frigatebirds and tropicbirds nesting on wind-exposed cliffs, tuning their cycles to marine resources. He infers that long-distance dispersal is enough to populate remote islands when suitable microhabitats exist."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XXI",
                    "gl": "Diario, capítulo XXI",
                    "eu": "Egunkaria, XXI. kapitulua",
                    "en": "Journal, Chapter XXI"
                }
            }
        ]
    },
    "Falmouth (regreso)": {
        "nombre": {
            "ca": "Falmouth (retorn)",
            "gl": "Falmouth (regreso)",
            "eu": "Falmouth (itzulera)",
            "en": "Falmouth (return)"
        },
        "interes": {
            "ca": "Tancament de la circumnavegació i recopilació científica.",
            "gl": "Peche da circunnavegación e recompilación científica.",
            "eu": "Mundubira amaiera eta bilduma zientifikoak.",
            "en": "End of the circumnavigation and scientific synthesis."
        },
        "texto": {
            "ca": "Desembarca a Falmouth amb dotze quaderns de camp, 1.529 espècimens en alcohol i centenars de roques etiquetades per origen. Revisa els instruments de mesura per verificar-ne la deriva després de gairebé cinc anys i anota correccions que permetran interpretar les dades amb rigor. Comprèn que la síntesi d'aquestes col·leccions transformarà la història natural britànica i obrirà la porta a noves teories evolutives.",
            "gl": "Desembarca en Falmouth con doce cadernos de campo, 1.529 especímenes en alcohol e centos de rochas etiquetadas pola súa orixe. Revisa os instrumentos de medición para verificar a súa deriva tras case cinco anos e anota correccións que permitirán interpretar os datos con rigor. Comprende que a síntese destas coleccións transformará a historia natural británica e abrirá a porta a novas teorías evolutivas.",
            "eu": "Falmouthen lehorreratzen da hamabi kanpoko koaderno, alkoholpean gordetako 1.529 ale eta jatorriaren arabera etiketatutako ehunka arroka eramanez. Neurketa tresnak berrikusten ditu ia bost urteren ondoren izan duten desbideratzea egiaztatzeko eta datuak zehaztasunez interpretatzeko zuzenketak idazten ditu. Ulertzen du bilduma horien sintesiak Britaniar historia naturala eraldatuko duela eta bilakaera teoria berriak zabalduko dituela.",
            "en": "He lands at Falmouth with twelve field notebooks, 1,529 specimens in alcohol, and hundreds of rocks labelled by origin. He checks the measuring instruments for drift after nearly five years and notes corrections that will let him interpret the data rigorously. He realises that synthesising these collections will reshape British natural history and open the door to new evolutionary theories."
        },
        "enlaces": [
            {
                "label_i18n": {
                    "ca": "Diari, capítol XXI",
                    "gl": "Diario, capítulo XXI",
                    "eu": "Egunkaria, XXI. kapitulua",
                    "en": "Journal, Chapter XXI"
                }
            }
        ]
    }
}


def apply_translations():
    path = Path('beagle.geojson')
    data = json.loads(path.read_text(encoding='utf-8'))
    for feature in data.get('features', []):
        props = feature.get('properties', {})
        name = props.get('nombre')
        payload = translations.get(name)
        if not payload:
            continue
        props['nombre_i18n'] = merge_with_spanish(props.get('nombre'), payload['nombre'])
        props['interes_i18n'] = merge_with_spanish(props.get('interes'), payload['interes'])
        props['texto_i18n'] = merge_with_spanish(props.get('texto'), payload['texto'])
        enlaces = props.get('enlaces', [])
        for idx, link in enumerate(enlaces):
            try:
                link_payload = payload['enlaces'][idx]
            except (KeyError, IndexError):
                continue
            link['label_i18n'] = merge_with_spanish(link.get('label'), link_payload['label_i18n'])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    apply_translations()
