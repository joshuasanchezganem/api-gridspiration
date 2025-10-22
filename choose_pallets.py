import pandas as pd

dicc_colores = {
        "#f4f5ea": ["Crisol", "001-01"],
        "#fcd8a1": ["Cava", "046-03"],
        "#915c4d": ["BBQ", "080-05"],

        "#e7eee7": ["Blanco Amanecer", "BlcoA-01"],
        "#feebcf": ["Yute", "053-02"],
        "#904033": ["Rojo Indio", "Rojín-01"],

        "#f7f6e4": ["Curry", "026-01"],
        "#ebe0ca": ["Campaña", "Cham-02"],
        "#f0b1c1": ["Julieta", "094-03"],

        "#ebe0ca": ["Blanco Ostión", "BIOs-01"],
        "#cf672e": ["Tejado", "066-07"],
        "#f7cce0": ["Mascada", "101-02"],

        "#42b359": ["Pastisal", "217-06"],
        "#eeede4": ["Soraya", "252-01"],
        "#b5b6a8": ["Gamella", "286-03"],

        "#668f6b": ["Midas", "224-05"],
        "#4e3c39": ["Mastín", "258-07"],
        "#b3cdc9": ["Julius", "293-02"],

        "#6e9b75": ["Mikado", "231-04"],
        "#654941": ["Castañuelas", "265-06"],
        "#c8d9de": ["Rayito", "300-01"],

        "#a13559": ["Amor Platónico", "114-07"],
        "#dccfe5": ["Neblina", "149-02"],
        "#54a9cd": ["Embarcadero", "183-04"],

        "#cb5491": ["Fascinación", "121-06"],
        "#dfe1e6": ["Maison", "156-01"],
        "#75c3d7": ["Bou", "190-03"],

        "#946589": ["Morgana", "128-05"],
        "#393f6f": ["Magneto", "162-07"],
        "#a2dadd": ["Infinito", "197-02"],

        "#c39ec3": ["Balerina", "135-04"],
        "#286ab0": ["Damisela", "169-06"],
        "#c2e1de": ["Madrigal", "204-01"],

        "#eaeaac": ["Chai", "283-03"],
        "#7b6c5d": ["Sonsonete", "272-05"],
        "#34333b": ["Catrín", "306-07"],

        "#f5f6d3": ["Bata", "245-02"],
        "#9a9682": ["Ajolote", "279-04"],
        "#45474a": ["Portafolio", "313-06"],

        "#f8efbb": ["Paja", "740"],
        "#f7dcb1": ["Crema", "712"],
        "#f1ecde": ["Blanco Apio", "736"],

        "#fae4a4": ["Amarillo Alegre", "774"],
        "#f6bc72": ["Amarillo Napolitano", "792"],
        "#f6e4c5": ["Marfil", "730"],

        "#ffdd66": ["Canario", "726"],
        "#eb935a": ["Tangerina", "790"],
        "#ecc690": ["Durazno", "770"],

        "#fece00": ["Amarillo Concentrado", "797"],
        "#d7683e": ["Naranja Concentrado", "715"],
        "#c69853": ["Mostaza", "714"],

        "#c1e5e9": ["Nitrógeno", "178-01"],
        "#bdd7d4": ["Verde Agua", "766"],
        "#c0cfba": ["Verde Manzana", "758"],

        "#91b9d5": ["Azul Cielo", "744"],
        "#a6c8c0": ["Verde Suave", "748"],
        "#7fa273": ["Ficus", "L3-11"],

        "#3e4e78": ["Azul Rey", "724"],
        "#01566f": ["Verde Bosque", "720"],
        "#a7a9ae": ["Gris Francés", "718"],

        "#e9e5db": ["Blanco Ostión", "764"],
        "#f3caa9": ["Salmón", "798"],
        "#dbb09f": ["Palo de Rosa", "716"],

        "#f0e0cb": ["Champaña", "776"],
        "#ecc5a4": ["Salmón Intenso", "723"],
        "#d47a79": ["Rosa Mexicano", "786"],

        "#dfc8ae": ["Piñón", "752"],
        "#f0b1b9": ["Niña", "089-05"],
        "#d4c7de": ["Pastelería", "142-02"],

        "#cdbca5": ["Beige", "708"],
        "#ce5d48": ["Rojo Cardenal", "710"],
        "#8f6b8f": ["Bella", "120-05"],

        "#846b5e": ["Cocoa", "728"],
        "#91543e": ["Rojo Indio", "732"],
        "#664760": ["Vid", "135-07"],

        "#519ac9": ["Azul Olimpia", "706"],
        "#71b6cc": ["Trópical", "772"],
        "#e6eae7": ["Blanco Amanecer", "756"],

        "#4f4775": ["Azul Colonial", "784"],
        "#017999": ["Turquesa", "722"],
        "#c1bfb9": ["Gris Perla", "760"],

        "#e1f2e8": ["ADALID", "210-01"],
        "#f1f5dd": ["FRUTAL", "226-02"],
        "#f1e5dd": ["PAVO", "048-01"],

        '#acdbd7': ['DIVINO', '202-02'],
        '#ced8c9': ['NÍSPERO', '228-02'],
        '#e5cfc6': ['CANELÓN', '267-01'],

        '#b3dacd': ['ORIGAMI', '211-02'],
        '#c1d0c7': ['SÁNDALO', '224-02'],
        '#bac1cc': ['CHUZA', '316-02'],

        "#f8eccd": ["CÁLIZ", "038-02"],
        "#fbe5e5": ["VIDA", "086-01"],
        "#f4e4ef": ["DIANA", "138-01"],

        '#f4ddbd': ['PROVOLONE', '043-02'],
        '#f7cbca': ['NONNA', '087-02'],
        '#ccc1cd': ['HORTENSIA', '148-02'],

        '#ffe6e0': ['TIRAMISÚ', '067-01'],
        '#ead4d4': ['DINASTÍA', '083-01'],
        'dbeff9': ['GOTA', '183-01'],

        '#fbd8c3': ['VALLA', '059-02'],
        '#c69a89': ['SEGOVIA', '079-02'],
        '#b9cfe6': ['ÓRBITA', '170-02'],

        '#fad4c1': ['MELÓN TROPICAL', '301'],
        '#edb9cb': ['PETUNIA', '097-02'],
        '#d9bcda': ['AZUCENA', 'A2-03'],

        '#f7a89d': ['BICHO', 'F2-06'],
        '#ed5272': ['SUEÑO', 'D1-11'],
        '#b24b9c': ['MARIPOSA', 'B1-09'],

        '#f16e59': ['CANGREJO', 'F2-09'],
        '#ee463d': ['ROJO', '314'],
        '#a6a4d0': ['CONFETI', 'T1-06'],

        '#d0382b': ['NARANJA', '315'],
        '#85322e': ['ROJO ÓXIDO', '320'],
        '#37236a': ['VIOLETA', '319'],

        '#7eaed9': ['AEROLITO', '179-02'],
        '#fff5cc': ['TRIGO SOLEADO', '305'],
        '#f7f3ed': ['BLANCO CHANTILLY', '306'],

        '#015f8e': ['VISHNÚ', '179-05'],
        '#ffcd00': ['AMARILLO', '316'],
        '#f4ebde': ['MARFIL EGIPCIO', '303'],

        '#222c62': ['AZUL', '318'],
        '#dad054': ['ZOO', 'K2-09'],
        '#fff5e6': ['ARENA MEDITERRÁNEA', '304'],

        '#d4caca': ['MERLUZA', 'H5-03'],
        '#6e9b59': ['APIO', 'L3-10'],
        '#e6c872': ['CREMA DULCE', '039-04'],

        '#878e92': ['MICRÓFONO', '312-03'],
        '#154733': ['VERDE', '317'],
        '#926929': ['AMARILLO ÓXIDO', '321'],

        '#eaa9ba': ['EUNICE', '101-03'],
        '#caaacb': ['TETERA', '120-03'],
        '#cee2ef': ['OBELISCO', '176-01'],

        '#ef5373': ['GUAYABA', '093-05'],
        '#6c2579': ['FIESTA', 'A1-12'],
        '#90c5e7': ['AZUL CIELO', '11-11'],

        '#d9252d': ['ROJO', '11-21'],
        '#ada9cd': ['MAGISTRAL', '152-03'],
        '#27637e': ['DARDO', '180-05'],

        '#7e2721': ['ROJO ÓXIDO', '11-29'],
        '#492c6c': ['MARRAKECH', 'T1-13'],
        '#182857': ['AZUL HIDALGO', '11-23'],

        '#acd8af': ['SÉPALO', '219-03'],
        '#fff1d9': ['MARFIL', '11-01'],
        '#fee9d8': ['CREMA', '11-08'],

        '#2f8d43': ['ESMERALDA', '219-05'],
        '#f7d894': ['VAINILLA', '033-04'],
        '#ffcf85': ['CHABACANO', '11-18'],

        '#a2dbcf': ['CÚSPIDE', '206-02'],
        '#f6ac3d': ['ABEJORRO', '12-10'],
        '#f59933': ['PANQUÉ', '049-05'],

        '#35b9a5': ['VERDE AGUAMARINA', '11-19'],
        '#e3d1c1': ['BEIGE', '11-09'],
        '#fdfaf3': ['BLANCO PERLA', '11-20'],

        '#015644': ['VERDE PINO', '11-22'],
        '#c08e28': ['AMARILLO SIENA', '11-25'],
        '#927d77': ['CRUTÓN', '273-04'],

        '#ffe8b6': ['NATILLA', '12-04'],
        '#facdb7': ['JENGIBRE', 'F2-04'],
        '#e2c1db': ['ORQUÍDEA', 'B1-03'],

        '#f8de8c': ['TRIGO', 'I2-08'],
        '#f79f7c': ['XALAPA', 'F2-07'],
        '#c47baa': ['HADA', 'B2-06'],

        '#fee4c5': ['MACADAMIA', 'G1-02'],
        '#f9dee1': ['CHIQUITÍN', 'D1-01'],
        '#cccae3': ['BRISILIA', 'S1-04'],

        '#ffce85': ['GALLETA', 'H2-08'],
        '#f8c2ce': ['BOQUITAS', 'D2-03'],
        '#aaa4d0': ['PEZ', 'S1-08'],

        '#f6ad68': ['CASTOR', 'G2-08'],
        '#dd7d8f': ['ARIES', 'D3-06'],
        '#5ea2ca': ['VAQUERO', 'P3-08'],

        '#dcecf4': ['VELERO', 'Q2-01'],
        '#ecf2c3': ['PINCEL', 'K1-04'],
        '#ececed': ['VODKA TONIC', 'L5-02'],

        '#7fbfd0': ['PULPO', 'P1-06'],
        '#e6ea7e': ['LIMA', 'K1-07'],
        '#cfc2a6': ['RASTA', 'J4-03'],

        '#72d0d0': ['OLA', 'O1-06'],
        '#b9cb90': ['ESPERANZA', 'L3-06'],
        '#b3b4b6': ['MARMOLEADO', 'L5-08'],

        '#a6d5e8': ['AZUL RIVIERA', '14-14'],
        '#c5e5cf': ['VERDE HORIZONTE', '14-03'],
        '#f8e5bf': ['BAMBÚ', '14-05'],

        '#60a8d8': ['AZUL APOLO', '14-13'],
        '#afdaa7': ['VALENTINA', '218-03'],
        '#f7e3c5': ['ARENA', '14-15'],

        '#3791ce': ['AZUL PALERMO', '14-17'],
        '#aeddcc': ['VERDE MENTA', '14-01'],
        '#fedaaf': ['GAMUZA', '14-04'],

        '#b8c4c0': ['GRIS ORIENTAL', '14-09'],
        '#92d3c9': ['VERDE MÓNACO', '14-12'],
        '#faf0a8': ['VAINILLA', '14-07'],

        '#98a3ad': ['ALAMBRE', '315-03'],
        '#2bb9a1': ['TURQUESA', '14-19'],
        '#f6e95f': ['AMARILLO', '14-18'],

        '#facabd': ['ROSA ÍNTIMO', '14-10'],
        '#fbe8de': ['TIRAMISÚ', '067-01'],
        '#cdc2ae': ['CHICLE', '14-06'],

        '#f8b0aa': ['ROSA TAPATÍO', '14-11'],
        '#fac9b2': ['SALMÓN', '14-22'],
        '#7a1f1f': ['ROJO ÓXIDO', '14-21'],

        '#f27f89': ['ROJO GRIEGO', '14-20'],
        '#fabd9e': ['SALMÓN PROFUNDO', '14-23'],
        '#513724': ['CAFÉ COLOMBIA', '14-16'],

        '#fae9ce': ['AMARANTO', 'I2-01'],
        '#fbd5da': ['QUESITO', 'D2-02'],
        '#e7daeb': ['SEURAT', 'T1-02'],

        '#f9daa9': ['MANTEQUILLA', 'I2-03'],
        '#f7b4bd': ['BRISAS', 'D2-05'],
        '#cfb8d3': ['DA SILVA', 'A4-04'],

        '#fde1d4': ['HINDÚ', 'F2-02'],
        '#e8c8c5': ['DINASTÍA', 'D3-02'],
        '#cde6ef': ['GRIEGO', 'P1-02'],

        '#fac6ad': ['TORONJA', 'F2-05'],
        '#d69892': ['ANTIGUO', 'D3-05'],
        '#a4bdda': ['ORIÓN', 'Q1-05'],

        '#eee4f1': ['YO-YO', '136-01'],
        '#b8dfcd': ['VERDE FLORIDO', '70-02'],
        '#f8ebca': ['MARFIL', '70-07'],

        '#cccae4': ['CHIFLÓN', '155-02'],
        '#acdccd': ['TURQUESA ANDALUCÍA', '70-10'],
        '#f6e0a6': ['CREMA CLÁSICO', '70-05'],

        '#d4ecf7': ['CLÍMAX', '186-01'],
        '#ecf5e7': ['PEPINO', 'L3-02'],
        '#e6dac5': ['AVELLANA', 'I4-04'],

        '#b6dae9': ['AZUL MARBELLA', '70-06'],
        '#c9e3bc': ['VERDE ALPES', '70-04'],
        '#d6c29f': ['CAFÉ CAPUCHINO', '70-09'],

        '#fceae3': ['CREMOSO', '078-01'],
        '#f2d0d9': ['MOCAMBO', '102-01'],
        '#f3ede2': ['NUBE', '70-08'],

        '#fbd8be': ['PENÉLOPE', '063-02'],
        '#f8c6c8': ['ROSA POMPOSO', '70-03'],
        '#e6dad9': ['CANELÓN', '267-01'],

        '#f7bca3': ['SALMÓN CLÁSICO', '70-98'],
        '#5f2219': ['TERRACOTA', '70-11'],
        '#b9bbc0': ['ESPÁTULA', '312-02'],

        '#c2e9ea': ['TECHNO', 'N3-01'],
        '#e4e97b': ['LIMA', 'K1-07'],
        '#e0e5e9': ['COLUMBUS', 'M5-01'],

        '#528eb5': ['MAZATLÁN', 'Q1-06'],
        '#539050': ['FICUS', 'L3-11'],
        '#878b8c': ['KIOSCO', 'L5-09'],

        '#143d66': ['AZUL LISBOA', '3312'],
        '#214327': ['VERDE LATINO', '3313'],
        '#686864': ['GRIS NAVAL', '3304'],

        '#162133': ['AZUL ROYAL', '3315'],
        '#1d2721': ['VERDE SELVA', '3314'],
        '#d7d7d7': ['ALUMINIO', '3320'],

        '#965225': ['AMARILLO ÓXIDO', '3310'],
        '#512517': ['PERUANO', 'F4-14'],
        '#2d2121': ['CAFÉ SIENA', '3308'],

        '#fbe1ae': ['NATILLA', 'I2-04'],
        '#f4dea6': ['POCHOCIO', 'J3-03'],
        '#d92530': ['NARANJA', '3306'],

        '#fee7c8': ['MARITZA', 'H2-01'],
        '#f4b335': ['AMARILLO', '3307'],
        '#b22830': ['BERMELLÓN', '3303'],

        '#e6d3c3': ['IVORY', 'G4-01'],
        '#fd8305': ['AMARILLO TOLEDO', '3311'],
        '#7f2529': ['ROJO CEDRO', '3309'],

        '#e8e62e': ['LIMÓN NEÓN', '3352'],
        '#f26423': ['MANDARINA NEÓN', '3355'],

        '#0baf4c': ['VERDE NEÓN', '3354'],
        '#ec2128': ['NARANJA NEÓN', '3351'],
        '#ec1e4a': ['CEREZA NEÓN', '3353'],

        '#243e88': ['AZUL NEÓN', '3356'],
        '#e92228': ['ROJO NEÓN', '3357'],
        '#af7529': ['ARAGÓN', 'J3-12'],
}

dicc_colores_2025 = {
    '#bbb5a8': ['Codium', '277-03'],
    '#e2dbd3': ['Tepache', '272-01'],
    '#c4d2cb': ['Piedra de Río', '290-01'],
    '#a1b1ab': ['Ladera', '289-03'],
    '#778b7e': ['Arcilla Verde', '289-04'],
    '#614844': ['Minotauro', '263-05'],
    '#d65a49': ['Diamantina', '082-06'],
    '#e29ba2': ['Remolacha', '091-04'],
    '#c92f51': ['Zapatilla', '101-07'],
    '#dad9d2': ['Esmalte Acrilico Aluminio', ''],
    '#d9e060': ['Bambú', '297-05'],
    '#4c4b5a': ['Mensajero', '310-06'],
    '#00a6ae': ['Tulúm', '01-10'],
    '#98b8e1': ['Amanecer', '165-03'],
    '#7d5387': ['Mus', '143-06'],
    '#d34b71': ['Carisma', '097-06'],
    '#f8b4bc': ['Infancia', '089-03'],
    '#f9e3ec': ['Inocencia', '099-01'],
    '#d8d3cd': ['Marmol', 'H5-04'],
    '#e9cfb7': ['Lino', 'G4-09'],
    '#c6ac9b': ['Istmo', '068-03'],
    '#917067': ['Equipal', '265-04'],
    '#d38c5b': ['Hermes', 'G3-09'],
    '#5f7381': ['Danés', 'P5-13'],
    '#3c4d63': ['Cobalto', 'R-12'],
    '#8d927d': ['Tampil', '287-04'],
    '#ebd889': ['Polen', 'J3-07'],
    '#cfc9c1': ['Ostra', '273-02'],
    '#cda394': ['Chanchito', '076-03'],
    '#e29a80': ['Mecedora', '075-04'],
    '#b59874': ['Mejorana', '052-04'],
    '#7c6041': ['Comex 100 Metal Rustic Oro 131', 'Oro 131'],
    '#355562': ['Kartell', 'P4-13'],
    '#3b463d': ['Hortal', '290-07'],
    '#cdde60': ['Ciénega', '233-05'],
    '#eaeebb': ['Punta Mita', 'K3-04'],
}

colores_2026 = {
    # Colores de TRAMA SAGRADA
    '#C7D7E0': ['Cielito Lindo', '297-01'],
    '#5A4545': ['Arándano', '104-07'],
    '#6D5F5A': ['Chia', 'D4-10'],
    '#CFAA56': ['Flor de Loto', 'I3-10'],
    '#9C8263': ['Cuero', 'G4-10'],
    '#A46D56': ['Navajo', 'E3-11'],
    '#A75F5B': ['Chamoy', 'D3-09'],
    '#9EA38A': ['Prado', 'K4-08'],
    '#E3E1D7': ['Beso de Coco', '271-01'],

    # Colores de INFINITO TORNASOL
    '#f3e4eb': ['Flor de Campo', '115-01'],
    '#dfe9ed': ['Alma', 'P5-01'],
    '#a05a70': ['Fieltro', '103-06'],
    '#2e7172': ['Laberinto', '200-06'],
    '#99b2a5': ['Asturias', 'M4-06'],
    '#bfc5d1': ['Selenio', '306-02'],
    '#4c505d': ['Romo', '306-06'],
    '#7b454b': ['Granate', 'B3-14'],
    '#ba7276': ['Épsilon', '091-05'],
    
    # Colores de MÁS SALSITA (POR FAVOR)
    '#e3ded1': ['Sancocho', '056-01'],
    '#da6842': ['Travieso', '073-07'],
    '#894547': ['Borgoña', '095-07'],
    '#859971': ['Escarola', '228-05'],
    '#f7d663': ['Giner', 'J2-09'],
    '#ad804c': ['Albaricoque', '047-07'],
    '#c25b76': ['Carisma', '097-06'],
    '#2d5156': ['Caimán', '199-07'],
    '#354654': ['Gigante', '184-07'],
    
    # Colores de OXIDACIÓN ATEMPORAL
    '#a0624d': ['Matope', '076-06'],
    '#b9aaa2': ['Teriyaki', '269-03'],
    '#5d4251': ['Xoconoxtle', '128-07'],
    '#bfc4b0': ['Hiedra', 'L4-03'],
    '#dddee2': ['Yeso', '310-01'],
    '#ce9d41': ['Azabache', 'I2-13'],
    '#a37d6e': ['Corcho', '080-04'],
    '#768f7d': ['Sábila', 'M4-09'],
    '#4e4e4eff': ['Martillo', '312-06']
}

palette = [
    'Trama Sagrada',
    'Infinito Tornasol',
    'Más Salsita (Por Favor)',
    'Oxidación Atemporal',
]

def choose_pallete(type_pal: bool) -> pd.DataFrame:
    if type_pal:
        df = pd.DataFrame.from_dict(colores_2026, orient='index', columns=['Nombres', 'Pantone']).reset_index()
        # Renombrar la columna de las llaves
        df = df.rename(columns={'index': 'Hexadecimal'})
        df['Paleta'] = df.index // 9
        # Asignar valores específicos por grupo
        df['Paleta'] = df['Paleta'].map(lambda x: palette[x % len(palette)])
        lista_de_colores = list(colores_2026.keys())
    else:
        df = pd.DataFrame.from_dict(dicc_colores, orient='index', columns=['Nombres', 'Pantone']).reset_index()
        # Renombrar la columna de las llaves
        df = df.rename(columns={'index': 'Hexadecimal'})
        df['Paleta'] = 'No asignada'
        lista_de_colores = list(dicc_colores.keys())
    
    return df, lista_de_colores
