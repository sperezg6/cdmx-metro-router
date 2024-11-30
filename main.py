from dataclasses import dataclass
from typing import Dict, List, Set, Tuple, Optional, NamedTuple
from collections import defaultdict, deque

def print_stations_by_line():
    """Imprime todas las estaciones organizadas por línea"""
    lineas = defaultdict(list)
    for estacion in metro_cdmx.keys():
        if ' L' in estacion:
            linea = 'L' + estacion.split(' L')[1]
            nombre_base = estacion.split(' L')[0]
            lineas[linea].append(nombre_base)
    
    print("\nEstaciones por línea:")
    for linea in sorted(lineas.keys()):
        print(f"\n{linea}:")
        for estacion in sorted(lineas[linea]):
            print(f"  - {estacion}")



"""En un diccionario se guardara todo el metro de la CDMX
Se guarda el elemento y las estaciones adyacentes
Cuando una estación es de transbordo, sus estaciones adyancetes incluye la misma estación pero de la otra línea"""
metro_cdmx = {
    # Línea 1 (Observatorio L1 - Pantitlán)
    #Transbordo
    'Pantitlan L1': ['Zaragoza L1', 'Pantitlan L5', 'Pantitlan L9', 'Pantitlan LA'],
    'Zaragoza L1': ['Pantitlan L1', 'Gomez_Farias L1'],
    'Gomez_Farias L1': ['Zaragoza L1', 'Boulevard_Puerto_Aereo L1'],
    'Boulevard_Puerto_Aereo L1': ['Gomez_Farias L1', 'Balbuena L1'],
    'Balbuena L1': ['Boulevard_Puerto_Aereo L1', 'Moctezuma L1'],
    'Moctezuma L1': ['Balbuena L1', 'San_Lazaro L1'],
    #Transbordo
    'San_Lazaro L1': ['Moctezuma L1', 'Candelaria L1', 'San Lazaro LB'],
    #Transbordo
    'Candelaria L1': ['San_Lazaro L1', 'Merced L1', 'Candelaria L4'],
    'Merced L1': ['Candelaria L1', 'Pino_Suarez L1'],
    'Pino_Suarez L1': ['Merced L1', 'Isabel_la_Catolica L1', 'Pino Suarez L2'],
    'Isabel_la_Catolica L1': ['Pino_Suarez L1', 'Salto_del_Agua L1'],
    #Transbordo
    'Salto_del_Agua L1': ['Isabel_la_Catolica L1', 'Balderas L1','Salto_del_Agua L8'],
    #Transbordo
    'Balderas L1': ['Salto_del_Agua L1', 'Cuauhtemoc L1','Balderas L3'],
    'Cuauhtemoc L1': ['Balderas L1', 'Insurgentes L1'],
    'Insurgentes L1': ['Cuauhtemoc L1', 'Sevilla L1'],
    'Sevilla L1': ['Insurgentes L1', 'Chapultepec L1'],
    'Chapultepec L1': ['Sevilla L1', 'Juanacatlan L1'],
    'Juanacatlan L1': ['Chapultepec L1', 'Tacubaya L1'],
    'Tacubaya L1': ['Juanacatlan L1', 'Observatorio L1', 'Tacubaya L7', 'Tacubaya L9'],
    'Observatorio L1': ['Tacubaya L1'],

    # Línea 2 (Cuatro_Caminos L1 - Tasqueña)
    'Cuatro_Caminos L2': ['Panteones L2'],
    'Panteones L2': ['Cuatro_Caminos L2', 'Tacuba L2'],
    #Transborde
    'Tacuba L2': ['Panteones L2', 'Cuitlahuac L2','Tacuba L7'],
    'Cuitlahuac L2': ['Tacuba L2', 'Popotla L2'],
    'Popotla L2': ['Cuitlahuac L2', 'Colegio_Militar L2'],
    'Colegio_Militar L2': ['Popotla L2', 'Normal L2'],
    'Normal L2': ['Colegio_Militar L2', 'San_Cosme L2'],
    'San_Cosme L2': ['Normal L2', 'Revolucion L2'],
    'Revolucion L2': ['San_Cosme L2', 'Hidalgo L2'],
    #Transborde
    'Hidalgo L2': ['Revolucion L2', 'Bellas_Artes L2', 'Hidalgo L3'],
    #Transborde
    'Bellas_Artes L2': ['Hidalgo L2', 'Allende L2','Bellas Artes L8'],
    'Allende L2': ['Bellas_Artes L2', 'Zocalo L2'],
    'Zocalo L2': ['Allende L2', 'Pino_Suarez L2'],
    #Transborde
    'Pino_Suarez L2': ['Zocalo L2', 'San_Antonio_Abad L2', 'Pino_Suarez L1'],
    'San_Antonio_Abad L2': ['Pino_Suarez L2', 'Chabacano L2'],
    #Transborde
    'Chabacano L2': ['San_Antonio_Abad L2', 'Viaducto L2', 'Chabacano L8', 'Chabacano L9'],
    'Viaducto L2': ['Chabacano L2', 'Xola L2'],
    'Xola L2': ['Viaducto L2', 'Villa_de_Cortes L2'],
    'Villa_de_Cortes L2': ['Xola L2', 'Nativitas L2'],
    'Nativitas L2': ['Portales L2', 'Villa_de_Cortes L2'],
    'Portales L2': ['Ermita L2', 'Nativitas L2'],
    #Transborde
    'Ermita L2': ['General_Anaya L2', 'Portales L2', 'Ermita L12'],
    'General_Anaya L2': ['Ermita L2', 'Tasquena L2'],
    'Tasquena L2': ['General_Anaya L2'],

    #Linea 3 (Indios Verdes L3 - Universidad)
    'Indios Verdes L3': ['Deportivo_18_de_Marzo'],
    #Transborde
    'Deportivo_18_de_Marzo L3': ['Indios Verdes L3', 'Potrero L3', 'Deportivo_18_de_Marzo L6'],
    'Potrero L3': ['Deportivo_18_de_Marzo L3','La_Raza L3'],
    #Transborde
    'La_Raza L3': ['Potrero L3', 'Tlaltelolco L3', 'La_Raza L5'],
    'Tlaltelolco L3': ['La_Raza L3', 'Guerrero L3'],
    #Transborde
    'Guerrero L3': ['Tlaltelolco L3', 'Hidalgo L3', 'Buenavista LB', 'Garibaldi'],
    'Hidalgo L3': ['Guerrero L3', 'Juarez L3', 'Hidalgo L2'],
    'Juarez L3': ['Hidalgo L3', 'Balderas L3'],
    'Balderas L3': ['Juarez L3', 'Ninos_heroes L3', 'Balderas L1'],
    'Ninos_heroes L3':['Balderas L3', 'Hospital_General L3'],
    'Hospital_General L3': ['Ninos_heroes L3','Centro_Medico L3'],
    #Transborde
    'Centro_Medico L3': ['Hospital_General L3', 'Etiopia L3', 'Centro_Medico L9'],
    'Etiopia L3': ['Centro_Medico L3','Eugenia L3'],
    'Eugenia L3': ['Etiopia L3', 'Division_del_Norte L3'],
    'Division_del_Norte L3': ['Eugenia L3', 'Zapata L3'],
    'Zapata L3': ['Division_del_Norte L3', 'Coyoacan L3', 'Zapata L12'],
    'Coyoacan L3': ['Zapata L3', 'Viveros L3'],
    'Viveros L3': ['Coyoacan L3', 'Miguel_Angel_de_Quevedo'],
    'Miguel_Angel_de_Quevedo': ['Viveros L3','Copilco L3'],
    'Copilco L3': ['Miguel_Angel_de_Quevedo', 'Universidad L3'],
    'Universidad L3': ['Copilco L3'],

    #Linea 4
    'Martin_Carrera L4': ['Talisman L4', 'Marin_Carrera L6'],
    'Talisman L4': ['Martin_Carrera L4', 'Bondojito L4'],
    'Bondojito L4': ['Talisman L4', 'Consulado L4'],
    'Consulado L4': ['Bondojito L4', 'Canal_del_Norte L4', 'Consulado L5'],
    'Canal_del_Norte L4': ['Consulado L4', 'Morelos L4'],
    'Morelos L4': ['Canal_del_Norte L4', 'Candelaria L4', 'Tepito LB', ''],
    'Candelaria L4': ['Morelos L4', 'Fray_Servando L4', 'Candelaria L1'],
    'Fray_Servando L4': ['Candelaria L4', 'Jamaica L4'],
    'Jamaica L4': ['Fray_Servando L4', 'Santa_Anita', 'Jamaica L9'],
    'Santa_Anita L4': ['Jamaica L4', 'Santa_Anita L8'],

    #Linea 5
    'Pantitlan L5': ['Hangares L5', 'Pantitlan L1', 'Pantitlan L9', 'Pantitlan LA'],
    'Hangares L5': ['Pantitlan L5', 'Terminal_Aerea L5'],
    'Terminal_Aerea L5': ['Hangares L5', 'Oceania L5'],
    'Oceania L5': ['Terminal_Aerea L5', 'Aragon L5'],
    'Aragon L5': ['Oceania L5', 'Eduardo_Molina L5'],
    'Eduardo_Molina L5': ['Aragon L5', 'Consulado L5'],
    'Consulado L5': ['Eduardo_Molina L5', 'Valle_Gomez L5', 'Consulado L4'],
    'Valle_Gomez L5': ['Consulado L5', 'Misterios'],
    'Misterios': ['Valle_Gomez L5', 'La Raza L5'],
    'La Raza L5': ['Misterios', 'Autobuses_del_Norte L5'],
    'Autobuses_del_Norte L5': ['La Raza L5', 'Instituto_del_Petroleo L5'],
    'Instituto_del_Petroleo L5': ['Autobuses_del_Norte L5', 'Politecnico L5', 'Instituto_del_Petroleo L6'],
    'Politecnico L5': ['Instituto del Petroleo L5'],

    #Linea 6
    'El_Rosario L6': ['Tezozomoc L6', 'Aquiles Serdan', 'El_Rosario L7'],
    'Tezozomoc L6': ['El_Rosario L6', 'UAM_Azcapotzalco L6'],
    'UAM_Azcapotzalco L6': ['Tezozómoc', 'Ferreria L6'],
    'Ferreria L6': ['UAM_Azcapotzalco L6', 'Norte_45 L6'],
    'Norte_45 L6': ['Ferreria L6', 'Vallejo L6'],
    'Vallejo L6': ['Norte_45 L6', 'Instituto_del_Petroleo L6'],
    'Instituto_del_Petroleo L6': ['Vallejo L6', 'Lindavista L6'],
    'Lindavista L6': ['Instituto_del_Petroleo L6', 'Deportivo_18_de_Marzo L6'],
    'Deportivo_18_de_Marzo L6': ['Lindavista L6', 'La_Villa L6', 'Deportivo_18_de_Marzo L3'],
    'La_Villa L6': ['Martin_Carrera L6', 'Deportivo_18_de_Marzo L6'],
    'Martin_Carrera L6': ['La_Villa L6'],

    #Linea 7
    'El_Rosario L7': ['Aquiles_Serdan L7', 'El_Rosario L6'],
    'Aquiles_Serdan L7': ['El_Rosario L7', 'Camarones L7'],
    'Camarones L7': ['Aquiles Serdan', 'Refineria L7'],
    'Refineria L7': ['Camarones L7', 'Tacuba L7'],
    'Tacuba L7': ['Refineria L7', 'San_Joaquin L7', 'Tacuba L2'],
    'San_Joaquin L7': ['Tacuba L7', 'Polanco L7'],
    'Polanco L7': ['San_Joaquin L7', 'Auditorio L7'],
    'Auditorio L7': ['Polanco L7', 'Constituyentes L7'],
    'Constituyentes L7': ['Auditorio L7', 'Tacubaya L7'],
    'Tacubaya L7': ['Constituyentes L7', 'San_Pedro_de_los_Pinos L7', 'Tacubaya L1', 'Tacubaya L9'],
    'San_Pedro_de_los_Pinos L7': ['Tacubaya L7', 'San_Antonio L7'],
    'San_Antonio L7': ['San_Pedro_de_los_Pinos L7', 'Mixcoac L7'],
    'Mixcoac L7': ['San_Antonio L7', 'Barranca_del_Muerto L7', 'Mixcoac L12'],
    'Barranca_del_Muerto L7': ['Mixcoac L7'],

    #Linea 8
    'Garibaldi L8': ['Bellas_Artes L8', 'Garibaldi LB'],
    'Bellas_Artes L8': ['Garibaldi L8', 'San_Juan_de_Letran L8'],
    'San_Juan_de_Letran L8': ['Bellas Artes L8', 'Salto_del_Agua L8'],
    'Salto_del_Agua L8': ['San_Juan_de_Letran L8', 'Doctores L8'],
    'Doctores L8': ['Salto_del_Agua L8', 'Obrera L8'],
    'Obrera L8': ['Doctores L8', 'Chabacano L8'],
    'Chabacano L8': ['Obrera L8', 'La Viga', 'Chabacano L9'],
    'La Viga': ['Chabacano L8', 'Santa_Anita L8'],
    'Santa_Anita L8': ['La Viga', 'Coyuya L8', 'Santa Anita L4'],
    'Coyuya L8': ['Santa_Anita L8', 'Iztacalco L8'],
    'Iztacalco L8': ['Coyuya L8', 'Apatlaco L8'],
    'Apatlaco L8': ['Iztacalco L8', 'Aculco L8'],
    'Aculco L8': ['Apatlaco L8', 'Escuadron_201 L8'],
    'Escuadron_201 L8': ['Aculco L8', 'Atlalilco L8'],
    'Atlalilco L8': ['Escuadron_201 L8', 'Iztapalapa L8', 'Atlalilco L12'],
    'Iztapalapa L8': ['Atlalilco L8', 'Cerro_de_la_Estrella L8'],
    'Cerro_de_la_Estrella L8': ['Iztapalapa L8', 'UAM-I L8'],
    'UAM-I L8': ['Cerro_de_la_Estrella L8', 'Constitucion_de_1917 L8'],
    'Constitucion_de_1917 L8': ['UAM-I L8'],

    #Linea 9
    'Pantitlan L9': ['Puebla L9', 'Pantitlan L1', 'Pantitlan L5', 'Pantitlan LA'],
    'Puebla L9': ['Pantitlan L9', 'Ciudad_Deportiva L9'],
    'Ciudad_Deportiva L9': ['Puebla L9', 'Velodromo L9'],
    'Velodromo L9': ['Ciudad_Deportiva L9', 'Mixiuhca L9'],
    'Mixiuhca L9': ['Velodromo L9', 'Jamaica L9'],
    'Jamaica L9': ['Mixiuhca L9', 'Chabacano L9'],
    'Chabacano L9': ['Jamaica L9', 'Lazaro_Cardenas L9', 'Chabacano L2', 'Chabacano L8'],
    'Lazaro_Cardenas L9': ['Chabacano', 'Centro_Medico L9'],
    'Centro_Medico L9': ['Lazaro_Cardenas L9', 'Chilpancingo L9', 'Centro Medico L3'],
    'Chilpancingo L9': ['Centro_Medico L9', 'Patriotismo L9'],
    'Patriotismo L9': ['Chilpancingo L9', 'Tacubaya L9'],
    'Tacubaya L9': ['Patriotismo L9', 'Tacubaya L7', 'Tacubaya L1'],

    #Linea A
    'Pantitlan LA': ['Agricola_Oriental LA', 'Pantitlan L1', 'Pantitlan L5', 'Pantitlan L9'],
    'Agricola_Oriental LA': ['Pantitlan LA', 'Canal_de_San_Juan LA'],
    'Canal_de_San_Juan LA': ['Agricola_Oriental LA', 'Tepalcates LA'],
    'Tepalcates LA': ['Canal_de_San_Juan LA', 'Guelatao LA'],
    'Guelatao LA': ['Tepalcates LA', 'Penon_Viejo LA'],
    'Penon_Viejo LA': ['Guelatao LA', 'Acatitla LA'],
    'Acatitla LA': ['Penon_Viejo LA', 'Santa_Marta LA'],
    'Santa_Marta LA': ['Acatitla LA', 'Los_Reyes LA'],
    'Los_Reyes LA': ['Santa_Marta LA', 'La_Paz LA'],
    'La_Paz LA': ['Los_Reyes LA'],

    #Linea B
    'Buenavista LB': ['Guerrero LB'],
    'Guerrero LB': ['Buenavista LB', 'Garibaldi LB', 'Guerrero L3'],
    'Garibaldi LB': ['Guerrero LB', 'Lagunilla LB', 'Garibaldi L8'],
    'Lagunilla LB': ['Garibaldi LB', 'Tepito LB'],
    'Tepito LB': ['Lagunilla LB', 'Morelos LB'],
    'Morelos LB': ['Tepito LB', 'San_Lazaro LB', 'Morelos L4'],
    'San_Lazaro LB': ['Morelos LB', 'Ricardo_Flores_Magon LB', 'San_Lazaro L1'],
    'Ricardo_Flores_Magon LB': ['San_Lazaro LB', 'Romero_Rubio LB'],
    'Romero_Rubio LB': ['Ricardo_Flores_Magon LB', 'Oceania LB'],
    'Oceania LB': ['Romero_Rubio LB', 'Deportivo_Oceania LB', 'Oceania L5'],
    'Deportivo_Oceania LB': ['Oceania LB', 'Villa_de_Aragon LB'],
    'Villa_de_Aragon LB': ['Deportivo_Oceania LB', 'Nezahualcoyotl LB'],
    'Nezahualcoyotl LB': ['Villa_de_Aragon LB', 'Impulsora LB'],
    'Impulsora LB': ['Nezahualcoyotl LB', 'Rio_de_los_Remedios LB'],
    'Rio_de_los_Remedios LB': ['Impulsora LB', 'Muzquiz LB'],
    'Muzquiz LB': ['Rio_de_los_Remedios LB', 'Ecatepec LB'],
    'Ecatepec LB': ['Muzquiz LB', 'Olimpica LB'],
    'Olimpica LB': ['Ecatepec LB', 'Plaza_Aragon LB'],
    'Plaza_Aragon LB': ['Olimpica LB', 'Ciudad_Azteca LB'],
    'Ciudad_Azteca LB': ['Plaza_Aragon LB'],

    #Linea 12
    'Mixcoac L12': ['Insurgentes_Sur L12', 'Mixcoac L7'],
    'Insurgentes_Sur L12': ['Mixcoac L12', '20_de_Noviembre L12'],
    '20_de_Noviembre L12': ['Insurgentes_Sur L12', 'Zapata L12'],
    'Zapata L12': ['20_de_Noviembre L12', 'Parque_de_los_Venados L12', 'Zapata L3'],
    'Parque_de_los_Venados L12': ['Zapata L12', 'Eje_Central L12'],
    'Eje_Central L12': ['Parque_de_los_Venados L12', 'Ermita L12'],
    'Ermita L12': ['Eje_Central L12', 'Mexicaltzingo L12', 'Ermita L12'],
    'Mexicaltzingo L12': ['Ermita L2', 'Atlalilco L12'],
    'Atlalilco L12': ['Mexicaltzingo L12', 'Culhuacan L12', 'Atlalilco L8'],
    'Culhuacan L12': ['Atlalilco L12', 'San_Andres_Tomatlan L12'],
    'San_Andres_Tomatlan L12': ['Culhuacan L12', 'Lomas_Estrella L12'],
    'Lomas_Estrella L12': ['San_Andres_Tomatlan L12', 'Calle_11 L12'],
    'Calle_11 L12': ['Lomas_Estrella L12', 'Periferico_Oriente L12'],
    'Periferico_Oriente L12': ['Calle_11 L12', 'Tezonco L12'],
    'Tezonco L12': ['Periferico_Oriente L12', 'Olivos L12'],
    'Olivos L12': ['Tezonco L12', 'Nopalera L12'],
    'Nopalera L12': ['Olivos L12', 'Zapotitlan L12'],
    'Zapotitlan L12': ['Nopalera L12', 'Tlaltenco L12'],
    'Tlaltenco L12': ['Zapotitlan L12', 'Tlahuac L12'],
    'Tlahuac L12': ['Tlaltenco L12']
}


# Definir las zonas y subzonas
zonas = {
    "Zona1": {
        "Subzona1": ["Ciudad_Azteca LB", "Plaza_Aragon LB", "Olimpica LB", "Ecatepec LB", "Muzquiz LB", "Rio_de_los_Remedios LB"],
        "Subzona2": ["Impulsora LB", "Nezahualcoyotl LB", "Villa_de_Aragon LB", "Bosque_de_Aragon LB", "Deportivo_Oceania LB", "Oceania L5"]
    },
    "Zona2": {
        "Subzona3": ["Martin_Carrera L6", "Martin_Carrera L4", "Talisman L4", "La_Villa L4"],
        "Subzona4": ["Bondojito L4", "Consulado L5", "Consulado L4", "Valle_Gomez L5", "Canal_del_Norte L4"],
        "Subzona5": ["Misterios L5", "Tlaltelolco L3", "La_Raza L3", "La_Raza L5", "Guerrero LB", "Guerrero L3"],
        "Subzona6": ["Politecnico L5", "Vallejo L6", "Instituto_del_Petroleo L6", "Instituto_del_Petroleo L5", "Autobuses_del_Norte L5", "Norte_45 L6"],
        "Subzona7": ["Indios_Verdes L3", "Deportivo_18_de_Marzo L3", "Deportivo_18_de_Marzo L6", "Lindavista L6", "Potrero L3"]
    },
    "Zona3": {
        "Subzona8": ["Oceania L5", "Oceania LB", "Eduardo_Molina L5", "Aragon L5", "Romero_Rubio LB", "Ricardo_Flores_Magon LB", "Aragon L5", "Deportivo_Oceania LB"],
        "Subzona9": ["Canal_del_Norte L4", "Morelos L4", "Morelos LB", "Tepito LB", "Merced L1", "Candelaria L1", "Candelaria L4", "San_Lazaro LB", "San_Lazaro L1", "Pino_Suarez L2"],
        "Subzona10": ["Moctezuma L1", "Balbuena L1", "Boulevard_Puerto_Aereo L1", "Terminal_Aerea L5", "Velodromo L9"],
        "Subzona11": ["La_Viga L8", "Jamaica L9", "Jamaica L4", "Mixiuhca L9", "Velodromo L9", "Santa_Anita L8", "Santa_Anita L4", "Chabacano L2", "Chabacano L9"],
        "Subzona12": ["Pantitlan L5", "Pantitlan L9", "Pantitlan L1", "Pantitlan LA", "Puebla L9", "Ciudad_deportiva L9", "Zaragoza L1", "Hangares L5", "Gomez_Farias L1", "Agricola_Oriental LA"]
    },
    "Zona4": {
        "Subzona13": ["Agricola_Oriental LA", "Canal_de_San_Juan LA", "Tepalcates LA", "Guelatao LA", "Pantitlan L1", "Pantitlan L5", "Pantitlan L9", "Pantitlan LA"],
        "Subzona14": ["Penon_Viejo LA", "Acatitla LA", "Santa_Marta LA", "Los_Reyes LA", "La_Paz LA"]
    },
    "Zona5": {
        "Subzona15": ["Coyuya L8", "Iztacalco L8", "Apatlalco L8", "Santa_Anita L4", "Santa_Anita L8"],
        "Subzona16": ["Aculco L8", "Escuadron_201 L8", "Atlalilco L12", "Atlalilco L8", "Iztapalapa L8", "Mexicaltzingo L12", "Ermita L2", "Ermita L12"],
        "Subzona17": ["Cerro_de_la_Estrella L8", "UAM-1 L8", "Constitucion_de_1917 L8"],
        "Subzona18": ["Culhuacan L12", "San_Andres_Tomatlan L12", "Lomas_Estrella L12", "Calle_11 L12"],
        "Subzona19": ["Periferico_Oriente L12", "Tezonco L12", "Olivos L12", "Nopalera L12", "Zapotitlan L12", "Tlaltenco L12", "Tlahuac L12"]
    },
    "Zona6": {
        "Subzona20": ["Division_del_Norte L3", "Zapata L3", "Zapata L12", "Parque_de_los_Venados L12", "Eje_Central L12", "Eugenia L3"],
        "Subzona21": ["Mixcoac L12", "Mixcoac L7", "Barranca_del_Muerto L7", "Hospital_20_de_Noviembre L12", "Insurgentes_Sur L12", "Coyoacan L3", "San_Antonio L7"],
        "Subzona22": ["Universidad L3", "Copilco L3", "Miguel_Angel_de_Quevedo L3", "Viveros L3"],
        "Subzona23": ["Nativitas L2", "Portales L2", "Ermita L12", "Ermita L2", "General_Anaya L2", "Tasquena L2", "Mexicaltzingo L12", "Villa_de_Cortes L2"]
    },

    "Zona7": {
        "Subzona24": ["Observatorio L1", "San_Antonio L1", "San_Pedro_de_los_Pinos L7", "Tacubaya L1", "Tacubaya L7", "Tacubaya L9", "Mixcoac L7", "Mixcoac L12"],
        "Subzona25": ["Patriotismo L9", "Chilpancingo L9", "Juancatlan L1", "Chapultepec L1", "Sevilla L1", "Insurgentes L1", "Cuauhtemoc L1", "Chilpancingo L9", "Centro_Medico L3", "Centro_Medico L9"],
        "Subzona26": ["San_Joaquin L7", "Polanco L7", "Auditorio L7", "Constituyentes L7", "Tacuba L7", "Tacuba L2"]
    },

    "Zona8": {
        "Subzona27": ["San_Cosme L2", "Normal L2", "Colegio_Militar L2", "Cuitlahuac L2", "Normal L2"],
        "Subzona28": ["Tacuba L2", "Tacuba L7", "Panteones L2", "Cuatro_Caminos L2", "Refineria L7", "San_Joaquin L7"],
        "Subzona29": ["Camarones L7", "El_Rosario L7", "Aquiles_Serdan L7", "El_Rosario L6", "Tezozomoc L6"],
        "Subzona30": ["Azcapotzalco L6", "Ferreria L6", "Norte_45 L6", "Vallejo L6"]
    },
    "Zona9": {
        "Subzona31": ["Eugenia L3", "Etiopia L3", "Viaducto L2", "Xola L2", "Villa_de_Cortes L2", "Nativitas L2", "Division_del_Norte L3"],
        "Subzona32": ["Centro_Medico L3", "Centro_Medico L9", "Lazaro_Cardenas L9", "Chabacano L2", "Chabacano L8", "Chabacano L8", "La_Viga L1"],
        "Subzona33": ["Hospital_General L3", "Obrera L8", "San_Antonio_Abdad L2", "Ninos_heroes L3", "Doctores L8"],
        "Subzona34": ["Cuathemoc L1", "Balderas L1", "Balderas L3", "Salto_del_Agua L2", "Salto_del_Agua L8", "Isabel_la_Catolica L1", "Pino_Suarez L1", "Pino_Suarez L2", "Merced L1"],
        "Subzona35": ["San_Juan_de_Letran L8", "Juarez L3", "Zocalo L2", "Allende L2", "Bellas_Artes L2", "Bellas_Artes L3"],
        "Subzona36": ["Hidalgo L2", "Hidalgo L3", "Revolucion L2", "San_Cosme L2", "Normal L2"],
        "Subzona37": ["Buenavista LB", "Guerrero L3", "Guerrero LB", "Garibaldi L8", "Garibaldi LB", "Lagunilla LB", "Tepito LB", "Tlaltelolco L3"]
    }
}

BASE_CASES = [
    # Caso 1: Universidad a Pantitlán (Sur a Este)
    {
        "origen": "Universidad L3",
        "destino": "Pantitlan L1",
        "ruta": [
            "Universidad L3", "Copilco L3", "Miguel_Angel_de_Quevedo",
            "Viveros L3", "Coyoacan L3", "Zapata L3", "Division_del_Norte L3",
            "Eugenia L3", "Centro_Medico L3", "Hospital_General L3",
            "Ninos_heroes L3", "Balderas L3", "Balderas L1",
            "Salto_del_Agua L1", "Isabel_la_Catolica L1", "Pino_Suarez L1",
            "Merced L1", "Candelaria L1", "San_Lazaro L1", "Moctezuma L1",
            "Balbuena L1", "Boulevard_Puerto_Aereo L1", "Gomez_Farias L1",
            "Zaragoza L1", "Pantitlan L1"
        ],
        "transbordos": [("Balderas L3", "L3", "L1")],
        "zona_origen": "Zona6",
        "subzona_origen": "Subzona22",
        "zona_destino": "Zona3",
        "subzona_destino": "Subzona12",
        "contador_uso": 100,
        "calificacion_promedio": 4.8
    },
    # Caso 2: Indios Verdes a Tasqueña (Norte a Sur)
    {
        "origen": "Indios Verdes L3",
        "destino": "Tasquena L2",
        "ruta": [
            "Indios Verdes L3", "Deportivo_18_de_Marzo L3", "Potrero L3",
            "La_Raza L3", "Tlaltelolco L3", "Guerrero L3", "Hidalgo L3",
            "Hidalgo L2", "Bellas_Artes L2", "Allende L2", "Zocalo L2",
            "Pino_Suarez L2", "San_Antonio_Abad L2", "Chabacano L2",
            "Viaducto L2", "Xola L2", "Villa_de_Cortes L2", "Nativitas L2",
            "Portales L2", "Ermita L2", "General_Anaya L2", "Tasquena L2"
        ],
        "transbordos": [("Hidalgo L3", "L3", "L2")],
        "zona_origen": "Zona2",
        "subzona_origen": "Subzona7",
        "zona_destino": "Zona6",
        "subzona_destino": "Subzona23",
        "contador_uso": 95,
        "calificacion_promedio": 4.7
    },
    # Caso 3 : El Rosario a Ciudad Azteca (Oeste a Este)
    {
        "origen": "El_Rosario L7",
        "destino": "Ciudad_Azteca LB",
        "ruta": [
            "El_Rosario L7", "Aquiles_Serdan L7", "Camarones L7", 
            "Refineria L7", "Tacuba L7", "San_Joaquin L7", "Polanco L7",
            "Auditorio L7", "Constituyentes L7", "Tacubaya L7",
            "Tacubaya L1", "Juanacatlan L1", "Chapultepec L1",
            "Sevilla L1", "Insurgentes L1", "Cuauhtemoc L1", "Balderas L1",
            "Salto_del_Agua L1", "Isabel_la_Catolica L1", "Pino_Suarez L1",
            "Merced L1", "Candelaria L1", "San_Lazaro L1", "San_Lazaro LB",
            "Morelos LB", "Tepito LB", "Lagunilla LB", "Garibaldi LB",
            "Guerrero LB", "Buenavista LB", "Deportivo_Oceania LB",
            "Bosque_de_Aragon LB", "Villa_de_Aragon LB", "Nezahualcoyotl LB",
            "Impulsora LB", "Rio_de_los_Remedios LB", "Muzquiz LB",
            "Ecatepec LB", "Olimpica LB", "Plaza_Aragon LB", "Ciudad_Azteca LB"
        ],
        "transbordos": [
            ("Tacubaya L7", "L7", "L1"),
            ("San_Lazaro L1", "L1", "LB")
        ],
        "zona_origen": "Zona8",
        "subzona_origen": "Subzona29",
        "zona_destino": "Zona1",
        "subzona_destino": "Subzona1",
        "contador_uso": 85,
        "calificacion_promedio": 4.6
    },
    # Caso 4  Constitución de 1917 a Observatorio (Este a Oeste)
    {
        "origen": "Constitucion_de_1917 L8",
        "destino": "Observatorio L1",
        "ruta": [
            "Constitucion_de_1917 L8", "UAM-I L8", "Cerro_de_la_Estrella L8",
            "Iztapalapa L8", "Atlalilco L8", "Escuadron_201 L8", "Aculco L8",
            "Apatlaco L8", "Iztacalco L8", "Coyuya L8", "Santa_Anita L8",
            "La Viga", "Chabacano L8", "Chabacano L2", "San_Antonio_Abad L2",
            "Pino_Suarez L2", "Zocalo L2", "Allende L2", "Bellas_Artes L2",
            "Hidalgo L2", "Hidalgo L3", "Guerrero L3", "Tlaltelolco L3",
            "La_Raza L3", "Potrero L3", "Deportivo_18_de_Marzo L3",
            "Indios Verdes L3", "Tacubaya L1", "Observatorio L1"
        ],
        "transbordos": [
            ("Chabacano L8", "L8", "L2"),
            ("Hidalgo L2", "L2", "L3"),
            ("Tacubaya L1", "L3", "L1")
        ],
        "zona_origen": "Zona5",
        "subzona_origen": "Subzona17",
        "zona_destino": "Zona7",
        "subzona_destino": "Subzona24",
        "contador_uso": 80,
        "calificacion_promedio": 4.5
    }
]


@dataclass
class Station:
    """Representa una estación del metro con sus propiedades"""
    nombre: str
    lineas: List[str]
    conexiones: List[str]
    zona: str
    subzona: str
    es_transbordo: bool = False

@dataclass
class Caso:
    """Representa un caso almacenado de una ruta"""
    origen: str
    destino: str
    ruta: List[str]
    transbordos: List[Tuple[str, str, str]]  # estación, de_línea, a_línea
    zona_origen: str
    subzona_origen: str
    zona_destino: str
    subzona_destino: str
    contador_uso: int = 0
    calificacion_promedio: float = 0.0

class GestorCasos:
    """
    Gestiona el almacenamiento y recuperación de casos usando árbol de decisión.
    
    Esta clase implementa la parte CBR (Case-Based Reasoning) del sistema:
    1. Mantiene una base de conocimiento de rutas exitosas previas
    2. Organiza los casos en una estructura jerárquica por zonas/subzonas
    3. Permite búsqueda eficiente de casos similares
    4. Mantiene estadísticas de uso y calificaciones de cada caso
    5. Admite la adición de nuevos casos y actualización de existentes
    
    Atributos:
        casos_por_zona: Estructura jerárquica que organiza casos por zona y subzona
                       usando un defaultdict anidado para acceso eficiente
    """
    def __init__(self):
        """
        Inicializa el gestor de casos con una estructura de árbol de decisión vacía
        y carga los casos base predefinidos.
        
        La estructura casos_por_zona usa defaultdict para crear automáticamente
        nuevos niveles en el árbol cuando se accede a zonas/subzonas no existentes.
        """
        self.casos_por_zona = defaultdict(lambda: defaultdict(list))
        self._inicializar_casos_base()
    
    def _inicializar_casos_base(self):
        """
        Inicializa la base de conocimiento con casos predefinidos.
        
        Estos casos base representan rutas comunes y bien conocidas del sistema,
        sirviendo como punto de partida para el razonamiento basado en casos.
        Cada caso base incluye:
        - Estaciones de origen y destino
        - Ruta completa
        - Información de transbordos
        - Zonificación
        - Estadísticas iniciales de uso y calificación
        """
        for caso_base in BASE_CASES:
            caso = Caso(
                origen=caso_base["origen"],
                destino=caso_base["destino"],
                ruta=caso_base["ruta"],
                transbordos=caso_base["transbordos"],
                zona_origen=caso_base["zona_origen"],
                subzona_origen=caso_base["subzona_origen"],
                zona_destino=caso_base["zona_destino"],
                subzona_destino=caso_base["subzona_destino"],
                contador_uso=caso_base["contador_uso"],
                calificacion_promedio=caso_base["calificacion_promedio"]
            )
            self.agregar_caso(caso)

    def agregar_caso(self, caso: Caso):
        """
        Agrega un nuevo caso al árbol de decisión.
        
        El caso se almacena en la estructura jerárquica usando dos niveles de claves:
        1. clave_zona: combina zona origen y destino
        2. clave_subzona: combina subzona origen y destino
        Esto permite una búsqueda eficiente basada en la ubicación geográfica.
        
        Args:
            caso: Instancia de Caso a agregar a la base de conocimiento
        """
        clave_zona = f"{caso.zona_origen}-{caso.zona_destino}"
        clave_subzona = f"{caso.subzona_origen}-{caso.subzona_destino}"
        self.casos_por_zona[clave_zona][clave_subzona].append(caso)

    def buscar_casos(self, zona_origen: str, zona_destino: str, 
                    subzona_origen: str, subzona_destino: str) -> List[Caso]:
        """
        Busca casos similares en la base de conocimiento usando el árbol de decisión.
        
        La búsqueda se realiza jerárquicamente:
        1. Primero filtra por zonas de origen y destino
        2. Luego filtra por subzonas específicas
        Este enfoque permite encontrar rápidamente casos relevantes en áreas geográficas similares.
        
        Args:
            zona_origen: Zona donde inicia la ruta
            zona_destino: Zona donde termina la ruta
            subzona_origen: Subzona específica de origen
            subzona_destino: Subzona específica de destino
            
        Returns:
            Lista de casos que coinciden con los criterios de búsqueda
        """
        clave_zona = f"{zona_origen}-{zona_destino}"
        clave_subzona = f"{subzona_origen}-{subzona_destino}"
        return self.casos_por_zona[clave_zona][clave_subzona]

    def obtener_todos_casos(self) -> List[Caso]:
        """
        Recupera todos los casos almacenados en la base de conocimiento.
        
        Recorre la estructura jerárquica completa y recopila todos los casos,
        independientemente de su ubicación en el árbol de decisión.
        
        Returns:
            Lista con todos los casos almacenados en el sistema
        """
        todos_casos = []
        for zona_casos in self.casos_por_zona.values():
            for subzona_casos in zona_casos.values():
                todos_casos.extend(subzona_casos)
        return todos_casos

    def calificar_caso(self, origen: str, destino: str, calificacion: float):
        """
        Actualiza la calificación de un caso existente.
        
        El método:
        1. Busca el caso específico por origen y destino
        2. Actualiza el contador de uso
        3. Recalcula la calificación promedio considerando la nueva calificación
        
        La calificación promedio se calcula ponderando todas las calificaciones
        recibidas por el caso hasta el momento.
        
        Args:
            origen: Estación de origen del caso
            destino: Estación de destino del caso
            calificacion: Nueva calificación a incorporar (entre 0 y 5)
        """
        for caso in self.obtener_todos_casos():
            if caso.origen == origen and caso.destino == destino:
                # Calcular nuevo promedio ponderado
                total_calif = caso.calificacion_promedio * caso.contador_uso
                caso.contador_uso += 1
                caso.calificacion_promedio = (total_calif + calificacion) / caso.contador_uso
                break

class GestorRutas:
    """
    Implementa el razonamiento basado en modelos con descenso recursivo según el
    paper de Router que utiliza mapas jerárquicos.
    
    Esta clase implementa una estrategia de planificación de rutas que:
    1. Organiza el metro en una estructura jerárquica de zonas y conexiones
    2. Utiliza descenso recursivo para resolver rutas de manera incremental
    3. Maneja tres niveles de planificación: interzonal, zonal e intrazonal
    4. Se inspira en el sistema Router para navegación en campus universitarios
    
    Atributos:
        metro: Diccionario con la red completa del metro
        zonas: Estructura jerárquica de zonas y subzonas
        verbose: Controla la impresión de logs del proceso
        nodo_raiz: Representación jerárquica de alto nivel del sistema
    """
    def __init__(self, metro_network: dict, zonas: dict, verbose=True):
        """
        Inicializa el gestor de rutas y construye el mapa jerárquico.
        
        Args:
            metro_network: Red completa del metro con conexiones
            zonas: Definición de zonas y subzonas
            verbose: Activa/desactiva logs detallados
        """
        self.metro = metro_network
        self.zonas = zonas
        self.verbose = verbose
        self.nodo_raiz = self._construir_mapa_jerarquico()

    def log(self, message: str, level=0):
        """
        Imprime mensajes de log indentados según el nivel de profundidad.
        
        Args:
            message: Mensaje a imprimir
            level: Nivel de indentación (2 espacios por nivel)
        """
        if self.verbose:
            indent = "  " * level
            print(f"\n{indent}>>> {message}")

    def _construir_mapa_jerarquico(self) -> dict:
        """
        Construye una representación jerárquica del sistema de metro.
        
        Similar al mapa esquemático que Router usa para el campus, esta estructura
        captura las conexiones principales entre zonas, ignorando detalles de
        bajo nivel para la planificación inicial.
        
        Returns:
            Diccionario con la estructura jerárquica del metro
        """
        conexiones = self._identificar_conexiones_principales()
        self.log("Construyendo mapa jerárquico")
        self.log(f"Conexiones principales identificadas: {len(conexiones)}")
        
        return {
            "tipo": "raiz",
            "zonas": self.zonas,
            "conexiones_principales": conexiones
        }

    def _identificar_conexiones_principales(self) -> List[Tuple[str, str]]:
        """
        Identifica conexiones de alto nivel entre zonas diferentes.
        
        Análogo a las calles principales en Router, estas conexiones
        representan las rutas principales entre zonas del metro.
        
        Returns:
            Lista de tuplas (zona_origen, zona_destino) representando conexiones
        """
        conexiones = set()
        for estacion, vecinos in self.metro.items():
            zona_actual = self._encontrar_zona(estacion)
            for vecino in vecinos:
                zona_vecino = self._encontrar_zona(vecino)
                if zona_actual != zona_vecino:
                    conexiones.add((zona_actual, zona_vecino))
        return list(conexiones)

    def _encontrar_zona(self, estacion: str) -> str:
        """
        Determina a qué zona pertenece una estación.
        
        Args:
            estacion: Nombre de la estación
            
        Returns:
            Nombre de la zona o 'desconocida' si no se encuentra
        """
        for zona, subzonas in self.zonas.items():
            for subzona, estaciones in subzonas.items():
                if estacion in estaciones:
                    return zona
        return "desconocida"

    def encontrar_ruta_recursiva(self, origen: str, destino: str) -> Optional[List[str]]:
        """
        Implementa el algoritmo principal de búsqueda de rutas usando descenso recursivo.
        
        El método sigue una estrategia similar a Router:
        1. Primero resuelve la ruta a nivel de zonas (alto nivel)
        2. Luego resuelve las transiciones entre zonas (nivel medio)
        3. Finalmente resuelve las rutas dentro de cada zona (bajo nivel)
        
        Args:
            origen: Estación de origen
            destino: Estación de destino
            
        Returns:
            Lista de estaciones que forman la ruta o None si no se encuentra
        """
        self.log("Iniciando búsqueda recursiva")
        
        # 1. Identificar zonas de origen y destino
        zona_origen = self._encontrar_zona(origen)
        zona_destino = self._encontrar_zona(destino)
        self.log(f"Analizando ruta entre Zona {zona_origen} y Zona {zona_destino}", 1)

        # 2. Caso especial: misma zona
        if zona_origen == zona_destino:
            self.log(f"Origen y destino en misma zona ({zona_origen})", 1)
            self.log("Realizando búsqueda intrazonal", 1)
            return self._busqueda_intrazonal(origen, destino)

        # 3. Caso general: zonas diferentes
        self.log("Planeando ruta entre zonas", 1)
        ruta_zonal = self._planear_ruta_interzonal(zona_origen, zona_destino)
        
        if not ruta_zonal:
            self.log("No se encontró ruta entre zonas", 1)
            return None

        self.log(f"Ruta entre zonas encontrada: {' -> '.join(ruta_zonal)}", 1)

        # 4. Resolver detalles de la ruta
        self.log("Resolviendo transiciones entre zonas", 1)
        return self._resolver_transiciones_zonas(origen, destino, ruta_zonal)

    def _busqueda_intrazonal(self, origen: str, destino: str) -> Optional[List[str]]:
        """
        Realiza búsqueda dentro de una misma zona usando BFS.
        
        Similar a la búsqueda exhaustiva que Router usa en nodos hoja,
        este método encuentra la ruta óptima entre estaciones de una misma zona.
        
        Args:
            origen: Estación de origen
            destino: Estación de destino
            
        Returns:
            Lista de estaciones que forman la ruta o None si no se encuentra
        """
        self.log(f"Iniciando búsqueda intrazonal de {origen} a {destino}", 2)
        visitados = set()
        cola = deque([(origen, [origen])])

        while cola:
            actual, ruta = cola.popleft()
            if actual == destino:
                self.log(f"Ruta intrazonal encontrada: {' -> '.join(ruta)}", 2)
                return ruta

            for vecino in self.metro.get(actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, ruta + [vecino]))
        
        self.log("No se encontró ruta intrazonal", 2)
        return None

    def _planear_ruta_interzonal(self, zona_origen: str, zona_destino: str) -> Optional[List[str]]:
        """
        Planifica ruta de alto nivel entre zonas diferentes.
        
        Similar a cómo Router usa el nodo raíz para planear rutas entre áreas grandes,
        este método determina la secuencia de zonas a atravesar.
        
        Args:
            zona_origen: Zona de partida
            zona_destino: Zona de llegada
            
        Returns:
            Lista de zonas a atravesar o None si no hay ruta
        """
        self.log(f"Planeando ruta entre zona {zona_origen} y zona {zona_destino}", 2)
        visitados = set()
        cola = deque([(zona_origen, [zona_origen])])

        while cola:
            zona_actual, ruta = cola.popleft()
            if zona_actual == zona_destino:
                self.log(f"Ruta interzonal encontrada: {' -> '.join(ruta)}", 2)
                return ruta

            for conexion in self._identificar_conexiones_principales():
                if conexion[0] == zona_actual and conexion[1] not in visitados:
                    visitados.add(conexion[1])
                    cola.append((conexion[1], ruta + [conexion[1]]))
        
        self.log("No se encontró ruta interzonal", 2)
        return None

    def _resolver_transiciones_zonas(self, origen: str, destino: str, 
                                   ruta_zonal: List[str]) -> Optional[List[str]]:
        """
        Resuelve el problema de conectar rutas entre diferentes zonas.
        
        Similar a cómo Router resuelve transiciones entre niveles del mapa,
        este método:
        1. Encuentra puntos de conexión entre zonas adyacentes
        2. Construye rutas dentro de cada zona
        3. Conecta las subrutas para formar la ruta completa
        
        Args:
            origen: Estación inicial
            destino: Estación final
            ruta_zonal: Secuencia de zonas a atravesar
            
        Returns:
            Lista completa de estaciones o None si no se puede resolver
        """
        self.log("Iniciando resolución de transiciones", 2)
        ruta_completa = []
        estacion_actual = origen

        # Resolver cada transición entre zonas
        for i in range(len(ruta_zonal) - 1):
            zona_actual = ruta_zonal[i]
            zona_siguiente = ruta_zonal[i + 1]
            
            self.log(f"Buscando transición de Zona {zona_actual} a Zona {zona_siguiente}", 2)
            punto_transicion = self._encontrar_punto_transicion(zona_actual, zona_siguiente)
            
            if punto_transicion:
                self.log(f"Punto de transición encontrado: {punto_transicion}", 3)
                subruta = self._busqueda_intrazonal(estacion_actual, punto_transicion)
                if subruta:
                    self.log(f"Subruta encontrada: {' -> '.join(subruta)}", 3)
                    ruta_completa.extend(subruta[:-1])
                    estacion_actual = punto_transicion
            else:
                self.log(f"No se encontró punto de transición", 3)

        # Conectar con el destino final
        self.log("Conectando con destino final", 2)
        ultima_ruta = self._busqueda_intrazonal(estacion_actual, destino)
        if ultima_ruta:
            self.log("Ruta completa encontrada", 2)
            ruta_completa.extend(ultima_ruta)
            return ruta_completa
        
        self.log("No se pudo completar la ruta", 2)
        return None

    def _encontrar_punto_transicion(self, zona1: str, zona2: str) -> Optional[str]:
        """
        Encuentra una estación que sirve como punto de conexión entre dos zonas.
        
        Args:
            zona1: Primera zona
            zona2: Segunda zona
            
        Returns:
            Nombre de la estación de transición o None si no se encuentra
        """
        self.log(f"Buscando punto de transición entre {zona1} y {zona2}", 3)
        for estacion, vecinos in self.metro.items():
            if self._encontrar_zona(estacion) == zona1:
                for vecino in vecinos:
                    if self._encontrar_zona(vecino) == zona2:
                        self.log(f"Punto de transición encontrado: {estacion}", 3)
                        return estacion
        self.log("No se encontró punto de transición", 3)
        return None

class MetroRouterHibrido:
    """
    Implementación híbrida que combina CBR (Case-Based Reasoning) y razonamiento basado en modelos,
    siguiendo los principios de Router.
    
    Esta clase implementa un sistema de planificación de rutas que:
    1. Primero intenta reutilizar casos previos exitosos (CBR)
    2. Si no encuentra casos adecuados, usa razonamiento basado en modelos
    3. Almacena nuevas soluciones como casos para uso futuro
    
    Atributos:
        gestor_casos: Maneja el almacenamiento y recuperación de casos previos
        gestor_rutas: Implementa el razonamiento basado en modelos
        zonas: Estructura jerárquica de las zonas del metro
        verbose: Controla la impresión de logs del proceso de razonamiento
    """
    def __init__(self, metro_network: dict, zonas: dict, verbose=True):
        """
        Inicializa el router híbrido.
        
        Args:
            metro_network: Diccionario con la red completa del metro
            zonas: Estructura jerárquica de zonas y subzonas
            verbose: Activa/desactiva logs detallados del proceso
        """
        self.gestor_casos = GestorCasos()
        self.gestor_rutas = GestorRutas(metro_network, zonas)
        self.zonas = zonas
        self.verbose = verbose

    def log(self, message: str):
        """
        Imprime mensajes de log del proceso de razonamiento.
        
        Args:
            message: Mensaje a imprimir
        """
        if self.verbose:
            print(f"\n>>> {message}")

    def encontrar_ruta(self, origen: str, destino: str) -> Tuple[Optional[List[str]], str]:
        """
        Método principal que combina CBR y razonamiento basado en modelos
        para encontrar una ruta entre dos estaciones.
        
        El método sigue estos pasos:
        1. Identifica zonas y subzonas de origen y destino
        2. Busca casos similares en la memoria
        3. Si encuentra un caso bueno (calificación >= 4.0), lo reutiliza
        4. Si no, usa razonamiento basado en modelos
        5. Si encuentra una ruta nueva, la almacena como caso
        
        Args:
            origen: Estación de origen
            destino: Estación de destino
            
        Returns:
            Tupla con la ruta encontrada (o None) y el método usado ('caso', 'modelo', 'no_ruta')
        """
        self.log(f"Buscando ruta de {origen} a {destino}")
        
        # 1. Identificar zonas y subzonas para reducir el espacio de búsqueda
        zona_origen = self.gestor_rutas._encontrar_zona(origen)
        zona_destino = self.gestor_rutas._encontrar_zona(destino)
        subzona_origen = self._encontrar_subzona(origen, zona_origen)
        subzona_destino = self._encontrar_subzona(destino, zona_destino)
        
        self.log(f"Origen: Zona {zona_origen}, Subzona {subzona_origen}")
        self.log(f"Destino: Zona {zona_destino}, Subzona {subzona_destino}")

        # 2. Buscar casos similares en la memoria (CBR)
        self.log("Buscando casos similares en la memoria...")
        casos = self.gestor_casos.buscar_casos(
            zona_origen, zona_destino,
            subzona_origen, subzona_destino
        )

        # 3. Analizar casos encontrados
        if casos:
            self.log(f"Se encontraron {len(casos)} casos similares")
            # Seleccionar el caso con mejor calificación
            mejor_caso = max(casos, key=lambda x: x.calificacion_promedio)
            self.log(f"Mejor caso encontrado:")
            self.log(f"- Calificación: {mejor_caso.calificacion_promedio}")
            self.log(f"- Usos previos: {mejor_caso.contador_uso}")
            
            # Reutilizar caso si tiene buena calificación
            if mejor_caso.calificacion_promedio >= 4.0:
                self.log("Caso considerado suficientemente bueno para ser reutilizado")
                return mejor_caso.ruta, "caso"
            else:
                self.log("Caso encontrado no tiene suficiente calificación")
                self.log("Usando razonamiento basado en modelos")
        else:
            self.log("No se encontraron casos similares")

        # 4. Usar razonamiento basado en modelos como respaldo
        self.log("Iniciando razonamiento basado en modelos con descenso recursivo")
        ruta = self.gestor_rutas.encontrar_ruta_recursiva(origen, destino)
        
        if ruta:
            self.log("Ruta encontrada usando modelo")
            # Identificar transbordos para análisis y registro
            transbordos = self._identificar_transbordos(ruta)
            if transbordos:
                self.log(f"La ruta requiere {len(transbordos)} transbordos:")
                for t in transbordos:
                    self.log(f"- En {t[0]}: cambio de {t[1]} a {t[2]}")
            
            # 5. Almacenar nueva ruta como caso para aprendizaje
            self.log("Almacenando nueva ruta como caso para uso futuro")
            nuevo_caso = Caso(
                origen=origen,
                destino=destino,
                ruta=ruta,
                transbordos=transbordos,
                zona_origen=zona_origen,
                subzona_origen=subzona_origen,
                zona_destino=zona_destino,
                subzona_destino=subzona_destino
            )
            self.gestor_casos.agregar_caso(nuevo_caso)
            return ruta, "modelo"

        self.log("No se pudo encontrar una ruta válida")
        return None, "no_ruta"

    def _encontrar_subzona(self, estacion: str, zona: str) -> str:
        """
        Encuentra la subzona a la que pertenece una estación dentro de su zona.
        
        Args:
            estacion: Nombre de la estación
            zona: Zona a la que pertenece la estación
            
        Returns:
            Nombre de la subzona o 'desconocida' si no se encuentra
        """
        for subzona, estaciones in self.zonas[zona].items():
            if estacion in estaciones:
                return subzona
        return "desconocida"

    def _identificar_transbordos(self, ruta: List[str]) -> List[Tuple[str, str, str]]:
        """
        Identifica los puntos donde se requiere cambiar de línea en una ruta.
        
        Para cada par de estaciones consecutivas, verifica si pertenecen
        a diferentes líneas. Si es así, registra un transbordo.
        
        Args:
            ruta: Lista de estaciones que forman la ruta
            
        Returns:
            Lista de tuplas (estacion, linea_origen, linea_destino) para cada transbordo
        """
        transbordos = []
        for i in range(len(ruta) - 1):
            actual = ruta[i]
            siguiente = ruta[i + 1]
            # Extraer números de línea de los nombres de estaciones
            linea_actual = actual.split(' L')[-1] if ' L' in actual else ''
            linea_siguiente = siguiente.split(' L')[-1] if ' L' in siguiente else ''
            # Registrar transbordo si hay cambio de línea
            if linea_actual and linea_siguiente and linea_actual != linea_siguiente:
                transbordos.append((actual, f"L{linea_actual}", f"L{linea_siguiente}"))
        return transbordos
def main():
    """Función principal del sistema de rutas del Metro CDMX.
    Implementa la interfaz de usuario y maneja la interacción con el sistema
    de razonamiento híbrido que combina CBR (Case-Based Reasoning) y 
    razonamiento basado en modelos."""
    
    # Inicializar el router híbrido con el mapa del metro y las zonas definidas
    router = MetroRouterHibrido(metro_cdmx, zonas, verbose=True)
    
    def imprimir_menu():
        """Muestra el menú principal del sistema con las opciones disponibles."""
        print("\n" + "="*50)
        print("Sistema de Rutas del Metro CDMX")
        print("="*50)
        print("1. Buscar ruta")
        print("2. Ver estaciones por línea")
        print("3. Ver estadísticas del sistema")
        print("4. Salir")
        print("="*50)

    def mostrar_estadisticas():
        """Muestra estadísticas del sistema incluyendo:
        - Total de casos base cargados
        - Número de casos utilizados
        - Top 5 de rutas más utilizadas con sus detalles"""
        print("\nEstadísticas del Sistema:")
        print("-" * 30)
        
        # Recolectar todos los casos almacenados en el sistema
        todos_casos = []
        for zona_casos in router.gestor_casos.casos_por_zona.values():
            for subzona_casos in zona_casos.values():
                if isinstance(subzona_casos, list):
                    todos_casos.extend(subzona_casos)
        
        # Calcular estadísticas generales
        total_casos = len(router.gestor_casos.obtener_todos_casos())
        print(f"Total de casos base cargados: {total_casos}")
        
        # Contar casos que han sido utilizados al menos una vez
        casos_usados = sum(1 for caso in todos_casos if caso.contador_uso > 0)
        
        # Mostrar porcentaje de uso si hay casos
        if total_casos > 0:
            porcentaje_uso = (casos_usados / total_casos) * 100
            print(f"Casos utilizados: {casos_usados} ({porcentaje_uso:.1f}%)")
        
        # Mostrar top 5 de rutas más utilizadas
        if casos_usados > 0:
            casos_ordenados = sorted(
                [caso for caso in todos_casos if caso.contador_uso > 0],
                key=lambda x: x.contador_uso,
                reverse=True
            )[:5]
            
            print("\nRutas más utilizadas:")
            for i, caso in enumerate(casos_ordenados, 1):
                print(f"\n{i}. {caso.origen} → {caso.destino}")
                print(f"   Usos: {caso.contador_uso}")
                print(f"   Zona: {caso.zona_origen} → {caso.zona_destino}")
                if caso.calificacion_promedio > 0:
                    print(f"   Calificación: {caso.calificacion_promedio:.1f}/5.0")

    def buscar_ruta():
        """Implementa la funcionalidad de búsqueda de rutas.
        Permite al usuario:
        1. Ver las estaciones disponibles
        2. Ingresar origen y destino
        3. Ver la ruta encontrada con detalles de transbordos y tiempos"""
        
        # Mostrar todas las estaciones disponibles organizadas por línea
        print("\nEstaciones disponibles por línea:")
        for linea, estaciones in router.gestor_rutas.metro.items():
            if ' L' in linea:  # Solo mostrar estaciones con número de línea
                print(f"\n{linea}:")
                print(f"  {', '.join(estaciones)}")

        # Solicitar entrada del usuario
        print("\nFormato de entrada: 'Nombre_Estacion L#' (ejemplo: 'Universidad L3')")
        origen = input("\nIngrese estación de origen: ").strip()
        destino = input("Ingrese estación de destino: ").strip()

        try:
            # Mostrar inicio del proceso de razonamiento
            print("\n" + "="*30)
            print("Iniciando Proceso de Razonamiento")
            print("="*30)
            
            # Buscar la ruta usando el sistema híbrido
            ruta, metodo = router.encontrar_ruta(origen, destino)
            
            # Mostrar resultados
            print("\n" + "="*20)
            print("Resultado Final")
            print("="*20)
            
            if ruta:
                # Mostrar la ruta encontrada y el método utilizado
                print(f"\nRuta encontrada usando razonamiento basado en {metodo}:")
                print("\nSecuencia de estaciones:")
                for i, estacion in enumerate(ruta, 1):
                    print(f"{i}. {estacion}")

                # Identificar y mostrar transbordos necesarios
                transbordos = router._identificar_transbordos(ruta)
                if transbordos:
                    print("\nTransbordos necesarios:")
                    for i, (estacion, linea1, linea2) in enumerate(transbordos, 1):
                        print(f"{i}. En {estacion}: cambiar de {linea1} a {linea2}")

                # Mostrar estadísticas de la ruta
                print(f"\nTotal de estaciones: {len(ruta)}")
                print(f"Total de transbordos: {len(transbordos)}")
                # Calcular tiempo estimado: 2 min por estación + 5 min por transbordo
                tiempo_estimado = len(ruta) * 2 + len(transbordos) * 5
                print(f"Tiempo estimado: {tiempo_estimado} minutos")
            else:
                print("\nNo se encontró una ruta válida entre las estaciones especificadas.")
        except KeyError as e:
            print(f"\nError: Estación no encontrada: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")

    # Bucle principal del programa
    while True:
        imprimir_menu()
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            
            # Procesar la opción seleccionada
            if opcion == "1":
                buscar_ruta()
            elif opcion == "2":
                # Mostrar lista de estaciones por línea
                print("\nEstaciones por línea:")
                for linea, estaciones in router.gestor_rutas.metro.items():
                    if ' L' in linea:
                        print(f"\n{linea}:")
                        print(f"  {', '.join(estaciones)}")
            elif opcion == "3":
                mostrar_estadisticas()
            elif opcion == "4":
                print("\n¡Gracias por usar el Sistema de Rutas del Metro CDMX!")
                break
            else:
                print("\nOpción no válida. Por favor, seleccione una opción del 1 al 4.")
        except Exception as e:
            # Manejo general de errores para mantener el programa en ejecución
            print(f"\nError: {e}")
            print("Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
