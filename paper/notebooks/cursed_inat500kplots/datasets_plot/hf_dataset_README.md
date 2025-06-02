---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: gbifID
    dtype: string
  - name: decimalLatitude
    dtype: float32
  - name: decimalLongitude
    dtype: float32
  - name: kingdom
    dtype:
      class_label:
        names:
          '0': Plantae
  - name: phylum
    dtype:
      class_label:
        names:
          '0': Tracheophyta
  - name: class
    dtype:
      class_label:
        names:
          '0': Cycadopsida
          '1': Gnetopsida
          '2': Liliopsida
          '3': Lycopodiopsida
          '4': Magnoliopsida
          '5': Pinopsida
          '6': Polypodiopsida
  - name: order
    dtype:
      class_label:
        names:
          '0': Alismatales
          '1': Apiales
          '2': Arecales
          '3': Asparagales
          '4': Asterales
          '5': Boraginales
          '6': Brassicales
          '7': Buxales
          '8': Caryophyllales
          '9': Celastrales
          '10': Ceratophyllales
          '11': Commelinales
          '12': Cornales
          '13': Crossosomatales
          '14': Cucurbitales
          '15': Cyatheales
          '16': Cycadales
          '17': Dilleniales
          '18': Dioscoreales
          '19': Dipsacales
          '20': Ephedrales
          '21': Equisetales
          '22': Ericales
          '23': Escalloniales
          '24': Fabales
          '25': Fagales
          '26': Gentianales
          '27': Geraniales
          '28': Gleicheniales
          '29': Hymenophyllales
          '30': Isoetales
          '31': Lamiales
          '32': Laurales
          '33': Liliales
          '34': Lycopodiales
          '35': Magnoliales
          '36': Malpighiales
          '37': Malvales
          '38': Myrtales
          '39': Nymphaeales
          '40': Ophioglossales
          '41': Oxalidales
          '42': Pandanales
          '43': Pinales
          '44': Piperales
          '45': Poales
          '46': Polypodiales
          '47': Proteales
          '48': Psilotales
          '49': Ranunculales
          '50': Rosales
          '51': Salviniales
          '52': Santalales
          '53': Sapindales
          '54': Saxifragales
          '55': Schizaeales
          '56': Solanales
          '57': Vitales
          '58': Zingiberales
          '59': Zygophyllales
  - name: family
    dtype:
      class_label:
        names:
          '0': Acanthaceae
          '1': Achariaceae
          '2': Aizoaceae
          '3': Alismataceae
          '4': Alstroemeriaceae
          '5': Amaranthaceae
          '6': Amaryllidaceae
          '7': Anacardiaceae
          '8': Ancistrocladaceae
          '9': Annonaceae
          '10': Apiaceae
          '11': Apocynaceae
          '12': Aponogetonaceae
          '13': Araceae
          '14': Araliaceae
          '15': Araucariaceae
          '16': Arecaceae
          '17': Aristolochiaceae
          '18': Asparagaceae
          '19': Asphodelaceae
          '20': Aspleniaceae
          '21': Asteraceae
          '22': Athyriaceae
          '23': Balanophoraceae
          '24': Balsaminaceae
          '25': Begoniaceae
          '26': Berberidaceae
          '27': Betulaceae
          '28': Biebersteiniaceae
          '29': Bignoniaceae
          '30': Blechnaceae
          '31': Boraginaceae
          '32': Brassicaceae
          '33': Bromeliaceae
          '34': Burmanniaceae
          '35': Burseraceae
          '36': Buxaceae
          '37': Cactaceae
          '38': Calophyllaceae
          '39': Campanulaceae
          '40': Cannabaceae
          '41': Cannaceae
          '42': Capparaceae
          '43': Caprifoliaceae
          '44': Caricaceae
          '45': Caryophyllaceae
          '46': Casuarinaceae
          '47': Celastraceae
          '48': Ceratophyllaceae
          '49': Cistaceae
          '50': Cleomaceae
          '51': Clethraceae
          '52': Clusiaceae
          '53': Colchicaceae
          '54': Comandraceae
          '55': Combretaceae
          '56': Commelinaceae
          '57': Convolvulaceae
          '58': Cordiaceae
          '59': Cornaceae
          '60': Costaceae
          '61': Crassulaceae
          '62': Cucurbitaceae
          '63': Cunoniaceae
          '64': Cupressaceae
          '65': Cyatheaceae
          '66': Cycadaceae
          '67': Cymodoceaceae
          '68': Cynomoriaceae
          '69': Cyperaceae
          '70': Cystopteridaceae
          '71': Cytinaceae
          '72': Dennstaedtiaceae
          '73': Diapensiaceae
          '74': Dilleniaceae
          '75': Dioscoreaceae
          '76': Dipterocarpaceae
          '77': Droseraceae
          '78': Dryopteridaceae
          '79': Ebenaceae
          '80': Elaeagnaceae
          '81': Ephedraceae
          '82': Equisetaceae
          '83': Ericaceae
          '84': Erythroxylaceae
          '85': Escalloniaceae
          '86': Euphorbiaceae
          '87': Fabaceae
          '88': Fagaceae
          '89': Frankeniaceae
          '90': Gentianaceae
          '91': Geraniaceae
          '92': Gesneriaceae
          '93': Gleicheniaceae
          '94': Goodeniaceae
          '95': Grossulariaceae
          '96': Haloragaceae
          '97': Heliconiaceae
          '98': Heliotropiaceae
          '99': Hernandiaceae
          '100': Hydrocharitaceae
          '101': Hydrophyllaceae
          '102': Hymenophyllaceae
          '103': Hypericaceae
          '104': Hypoxidaceae
          '105': Hypseocharitaceae
          '106': Iridaceae
          '107': Isoetaceae
          '108': Ixioliriaceae
          '109': Juglandaceae
          '110': Juncaceae
          '111': Juncaginaceae
          '112': Krameriaceae
          '113': Lamiaceae
          '114': Lauraceae
          '115': Lecythidaceae
          '116': Lentibulariaceae
          '117': Liliaceae
          '118': Linaceae
          '119': Linderniaceae
          '120': Lindsaeaceae
          '121': Loasaceae
          '122': Loganiaceae
          '123': Loranthaceae
          '124': Lycopodiaceae
          '125': Lythraceae
          '126': Magnoliaceae
          '127': Malpighiaceae
          '128': Malvaceae
          '129': Marsileaceae
          '130': Mazaceae
          '131': Melanthiaceae
          '132': Melastomataceae
          '133': Meliaceae
          '134': Menispermaceae
          '135': Menyanthaceae
          '136': Misodendraceae
          '137': Molluginaceae
          '138': Monimiaceae
          '139': Montiaceae
          '140': Moraceae
          '141': Moringaceae
          '142': Musaceae
          '143': Myricaceae
          '144': Myrtaceae
          '145': Nelumbonaceae
          '146': Nepenthaceae
          '147': Nephrolepidaceae
          '148': Nyctaginaceae
          '149': Nymphaeaceae
          '150': Ochnaceae
          '151': Oleaceae
          '152': Onagraceae
          '153': Onocleaceae
          '154': Ophioglossaceae
          '155': Opiliaceae
          '156': Orchidaceae
          '157': Orobanchaceae
          '158': Oxalidaceae
          '159': Paeoniaceae
          '160': Pandanaceae
          '161': Papaveraceae
          '162': Parnassiaceae
          '163': Passifloraceae
          '164': Pedaliaceae
          '165': Pennantiaceae
          '166': Peraceae
          '167': Phrymaceae
          '168': Phyllanthaceae
          '169': Phytolaccaceae
          '170': Picrodendraceae
          '171': Pinaceae
          '172': Piperaceae
          '173': Pittosporaceae
          '174': Plantaginaceae
          '175': Platanaceae
          '176': Plumbaginaceae
          '177': Poaceae
          '178': Podocarpaceae
          '179': Polemoniaceae
          '180': Polygalaceae
          '181': Polygonaceae
          '182': Polypodiaceae
          '183': Pontederiaceae
          '184': Posidoniaceae
          '185': Potamogetonaceae
          '186': Primulaceae
          '187': Proteaceae
          '188': Psilotaceae
          '189': Pteridaceae
          '190': Ranunculaceae
          '191': Resedaceae
          '192': Restionaceae
          '193': Rhamnaceae
          '194': Rhizophoraceae
          '195': Ripogonaceae
          '196': Rosaceae
          '197': Rubiaceae
          '198': Rutaceae
          '199': Salicaceae
          '200': Salviniaceae
          '201': Sapindaceae
          '202': Sapotaceae
          '203': Sarcobataceae
          '204': Saxifragaceae
          '205': Schizaeaceae
          '206': Scrophulariaceae
          '207': Simaroubaceae
          '208': Simmondsiaceae
          '209': Smilacaceae
          '210': Solanaceae
          '211': Staphyleaceae
          '212': Stilbaceae
          '213': Styracaceae
          '214': Talinaceae
          '215': Taxaceae
          '216': Tectariaceae
          '217': Tetradiclidaceae
          '218': Thelypteridaceae
          '219': Thesiaceae
          '220': Thymelaeaceae
          '221': Turneraceae
          '222': Typhaceae
          '223': Ulmaceae
          '224': Urticaceae
          '225': Verbenaceae
          '226': Viburnaceae
          '227': Violaceae
          '228': Vitaceae
          '229': Woodsiaceae
          '230': Ximeniaceae
          '231': Zamiaceae
          '232': Zingiberaceae
          '233': Zosteraceae
          '234': Zygophyllaceae
  - name: genus
    dtype:
      class_label:
        names:
          '0': Abelia
          '1': Abrus
          '2': Abutilon
          '3': Acacia
          '4': Acaena
          '5': Acalypha
          '6': Acanthus
          '7': Acer
          '8': Achillea
          '9': Achyranthemum
          '10': Achyranthes
          '11': Acianthus
          '12': Aciphylla
          '13': Ackama
          '14': Acmella
          '15': Acmispon
          '16': Aconitum
          '17': Acrodon
          '18': Acrotriche
          '19': Adansonia
          '20': Adenandra
          '21': Adenanthera
          '22': Adenanthos
          '23': Adenium
          '24': Adiantum
          '25': Adonidia
          '26': Adonis
          '27': Aechmea
          '28': Aegilops
          '29': Aegonychon
          '30': Aerva
          '31': Aesculus
          '32': Afrosolen
          '33': Agalinis
          '34': Agave
          '35': Ageratum
          '36': Aglaia
          '37': Agrostis
          '38': Ailanthus
          '39': Aira
          '40': Aizoon
          '41': Ajuga
          '42': Albizia
          '43': Alcea
          '44': Alchemilla
          '45': Aldama
          '46': Alepidea
          '47': Aleurites
          '48': Aleuritopteris
          '49': Alisma
          '50': Allenrolfea
          '51': Alliaria
          '52': Allium
          '53': Alloberberis
          '54': Allocasuarina
          '55': Alocasia
          '56': Aloe
          '57': Alphitonia
          '58': Alpinia
          '59': Alternanthera
          '60': Althaea
          '61': Alyssum
          '62': Amaranthus
          '63': Ambrosia
          '64': Amelanchier
          '65': Ammannia
          '66': Amomyrtus
          '67': Amorphophallus
          '68': Amyema
          '69': Anacamptis
          '70': Anacardium
          '71': Anadenanthera
          '72': Anagyris
          '73': Anaphalis
          '74': Anastatica
          '75': Anchusa
          '76': Ancistrocladus
          '77': Andrographis
          '78': Androsace
          '79': Anemonastrum
          '80': Anemone
          '81': Anethum
          '82': Angelica
          '83': Anopterus
          '84': Antennaria
          '85': Anthemis
          '86': Anthericum
          '87': Anthospermum
          '88': Anthoxanthum
          '89': Anthriscus
          '90': Anthyllis
          '91': Antigonon
          '92': Aphelandra
          '93': Aponogeton
          '94': Aquarius
          '95': Aquilegia
          '96': Arabidopsis
          '97': Arachniodes
          '98': Aralia
          '99': Araucaria
          '100': Arctium
          '101': Arctopoa
          '102': Arctostaphylos
          '103': Arenaria
          '104': Argemone
          '105': Arisarum
          '106': Aristea
          '107': Aristida
          '108': Aristolochia
          '109': Arivela
          '110': Armeria
          '111': Arnebia
          '112': Artemisia
          '113': Arthrobotrya
          '114': Artocarpus
          '115': Arum
          '116': Arundinella
          '117': Arundo
          '118': Asarum
          '119': Asclepias
          '120': Aspalathus
          '121': Asparagus
          '122': Asphodelus
          '123': Aspidistra
          '124': Aspidotis
          '125': Asplenium
          '126': Asterothamnus
          '127': Astragalus
          '128': Astrantia
          '129': Asystasia
          '130': Athanasia
          '131': Athysanus
          '132': Atocion
          '133': Atractocarpus
          '134': Atraphaxis
          '135': Atriplex
          '136': Aureolaria
          '137': Austrolycopodium
          '138': Austrostipa
          '139': Avena
          '140': Avenella
          '141': Averrhoa
          '142': Avicennia
          '143': Ayenia
          '144': Azadirachta
          '145': Azolla
          '146': Azorella
          '147': Baccharis
          '148': Baileya
          '149': Bajacalia
          '150': Balanites
          '151': Ballota
          '152': Balsamorhiza
          '153': Bambusa
          '154': Banksia
          '155': Barbarea
          '156': Barleria
          '157': Barringtonia
          '158': Bartonia
          '159': Bassia
          '160': Bauhinia
          '161': Begonia
          '162': Bellardia
          '163': Bellis
          '164': Berberis
          '165': Bergeranthus
          '166': Berkheya
          '167': Berteroa
          '168': Bertholletia
          '169': Berula
          '170': Beta
          '171': Betonica
          '172': Betula
          '173': Bidens
          '174': Biebersteinia
          '175': Billardiera
          '176': Bistorta
          '177': Blackstonia
          '178': Blepharis
          '179': Blephilia
          '180': Blitum
          '181': Boechera
          '182': Bolax
          '183': Bolbitis
          '184': Bomarea
          '185': Bonellia
          '186': Borago
          '187': Borassus
          '188': Boronia
          '189': Boschniakia
          '190': Bosmania
          '191': Bossiaea
          '192': Botrychium
          '193': Bouteloua
          '194': Bouvardia
          '195': Brachycereus
          '196': Brachyelytrum
          '197': Brachypodium
          '198': Brachyscome
          '199': Brackenridgea
          '200': Breynia
          '201': Brickellia
          '202': Bridelia
          '203': Briza
          '204': Brocchinia
          '205': Bromus
          '206': Brongniartia
          '207': Browningia
          '208': Brugmansia
          '209': Bulbine
          '210': Bunias
          '211': Bupleurum
          '212': Bursera
          '213': Buxus
          '214': Byrsonima
          '215': Caesalpinia
          '216': Caladenia
          '217': Caladium
          '218': Calamagrostis
          '219': Calandrinia
          '220': Calanthe
          '221': Calliandra
          '222': Callianthe
          '223': Callitriche
          '224': Calluna
          '225': Calochortus
          '226': Calophyllum
          '227': Calostephane
          '228': Calotropis
          '229': Caltha
          '230': Calycadenia
          '231': Calyptridium
          '232': Calystegia
          '233': Camelina
          '234': Camissonia
          '235': Campanula
          '236': Campomanesia
          '237': Canna
          '238': Cannabis
          '239': Capparidastrum
          '240': Capparis
          '241': Capsicum
          '242': Caragana
          '243': Cardamine
          '244': Carduus
          '245': Carex
          '246': Carica
          '247': Carlina
          '248': Carmichaelia
          '249': Carpinus
          '250': Carpobrotus
          '251': Caryota
          '252': Cascabela
          '253': Cassinia
          '254': Cassytha
          '255': Castanea
          '256': Castela
          '257': Castilleja
          '258': Casuarina
          '259': Catapodium
          '260': Catharanthus
          '261': Causonis
          '262': Cavendishia
          '263': Ceanothus
          '264': Cecropia
          '265': Ceiba
          '266': Celmisia
          '267': Celtis
          '268': Cenchrus
          '269': Centaurea
          '270': Centella
          '271': Centranthera
          '272': Centranthus
          '273': Centrosema
          '274': Cephalanthera
          '275': Cephalocereus
          '276': Cephalophyllum
          '277': Cerastium
          '278': Ceratophyllum
          '279': Cerbera
          '280': Cereus
          '281': Cerinthe
          '282': Ceropegia
          '283': Cestrum
          '284': Chaenorhinum
          '285': Chaerophyllum
          '286': Chaetogastra
          '287': Chamaecrista
          '288': Chamaecytisus
          '289': Chamaenerion
          '290': Chamaerops
          '291': Chamaesciadium
          '292': Chamelaucium
          '293': Champereia
          '294': Chascolytrum
          '295': Cheirolophus
          '296': Chelidonium
          '297': Chenopodiastrum
          '298': Chenopodium
          '299': Cherleria
          '300': Chiropetalum
          '301': Choisya
          '302': Chondrilla
          '303': Chromolaena
          '304': Chrysanthemum
          '305': Chrysojasminum
          '306': Chrysolaena
          '307': Chrysosplenium
          '308': Chrysothemis
          '309': Circaea
          '310': Cirsium
          '311': Cissampelos
          '312': Cistanche
          '313': Cistus
          '314': Citrullus
          '315': Cladium
          '316': Clappertonia
          '317': Clarkia
          '318': Claytonia
          '319': Cleistesiopsis
          '320': Cleistocactus
          '321': Clematis
          '322': Cleomella
          '323': Clerodendrum
          '324': Clethra
          '325': Cliffortia
          '326': Clinopodium
          '327': Clitoria
          '328': Clowesia
          '329': Clutia
          '330': Cnidoscolus
          '331': Coccinia
          '332': Coccoloba
          '333': Coccothrinax
          '334': Cocos
          '335': Coelogyne
          '336': Coffea
          '337': Colchicum
          '338': Coleus
          '339': Colletia
          '340': Collomia
          '341': Colobanthus
          '342': Colocasia
          '343': Cologania
          '344': Columnea
          '345': Comandra
          '346': Commelina
          '347': Commiphora
          '348': Conchocarpus
          '349': Condalia
          '350': Coniogramme
          '351': Conium
          '352': Conocarpus
          '353': Conophytum
          '354': Convolvulus
          '355': Copernicia
          '356': Coprosma
          '357': Corchorus
          '358': Cordia
          '359': Cordylanthus
          '360': Cordyline
          '361': Coreopsis
          '362': Coriandrum
          '363': Cornus
          '364': Coronilla
          '365': Correa
          '366': Corryocactus
          '367': Cortaderia
          '368': Corydalis
          '369': Corylus
          '370': Corymbia
          '371': Corynandra
          '372': Cosmos
          '373': Costus
          '374': Cota
          '375': Cotoneaster
          '376': Cotula
          '377': Coutoubea
          '378': Cranfillia
          '379': Crantzia
          '380': Crassula
          '381': Crataegus
          '382': Crepis
          '383': Crithmum
          '384': Crossopteryx
          '385': Crotalaria
          '386': Croton
          '387': Cruciata
          '388': Cryptantha
          '389': Cryptolepis
          '390': Cucumis
          '391': Culcitium
          '392': Cumulopuntia
          '393': Cupania
          '394': Cuphea
          '395': Cupressus
          '396': Curatella
          '397': Cuscuta
          '398': Cyanothamnus
          '399': Cyanotis
          '400': Cyathea
          '401': Cycas
          '402': Cyclamen
          '403': Cydonia
          '404': Cylindropuntia
          '405': Cymbalaria
          '406': Cymbopogon
          '407': Cymodocea
          '408': Cynanchum
          '409': Cynodon
          '410': Cynoglossum
          '411': Cynomorium
          '412': Cynosurus
          '413': Cyperus
          '414': Cyphostemma
          '415': Cypripedium
          '416': Cyrtochilum
          '417': Cyrtostylis
          '418': Cystopteris
          '419': Cytinus
          '420': Cytisus
          '421': Dactylis
          '422': Dactyloctenium
          '423': Dactylorhiza
          '424': Dalbergia
          '425': Dalea
          '426': Danthonia
          '427': Daphne
          '428': Daphnopsis
          '429': Dasiphora
          '430': Dasylirion
          '431': Datura
          '432': Daucus
          '433': Dayia
          '434': Dedeckera
          '435': Deeringia
          '436': Deherainia
          '437': Delonix
          '438': Delosperma
          '439': Delphinium
          '440': Dendrobium
          '441': Dendrosicyos
          '442': Deparia
          '443': Deschampsia
          '444': Descurainia
          '445': Desmodium
          '446': Desmos
          '447': Dianthus
          '448': Diapensia
          '449': Dichanthelium
          '450': Dichondra
          '451': Dichrostachys
          '452': Dicoma
          '453': Dicranopteris
          '454': Digitalis
          '455': Digitaria
          '456': Dioscorea
          '457': Diospyros
          '458': Diplacus
          '459': Diplaspis
          '460': Diplazium
          '461': Diplotaxis
          '462': Dipsacus
          '463': Dirca
          '464': Disa
          '465': Disperis
          '466': Distichlis
          '467': Distimake
          '468': Dittrichia
          '469': Diuris
          '470': Dodecahema
          '471': Dodecatheon
          '472': Dodonaea
          '473': Dolichandra
          '474': Dombeya
          '475': Doodia
          '476': Dorstenia
          '477': Doryopteris
          '478': Draba
          '479': Dracaena
          '480': Dracocephalum
          '481': Dracophyllum
          '482': Drimia
          '483': Drosanthemum
          '484': Drosera
          '485': Dryas
          '486': Drymaria
          '487': Drymocallis
          '488': Drymonia
          '489': Dryopteris
          '490': Dumasia
          '491': Duranta
          '492': Dyschoriste
          '493': Dysphania
          '494': Eastwoodiella
          '495': Ecballium
          '496': Echeveria
          '497': Echinocereus
          '498': Echinochloa
          '499': Echinops
          '500': Echinospartum
          '501': Echium
          '502': Elaeagnus
          '503': Elaphoglossum
          '504': Elatostema
          '505': Elegia
          '506': Eleocharis
          '507': Elleanthus
          '508': Elodea
          '509': Elymus
          '510': Elytropappus
          '511': Enkianthus
          '512': Entada
          '513': Ephedra
          '514': Epidendrum
          '515': Epilobium
          '516': Epipactis
          '517': Epipremnum
          '518': Episcia
          '519': Equisetum
          '520': Eragrostis
          '521': Eremophila
          '522': Eremopyrum
          '523': Erepsia
          '524': Eriastrum
          '525': Erica
          '526': Erigeron
          '527': Eriogonum
          '528': Eriophorum
          '529': Eriophyllum
          '530': Eriospermum
          '531': Eriosyce
          '532': Erodium
          '533': Eryngium
          '534': Erysimum
          '535': Erythranthe
          '536': Erythrina
          '537': Erythronium
          '538': Erythroxylum
          '539': Eschenbachia
          '540': Escobedia
          '541': Esenbeckia
          '542': Espeletia
          '543': Etlingera
          '544': Eucalyptus
          '545': Eugenia
          '546': Eulophia
          '547': Euonymus
          '548': Eupatorium
          '549': Euphorbia
          '550': Euphrasia
          '551': Euploca
          '552': Euryale
          '553': Eurybia
          '554': Euthamia
          '555': Evolvulus
          '556': Exacum
          '557': Excoecaria
          '558': Extriplex
          '559': Fagonia
          '560': Fagraea
          '561': Fagus
          '562': Fallopia
          '563': Fallugia
          '564': Ferula
          '565': Festuca
          '566': Ficaria
          '567': Ficinia
          '568': Ficus
          '569': Filipendula
          '570': Fimbristylis
          '571': Flaveria
          '572': Forsskaolea
          '573': Fragaria
          '574': Frangula
          '575': Frankenia
          '576': Fraxinus
          '577': Fritillaria
          '578': Fuchsia
          '579': Fumana
          '580': Funastrum
          '581': Gagea
          '582': Gahnia
          '583': Galactia
          '584': Galeopsis
          '585': Galinsoga
          '586': Galium
          '587': Gambelia
          '588': Gamochaeta
          '589': Gardenia
          '590': Garuleum
          '591': Gaultheria
          '592': Gaylussacia
          '593': Gazania
          '594': Geissois
          '595': Geissorhiza
          '596': Genista
          '597': Gentiana
          '598': Gentianella
          '599': Geranium
          '600': Gethyllis
          '601': Geum
          '602': Gibbaeum
          '603': Gladiolus
          '604': Glebionis
          '605': Glechoma
          '606': Gleditsia
          '607': Glia
          '608': Glinus
          '609': Gliricidia
          '610': Globularia
          '611': Gloriosa
          '612': Glycyrrhiza
          '613': Gmelina
          '614': Gnidia
          '615': Gomphocarpus
          '616': Gomphrena
          '617': Gonolobus
          '618': Goodenia
          '619': Gorteria
          '620': Gossypium
          '621': Gratiola
          '622': Grevillea
          '623': Guadua
          '624': Guaiacum
          '625': Guazuma
          '626': Guilandina
          '627': Gustavia
          '628': Gutierrezia
          '629': Guzmania
          '630': Gymnadenia
          '631': Gymnanthemum
          '632': Gymnocarpium
          '633': Gymnoschoenus
          '634': Gymnosiphon
          '635': Gymnosporia
          '636': Gynandropsis
          '637': Gynerium
          '638': Gynochthodes
          '639': Habenaria
          '640': Hakea
          '641': Halenia
          '642': Halimium
          '643': Halleria
          '644': Halocarpus
          '645': Hardenbergia
          '646': Harfordia
          '647': Harrisia
          '648': Haworthia
          '649': Hechtia
          '650': Hedera
          '651': Hedypnois
          '652': Helenium
          '653': Helianthemum
          '654': Helianthus
          '655': Helichrysum
          '656': Heliconia
          '657': Heliophila
          '658': Heliotropium
          '659': Helleborus
          '660': Helminthotheca
          '661': Helosis
          '662': Hemarthria
          '663': Hemitomes
          '664': Hepatica
          '665': Heptapleurum
          '666': Heracleum
          '667': Herminium
          '668': Hernandia
          '669': Herniaria
          '670': Hesperantha
          '671': Hesperis
          '672': Hesperocodon
          '673': Heteropogon
          '674': Heterotheca
          '675': Heterotis
          '676': Heuchera
          '677': Hibbertia
          '678': Hibiscus
          '679': Hieracium
          '680': Himantoglossum
          '681': Hippocrepis
          '682': Hippomane
          '683': Hippophae
          '684': Hippuris
          '685': Hiptage
          '686': Hoffmannseggia
          '687': Holcus
          '688': Hordeum
          '689': Horminum
          '690': Hoya
          '691': Hunzikeria
          '692': Huperzia
          '693': Hyaenanche
          '694': Hyaloseris
          '695': Hydrocotyle
          '696': Hygrophila
          '697': Hylotelephium
          '698': Hymenocallis
          '699': Hymenophyllum
          '700': Hymenoxys
          '701': Hyoscyamus
          '702': Hypericum
          '703': Hyphaene
          '704': Hypochaeris
          '705': Hypodiscus
          '706': Hypoestes
          '707': Hypolepis
          '708': Hypoxis
          '709': Hypseocharis
          '710': Hypserpa
          '711': Icarus
          '712': Idahoa
          '713': Illigera
          '714': Impatiens
          '715': Imperata
          '716': Imperatoria
          '717': Indigofera
          '718': Iochroma
          '719': Ipomoea
          '720': Iris
          '721': Isoetes
          '722': Iva
          '723': Ixiolirion
          '724': Ixora
          '725': Jacaranda
          '726': Jacksonia
          '727': Jacobaea
          '728': Jasione
          '729': Jatropha
          '730': Johnstonella
          '731': Jouvea
          '732': Juanulloa
          '733': Juglans
          '734': Juncus
          '735': Juniperus
          '736': Jurinea
          '737': Justicia
          '738': Kaempferia
          '739': Kalanchoe
          '740': Kandelia
          '741': Karomia
          '742': Kernera
          '743': Khaya
          '744': Kickxia
          '745': Kigelia
          '746': Kitagawia
          '747': Knautia
          '748': Kniphofia
          '749': Koeleria
          '750': Koenigia
          '751': Kohleria
          '752': Krameria
          '753': Krapovickasia
          '754': Kunzea
          '755': Laburnum
          '756': Lachenalia
          '757': Lactuca
          '758': Lagarosiphon
          '759': Lagarostrobos
          '760': Lagurus
          '761': Lamium
          '762': Lantana
          '763': Lappula
          '764': Lapsana
          '765': Laser
          '766': Lastreopsis
          '767': Lathyrus
          '768': Launaea
          '769': Lavandula
          '770': Lawsonia
          '771': Lebeckia
          '772': Ledebouria
          '773': Leersia
          '774': Lenwebbia
          '775': Leonurus
          '776': Lepechinia
          '777': Lepidagathis
          '778': Lepidium
          '779': Lepisorus
          '780': Leporella
          '781': Leptadenia
          '782': Leptospermum
          '783': Leucadendron
          '784': Leucaena
          '785': Leucojum
          '786': Leucospermum
          '787': Leymus
          '788': Liatris
          '789': Ligustrum
          '790': Lilaeopsis
          '791': Lilium
          '792': Limonium
          '793': Linanthus
          '794': Linaria
          '795': Lindelofia
          '796': Lindera
          '797': Lindernia
          '798': Lindheimera
          '799': Lindsaea
          '800': Linum
          '801': Liparis
          '802': Liriodendron
          '803': Liriope
          '804': Lithocarpus
          '805': Litsea
          '806': Littorella
          '807': Loasa
          '808': Lobelia
          '809': Lolium
          '810': Lomandra
          '811': Lomariocycas
          '812': Lomatium
          '813': Lomatogonium
          '814': Lonicera
          '815': Lopezia
          '816': Lotus
          '817': Loxostylis
          '818': Ludwigia
          '819': Luffa
          '820': Lumnitzera
          '821': Lunaria
          '822': Lupinus
          '823': Luzula
          '824': Luzuriaga
          '825': Lycianthes
          '826': Lycium
          '827': Lycopodiella
          '828': Lyonia
          '829': Lysimachia
          '830': Maackia
          '831': Macroptilium
          '832': Macrozamia
          '833': Mahonia
          '834': Maianthemum
          '835': Maireana
          '836': Malachra
          '837': Mallotus
          '838': Malva
          '839': Mammillaria
          '840': Marina
          '841': Marsilea
          '842': Massonia
          '843': Matelea
          '844': Matricaria
          '845': Mazus
          '846': Medicago
          '847': Medinilla
          '848': Megathyrsus
          '849': Meiogyne
          '850': Melaleuca
          '851': Melampyrum
          '852': Melanolepis
          '853': Melanthera
          '854': Melasphaerula
          '855': Melastoma
          '856': Melica
          '857': Melicoccus
          '858': Melicope
          '859': Melicytus
          '860': Melilotus
          '861': Melissa
          '862': Melittis
          '863': Melocactus
          '864': Melochia
          '865': Mentha
          '866': Mentzelia
          '867': Meryta
          '868': Mesembryanthemum
          '869': Mesosphaerum
          '870': Metalasia
          '871': Metastelma
          '872': Miconia
          '873': Micranthes
          '874': Microcoelia
          '875': Microcybe
          '876': Microlepia
          '877': Microseris
          '878': Microsorum
          '879': Mikania
          '880': Mimosa
          '881': Mimulus
          '882': Mirabilis
          '883': Misodendrum
          '884': Momordica
          '885': Monachosorum
          '886': Monarda
          '887': Monardella
          '888': Moneses
          '889': Monnina
          '890': Monopsis
          '891': Monotropastrum
          '892': Monsonia
          '893': Monstera
          '894': Monteverdia
          '895': Moraea
          '896': Morella
          '897': Morettia
          '898': Morinda
          '899': Moringa
          '900': Morus
          '901': Mucuna
          '902': Muhlenbergia
          '903': Mummenhoffia
          '904': Murraya
          '905': Musa
          '906': Muscari
          '907': Mussaenda
          '908': Mutisia
          '909': Myoporum
          '910': Myosurus
          '911': Myriophyllum
          '912': Myriopteris
          '913': Myrsine
          '914': Myrtillocactus
          '915': Myrtus
          '916': Nanhaia
          '917': Narcissus
          '918': Nardus
          '919': Nassella
          '920': Nauclea
          '921': Nelumbo
          '922': Nemacladus
          '923': Nemesia
          '924': Nemophila
          '925': Neottia
          '926': Neowerdermannia
          '927': Nepenthes
          '928': Nepeta
          '929': Nephrolepis
          '930': Nerine
          '931': Nerium
          '932': Neustanthus
          '933': Nicandra
          '934': Nicotiana
          '935': Nigella
          '936': Nonea
          '937': Notelaea
          '938': Notogrammitis
          '939': Notopleura
          '940': Nuphar
          '941': Nuxia
          '942': Nyctaginia
          '943': Nymphaea
          '944': Nymphoides
          '945': Nypa
          '946': Ochradiscus
          '947': Oedera
          '948': Oenothera
          '949': Olea
          '950': Olearia
          '951': Oloptum
          '952': Oncidium
          '953': Onobrychis
          '954': Onoclea
          '955': Onopordum
          '956': Onosma
          '957': Ophioglossum
          '958': Ophrys
          '959': Oplismenus
          '960': Opuntia
          '961': Orchis
          '962': Oreocharis
          '963': Origanum
          '964': Ornithogalum
          '965': Ornithopus
          '966': Orobanche
          '967': Orthocarpus
          '968': Osmolindsaea
          '969': Ostrya
          '970': Othonna
          '971': Oxalis
          '972': Oxyria
          '973': Oxytropis
          '974': Ozothamnus
          '975': Pachylaena
          '976': Pachypodium
          '977': Pachystachys
          '978': Packera
          '979': Paeonia
          '980': Palhinhaea
          '981': Palicourea
          '982': Pallenis
          '983': Pandanus
          '984': Pangium
          '985': Panicum
          '986': Papaver
          '987': Paranomus
          '988': Parapolystichum
          '989': Paraprenanthes
          '990': Parasenecio
          '991': Parietaria
          '992': Paris
          '993': Parkia
          '994': Parnassia
          '995': Parodia
          '996': Parogonum
          '997': Parrya
          '998': Parthenocissus
          '999': Passiflora
          '1000': Patersonia
          '1001': Pavonia
          '1002': Pectis
          '1003': Pedicularis
          '1004': Peganum
          '1005': Pelargonium
          '1006': Pelecyphora
          '1007': Peliostomum
          '1008': Pemphis
          '1009': Pennantia
          '1010': Penstemon
          '1011': Pentagramma
          '1012': Pentameris
          '1013': Pentodon
          '1014': Peperomia
          '1015': Pergularia
          '1016': Perilla
          '1017': Perityle
          '1018': Persea
          '1019': Persicaria
          '1020': Persoonia
          '1021': Perymenium
          '1022': Petasites
          '1023': Petrea
          '1024': Phacelia
          '1025': Phedimus
          '1026': Phelipanche
          '1027': Philgamia
          '1028': Philibertia
          '1029': Philodendron
          '1030': Phleum
          '1031': Phlojodicarpus
          '1032': Phlox
          '1033': Phoenix
          '1034': Phormium
          '1035': Phragmites
          '1036': Phyla
          '1037': Phylica
          '1038': Phyllanthus
          '1039': Phyllodoce
          '1040': Phylloglossum
          '1041': Phyllosma
          '1042': Physalis
          '1043': Physaria
          '1044': Physochlaina
          '1045': Phyteuma
          '1046': Phytolacca
          '1047': Picea
          '1048': Picnomon
          '1049': Pilea
          '1050': Piliostigma
          '1051': Pilosella
          '1052': Pilosocereus
          '1053': Pimelea
          '1054': Pinguicula
          '1055': Pinochia
          '1056': Pinus
          '1057': Piper
          '1058': Pipturus
          '1059': Piqueria
          '1060': Pisonia
          '1061': Pistacia
          '1062': Pistia
          '1063': Pitcairnia
          '1064': Pithecellobium
          '1065': Pittosporum
          '1066': Plagius
          '1067': Planocarpa
          '1068': Plantago
          '1069': Platanthera
          '1070': Platanus
          '1071': Pleopeltis
          '1072': Pleradenophora
          '1073': Pleroma
          '1074': Pleurolobus
          '1075': Pleurothallis
          '1076': Plumbago
          '1077': Plumeria
          '1078': Poa
          '1079': Poacynum
          '1080': Podocarpus
          '1081': Podotheca
          '1082': Pogonolepis
          '1083': Pogostemon
          '1084': Polemonium
          '1085': Pollia
          '1086': Polygala
          '1087': Polygonatum
          '1088': Polypodium
          '1089': Polypogon
          '1090': Polystemma
          '1091': Polystichum
          '1092': Pontederia
          '1093': Populus
          '1094': Porophyllum
          '1095': Posidonia
          '1096': Potamogeton
          '1097': Potentilla
          '1098': Poterium
          '1099': Prasium
          '1100': Premna
          '1101': Primula
          '1102': Priva
          '1103': Prosartes
          '1104': Prosthechea
          '1105': Protea
          '1106': Prunella
          '1107': Prunus
          '1108': Psammophora
          '1109': Psephellus
          '1110': Pseudathyrium
          '1111': Pseudobombax
          '1112': Pseudogynoxys
          '1113': Pseudopodospermum
          '1114': Pseudoschoenus
          '1115': Pseudotsuga
          '1116': Psilocarphus
          '1117': Psilotum
          '1118': Psoralea
          '1119': Psychotria
          '1120': Pteridium
          '1121': Pteris
          '1122': Pterocaulon
          '1123': Pterocephalus
          '1124': Pterolepis
          '1125': Pterygodium
          '1126': Ptilimnium
          '1127': Ptilotus
          '1128': Pueraria
          '1129': Pulicaria
          '1130': Pulmonaria
          '1131': Pulsatilla
          '1132': Pultenaea
          '1133': Punica
          '1134': Puschkinia
          '1135': Puya
          '1136': Pycnanthemum
          '1137': Pygmaeothamnus
          '1138': Pyracantha
          '1139': Pyrostegia
          '1140': Pyrrosia
          '1141': Pyrus
          '1142': Quercus
          '1143': Rabelera
          '1144': Rafnia
          '1145': Ranunculus
          '1146': Raphanus
          '1147': Rapicactus
          '1148': Reseda
          '1149': Restio
          '1150': Reynoutria
          '1151': Rhamnus
          '1152': Rhaphidophora
          '1153': Rhaphiolepis
          '1154': Rhinanthus
          '1155': Rhinotropis
          '1156': Rhipsalis
          '1157': Rhizophora
          '1158': Rhodamnia
          '1159': Rhododendron
          '1160': Rhus
          '1161': Rhynchospermum
          '1162': Rhynchospora
          '1163': Rhynchostele
          '1164': Ribes
          '1165': Ricinus
          '1166': Rinzia
          '1167': Ripogonum
          '1168': Rivina
          '1169': Robinia
          '1170': Roella
          '1171': Romulea
          '1172': Rorippa
          '1173': Rosa
          '1174': Rubus
          '1175': Rudbeckia
          '1176': Ruellia
          '1177': Rumex
          '1178': Ruschia
          '1179': Russelia
          '1180': Ruta
          '1181': Sabal
          '1182': Sabatia
          '1183': Sabulina
          '1184': Sagina
          '1185': Sagittaria
          '1186': Salicornia
          '1187': Salix
          '1188': Salsola
          '1189': Salvia
          '1190': Salvinia
          '1191': Sambucus
          '1192': Sanguisorba
          '1193': Sanicula
          '1194': Sapium
          '1195': Saponaria
          '1196': Sarcobatus
          '1197': Sarcomphalus
          '1198': Satyrium
          '1199': Saxifraga
          '1200': Scabiosa
          '1201': Scadoxus
          '1202': Scaevola
          '1203': Scandia
          '1204': Scaphyglottis
          '1205': Schizachyrium
          '1206': Schizaea
          '1207': Schlagintweitia
          '1208': Schoenoplectus
          '1209': Schoenus
          '1210': Scilla
          '1211': Scirpoides
          '1212': Scirpus
          '1213': Sclerocactus
          '1214': Scolopia
          '1215': Scrophularia
          '1216': Scutellaria
          '1217': Sebaea
          '1218': Securidaca
          '1219': Sedum
          '1220': Selago
          '1221': Selenicereus
          '1222': Selinum
          '1223': Sempervivum
          '1224': Senecio
          '1225': Senna
          '1226': Serapias
          '1227': Sesbania
          '1228': Seseli
          '1229': Sesuvium
          '1230': Setaria
          '1231': Sherardia
          '1232': Sibbaldia
          '1233': Sida
          '1234': Sidalcea
          '1235': Sieruela
          '1236': Silene
          '1237': Silphium
          '1238': Silybum
          '1239': Simmondsia
          '1240': Sinapis
          '1241': Siphonochilus
          '1242': Sisymbrium
          '1243': Sisyrinchium
          '1244': Smilax
          '1245': Sobralia
          '1246': Soehrensia
          '1247': Solanum
          '1248': Soleirolia
          '1249': Solidago
          '1250': Sonchus
          '1251': Sophora
          '1252': Sorbus
          '1253': Sorghum
          '1254': Sorocea
          '1255': Spartium
          '1256': Spathodea
          '1257': Spathoglottis
          '1258': Spergularia
          '1259': Spermacoce
          '1260': Sphagneticola
          '1261': Spondias
          '1262': Stachys
          '1263': Stachytarpheta
          '1264': Staphylea
          '1265': Stellaria
          '1266': Stenandrium
          '1267': Stenocarpus
          '1268': Stenocereus
          '1269': Stenotis
          '1270': Stetsonia
          '1271': Sticherus
          '1272': Stigmaphyllon
          '1273': Stillingia
          '1274': Stipellula
          '1275': Stratiotes
          '1276': Streptocarpus
          '1277': Streptopus
          '1278': Striga
          '1279': Strobilanthes
          '1280': Strumpfia
          '1281': Strychnos
          '1282': Stuckenia
          '1283': Styphelia
          '1284': Styrax
          '1285': Succisa
          '1286': Succisella
          '1287': Swietenia
          '1288': Syagrus
          '1289': Symphonia
          '1290': Symphyotrichum
          '1291': Symphytum
          '1292': Synelcosciadium
          '1293': Syngonium
          '1294': Syzygium
          '1295': Tabebuia
          '1296': Tacazzea
          '1297': Taenidia
          '1298': Tagetes
          '1299': Talinum
          '1300': Talipariti
          '1301': Tanacetum
          '1302': Tapinanthus
          '1303': Taraxacum
          '1304': Taxus
          '1305': Tecoma
          '1306': Tecomaria
          '1307': Tectaria
          '1308': Tectona
          '1309': Tephroseris
          '1310': Terminalia
          '1311': Tetradenia
          '1312': Tetradymia
          '1313': Tetraena
          '1314': Tetragonia
          '1315': Tetrapanax
          '1316': Tetraria
          '1317': Teucrium
          '1318': Thalassia
          '1319': Thalictrum
          '1320': Thamnosma
          '1321': Thelypteris
          '1322': Theobroma
          '1323': Thermopsis
          '1324': Thesium
          '1325': Thespesia
          '1326': Thismia
          '1327': Thlaspi
          '1328': Thunbergia
          '1329': Thymelaea
          '1330': Thymus
          '1331': Tilesia
          '1332': Tillandsia
          '1333': Tithonia
          '1334': Tolmiea
          '1335': Torenia
          '1336': Torilis
          '1337': Torreyochloa
          '1338': Tournefortia
          '1339': Toxicoscordion
          '1340': Trachymene
          '1341': Tradescantia
          '1342': Tragopogon
          '1343': Traunsteinera
          '1344': Trichocereus
          '1345': Trichophorum
          '1346': Trichosanthes
          '1347': Trichostema
          '1348': Tridax
          '1349': Tridens
          '1350': Trifolium
          '1351': Triglochin
          '1352': Trillium
          '1353': Tripolium
          '1354': Tripterocalyx
          '1355': Trisetum
          '1356': Triumfetta
          '1357': Trollius
          '1358': Tropidia
          '1359': Tsuga
          '1360': Tulipa
          '1361': Tulista
          '1362': Turnera
          '1363': Turritis
          '1364': Tussilago
          '1365': Tylecodon
          '1366': Typha
          '1367': Typhonium
          '1368': Ulmus
          '1369': Umbilicus
          '1370': Uncarina
          '1371': Urena
          '1372': Urera
          '1373': Ursinia
          '1374': Urvillea
          '1375': Utricularia
          '1376': Vaccinium
          '1377': Vachellia
          '1378': Valeriana
          '1379': Vasconcellea
          '1380': Vateria
          '1381': Veratrum
          '1382': Verbascum
          '1383': Verbena
          '1384': Vernicia
          '1385': Vernonanthura
          '1386': Veronica
          '1387': Vesper
          '1388': Viburnum
          '1389': Vicia
          '1390': Victoria
          '1391': Vinca
          '1392': Vincetoxicum
          '1393': Viola
          '1394': Virgilia
          '1395': Viscaria
          '1396': Vitellaria
          '1397': Vitex
          '1398': Vitis
          '1399': Volkameria
          '1400': Voyria
          '1401': Wahlenbergia
          '1402': Waltheria
          '1403': Warszewiczia
          '1404': Wendlandia
          '1405': Westringia
          '1406': Wilkiea
          '1407': Wodyetia
          '1408': Wollastonia
          '1409': Woodsia
          '1410': Wurmbea
          '1411': Xanthorrhoea
          '1412': Xeranthemum
          '1413': Xerochloa
          '1414': Xerophyllum
          '1415': Ximenia
          '1416': Xylomelum
          '1417': Youngia
          '1418': Zaluzianskya
          '1419': Zamia
          '1420': Zamioculcas
          '1421': Zantedeschia
          '1422': Zanthoxylum
          '1423': Zelkova
          '1424': Zephyranthes
          '1425': Zilla
          '1426': Zizania
          '1427': Zizia
          '1428': Zostera
  - name: species
    dtype:
      class_label:
        names:
          '0': Abelia chinensis
          '1': Abrus precatorius
          '2': Abutilon dugesii
          '3': Abutilon indicum
          '4': Acacia auriculiformis
          '5': Acacia dealbata
          '6': Acaena magellanica
          '7': Acaena tenera
          '8': Acalypha gracilens
          '9': Acanthus mollis
          '10': Acer barbinerve
          '11': Acer campestre
          '12': Acer monspessulanum
          '13': Acer negundo
          '14': Acer platanoides
          '15': Acer tataricum
          '16': Achillea clusiana
          '17': Achillea ptarmica
          '18': Achillea roseoalba
          '19': Achyranthemum recurvatum
          '20': Achyranthes bidentata
          '21': Acianthus caudatus
          '22': Aciphylla aurea
          '23': Aciphylla glaucescens
          '24': Ackama rosifolia
          '25': Acmella uliginosa
          '26': Acmispon micranthus
          '27': Aconitum rotundifolium
          '28': Acrodon subulatus
          '29': Acrotriche aggregata
          '30': Adansonia digitata
          '31': Adenandra villosa
          '32': Adenanthera pavonina
          '33': Adenanthos meisneri
          '34': Adenium obesum
          '35': Adiantum capillus-veneris
          '36': Adiantum concinnum
          '37': Adiantum diaphanum
          '38': Adiantum fragile
          '39': Adiantum latifolium
          '40': Adiantum philippense
          '41': Adiantum raddianum
          '42': Adiantum tetraphyllum
          '43': Adonidia merrillii
          '44': Adonis aestivalis
          '45': Adonis amurensis
          '46': Aechmea angustifolia
          '47': Aechmea aquilega
          '48': Aechmea lueddemanniana
          '49': Aegilops triuncialis
          '50': Aegonychon zollingeri
          '51': Aerva javanica
          '52': Aesculus hippocastanum
          '53': Aesculus mutabilis
          '54': Aesculus parviflora
          '55': Afrosolen sandersonii
          '56': Agalinis auriculata
          '57': Agalinis strictifolia
          '58': Agave multicolor
          '59': Agave variegata
          '60': Ageratum houstonianum
          '61': Aglaia rimosa
          '62': Agrostis gigantea
          '63': Ailanthus altissima
          '64': Aira caryophyllea
          '65': Aira praecox
          '66': Aizoon secundum
          '67': Ajuga orientalis
          '68': Ajuga reptans
          '69': Albizia julibrissin
          '70': Alcea rosea
          '71': Alchemilla mollis
          '72': Aldama cordifolia
          '73': Alepidea peduncularis
          '74': Aleurites moluccanus
          '75': Aleuritopteris farinosa
          '76': Alisma gramineum
          '77': Alisma plantago-aquatica
          '78': Allenrolfea occidentalis
          '79': Alliaria petiolata
          '80': Allium angulosum
          '81': Allium bigelovii
          '82': Allium falcifolium
          '83': Allium lusitanicum
          '84': Allium nigrum
          '85': Allium paradoxum
          '86': Allium parvum
          '87': Allium rosenorum
          '88': Allium tenuissimum
          '89': Alloberberis fremontii
          '90': Allocasuarina muelleriana
          '91': Allocasuarina verticillata
          '92': Alocasia macrorrhizos
          '93': Aloe pretoriensis
          '94': Aloe vera
          '95': Alphitonia excelsa
          '96': Alpinia purpurata
          '97': Alternanthera brasiliana
          '98': Althaea officinalis
          '99': Alyssum alyssoides
          '100': Amaranthus retroflexus
          '101': Amaranthus spinosus
          '102': Ambrosia artemisiifolia
          '103': Amelanchier bartramiana
          '104': Ammannia auriculata
          '105': Amomyrtus meli
          '106': Amorphophallus dracontioides
          '107': Amyema gibberula
          '108': Anacamptis morio
          '109': Anacamptis pyramidalis
          '110': Anacardium occidentale
          '111': Anadenanthera colubrina
          '112': Anagyris foetida
          '113': Anaphalis javanica
          '114': Anastatica hierochuntica
          '115': Anchusa officinalis
          '116': Ancistrocladus heyneanus
          '117': Andrographis paniculata
          '118': Androsace elongata
          '119': Androsace maxima
          '120': Androsace septentrionalis
          '121': Anemonastrum narcissiflorum
          '122': Anemone coronaria
          '123': Anemone ranunculoides
          '124': Anemone tuberosa
          '125': Anethum graveolens
          '126': Angelica ampla
          '127': Angelica czernaevia
          '128': Angelica sylvestris
          '129': Anopterus macleayanus
          '130': Antennaria howellii
          '131': Antennaria lanata
          '132': Antennaria marginata
          '133': Anthemis arvensis
          '134': Anthericum liliago
          '135': Anthospermum rigidum
          '136': Anthoxanthum australe
          '137': Anthriscus cerefolium
          '138': Anthriscus sylvestris
          '139': Anthyllis barba-jovis
          '140': Anthyllis vulneraria
          '141': Antigonon leptopus
          '142': Aphelandra aurantiaca
          '143': Aponogeton distachyos
          '144': Aquarius grandiflorus
          '145': Aquilegia atrata
          '146': Aquilegia flavescens
          '147': Aquilegia vulgaris
          '148': Arabidopsis lyrata
          '149': Arachniodes aristata
          '150': Aralia spinosa
          '151': Araucaria heterophylla
          '152': Arctium minus
          '153': Arctium tomentosum
          '154': Arctopoa eminens
          '155': Arctostaphylos hispidula
          '156': Arctostaphylos rudis
          '157': Arenaria serpyllifolia
          '158': Argemone mexicana
          '159': Arisarum simorrhinum
          '160': Aristea ecklonii
          '161': Aristida purpurea
          '162': Aristolochia baetica
          '163': Aristolochia clematitis
          '164': Aristolochia maxima
          '165': Aristolochia rotunda
          '166': Aristolochia versabilifolia
          '167': Arivela viscosa
          '168': Armeria maritima
          '169': Armeria ruscinonensis
          '170': Arnebia decumbens
          '171': Artemisia alpina
          '172': Artemisia biennis
          '173': Artemisia campestris
          '174': Artemisia maritima
          '175': Artemisia rigida
          '176': Artemisia umbelliformis
          '177': Artemisia vulgaris
          '178': Arthrobotrya wilkesiana
          '179': Artocarpus altilis
          '180': Artocarpus heterophyllus
          '181': Arum korolkowii
          '182': Arum maculatum
          '183': Arundinella nepalensis
          '184': Arundo micrantha
          '185': Asarum nipponicum
          '186': Asclepias cucullata
          '187': Asclepias erosa
          '188': Asclepias pedicellata
          '189': Asclepias syriaca
          '190': Aspalathus glabrescens
          '191': Aspalathus incurvifolia
          '192': Aspalathus nigra
          '193': Asparagus horridus
          '194': Asphodelus ramosus
          '195': Aspidistra elatior
          '196': Aspidotis californica
          '197': Asplenium australasicum
          '198': Asplenium milnei
          '199': Asplenium nidus
          '200': Asplenium pinnatifidum
          '201': Asplenium polyodon
          '202': Asplenium sarelii
          '203': Asplenium scolopendrium
          '204': Asplenium tenuifolium
          '205': Asplenium trichomanes
          '206': Asplenium vespertinum
          '207': Asterothamnus centraliasiaticus
          '208': Astragalus asper
          '209': Astragalus austriacus
          '210': Astragalus calycinus
          '211': Astragalus clevelandii
          '212': Astragalus cruentiflorus
          '213': Astragalus emoryanus
          '214': Astragalus follicularis
          '215': Astragalus glycyphyllos
          '216': Astragalus lotiflorus
          '217': Astragalus macropus
          '218': Astragalus physodes
          '219': Astragalus simplicifolius
          '220': Astrantia major
          '221': Asystasia intrusa
          '222': Athanasia tomentosa
          '223': Athysanus pusillus
          '224': Atocion armeria
          '225': Atractocarpus merikin
          '226': Atraphaxis replicata
          '227': Atriplex billardierei
          '228': Atriplex littoralis
          '229': Atriplex micrantha
          '230': Atriplex patula
          '231': Atriplex semibaccata
          '232': Aureolaria pedicularia
          '233': Austrolycopodium fastigiatum
          '234': Austrostipa stipoides
          '235': Avena barbata
          '236': Avena sterilis
          '237': Avenella flexuosa
          '238': Averrhoa bilimbi
          '239': Avicennia germinans
          '240': Ayenia compacta
          '241': Azadirachta indica
          '242': Azolla filiculoides
          '243': Azolla pinnata
          '244': Azorella pedunculata
          '245': Azorella trifurcata
          '246': Baccharis bolivensis
          '247': Baccharis racemosa
          '248': Baileya pleniradiata
          '249': Bajacalia tridentata
          '250': Balanites aegyptiaca
          '251': Ballota nigra
          '252': Balsamorhiza hispidula
          '253': Bambusa vulgaris
          '254': Banksia baxteri
          '255': Banksia littoralis
          '256': Banksia sceptrum
          '257': Barbarea verna
          '258': Barleria cristata
          '259': Barleria mysorensis
          '260': Barleria pretoriensis
          '261': Barringtonia asiatica
          '262': Bartonia virginica
          '263': Bassia scoparia
          '264': Bauhinia purpurea
          '265': Bauhinia variegata
          '266': Begonia peruviana
          '267': Begonia urticae
          '268': Bellardia viscosa
          '269': Bellis annua
          '270': Bellis perennis
          '271': Berberis chilensis
          '272': Berberis vulgaris
          '273': Bergeranthus multiceps
          '274': Berkheya dregei
          '275': Berteroa incana
          '276': Bertholletia excelsa
          '277': Berula erecta
          '278': Beta vulgaris
          '279': Betonica hirsuta
          '280': Betonica officinalis
          '281': Betula pendula
          '282': Bidens alba
          '283': Bidens odorata
          '284': Bidens pilosa
          '285': Bidens tripartita
          '286': Biebersteinia odora
          '287': Billardiera longiflora
          '288': Bistorta amplexicaulis
          '289': Bistorta officinalis
          '290': Bistorta vivipara
          '291': Blackstonia grandiflora
          '292': Blepharis petalidioides
          '293': Blephilia subnuda
          '294': Blitum bonus-henricus
          '295': Boechera lyallii
          '296': Bolax gummifera
          '297': Bolbitis scalpturata
          '298': Bomarea linifolia
          '299': Bonellia nervosa
          '300': Borago officinalis
          '301': Borassus aethiopum
          '302': Borassus flabellifer
          '303': Boronia ternata
          '304': Boschniakia himalaica
          '305': Bosmania membranacea
          '306': Bossiaea ornata
          '307': Botrychium pinnatum
          '308': Botrychium tenebrosum
          '309': Bouteloua gracilis
          '310': Bouvardia multiflora
          '311': Brachycereus nesioticus
          '312': Brachyelytrum aristosum
          '313': Brachypodium pinnatum
          '314': Brachyscome nivalis
          '315': Brackenridgea nitida
          '316': Breynia cernua
          '317': Brickellia secundiflora
          '318': Bridelia mollis
          '319': Briza minor
          '320': Brocchinia micrantha
          '321': Bromus carinatus
          '322': Bromus catharticus
          '323': Bromus inermis
          '324': Bromus pumpellianus
          '325': Brongniartia foliolosa
          '326': Browningia hertlingiana
          '327': Brugmansia sanguinea
          '328': Bulbine lagopus
          '329': Bunias orientalis
          '330': Bupleurum rotundifolium
          '331': Bursera lancifolia
          '332': Buxus sempervirens
          '333': Byrsonima guilleminiana
          '334': Caesalpinia pulcherrima
          '335': Caladenia erythronema
          '336': Caladenia falcata
          '337': Caladenia speciosa
          '338': Caladium bicolor
          '339': Calamagrostis avenoides
          '340': Calandrinia caespitosa
          '341': Calandrinia pilosiuscula
          '342': Calanthe calanthoides
          '343': Calliandra dysantha
          '344': Callianthe picta
          '345': Callitriche terrestris
          '346': Calluna vulgaris
          '347': Calochortus amabilis
          '348': Calochortus catalinae
          '349': Calophyllum inophyllum
          '350': Calostephane divaricata
          '351': Calotropis gigantea
          '352': Calotropis procera
          '353': Caltha palustris
          '354': Calycadenia truncata
          '355': Calyptridium umbellatum
          '356': Calystegia sepium
          '357': Camelina microcarpa
          '358': Camissonia kernensis
          '359': Campanula barbata
          '360': Campanula persicifolia
          '361': Campanula uniflora
          '362': Campomanesia phaea
          '363': Canna generalis
          '364': Cannabis sativa
          '365': Capparidastrum petiolare
          '366': Capparis mitchellii
          '367': Capparis spinosa
          '368': Capsicum annuum
          '369': Caragana spinosa
          '370': Cardamine appendiculata
          '371': Cardamine flexuosa
          '372': Cardamine hirsuta
          '373': Cardamine impatiens
          '374': Carduus acanthoides
          '375': Carduus broteroi
          '376': Carduus crispus
          '377': Carduus nutans
          '378': Carduus personata
          '379': Carex acuta
          '380': Carex bohemica
          '381': Carex bonariensis
          '382': Carex excelsa
          '383': Carex glacialis
          '384': Carex haydenii
          '385': Carex hirta
          '386': Carex hystericina
          '387': Carex laevissima
          '388': Carex leersii
          '389': Carex lupulina
          '390': Carex maorica
          '391': Carex michelii
          '392': Carex molesta
          '393': Carex montana
          '394': Carex muehlenbergii
          '395': Carex nigra
          '396': Carex novae-angliae
          '397': Carex otrubae
          '398': Carex praticola
          '399': Carex pulicaris
          '400': Carex rostrata
          '401': Carex squarrosa
          '402': Carex sylvatica
          '403': Carex tomentosa
          '404': Carex tuckermanii
          '405': Carex umbrosa
          '406': Carica papaya
          '407': Carlina acanthifolia
          '408': Carlina acaulis
          '409': Carlina graeca
          '410': Carmichaelia williamsii
          '411': Carpinus betulus
          '412': Carpinus orientalis
          '413': Carpobrotus chilensis
          '414': Carpobrotus edulis
          '415': Carpobrotus mellei
          '416': Caryota urens
          '417': Cascabela thevetia
          '418': Cassinia laevis
          '419': Cassytha ciliolata
          '420': Cassytha pubescens
          '421': Castanea sativa
          '422': Castela tortuosa
          '423': Castilleja elegans
          '424': Castilleja lanata
          '425': Castilleja lutescens
          '426': Casuarina equisetifolia
          '427': Catapodium rigidum
          '428': Catharanthus roseus
          '429': Causonis corniculata
          '430': Cavendishia bracteata
          '431': Ceanothus masonii
          '432': Cecropia pachystachya
          '433': Cecropia peltata
          '434': Ceiba pentandra
          '435': Celmisia petriei
          '436': Celmisia sericophylla
          '437': Celtis bungeana
          '438': Cenchrus ciliaris
          '439': Cenchrus longisetus
          '440': Centaurea aspera
          '441': Centaurea australis
          '442': Centaurea calcitrapa
          '443': Centaurea cyanus
          '444': Centaurea majorovii
          '445': Centaurea solstitialis
          '446': Centella asiatica
          '447': Centella uniflora
          '448': Centranthera cochinchinensis
          '449': Centranthus lecoqii
          '450': Centranthus ruber
          '451': Centrosema sagittatum
          '452': Cephalanthera longifolia
          '453': Cephalocereus columna-trajani
          '454': Cephalophyllum parviflorum
          '455': Cerastium arcticum
          '456': Cerastium beeringianum
          '457': Cerastium brachypetalum
          '458': Cerastium fontanum
          '459': Cerastium glomeratum
          '460': Cerastium holosteoides
          '461': Ceratophyllum demersum
          '462': Cerbera manghas
          '463': Cereus repandus
          '464': Cereus stenogonus
          '465': Cerinthe retorta
          '466': Ceropegia socotrana
          '467': Cestrum citrifolium
          '468': Chaenorhinum origanifolium
          '469': Chaerophyllum hirsutum
          '470': Chaerophyllum temulum
          '471': Chaetogastra longifolia
          '472': Chamaecrista mimosoides
          '473': Chamaecrista nictitans
          '474': Chamaecrista nomame
          '475': Chamaecytisus hirsutus
          '476': Chamaecytisus supinus
          '477': Chamaenerion angustifolium
          '478': Chamaerops humilis
          '479': Chamaesciadium acaule
          '480': Chamelaucium ciliatum
          '481': Champereia manillana
          '482': Chascolytrum subaristatum
          '483': Cheirolophus crassifolius
          '484': Chelidonium majus
          '485': Chenopodiastrum hybridum
          '486': Chenopodiastrum murale
          '487': Chenopodium album
          '488': Chenopodium ficifolium
          '489': Cherleria yukonensis
          '490': Chiropetalum griseum
          '491': Choisya ternata
          '492': Chondrilla juncea
          '493': Chromolaena odorata
          '494': Chrysanthemum indicum
          '495': Chrysojasminum fruticans
          '496': Chrysolaena flexuosa
          '497': Chrysosplenium alternifolium
          '498': Chrysothemis melittifolia
          '499': Circaea alpina
          '500': Cirsium alsophilum
          '501': Cirsium arvense
          '502': Cirsium brevifolium
          '503': Cirsium dissectum
          '504': Cirsium fontinale
          '505': Cirsium quercetorum
          '506': Cirsium simplex
          '507': Cirsium vulgare
          '508': Cissampelos mucronata
          '509': Cissampelos pareira
          '510': Cistanche tubulosa
          '511': Cistus albidus
          '512': Cistus inflatus
          '513': Cistus monspeliensis
          '514': Citrullus colocynthis
          '515': Citrullus lanatus
          '516': Cladium mariscus
          '517': Clappertonia ficifolia
          '518': Clarkia delicata
          '519': Clarkia purpurea
          '520': Claytonia cordifolia
          '521': Claytonia sarmentosa
          '522': Cleistesiopsis bifaria
          '523': Cleistocactus baumannii
          '524': Cleistocactus candelilla
          '525': Cleistocactus hyalacanthus
          '526': Clematis afoliata
          '527': Clematis arenicola
          '528': Clematis flammula
          '529': Clematis hexapetala
          '530': Clematis montana
          '531': Clematis orientalis
          '532': Clematis psilandra
          '533': Clematis vitalba
          '534': Cleomella serrulata
          '535': Clerodendrum chinense
          '536': Clerodendrum paniculatum
          '537': Clerodendrum quadriloculare
          '538': Clethra alnifolia
          '539': Cliffortia heterophylla
          '540': Cliffortia ruscifolia
          '541': Clinopodium chandleri
          '542': Clitoria ternatea
          '543': Clowesia russelliana
          '544': Clutia polifolia
          '545': Cnidoscolus urens
          '546': Coccinia grandis
          '547': Coccoloba uvifera
          '548': Coccothrinax proctorii
          '549': Cocos nucifera
          '550': Coelogyne chinensis
          '551': Coffea arabica
          '552': Colchicum autumnale
          '553': Colchicum stevenii
          '554': Coleus cylindraceus
          '555': Colletia hystrix
          '556': Colletia spinosissima
          '557': Collomia mazama
          '558': Colobanthus quitensis
          '559': Colocasia esculenta
          '560': Colocasia fontanesii
          '561': Cologania angustifolia
          '562': Columnea minor
          '563': Comandra umbellata
          '564': Commelina benghalensis
          '565': Commelina communis
          '566': Commelina tuberosa
          '567': Commiphora glandulosa
          '568': Conchocarpus macrophyllus
          '569': Condalia globosa
          '570': Coniogramme pilosa
          '571': Conium maculatum
          '572': Conocarpus erectus
          '573': Conophytum minutum
          '574': Conophytum swanepoelianum
          '575': Convolvulus arvensis
          '576': Convolvulus sabatius
          '577': Convolvulus tricolor
          '578': Convolvulus virgatus
          '579': Copernicia alba
          '580': Coprosma autumnalis
          '581': Coprosma chathamica
          '582': Corchorus siliquosus
          '583': Cordia sebestena
          '584': Cordia subcordata
          '585': Cordylanthus pilosus
          '586': Cordyline fruticosa
          '587': Coreopsis petrophiloides
          '588': Coriandrum sativum
          '589': Cornus mas
          '590': Coronilla securidaca
          '591': Correa alba
          '592': Corryocactus aureus
          '593': Cortaderia jubata
          '594': Corydalis caucasica
          '595': Corydalis caudata
          '596': Corydalis paczoskii
          '597': Corydalis solida
          '598': Corydalis triternata
          '599': Corylus avellana
          '600': Corylus colurna
          '601': Corymbia ficifolia
          '602': Corynandra simplicifolia
          '603': Cosmos bipinnatus
          '604': Cosmos caudatus
          '605': Costus guanaiensis
          '606': Costus lucanusianus
          '607': Costus scaber
          '608': Costus spectabilis
          '609': Cota tinctoria
          '610': Cotoneaster melanocarpus
          '611': Cotula coronopifolia
          '612': Coutoubea spicata
          '613': Cranfillia nigra
          '614': Crantzia cristata
          '615': Crassula cremnophila
          '616': Crassula sericea
          '617': Crassula setulosa
          '618': Crataegus brachyacantha
          '619': Crataegus flava
          '620': Crepis paludosa
          '621': Crepis vesicaria
          '622': Crithmum maritimum
          '623': Crossopteryx febrifuga
          '624': Crotalaria goreensis
          '625': Crotalaria retusa
          '626': Crotalaria verrucosa
          '627': Croton bathianus
          '628': Croton humilis
          '629': Croton subpannosus
          '630': Cruciata laevipes
          '631': Cryptantha recurvata
          '632': Cryptolepis cryptolepioides
          '633': Cucumis dipsaceus
          '634': Cucumis metuliferus
          '635': Culcitium humile
          '636': Cumulopuntia corotilla
          '637': Cumulopuntia leucophaea
          '638': Cupania vernalis
          '639': Cuphea hyssopifolia
          '640': Cuphea ignea
          '641': Cupressus arizonica
          '642': Curatella americana
          '643': Cuscuta epithymum
          '644': Cuscuta exaltata
          '645': Cyanothamnus coerulescens
          '646': Cyanotis speciosa
          '647': Cyathea cunninghamii
          '648': Cycas glauca
          '649': Cyclamen hederifolium
          '650': Cyclamen persicum
          '651': Cydonia oblonga
          '652': Cylindropuntia kleiniae
          '653': Cymbalaria muralis
          '654': Cymbopogon bombycinus
          '655': Cymodocea nodosa
          '656': Cynanchum daltonii
          '657': Cynodon dactylon
          '658': Cynoglossum creticum
          '659': Cynomorium coccineum
          '660': Cynosurus cristatus
          '661': Cynosurus echinatus
          '662': Cyperus alternifolius
          '663': Cyperus blepharoleptos
          '664': Cyperus flavicomus
          '665': Cyperus mindorensis
          '666': Cyperus odoratus
          '667': Cyperus papyrus
          '668': Cyperus reflexus
          '669': Cyphostemma lanigerum
          '670': Cypripedium arietinum
          '671': Cypripedium japonicum
          '672': Cypripedium molle
          '673': Cyrtochilum meirax
          '674': Cyrtochilum ramosissimum
          '675': Cyrtostylis huegelii
          '676': Cystopteris fragilis
          '677': Cytinus ruber
          '678': Cytisus scoparius
          '679': Dactylis glomerata
          '680': Dactyloctenium aegyptium
          '681': Dactyloctenium radulans
          '682': Dactylorhiza incarnata
          '683': Dactylorhiza majalis
          '684': Dactylorhiza romana
          '685': Dactylorhiza viridis
          '686': Dalbergia sissoo
          '687': Dalea lutea
          '688': Danthonia decumbens
          '689': Daphne bholua
          '690': Daphne cneorum
          '691': Daphne laureola
          '692': Daphne striata
          '693': Daphnopsis racemosa
          '694': Dasiphora fruticosa
          '695': Dasylirion quadrangulatum
          '696': Datura stramonium
          '697': Datura wrightii
          '698': Daucus carota
          '699': Dayia glutinosa
          '700': Dedeckera eurekensis
          '701': Deeringia amaranthoides
          '702': Deherainia smaragdina
          '703': Delonix regia
          '704': Delosperma carterae
          '705': Delosperma cloeteae
          '706': Delphinium consolida
          '707': Delphinium elatum
          '708': Delphinium retropilosum
          '709': Delphinium variegatum
          '710': Dendrobium crumenatum
          '711': Dendrobium cuthbertsonii
          '712': Dendrosicyos socotrana
          '713': Deparia petersenii
          '714': Deschampsia antarctica
          '715': Descurainia erodiifolia
          '716': Desmodium fernaldii
          '717': Desmodium molliculum
          '718': Desmodium procumbens
          '719': Desmos chinensis
          '720': Dianthus barbatus
          '721': Dianthus carthusianorum
          '722': Dianthus hyssopifolius
          '723': Dianthus nudiflorus
          '724': Dianthus serotinus
          '725': Dianthus strictus
          '726': Dianthus superbus
          '727': Diapensia lapponica
          '728': Dichanthelium acuminatum
          '729': Dichondra argentea
          '730': Dichondra carolinensis
          '731': Dichondra occidentalis
          '732': Dichrostachys cinerea
          '733': Dicoma anomala
          '734': Dicranopteris linearis
          '735': Digitalis grandiflora
          '736': Digitalis purpurea
          '737': Digitaria sanguinalis
          '738': Dioscorea bulbifera
          '739': Diospyros tropophylla
          '740': Diplacus nanus
          '741': Diplaspis cordifolia
          '742': Diplazium esculentum
          '743': Diplotaxis tenuifolia
          '744': Dipsacus laciniatus
          '745': Dirca palustris
          '746': Disa atrorubens
          '747': Disa cernua
          '748': Disperis micrantha
          '749': Distichlis spicata
          '750': Distimake aureus
          '751': Distimake quinquefolius
          '752': Dittrichia viscosa
          '753': Diuris abbreviata
          '754': Diuris monticola
          '755': Diuris porrifolia
          '756': Dodecahema leptoceras
          '757': Dodecatheon alpinum
          '758': Dodecatheon hendersonii
          '759': Dodonaea pinnata
          '760': Dodonaea procumbens
          '761': Dodonaea viscosa
          '762': Dolichandra unguis-cati
          '763': Dombeya ledermannii
          '764': Dombeya punctata
          '765': Doodia caudata
          '766': Dorstenia gigas
          '767': Doryopteris decipiens
          '768': Doryopteris pedata
          '769': Draba howellii
          '770': Draba verna
          '771': Draba yukonensis
          '772': Dracaena angustifolia
          '773': Dracaena aubryana
          '774': Dracaena trifasciata
          '775': Dracocephalum nutans
          '776': Dracophyllum desgrazii
          '777': Drimia media
          '778': Drosanthemum archeri
          '779': Drosera hilaris
          '780': Drosera kaieteurensis
          '781': Drosera nidiformis
          '782': Drosera rotundifolia
          '783': Drosera spatulata
          '784': Dryas octopetala
          '785': Drymaria debilis
          '786': Drymocallis convallaria
          '787': Drymonia lanceolata
          '788': Dryopteris bissetiana
          '789': Dryopteris erythrosora
          '790': Dryopteris fragrans
          '791': Dryopteris wallichiana
          '792': Dumasia villosa
          '793': Duranta erecta
          '794': Dyschoriste hildebrandtii
          '795': Dysphania ambrosioides
          '796': Eastwoodiella californica
          '797': Ecballium elaterium
          '798': Echeveria multicolor
          '799': Echinocereus roetteri
          '800': Echinochloa crus-galli
          '801': Echinops sphaerocephalus
          '802': Echinospartum ibericum
          '803': Echium candicans
          '804': Elaeagnus angustifolia
          '805': Elaphoglossum hybridum
          '806': Elatostema scabrum
          '807': Elegia filacea
          '808': Eleocharis obtusa
          '809': Elleanthus capitatus
          '810': Elodea canadensis
          '811': Elodea nuttallii
          '812': Elymus nodosus
          '813': Elymus repens
          '814': Elytropappus hispidus
          '815': Enkianthus perulatus
          '816': Entada rheedei
          '817': Ephedra nebrodensis
          '818': Ephedra torreyana
          '819': Epidendrum fimbriatum
          '820': Epidendrum obrienianum
          '821': Epidendrum propinquum
          '822': Epilobium alpestre
          '823': Epilobium brevifolium
          '824': Epipactis atrorubens
          '825': Epipremnum aureum
          '826': Episcia cupreata
          '827': Equisetum arvense
          '828': Equisetum hyemale
          '829': Equisetum palustre
          '830': Equisetum telmateia
          '831': Eragrostis patens
          '832': Eragrostis pectinacea
          '833': Eragrostis pilosa
          '834': Eragrostis tenella
          '835': Eremophila debilis
          '836': Eremophila decipiens
          '837': Eremopyrum orientale
          '838': Erepsia patula
          '839': Erepsia saturata
          '840': Eriastrum rosamondense
          '841': Erica abietina
          '842': Erica canaliculata
          '843': Erica chloroloma
          '844': Erica cinerea
          '845': Erica cylindrica
          '846': Erica equisetifolia
          '847': Erica lutea
          '848': Erica oreotragus
          '849': Erica planifolia
          '850': Erica rosacea
          '851': Erica totta
          '852': Erigeron annuus
          '853': Erigeron delphinifolius
          '854': Eriogonum deflexum
          '855': Eriogonum truncatum
          '856': Eriophorum angustifolium
          '857': Eriophorum latifolium
          '858': Eriophorum vaginatum
          '859': Eriophyllum lanosum
          '860': Eriophyllum pringlei
          '861': Eriospermum zeyheri
          '862': Eriosyce armata
          '863': Erodium cicutarium
          '864': Erodium crinitum
          '865': Erodium fumarioides
          '866': Eryngium echinatum
          '867': Eryngium maritimum
          '868': Eryngium regnellii
          '869': Eryngium yuccifolium
          '870': Erysimum bicolor
          '871': Erysimum cheiranthoides
          '872': Erythranthe rubella
          '873': Erythrina breviflora
          '874': Erythrina caffra
          '875': Erythrina crista-galli
          '876': Erythrina speciosa
          '877': Erythronium dens-canis
          '878': Erythroxylum urbanii
          '879': Eschenbachia japonica
          '880': Escobedia crassipes
          '881': Esenbeckia berlandieri
          '882': Espeletia neriifolia
          '883': Etlingera elatior
          '884': Eucalyptus coolabah
          '885': Eucalyptus deglupta
          '886': Eucalyptus globulus
          '887': Eucalyptus gunnii
          '888': Eucalyptus haemastoma
          '889': Eucalyptus latisinensis
          '890': Eucalyptus robusta
          '891': Eucalyptus yarraensis
          '892': Eugenia candolleana
          '893': Eugenia haematocarpa
          '894': Eugenia sessiliflora
          '895': Eugenia uniflora
          '896': Eulophia cucullata
          '897': Eulophia maculata
          '898': Euonymus europaeus
          '899': Euonymus verrucosus
          '900': Eupatorium cannabinum
          '901': Eupatorium leucolepis
          '902': Euphorbia atoto
          '903': Euphorbia cinerascens
          '904': Euphorbia condylocarpa
          '905': Euphorbia cooperi
          '906': Euphorbia cyparissias
          '907': Euphorbia dendroides
          '908': Euphorbia dentata
          '909': Euphorbia exigua
          '910': Euphorbia guerichiana
          '911': Euphorbia hirta
          '912': Euphorbia hyssopifolia
          '913': Euphorbia leucocephala
          '914': Euphorbia maculata
          '915': Euphorbia mesembryanthemifolia
          '916': Euphorbia microcarpa
          '917': Euphorbia missurica
          '918': Euphorbia myrsinites
          '919': Euphorbia ophthalmica
          '920': Euphorbia pedilanthoides
          '921': Euphorbia pilosa
          '922': Euphorbia polygona
          '923': Euphorbia prostrata
          '924': Euphorbia regis-jubae
          '925': Euphorbia serpens
          '926': Euphorbia tetrapora
          '927': Euphorbia thymifolia
          '928': Euphorbia tirucalli
          '929': Euphorbia tithymaloides
          '930': Euphorbia wildii
          '931': Euphrasia nemorosa
          '932': Euploca ovalifolia
          '933': Euryale ferox
          '934': Eurybia divaricata
          '935': Euthamia graminifolia
          '936': Evolvulus nummularius
          '937': Exacum affine
          '938': Excoecaria agallocha
          '939': Extriplex californica
          '940': Fagonia indica
          '941': Fagraea berteroana
          '942': Fagus sylvatica
          '943': Fallopia convolvulus
          '944': Fallopia dumetorum
          '945': Fallugia paradoxa
          '946': Ferula glauca
          '947': Festuca contracta
          '948': Festuca microstachys
          '949': Festuca subverticillata
          '950': Ficaria verna
          '951': Ficinia nodosa
          '952': Ficinia oligantha
          '953': Ficus abutilifolia
          '954': Ficus benghalensis
          '955': Ficus carica
          '956': Ficus drupacea
          '957': Ficus grossularioides
          '958': Ficus microcarpa
          '959': Ficus natalensis
          '960': Ficus pumila
          '961': Ficus salicifolia
          '962': Ficus simplicissima
          '963': Ficus vasta
          '964': Ficus virens
          '965': Filipendula ulmaria
          '966': Fimbristylis littoralis
          '967': Flaveria linearis
          '968': Forsskaolea tenacissima
          '969': Fragaria chiloensis
          '970': Fragaria nubicola
          '971': Fragaria vesca
          '972': Frangula alnus
          '973': Frankenia salina
          '974': Fraxinus albicans
          '975': Fraxinus excelsior
          '976': Fraxinus quadrangulata
          '977': Fritillaria meleagris
          '978': Fuchsia arborescens
          '979': Fuchsia triphylla
          '980': Fumana thymifolia
          '981': Funastrum cynanchoides
          '982': Gagea bohemica
          '983': Gahnia procera
          '984': Galactia pinetorum
          '985': Galactia purshii
          '986': Galeopsis ladanum
          '987': Galeopsis pubescens
          '988': Galeopsis speciosa
          '989': Galeopsis tetrahit
          '990': Galinsoga parviflora
          '991': Galinsoga quadriradiata
          '992': Galium boreale
          '993': Galium lanceolatum
          '994': Galium mollugo
          '995': Galium palustre
          '996': Galium setaceum
          '997': Gambelia juncea
          '998': Gamochaeta pensylvanica
          '999': Gamochaeta stagnalis
          '1000': Gardenia aubryi
          '1001': Gardenia jasminoides
          '1002': Garuleum bipinnatum
          '1003': Gaultheria pumila
          '1004': Gaylussacia ursina
          '1005': Gazania rigens
          '1006': Gazania splendens
          '1007': Geissois pruinosa
          '1008': Geissorhiza furva
          '1009': Genista desoleana
          '1010': Gentiana aquatica
          '1011': Gentiana bambuseti
          '1012': Gentiana burseri
          '1013': Gentiana calycosa
          '1014': Gentiana lutea
          '1015': Gentiana macrophylla
          '1016': Gentiana sierrae
          '1017': Gentiana verna
          '1018': Gentianella campestris
          '1019': Gentianella chathamica
          '1020': Gentianella nummulariifolia
          '1021': Gentianella ramosa
          '1022': Geranium columbinum
          '1023': Geranium oxonianum
          '1024': Geranium pratense
          '1025': Geranium pyrenaicum
          '1026': Geranium robertianum
          '1027': Geranium sanguineum
          '1028': Geranium sylvaticum
          '1029': Gethyllis villosa
          '1030': Geum canadense
          '1031': Geum rivale
          '1032': Gibbaeum dispar
          '1033': Gladiolus alatus
          '1034': Gladiolus grandiflorus
          '1035': Gladiolus griseus
          '1036': Gladiolus imbricatus
          '1037': Gladiolus longicollis
          '1038': Glebionis segetum
          '1039': Glechoma hederacea
          '1040': Gleditsia triacanthos
          '1041': Glia prolifera
          '1042': Glinus lotoides
          '1043': Gliricidia sepium
          '1044': Globularia cordifolia
          '1045': Globularia meridionalis
          '1046': Globularia nudicaulis
          '1047': Gloriosa superba
          '1048': Glycyrrhiza glabra
          '1049': Gmelina arborea
          '1050': Gnidia squarrosa
          '1051': Gomphocarpus fruticosus
          '1052': Gomphrena vermicularis
          '1053': Gonolobus cteniophorus
          '1054': Gonolobus pectinatus
          '1055': Goodenia arguta
          '1056': Goodenia fascicularis
          '1057': Gorteria alienata
          '1058': Gossypium hirsutum
          '1059': Gratiola amphiantha
          '1060': Gratiola lutea
          '1061': Grevillea chrysophaea
          '1062': Grevillea longifolia
          '1063': Grevillea robusta
          '1064': Guadua trinii
          '1065': Guaiacum officinale
          '1066': Guazuma ulmifolia
          '1067': Guilandina bonduc
          '1068': Gustavia augusta
          '1069': Gutierrezia gilliesii
          '1070': Guzmania lingulata
          '1071': Guzmania scherzeriana
          '1072': Guzmania squarrosa
          '1073': Gymnadenia conopsea
          '1074': Gymnadenia rhellicani
          '1075': Gymnanthemum crataegifolium
          '1076': Gymnocarpium dryopteris
          '1077': Gymnocarpium robertianum
          '1078': Gymnoschoenus sphaerocephalus
          '1079': Gymnosiphon suaveolens
          '1080': Gymnosporia senegalensis
          '1081': Gynandropsis gynandra
          '1082': Gynerium sagittatum
          '1083': Gynochthodes umbellata
          '1084': Habenaria repens
          '1085': Hakea amplexicaulis
          '1086': Hakea marginata
          '1087': Halenia corniculata
          '1088': Halenia elliptica
          '1089': Halimium umbellatum
          '1090': Halleria lucida
          '1091': Halocarpus kirkii
          '1092': Hardenbergia violacea
          '1093': Harfordia macroptera
          '1094': Harrisia gracilis
          '1095': Haworthia arachnoidea
          '1096': Hechtia glomerata
          '1097': Hechtia texensis
          '1098': Hedera helix
          '1099': Hedera hibernica
          '1100': Hedera nepalensis
          '1101': Hedypnois rhagadioloides
          '1102': Helenium bigelovii
          '1103': Helianthemum nummularium
          '1104': Helianthus annuus
          '1105': Helichrysum arenarium
          '1106': Helichrysum reflexum
          '1107': Heliconia aemygdiana
          '1108': Heliconia bihai
          '1109': Heliconia chartacea
          '1110': Heliconia psittacorum
          '1111': Heliconia rostrata
          '1112': Heliconia wagneriana
          '1113': Heliophila digitata
          '1114': Heliophila trifurca
          '1115': Heliotropium bacciferum
          '1116': Heliotropium velutinum
          '1117': Helleborus orientalis
          '1118': Helminthotheca echioides
          '1119': Helosis cayennensis
          '1120': Hemarthria altissima
          '1121': Hemitomes congestum
          '1122': Hepatica nobilis
          '1123': Heptapleurum actinophyllum
          '1124': Heracleum dissectum
          '1125': Heracleum mantegazzianum
          '1126': Heracleum sphondylium
          '1127': Herminium lanceum
          '1128': Hernandia nymphaeifolia
          '1129': Herniaria polygama
          '1130': Hesperantha longicollis
          '1131': Hesperis matronalis
          '1132': Hesperocodon hederaceus
          '1133': Heteropogon contortus
          '1134': Heterotheca angustifolia
          '1135': Heterotheca pedunculata
          '1136': Heterotheca pumila
          '1137': Heterotis rotundifolia
          '1138': Heuchera americana
          '1139': Hibbertia acerosa
          '1140': Hibbertia microphylla
          '1141': Hibiscus archeri
          '1142': Hibiscus clayi
          '1143': Hibiscus denudatus
          '1144': Hibiscus sabdariffa
          '1145': Hibiscus trionum
          '1146': Hieracium abscissum
          '1147': Hieracium murorum
          '1148': Hieracium umbellatum
          '1149': Himantoglossum caprinum
          '1150': Himantoglossum hircinum
          '1151': Hippocrepis emerus
          '1152': Hippomane mancinella
          '1153': Hippophae rhamnoides
          '1154': Hippuris vulgaris
          '1155': Hiptage benghalensis
          '1156': Hoffmannseggia intricata
          '1157': Holcus lanatus
          '1158': Hordeum murinum
          '1159': Horminum pyrenaicum
          '1160': Hoya lacunosa
          '1161': Hunzikeria texana
          '1162': Huperzia selago
          '1163': Hyaenanche globosa
          '1164': Hyaloseris salicifolia
          '1165': Hydrocotyle alata
          '1166': Hydrocotyle ranunculoides
          '1167': Hygrophila auriculata
          '1168': Hylotelephium ewersii
          '1169': Hylotelephium maximum
          '1170': Hymenocallis littoralis
          '1171': Hymenophyllum malingii
          '1172': Hymenophyllum punctisorum
          '1173': Hymenoxys texana
          '1174': Hyoscyamus niger
          '1175': Hypericum anagalloides
          '1176': Hypericum densiflorum
          '1177': Hypericum hirsutum
          '1178': Hypericum humifusum
          '1179': Hypericum kalmianum
          '1180': Hypericum lydium
          '1181': Hypericum tetrapterum
          '1182': Hypericum triquetrifolium
          '1183': Hyphaene coriacea
          '1184': Hyphaene thebaica
          '1185': Hypochaeris megapotamica
          '1186': Hypochaeris radicata
          '1187': Hypodiscus procurrens
          '1188': Hypoestes phyllostachya
          '1189': Hypolepis dicksonioides
          '1190': Hypoxis multiceps
          '1191': Hypseocharis pimpinellifolia
          '1192': Hypserpa laurina
          '1193': Icarus filiformis
          '1194': Idahoa scapigera
          '1195': Illigera luzonensis
          '1196': Impatiens balfourii
          '1197': Impatiens balsamina
          '1198': Impatiens bequaertii
          '1199': Impatiens glandulifera
          '1200': Impatiens hawkeri
          '1201': Impatiens noli-tangere
          '1202': Impatiens oppositifolia
          '1203': Impatiens parviflora
          '1204': Impatiens semounensis
          '1205': Impatiens sodenii
          '1206': Impatiens stuhlmannii
          '1207': Imperata cylindrica
          '1208': Imperatoria ostruthium
          '1209': Indigofera fruticosa
          '1210': Indigofera monophylla
          '1211': Indigofera porrecta
          '1212': Iochroma fuchsioides
          '1213': Ipomoea alba
          '1214': Ipomoea amnicola
          '1215': Ipomoea hederifolia
          '1216': Ipomoea indica
          '1217': Ipomoea macrorhiza
          '1218': Ipomoea nil
          '1219': Ipomoea pes-caprae
          '1220': Iris domestica
          '1221': Iris hybrida
          '1222': Iris nigricans
          '1223': Iris pallida
          '1224': Iris pseudacorus
          '1225': Iris reticulata
          '1226': Iris sanguinea
          '1227': Iris stolonifera
          '1228': Isoetes novogranadensis
          '1229': Iva annua
          '1230': Ixiolirion tataricum
          '1231': Ixora ripicola
          '1232': Jacaranda mimosifolia
          '1233': Jacksonia stackhousei
          '1234': Jacobaea maritima
          '1235': Jacobaea uniflora
          '1236': Jacobaea vulgaris
          '1237': Jasione montana
          '1238': Jatropha gossypiifolia
          '1239': Jatropha podagrica
          '1240': Johnstonella micromeres
          '1241': Jouvea pilosa
          '1242': Juanulloa mexicana
          '1243': Juglans regia
          '1244': Juncus conglomeratus
          '1245': Juncus effusus
          '1246': Juncus inflexus
          '1247': Juncus torreyi
          '1248': Juniperus phoenicea
          '1249': Jurinea stoechadifolia
          '1250': Justicia brasiliana
          '1251': Kaempferia rotunda
          '1252': Kalanchoe beharensis
          '1253': Kalanchoe daigremontiana
          '1254': Kalanchoe delagoensis
          '1255': Kalanchoe houghtonii
          '1256': Kalanchoe pinnata
          '1257': Kandelia obovata
          '1258': Karomia speciosa
          '1259': Kernera saxatilis
          '1260': Khaya senegalensis
          '1261': Kickxia elatine
          '1262': Kigelia africana
          '1263': Kitagawia terebinthacea
          '1264': Knautia arvensis
          '1265': Kniphofia caulescens
          '1266': Koeleria macrantha
          '1267': Koenigia divaricata
          '1268': Kohleria tubiflora
          '1269': Krameria lanceolata
          '1270': Krameria pauciflora
          '1271': Krapovickasia flavescens
          '1272': Kunzea ericoides
          '1273': Laburnum anagyroides
          '1274': Lachenalia splendida
          '1275': Lactuca serriola
          '1276': Lactuca viminea
          '1277': Lagarosiphon major
          '1278': Lagarostrobos franklinii
          '1279': Lagurus ovatus
          '1280': Lamium album
          '1281': Lamium amplexicaule
          '1282': Lamium galeobdolon
          '1283': Lamium hybridum
          '1284': Lamium maculatum
          '1285': Lamium purpureum
          '1286': Lantana camara
          '1287': Lantana peduncularis
          '1288': Lantana strigocamara
          '1289': Lappula squarrosa
          '1290': Lapsana communis
          '1291': Laser trilobum
          '1292': Lastreopsis hispida
          '1293': Lathyrus angulatus
          '1294': Lathyrus linifolius
          '1295': Lathyrus nervosus
          '1296': Lathyrus nevadensis
          '1297': Lathyrus ochrus
          '1298': Lathyrus pratensis
          '1299': Lathyrus tuberosus
          '1300': Lathyrus vernus
          '1301': Launaea nana
          '1302': Lavandula subnuda
          '1303': Lawsonia inermis
          '1304': Lebeckia meyeriana
          '1305': Ledebouria apertiflora
          '1306': Leersia virginica
          '1307': Lenwebbia prominens
          '1308': Leonurus japonicus
          '1309': Lepechinia rossii
          '1310': Lepidagathis cristata
          '1311': Lepidium africanum
          '1312': Lepidium campestre
          '1313': Lepidium hirtum
          '1314': Lepidium virginicum
          '1315': Lepisorus schraderi
          '1316': Leporella fimbriata
          '1317': Leptadenia pyrotechnica
          '1318': Leptospermum scoparium
          '1319': Leucadendron corymbosum
          '1320': Leucaena diversifolia
          '1321': Leucaena leucocephala
          '1322': Leucojum aestivum
          '1323': Leucojum vernum
          '1324': Leucospermum oleifolium
          '1325': Leymus mollis
          '1326': Liatris laevigata
          '1327': Ligustrum lucidum
          '1328': Ligustrum vulgare
          '1329': Lilaeopsis polyantha
          '1330': Lilium pyrenaicum
          '1331': Limonium brasiliense
          '1332': Limonium scoparium
          '1333': Limonium vulgare
          '1334': Linanthus orcuttii
          '1335': Linaria alpina
          '1336': Linaria pelisseriana
          '1337': Linaria ricardoi
          '1338': Linaria simplex
          '1339': Linaria spartea
          '1340': Lindelofia stylosa
          '1341': Lindera communis
          '1342': Lindernia dubia
          '1343': Lindheimera texana
          '1344': Lindsaea linearis
          '1345': Linum alpinum
          '1346': Linum hirsutum
          '1347': Linum strictum
          '1348': Linum tenuifolium
          '1349': Liparis odorata
          '1350': Liriodendron tulipifera
          '1351': Liriope muscari
          '1352': Lithocarpus dodonaeifolius
          '1353': Litsea cubeba
          '1354': Litsea morrisonensis
          '1355': Littorella uniflora
          '1356': Loasa mollensis
          '1357': Lobelia goetzei
          '1358': Lobelia laxiflora
          '1359': Lobelia stricta
          '1360': Lolium arundinaceum
          '1361': Lomandra elongata
          '1362': Lomariocycas magellanica
          '1363': Lomatium parvifolium
          '1364': Lomatogonium rotatum
          '1365': Lonicera caerulea
          '1366': Lonicera flava
          '1367': Lonicera implexa
          '1368': Lonicera involucrata
          '1369': Lonicera xylosteum
          '1370': Lopezia grandiflora
          '1371': Lotus creticus
          '1372': Lotus germanicus
          '1373': Lotus maritimus
          '1374': Lotus pedunculatus
          '1375': Lotus tenuis
          '1376': Loxostylis alata
          '1377': Ludwigia octovalvis
          '1378': Luffa acutangula
          '1379': Lumnitzera littorea
          '1380': Lunaria rediviva
          '1381': Lupinus alopecuroides
          '1382': Lupinus croceus
          '1383': Lupinus polyphyllus
          '1384': Lupinus rivularis
          '1385': Luzula alopecurus
          '1386': Luzuriaga polyphylla
          '1387': Lycianthes ciliolata
          '1388': Lycianthes lycioides
          '1389': Lycium chinense
          '1390': Lycium ferocissimum
          '1391': Lycopodiella inundata
          '1392': Lyonia fruticosa
          '1393': Lysimachia arvensis
          '1394': Lysimachia azorica
          '1395': Lysimachia foemina
          '1396': Lysimachia japonica
          '1397': Lysimachia nummularia
          '1398': Lysimachia terrestris
          '1399': Maackia taiwanensis
          '1400': Macroptilium atropurpureum
          '1401': Macroptilium lathyroides
          '1402': Macrozamia pauli-guilielmi
          '1403': Mahonia aquifolium
          '1404': Maianthemum bifolium
          '1405': Maireana sedifolia
          '1406': Malachra capitata
          '1407': Mallotus oppositifolius
          '1408': Malva arborea
          '1409': Malva multiflora
          '1410': Malva neglecta
          '1411': Malva parviflora
          '1412': Malva sylvestris
          '1413': Mammillaria beneckei
          '1414': Mammillaria haageana
          '1415': Mammillaria nunezii
          '1416': Mammillaria plumosa
          '1417': Marina vetula
          '1418': Marsilea mutica
          '1419': Massonia triflora
          '1420': Matelea parvifolia
          '1421': Matricaria discoidea
          '1422': Mazus alpinus
          '1423': Medicago arabica
          '1424': Medicago disciformis
          '1425': Medicago falcata
          '1426': Medicago lupulina
          '1427': Medicago minima
          '1428': Medicago orbicularis
          '1429': Medicago ruthenica
          '1430': Medicago varia
          '1431': Medinilla magnifica
          '1432': Megathyrsus maximus
          '1433': Meiogyne cylindrocarpa
          '1434': Melaleuca hypericifolia
          '1435': Melaleuca preissiana
          '1436': Melaleuca squarrosa
          '1437': Melampyrum barbatum
          '1438': Melampyrum cristatum
          '1439': Melampyrum pratense
          '1440': Melampyrum sylvaticum
          '1441': Melanolepis multiglandulosa
          '1442': Melanthera nivea
          '1443': Melasphaerula graminea
          '1444': Melastoma malabathricum
          '1445': Melica transsilvanica
          '1446': Melicoccus bijugatus
          '1447': Melicope spathulata
          '1448': Melicope triphylla
          '1449': Melicytus obovatus
          '1450': Melilotus albus
          '1451': Melilotus indicus
          '1452': Melissa officinalis
          '1453': Melittis melissophyllum
          '1454': Melocactus intortus
          '1455': Melochia tomentosa
          '1456': Mentha longifolia
          '1457': Mentha pulegium
          '1458': Mentzelia dispersa
          '1459': Mentzelia longiloba
          '1460': Mentzelia nitens
          '1461': Mentzelia veatchiana
          '1462': Meryta sinclairii
          '1463': Mesembryanthemum crystallinum
          '1464': Mesembryanthemum nitidum
          '1465': Mesembryanthemum sladenianum
          '1466': Mesosphaerum suaveolens
          '1467': Metalasia aurea
          '1468': Metastelma barbigerum
          '1469': Miconia crenata
          '1470': Micranthes hieraciifolia
          '1471': Micranthes nudicaulis
          '1472': Micranthes pensylvanica
          '1473': Microcoelia gilpiniae
          '1474': Microcybe pauciflora
          '1475': Microlepia nepalensis
          '1476': Microseris scapigera
          '1477': Microsorum grossum
          '1478': Microsorum scolopendria
          '1479': Mikania micrantha
          '1480': Mimosa malacophylla
          '1481': Mimosa pudica
          '1482': Mimulus gracilis
          '1483': Mirabilis jalapa
          '1484': Mirabilis nyctaginea
          '1485': Mirabilis triflora
          '1486': Misodendrum quadriflorum
          '1487': Momordica charantia
          '1488': Monachosorum henryi
          '1489': Monarda maritima
          '1490': Monardella australis
          '1491': Moneses uniflora
          '1492': Monnina xalapensis
          '1493': Monopsis debilis
          '1494': Monopsis unidentata
          '1495': Monotropastrum humile
          '1496': Monsonia multifida
          '1497': Monstera deliciosa
          '1498': Monteverdia laevigata
          '1499': Moraea aristata
          '1500': Moraea setifolia
          '1501': Morella faya
          '1502': Morettia parviflora
          '1503': Morinda citrifolia
          '1504': Moringa oleifera
          '1505': Morus alba
          '1506': Morus indica
          '1507': Morus nigra
          '1508': Mucuna monticola
          '1509': Mucuna pruriens
          '1510': Muhlenbergia paniculata
          '1511': Mummenhoffia alliacea
          '1512': Murraya paniculata
          '1513': Musa itinerans
          '1514': Muscari comosum
          '1515': Muscari neglectum
          '1516': Mussaenda philippica
          '1517': Mutisia decurrens
          '1518': Myoporum platycarpum
          '1519': Myosurus minimus
          '1520': Myriophyllum aquaticum
          '1521': Myriophyllum spicatum
          '1522': Myriopteris intertexta
          '1523': Myrsine guianensis
          '1524': Myrtillocactus chende
          '1525': Myrtus communis
          '1526': Nanhaia speciosa
          '1527': Narcissus cuneiflorus
          '1528': Narcissus deficiens
          '1529': Narcissus medioluteus
          '1530': Narcissus pseudonarcissus
          '1531': Narcissus tazetta
          '1532': Nardus stricta
          '1533': Nassella neesiana
          '1534': Nauclea latifolia
          '1535': Nelumbo nucifera
          '1536': Nemacladus capillaris
          '1537': Nemesia bicornis
          '1538': Nemesia lucida
          '1539': Nemophila maculata
          '1540': Neottia nidus-avis
          '1541': Neowerdermannia vorwerkii
          '1542': Nepenthes gracilis
          '1543': Nepenthes mirabilis
          '1544': Nepenthes rafflesiana
          '1545': Nepeta multifida
          '1546': Nepeta teydea
          '1547': Nephrolepis cordifolia
          '1548': Nerine krigei
          '1549': Nerium oleander
          '1550': Neustanthus phaseoloides
          '1551': Nicandra physalodes
          '1552': Nicotiana glauca
          '1553': Nigella arvensis
          '1554': Nonea flavescens
          '1555': Nonea pulla
          '1556': Notelaea linearis
          '1557': Notogrammitis billardierei
          '1558': Notopleura uliginosa
          '1559': Nuphar advena
          '1560': Nuxia oppositifolia
          '1561': Nyctaginia capitata
          '1562': Nymphaea gracilis
          '1563': Nymphaea nouchali
          '1564': Nymphoides cordata
          '1565': Nypa fruticans
          '1566': Ochradiscus aucheri
          '1567': Oedera genistifolia
          '1568': Oedera rotundifolia
          '1569': Oenothera coronopifolia
          '1570': Oenothera curtiflora
          '1571': Oenothera lindheimeri
          '1572': Oenothera nuttallii
          '1573': Oenothera rubricaulis
          '1574': Oenothera stricta
          '1575': Oenothera tetraptera
          '1576': Olea europaea
          '1577': Olearia cheesemanii
          '1578': Olearia fragrantissima
          '1579': Olearia obcordata
          '1580': Oloptum thomasii
          '1581': Oncidium graminifolium
          '1582': Oncidium sotoanum
          '1583': Onobrychis arenaria
          '1584': Onoclea sensibilis
          '1585': Onopordum acanthium
          '1586': Onopordum tauricum
          '1587': Onosma microcarpa
          '1588': Ophioglossum lusitanicum
          '1589': Ophioglossum pusillum
          '1590': Ophrys bombyliflora
          '1591': Ophrys lutea
          '1592': Ophrys sphegodes
          '1593': Ophrys tenthredinifera
          '1594': Oplismenus hirtellus
          '1595': Opuntia columbiana
          '1596': Opuntia ficus-indica
          '1597': Opuntia pottsii
          '1598': Opuntia pubescens
          '1599': Opuntia stricta
          '1600': Orchis anatolica
          '1601': Orchis mascula
          '1602': Orchis olbiensis
          '1603': Orchis pallens
          '1604': Orchis purpurea
          '1605': Oreocharis sinensis
          '1606': Origanum vulgare
          '1607': Ornithogalum hispidum
          '1608': Ornithogalum neurostegium
          '1609': Ornithogalum refractum
          '1610': Ornithogalum rupestre
          '1611': Ornithopus compressus
          '1612': Orobanche caryophyllacea
          '1613': Orobanche gracilis
          '1614': Orobanche reticulata
          '1615': Orthocarpus imbricatus
          '1616': Osmolindsaea odorata
          '1617': Ostrya carpinifolia
          '1618': Othonna coronopifolia
          '1619': Othonna retrorsa
          '1620': Oxalis acetosella
          '1621': Oxalis articulata
          '1622': Oxalis corniculata
          '1623': Oxalis debilis
          '1624': Oxalis imbricata
          '1625': Oxalis laciniata
          '1626': Oxalis pes-caprae
          '1627': Oxalis tenuifolia
          '1628': Oxyria digyna
          '1629': Oxytropis altaica
          '1630': Oxytropis chakassiensis
          '1631': Oxytropis deflexa
          '1632': Ozothamnus obcordatus
          '1633': Pachylaena atriplicifolia
          '1634': Pachypodium lamerei
          '1635': Pachystachys lutea
          '1636': Packera multilobata
          '1637': Paeonia mascula
          '1638': Paeonia officinalis
          '1639': Palhinhaea cernua
          '1640': Palicourea alba
          '1641': Palicourea deflexa
          '1642': Palicourea erythrocephala
          '1643': Palicourea pubescens
          '1644': Pallenis maritima
          '1645': Pandanus analamerensis
          '1646': Pandanus tectorius
          '1647': Pangium edule
          '1648': Panicum brevifolium
          '1649': Panicum capillare
          '1650': Panicum decompositum
          '1651': Panicum miliaceum
          '1652': Papaver cambricum
          '1653': Papaver rhoeas
          '1654': Papaver umbonatum
          '1655': Paranomus lagopus
          '1656': Paranomus longicaulis
          '1657': Paranomus tomentosus
          '1658': Parapolystichum microsorum
          '1659': Paraprenanthes melanantha
          '1660': Parasenecio auriculata
          '1661': Parietaria judaica
          '1662': Paris quadrifolia
          '1663': Parkia speciosa
          '1664': Parnassia palustris
          '1665': Parodia erinacea
          '1666': Parogonum ciliinode
          '1667': Parrya arctica
          '1668': Parthenocissus quinquefolia
          '1669': Parthenocissus tricuspidata
          '1670': Passiflora coccinea
          '1671': Passiflora edulis
          '1672': Passiflora laurifolia
          '1673': Passiflora mediterranea
          '1674': Passiflora pallens
          '1675': Passiflora pallida
          '1676': Passiflora peduncularis
          '1677': Passiflora rubra
          '1678': Passiflora suberosa
          '1679': Passiflora tarminiana
          '1680': Passiflora tenuifila
          '1681': Passiflora venusta
          '1682': Patersonia sericea
          '1683': Pavonia missionum
          '1684': Pectis multiseta
          '1685': Pedicularis cheilanthifolia
          '1686': Pedicularis macrochila
          '1687': Pedicularis oederi
          '1688': Pedicularis resupinata
          '1689': Pedicularis rigginsiae
          '1690': Pedicularis rostratospicata
          '1691': Pedicularis sylvatica
          '1692': Pedicularis tuberosa
          '1693': Peganum harmala
          '1694': Pelargonium columbinum
          '1695': Pelargonium cucullatum
          '1696': Pelargonium luridum
          '1697': Pelargonium ternifolium
          '1698': Pelecyphora hesteri
          '1699': Pelecyphora missouriensis
          '1700': Peliostomum leucorrhizum
          '1701': Pemphis acidula
          '1702': Pennantia corymbosa
          '1703': Penstemon cyaneus
          '1704': Penstemon neotericus
          '1705': Penstemon palmeri
          '1706': Penstemon rattanii
          '1707': Penstemon subglaber
          '1708': Penstemon subserratus
          '1709': Penstemon virens
          '1710': Pentagramma viscosa
          '1711': Pentameris curvifolia
          '1712': Pentodon pentandrus
          '1713': Peperomia circinnata
          '1714': Peperomia rotundifolia
          '1715': Pergularia tomentosa
          '1716': Perilla frutescens
          '1717': Perityle crassifolia
          '1718': Persea americana
          '1719': Persicaria amphibia
          '1720': Persicaria capitata
          '1721': Persicaria hydropiper
          '1722': Persicaria maculosa
          '1723': Persoonia confertifolia
          '1724': Persoonia gunnii
          '1725': Persoonia levis
          '1726': Perymenium discolor
          '1727': Petasites albus
          '1728': Petasites pyrenaicus
          '1729': Petasites spurius
          '1730': Petrea volubilis
          '1731': Phacelia brachyloba
          '1732': Phacelia tanacetifolia
          '1733': Phedimus ellacombeanus
          '1734': Phelipanche mutelii
          '1735': Philgamia hibbertioides
          '1736': Philibertia tomentosa
          '1737': Philodendron giganteum
          '1738': Philodendron radiatum
          '1739': Philodendron verrucosum
          '1740': Phleum alpinum
          '1741': Phleum pratense
          '1742': Phlojodicarpus sibiricus
          '1743': Phlox gracilis
          '1744': Phlox tenuifolia
          '1745': Phoenix dactylifera
          '1746': Phoenix reclinata
          '1747': Phormium tenax
          '1748': Phragmites australis
          '1749': Phragmites karka
          '1750': Phyla nodiflora
          '1751': Phylica cuspidata
          '1752': Phylica lachneaeoides
          '1753': Phyllanthus abnormis
          '1754': Phyllanthus epiphyllanthus
          '1755': Phyllodoce breweri
          '1756': Phylloglossum drummondii
          '1757': Phyllosma capensis
          '1758': Physalis angulata
          '1759': Physalis peruviana
          '1760': Physaria kingii
          '1761': Physochlaina orientalis
          '1762': Phyteuma serratum
          '1763': Phytolacca americana
          '1764': Picea abies
          '1765': Picnomon acarna
          '1766': Pilea melastomoides
          '1767': Piliostigma reticulatum
          '1768': Pilosella officinarum
          '1769': Pilosocereus polygonus
          '1770': Pimelea drupacea
          '1771': Pimelea orthia
          '1772': Pimelea rosea
          '1773': Pimelea spinescens
          '1774': Pinguicula orchidioides
          '1775': Pinguicula vulgaris
          '1776': Pinochia corymbosa
          '1777': Pinus herrerae
          '1778': Pinus lambertiana
          '1779': Pinus nigra
          '1780': Pinus roxburghii
          '1781': Pinus sibirica
          '1782': Pinus sylvestris
          '1783': Piper amalago
          '1784': Piper auritum
          '1785': Pipturus argenteus
          '1786': Piqueria trinervia
          '1787': Pisonia horneae
          '1788': Pistacia chinensis
          '1789': Pistacia lentiscus
          '1790': Pistia stratiotes
          '1791': Pitcairnia bifrons
          '1792': Pitcairnia chiapensis
          '1793': Pithecellobium keyense
          '1794': Pithecellobium unguis-cati
          '1795': Pittosporum tobira
          '1796': Plagius maghrebinus
          '1797': Planocarpa petiolaris
          '1798': Plantago atrata
          '1799': Plantago major
          '1800': Plantago maritima
          '1801': Plantago maxima
          '1802': Plantago media
          '1803': Plantago rigida
          '1804': Platanthera canbyi
          '1805': Platanthera elongata
          '1806': Platanus hispanica
          '1807': Platanus occidentalis
          '1808': Platanus orientalis
          '1809': Pleopeltis minima
          '1810': Pleopeltis polypodioides
          '1811': Pleradenophora bilocularis
          '1812': Pleroma urvilleanum
          '1813': Pleurolobus gangeticus
          '1814': Pleurothallis microcardia
          '1815': Plumbago auriculata
          '1816': Plumbago zeylanica
          '1817': Plumeria obtusa
          '1818': Poa annua
          '1819': Poa bulbosa
          '1820': Poa compressa
          '1821': Poa lanata
          '1822': Poa trivialis
          '1823': Poacynum lancifolium
          '1824': Podocarpus oleifolius
          '1825': Podotheca angustifolia
          '1826': Pogonolepis muelleriana
          '1827': Pogostemon formosanus
          '1828': Polemonium pulcherrimum
          '1829': Pollia secundiflora
          '1830': Polygala alba
          '1831': Polygala molluginifolia
          '1832': Polygonatum multiflorum
          '1833': Polypodium californicum
          '1834': Polypodium vulgare
          '1835': Polypogon monspeliensis
          '1836': Polystemma guatemalense
          '1837': Polystichum formosanum
          '1838': Polystichum lonchitis
          '1839': Polystichum mohrioides
          '1840': Polystichum setiferum
          '1841': Polystichum thomsonii
          '1842': Polystichum tripteron
          '1843': Pontederia crassipes
          '1844': Pontederia vaginalis
          '1845': Populus alba
          '1846': Populus canescens
          '1847': Populus nigra
          '1848': Populus tremula
          '1849': Porophyllum scoparium
          '1850': Porophyllum viridiflorum
          '1851': Posidonia oceanica
          '1852': Potamogeton hillii
          '1853': Potamogeton perfoliatus
          '1854': Potamogeton richardsonii
          '1855': Potentilla alchimilloides
          '1856': Potentilla humifusa
          '1857': Potentilla indica
          '1858': Potentilla sphenophylla
          '1859': Potentilla verna
          '1860': Poterium sanguisorba
          '1861': Prasium majus
          '1862': Premna serratifolia
          '1863': Primula borealis
          '1864': Primula cuneifolia
          '1865': Primula farinosa
          '1866': Primula glutinosa
          '1867': Primula hirsuta
          '1868': Primula longiscapa
          '1869': Primula marginata
          '1870': Primula nutans
          '1871': Primula specuicola
          '1872': Primula vulgaris
          '1873': Priva lappulacea
          '1874': Prosartes lanuginosa
          '1875': Prosthechea fragrans
          '1876': Protea angolensis
          '1877': Protea laetans
          '1878': Protea madiensis
          '1879': Protea tenax
          '1880': Prunella laciniata
          '1881': Prunella vulgaris
          '1882': Prunus alabamensis
          '1883': Prunus armeniaca
          '1884': Prunus avium
          '1885': Prunus domestica
          '1886': Prunus laurocerasus
          '1887': Prunus lusitanica
          '1888': Prunus maximowiczii
          '1889': Prunus padus
          '1890': Prunus pedunculata
          '1891': Prunus spinosa
          '1892': Psammophora modesta
          '1893': Psephellus daghestanicus
          '1894': Pseudathyrium alpestre
          '1895': Pseudobombax septenatum
          '1896': Pseudogynoxys cumingii
          '1897': Pseudopodospermum undulatum
          '1898': Pseudoschoenus inanis
          '1899': Pseudotsuga menziesii
          '1900': Psilocarphus tenellus
          '1901': Psilotum nudum
          '1902': Psoralea ivumba
          '1903': Psychotria armandii
          '1904': Psychotria erythrocarpa
          '1905': Psychotria nervosa
          '1906': Psychotria urbaniana
          '1907': Pteridium aquilinum
          '1908': Pteris ensiformis
          '1909': Pteris umbrosa
          '1910': Pteris vittata
          '1911': Pterocaulon virgatum
          '1912': Pterocephalus porphyranthus
          '1913': Pterolepis glomerata
          '1914': Pterygodium magnum
          '1915': Ptilimnium costatum
          '1916': Ptilotus semilanatus
          '1917': Pueraria montana
          '1918': Pulicaria dysenterica
          '1919': Pulmonaria angustifolia
          '1920': Pulmonaria mollis
          '1921': Pulsatilla alpina
          '1922': Pulsatilla campanella
          '1923': Pulsatilla grandis
          '1924': Pulsatilla patens
          '1925': Pultenaea robusta
          '1926': Pultenaea rostrata
          '1927': Punica granatum
          '1928': Puschkinia scilloides
          '1929': Puya trianae
          '1930': Pycnanthemum tenuifolium
          '1931': Pygmaeothamnus zeyheri
          '1932': Pyracantha coccinea
          '1933': Pyrostegia venusta
          '1934': Pyrrosia longifolia
          '1935': Pyrus communis
          '1936': Quercus bicolor
          '1937': Quercus brantii
          '1938': Quercus cerris
          '1939': Quercus coccifera
          '1940': Quercus ganderi
          '1941': Quercus ilex
          '1942': Quercus macranthera
          '1943': Quercus pubescens
          '1944': Quercus rubra
          '1945': Quercus tarokoensis
          '1946': Quercus velutina
          '1947': Rabelera holostea
          '1948': Rafnia crassifolia
          '1949': Rafnia rostrata
          '1950': Ranunculus aconitifolius
          '1951': Ranunculus adoneus
          '1952': Ranunculus altaicus
          '1953': Ranunculus austrooreganus
          '1954': Ranunculus bulbosus
          '1955': Ranunculus caucasicus
          '1956': Ranunculus flabellaris
          '1957': Ranunculus lingua
          '1958': Ranunculus platanifolius
          '1959': Raphanus raphanistrum
          '1960': Rapicactus beguinii
          '1961': Reseda lutea
          '1962': Reseda media
          '1963': Reseda phyteuma
          '1964': Reseda stricta
          '1965': Restio subverticillatus
          '1966': Reynoutria japonica
          '1967': Reynoutria sachalinensis
          '1968': Rhamnus cathartica
          '1969': Rhaphidophora hongkongensis
          '1970': Rhaphiolepis bibas
          '1971': Rhaphiolepis indica
          '1972': Rhaphiolepis umbellata
          '1973': Rhinanthus minor
          '1974': Rhinanthus serotinus
          '1975': Rhinotropis cornuta
          '1976': Rhipsalis baccifera
          '1977': Rhizophora mangle
          '1978': Rhodamnia argentea
          '1979': Rhododendron anthopogon
          '1980': Rhododendron arboreum
          '1981': Rhododendron dilatatum
          '1982': Rhododendron hirsutum
          '1983': Rhododendron indicum
          '1984': Rhododendron maximum
          '1985': Rhododendron pulchrum
          '1986': Rhus coriaria
          '1987': Rhus microphylla
          '1988': Rhus typhina
          '1989': Rhynchospermum verticillatum
          '1990': Rhynchospora alba
          '1991': Rhynchospora capillacea
          '1992': Rhynchostele aptera
          '1993': Ribes glandulosum
          '1994': Ribes punctatum
          '1995': Ribes rubrum
          '1996': Ribes sanguineum
          '1997': Ribes uva-crispa
          '1998': Ricinus communis
          '1999': Rinzia orientalis
          '2000': Ripogonum discolor
          '2001': Rivina humilis
          '2002': Robinia pseudoacacia
          '2003': Roella prostrata
          '2004': Romulea montana
          '2005': Rorippa austriaca
          '2006': Rorippa palustris
          '2007': Rosa abyssinica
          '2008': Rosa gallica
          '2009': Rosa pulverulenta
          '2010': Rosa rubiginosa
          '2011': Rosa rugosa
          '2012': Rubus idaeus
          '2013': Rubus leucodermis
          '2014': Rubus nepalensis
          '2015': Rubus odoratus
          '2016': Rubus pungens
          '2017': Rubus rosifolius
          '2018': Rubus spectabilis
          '2019': Rudbeckia fulgida
          '2020': Rudbeckia laciniata
          '2021': Ruellia ciliatiflora
          '2022': Ruellia drummondiana
          '2023': Ruellia floribunda
          '2024': Ruellia patula
          '2025': Ruellia simplex
          '2026': Ruellia tuberosa
          '2027': Rumex acetosa
          '2028': Rumex crassus
          '2029': Rumex hydrolapathum
          '2030': Rumex lapponicus
          '2031': Rumex obtusifolius
          '2032': Rumex pulcher
          '2033': Rumex tuberosus
          '2034': Rumex venosus
          '2035': Ruschia dichroa
          '2036': Russelia equisetiformis
          '2037': Ruta graveolens
          '2038': Sabal bermudana
          '2039': Sabatia gentianoides
          '2040': Sabulina rubella
          '2041': Sagina nodosa
          '2042': Sagittaria latifolia
          '2043': Salicornia europaea
          '2044': Salicornia neei
          '2045': Salix acutifolia
          '2046': Salix atrocinerea
          '2047': Salix aurita
          '2048': Salix babylonica
          '2049': Salix discolor
          '2050': Salix eleagnos
          '2051': Salix herbacea
          '2052': Salix myrsinifolia
          '2053': Salix petiolaris
          '2054': Salix polaris
          '2055': Salix purpurea
          '2056': Salix silesiaca
          '2057': Salsola paulsenii
          '2058': Salsola tragus
          '2059': Salvia aegyptiaca
          '2060': Salvia aethiopis
          '2061': Salvia carduacea
          '2062': Salvia coccinea
          '2063': Salvia oppositiflora
          '2064': Salvia pineticola
          '2065': Salvia pratensis
          '2066': Salvia rosmarinus
          '2067': Salvia verbascifolia
          '2068': Salvia viridis
          '2069': Salvia vitifolia
          '2070': Salvinia cucullata
          '2071': Sambucus ebulus
          '2072': Sambucus nigra
          '2073': Sambucus racemosa
          '2074': Sanguisorba officinalis
          '2075': Sanicula epipactis
          '2076': Sanicula europaea
          '2077': Sanicula trifoliata
          '2078': Sapium glandulosum
          '2079': Sapium haematospermum
          '2080': Saponaria officinalis
          '2081': Sarcobatus baileyi
          '2082': Sarcomphalus amole
          '2083': Sarcomphalus mistol
          '2084': Satyrium kitimboense
          '2085': Satyrium longicauda
          '2086': Saxifraga carpetana
          '2087': Saxifraga debilis
          '2088': Saxifraga granulata
          '2089': Saxifraga seguieri
          '2090': Saxifraga stolonifera
          '2091': Saxifraga valdensis
          '2092': Scabiosa columbaria
          '2093': Scabiosa ochroleuca
          '2094': Scadoxus multiflorus
          '2095': Scaevola angustata
          '2096': Scaevola taccada
          '2097': Scandia geniculata
          '2098': Scaphyglottis imbricata
          '2099': Schizachyrium niveum
          '2100': Schizachyrium sanguineum
          '2101': Schizaea dichotoma
          '2102': Schlagintweitia intybacea
          '2103': Schoenoplectus acutus
          '2104': Schoenus nigricans
          '2105': Scilla verna
          '2106': Scirpoides holoschoenus
          '2107': Scirpus longii
          '2108': Scirpus ternatanus
          '2109': Sclerocactus wrightiae
          '2110': Scolopia mundii
          '2111': Scrophularia cretacea
          '2112': Scrophularia frutescens
          '2113': Scrophularia nodosa
          '2114': Scrophularia rubricaulis
          '2115': Scrophularia rupestris
          '2116': Scrophularia smithii
          '2117': Scutellaria alpina
          '2118': Scutellaria galericulata
          '2119': Scutellaria tuberosa
          '2120': Sebaea aurea
          '2121': Securidaca longepedunculata
          '2122': Sedum acre
          '2123': Sedum candollei
          '2124': Sedum confusum
          '2125': Sedum sexangulare
          '2126': Sedum spathulifolium
          '2127': Selago setulosa
          '2128': Selenicereus setaceus
          '2129': Selinum alatum
          '2130': Sempervivum ciliosum
          '2131': Sempervivum ruthenicum
          '2132': Sempervivum tectorum
          '2133': Senecio brasiliensis
          '2134': Senecio candidans
          '2135': Senecio ceratophylloides
          '2136': Senecio cyaneus
          '2137': Senecio falklandicus
          '2138': Senecio lanceus
          '2139': Senecio lividus
          '2140': Senecio magnificus
          '2141': Senecio nemorensis
          '2142': Senecio vagus
          '2143': Senecio varicosus
          '2144': Senecio variifolius
          '2145': Senna didymobotrya
          '2146': Senna occidentalis
          '2147': Senna reticulata
          '2148': Serapias parviflora
          '2149': Sesbania bispinosa
          '2150': Sesbania cannabina
          '2151': Sesbania virgata
          '2152': Seseli krylovii
          '2153': Seseli seseloides
          '2154': Sesuvium portulacastrum
          '2155': Setaria viridis
          '2156': Sherardia arvensis
          '2157': Sibbaldia tridentata
          '2158': Sida acuta
          '2159': Sidalcea glaucescens
          '2160': Sidalcea robusta
          '2161': Sieruela maculata
          '2162': Silene acaulis
          '2163': Silene aegyptiaca
          '2164': Silene amoena
          '2165': Silene baccifera
          '2166': Silene bungei
          '2167': Silene dioica
          '2168': Silene gallica
          '2169': Silene littorea
          '2170': Silene nutans
          '2171': Silene uniflora
          '2172': Silene uralensis
          '2173': Silene vulgaris
          '2174': Silphium perfoliatum
          '2175': Silybum marianum
          '2176': Simmondsia chinensis
          '2177': Sinapis alba
          '2178': Siphonochilus puncticulatus
          '2179': Sisymbrium irio
          '2180': Sisymbrium officinale
          '2181': Sisyrinchium angustissimum
          '2182': Sisyrinchium commutatum
          '2183': Sisyrinchium micranthum
          '2184': Smilax anceps
          '2185': Smilax auriculata
          '2186': Smilax walteri
          '2187': Sobralia violacea
          '2188': Sobralia warszewiczii
          '2189': Sobralia xantholeuca
          '2190': Soehrensia spachiana
          '2191': Solanum anceps
          '2192': Solanum betaceum
          '2193': Solanum capsicoides
          '2194': Solanum carolinense
          '2195': Solanum dulcamara
          '2196': Solanum lycopersicum
          '2197': Solanum marginatum
          '2198': Solanum nigrescens
          '2199': Solanum pseudocapsicum
          '2200': Solanum torvum
          '2201': Solanum variabile
          '2202': Solanum viarum
          '2203': Soleirolia soleirolii
          '2204': Solidago canadensis
          '2205': Solidago decurrens
          '2206': Solidago gigantea
          '2207': Sonchus asper
          '2208': Sonchus oleraceus
          '2209': Sonchus palustris
          '2210': Sophora chrysophylla
          '2211': Sorbus americana
          '2212': Sorbus aucuparia
          '2213': Sorghum bicolor
          '2214': Sorocea bonplandii
          '2215': Spartium junceum
          '2216': Spathodea campanulata
          '2217': Spathoglottis plicata
          '2218': Spergularia rubra
          '2219': Spermacoce latifolia
          '2220': Sphagneticola trilobata
          '2221': Spondias mombin
          '2222': Stachys annua
          '2223': Stachys byzantina
          '2224': Stachys germanica
          '2225': Stachys grandidentata
          '2226': Stachys recta
          '2227': Stachys sylvatica
          '2228': Stachytarpheta jamaicensis
          '2229': Staphylea pinnata
          '2230': Stellaria aquatica
          '2231': Stellaria borealis
          '2232': Stenandrium dulce
          '2233': Stenocarpus salignus
          '2234': Stenocereus griseus
          '2235': Stenotis brevipes
          '2236': Stetsonia coryne
          '2237': Sticherus tener
          '2238': Stigmaphyllon emarginatum
          '2239': Stillingia lineata
          '2240': Stipellula capensis
          '2241': Stratiotes aloides
          '2242': Streptocarpus confusus
          '2243': Streptopus amplexifolius
          '2244': Striga asiatica
          '2245': Strobilanthes reptans
          '2246': Strumpfia maritima
          '2247': Strychnos gerrardii
          '2248': Stuckenia pectinata
          '2249': Styphelia discolor
          '2250': Styphelia tenuiflora
          '2251': Styrax officinalis
          '2252': Succisa pratensis
          '2253': Succisella inflexa
          '2254': Swietenia mahagoni
          '2255': Syagrus cearensis
          '2256': Symphonia globulifera
          '2257': Symphyotrichum lateriflorum
          '2258': Symphytum tuberosum
          '2259': Symphytum uplandicum
          '2260': Synelcosciadium carmeli
          '2261': Syngonium podophyllum
          '2262': Syzygium cordatum
          '2263': Syzygium jambos
          '2264': Tabebuia aurea
          '2265': Tabebuia cassinoides
          '2266': Tacazzea apiculata
          '2267': Taenidia integerrima
          '2268': Tagetes tenuifolia
          '2269': Talinum paniculatum
          '2270': Talipariti tiliaceum
          '2271': Tanacetum parthenium
          '2272': Tanacetum vulgare
          '2273': Tapinanthus rubromarginatus
          '2274': Taraxacum officinale
          '2275': Taxus baccata
          '2276': Tecoma fulva
          '2277': Tecoma stans
          '2278': Tecomaria capensis
          '2279': Tectaria incisa
          '2280': Tectona grandis
          '2281': Tephroseris crispa
          '2282': Terminalia brachystemma
          '2283': Terminalia catappa
          '2284': Tetradenia brevispicata
          '2285': Tetradymia nuttallii
          '2286': Tetraena gaetula
          '2287': Tetraena simplex
          '2288': Tetragonia fruticosa
          '2289': Tetrapanax papyrifer
          '2290': Tetraria fimbriolata
          '2291': Tetraria triangularis
          '2292': Teucrium africanum
          '2293': Thalassia testudinum
          '2294': Thalictrum aquilegiifolium
          '2295': Thalictrum isopyroides
          '2296': Thalictrum sparsiflorum
          '2297': Thamnosma montana
          '2298': Thelypteris palustris
          '2299': Theobroma cacao
          '2300': Thermopsis gracilis
          '2301': Thesium commutatum
          '2302': Thesium ebracteatum
          '2303': Thesium humifusum
          '2304': Thesium viridifolium
          '2305': Thespesia populnea
          '2306': Thismia mirabilis
          '2307': Thlaspi arvense
          '2308': Thunbergia alata
          '2309': Thunbergia laurifolia
          '2310': Thymelaea hirsuta
          '2311': Thymelaea passerina
          '2312': Thymelaea tartonraira
          '2313': Thymus lotocephalus
          '2314': Thymus pannonicus
          '2315': Thymus serpyllum
          '2316': Thymus villosus
          '2317': Tilesia baccata
          '2318': Tillandsia butzii
          '2319': Tillandsia capitata
          '2320': Tillandsia caput-medusae
          '2321': Tillandsia elongata
          '2322': Tillandsia fasciculata
          '2323': Tillandsia leiboldiana
          '2324': Tillandsia recurvata
          '2325': Tillandsia streptophylla
          '2326': Tillandsia usneoides
          '2327': Tithonia diversifolia
          '2328': Tolmiea menziesii
          '2329': Torenia anagallis
          '2330': Torenia asiatica
          '2331': Torilis arvensis
          '2332': Torilis japonica
          '2333': Torreyochloa pallida
          '2334': Tournefortia gnaphalodes
          '2335': Toxicoscordion paniculatum
          '2336': Trachymene incisa
          '2337': Tradescantia poelliae
          '2338': Tragopogon porrifolius
          '2339': Traunsteinera globosa
          '2340': Trichocereus macrogonus
          '2341': Trichophorum cespitosum
          '2342': Trichosanthes cucumeroides
          '2343': Trichostema nesophilum
          '2344': Tridax procumbens
          '2345': Tridens flavus
          '2346': Trifolium angustifolium
          '2347': Trifolium arvense
          '2348': Trifolium campestre
          '2349': Trifolium dubium
          '2350': Trifolium hybridum
          '2351': Trifolium medium
          '2352': Trifolium montanum
          '2353': Trifolium pratense
          '2354': Trifolium repens
          '2355': Trifolium resupinatum
          '2356': Trifolium scabrum
          '2357': Triglochin maritima
          '2358': Trillium decumbens
          '2359': Tripolium pannonicum
          '2360': Tripterocalyx crux-maltae
          '2361': Trisetum flavescens
          '2362': Triumfetta semitriloba
          '2363': Trollius europaeus
          '2364': Tropidia curculigoides
          '2365': Tsuga dumosa
          '2366': Tulipa humilis
          '2367': Tulipa suaveolens
          '2368': Tulipa sylvestris
          '2369': Tulista marginata
          '2370': Turnera coerulea
          '2371': Turnera subulata
          '2372': Turnera ulmifolia
          '2373': Turritis glabra
          '2374': Tussilago farfara
          '2375': Tylecodon paniculatus
          '2376': Typha domingensis
          '2377': Typha latifolia
          '2378': Typha orientalis
          '2379': Typhonium roxburghii
          '2380': Ulmus glabra
          '2381': Ulmus mexicana
          '2382': Ulmus minor
          '2383': Umbilicus rupestris
          '2384': Uncarina peltata
          '2385': Urena lobata
          '2386': Urera baccifera
          '2387': Ursinia sericea
          '2388': Urvillea uniloba
          '2389': Utricularia vulgaris
          '2390': Vaccinium floribundum
          '2391': Vaccinium japonicum
          '2392': Vaccinium oxycoccos
          '2393': Vaccinium stenophyllum
          '2394': Vachellia nilotica
          '2395': Valeriana edulis
          '2396': Valeriana officinalis
          '2397': Vasconcellea pubescens
          '2398': Vateria indica
          '2399': Veratrum maackii
          '2400': Veratrum oxysepalum
          '2401': Verbascum galilaeum
          '2402': Verbascum nigrum
          '2403': Verbascum pinnatifidum
          '2404': Verbascum thapsus
          '2405': Verbena californica
          '2406': Verbena montevidensis
          '2407': Verbena officinalis
          '2408': Verbena rigida
          '2409': Vernicia montana
          '2410': Vernonanthura nudiflora
          '2411': Veronica agrestis
          '2412': Veronica anagalloides
          '2413': Veronica cardiocarpa
          '2414': Veronica chamaedrys
          '2415': Veronica fruticans
          '2416': Veronica plantaginea
          '2417': Veronica praecox
          '2418': Veronica scutellata
          '2419': Veronica serpyllifolia
          '2420': Veronica syriaca
          '2421': Veronica teucrium
          '2422': Vesper montanus
          '2423': Viburnum cassinoides
          '2424': Viburnum lantana
          '2425': Viburnum lentago
          '2426': Viburnum opulus
          '2427': Viburnum plicatum
          '2428': Vicia dumetorum
          '2429': Vicia pisiformis
          '2430': Vicia sativa
          '2431': Vicia sepium
          '2432': Vicia venosa
          '2433': Vicia villosa
          '2434': Victoria amazonica
          '2435': Vinca major
          '2436': Vincetoxicum hirundinaria
          '2437': Vincetoxicum rossicum
          '2438': Viola acuminata
          '2439': Viola beckwithii
          '2440': Viola biflora
          '2441': Viola elatior
          '2442': Viola kitaibeliana
          '2443': Viola montagnei
          '2444': Viola nuttallii
          '2445': Viola patrinii
          '2446': Viola pedunculata
          '2447': Viola reichenbachiana
          '2448': Viola riviniana
          '2449': Viola sororia
          '2450': Viola tricolor
          '2451': Viola wittrockiana
          '2452': Virgilia oroboides
          '2453': Viscaria vulgaris
          '2454': Vitellaria paradoxa
          '2455': Vitex negundo
          '2456': Vitex rehmannii
          '2457': Vitis gmelinii
          '2458': Vitis rupestris
          '2459': Volkameria mollis
          '2460': Voyria aurantiaca
          '2461': Wahlenbergia gracilis
          '2462': Wahlenbergia marginata
          '2463': Waltheria indica
          '2464': Warszewiczia coccinea
          '2465': Wendlandia uvariifolia
          '2466': Westringia glabra
          '2467': Wilkiea macrophylla
          '2468': Wodyetia bifurcata
          '2469': Wollastonia uniflora
          '2470': Woodsia glabella
          '2471': Wurmbea spicata
          '2472': Xanthorrhoea acanthostachya
          '2473': Xeranthemum cylindraceum
          '2474': Xerochloa imberbis
          '2475': Xerophyllum asphodeloides
          '2476': Ximenia americana
          '2477': Xylomelum angustifolium
          '2478': Youngia japonica
          '2479': Zaluzianskya capensis
          '2480': Zamia erosa
          '2481': Zamioculcas zamiifolia
          '2482': Zantedeschia aethiopica
          '2483': Zanthoxylum rhoifolium
          '2484': Zelkova serrata
          '2485': Zephyranthes candida
          '2486': Zephyranthes concolor
          '2487': Zilla spinosa
          '2488': Zizania texana
          '2489': Zizia aptera
          '2490': Zostera muelleri
  splits:
  - name: train
    num_bytes: 135850179158.875
    num_examples: 300545
  - name: validation
    num_bytes: 45331169320.25
    num_examples: 100182
  - name: test
    num_bytes: 45374513391.25
    num_examples: 100182
  download_size: 226630605159
  dataset_size: 226555861870.375
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---
