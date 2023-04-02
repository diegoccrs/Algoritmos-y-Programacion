#Diego Caceres 20211110856
def inventory():
    return {
    "pilots":[
        {"name": "Axel Gutierrez", "dni": 29456987, "nacionality":"Venezolano", "salary": 120890.56, "plane_id": 4},
        {"name": "Alejandro Ricaurte", "dni": 24505208, "nacionality":"Español", "salary": 102851.11, "plane_id": 1},
        {"name": "Vannesa Hernandez", "dni": 14616010, "nacionality":"Ingles", "salary": 99500.99, "plane_id": 2},
        {"name": "Demian Specter", "dni": 131315159, "nacionality":"Argentino", "salary": 150400.79, "plane_id": 3}
    ],
    "passengers":[
        {"name": "Elizabeth Bermudez", "dni": 27965616, "nacionality":"Frances", "t_seat": "first class", "travel_id": 101, "p_confirmed": False},
        {"name": "Panchito De La Costa", "dni": 67005698, "nacionality": "Mexicano", "t_seat": "first class", "travel_id": 101, "p_confirmed": False},
        {"name": "Pepito Linguini", "dni": 11045678, "nacionality":"Italiano", "t_seat": "Turist", "travel_id": 102, "p_confirmed": False},
        {"name": "Kirishimoto Akira", "dni": 10248098, "nacionality":"Japones", "t_seat": "first class", "travel_id": 103, "p_confirmed": False},
        {"name": "Camila Rodriguez", "dni": 0, "nacionality":"Austriaco", "t_seat": "Turist", "travel_id": 103, "p_confirmed": False},
        {"name": "Willians Robbinson", "dni": 23451362, "nacionality":"EstadoUnidense", "t_seat": "Turist", "travel_id": 104, "p_confirmed": False},
        {"name": "Kiyoshi Kurosaki", "dni": 99799899, "nacionality":"Japones", "t_seat": "Turist", "travel_id": 108, "p_confirmed": False},
        {"name": "Timoteo De Abreu", "dni": 12356987, "nacionality":"Portugues", "t_seat": "Turist", "travel_id": 109, "p_confirmed": False},
        {"name": "Madhur Rathod", "dni": 81525461, "nacionality":"Saudita", "t_seat": "Turist", "travel_id": 107, "p_confirmed": False},
        {"name": "Dariana Azuaje", "dni": 29325789, "nacionality":"Venezolano", "t_seat": "first class", "travel_id": 108, "p_confirmed": False},
        {"name": "Pemo Yajuri", "dni": 15456987, "nacionality":"Venezolano", "t_seat": "first class", "travel_id": 103, "p_confirmed": False},
        {"name": "Andromeda De Texas", "dni": 28038234, "nacionality":"Griego", "t_seat": "Turist", "travel_id": 102, "p_confirmed": False},
        {"name": "Homero Addams", "dni": 10109001, "nacionality":"Español", "t_seat": "Turist", "travel_id": 102, "p_confirmed": False},
        {"name": "Dmitry Nepomnyashchy", "dni": 29023456, "nacionality":"Ruso", "t_seat": "Turist", "travel_id": 101, "p_confirmed": False},
        {"name": "Edwina Müller", "dni": 280324291, "nacionality":"Aleman", "t_seat": "Turist", "travel_id": 105, "p_confirmed": False},
        {"name": "Arthur Davies", "dni": 28000103, "nacionality":"Suizo", "t_seat": "first class", "travel_id": 106, "p_confirmed": False},
        {"name": "SeoJoon Uzumaki", "dni": 19019203, "nacionality":"SurCoreano", "t_seat": "first class", "travel_id": 101, "p_confirmed": False},
        {"name": "Woo Young", "dni": 11378405, "nacionality":"SurCoreano", "t_seat": "Turist", "travel_id": 106, "p_confirmed": False}
    ],
    "plane":[
        { "id": 1, "model": "Boeing 737", "t_model":"Pasillo único", "flights": [101,103]},
        { "id": 2, "model": "Airbus A380", "t_model":"Pasillo Doble", "flights": [102,105,106]},
        { "id": 3, "model": "Boeing 757", "t_model":"Pasillo único", "flights": [104,108]},
        { "id": 4, "model": "Ilyushin Il-96", "t_model":"Pasillo Doble", "flights": [107,109]}
    ],
    "travel":[
        {"travel_id": 101, "dep_city": "Miami", "des_city": "Madrid", "scheculed": "09:45 am"},
        {"travel_id": 102, "dep_city": "La Habana", "des_city": "Caracas", "scheculed": "07:00 am"},
        {"travel_id": 103, "dep_city": "Moscu", "des_city": "Tokyo", "scheculed": "05:30 pm"},
        {"travel_id": 104, "dep_city": "Marrakech-Safí", "des_city": "Ciudad de México", "scheculed": "11:00 am"},
        {"travel_id": 105, "dep_city": "Lisboa", "des_city": "Miami", "scheculed": "07:15 pm"},
        {"travel_id": 106, "dep_city": "Kabul", "des_city": "Zúrich​", "scheculed": "10:30 am"},
        {"travel_id": 107, "dep_city": "Buenos Aires", "des_city": "Rio de Janeiro", "scheculed": "01:15 pm"},
        {"travel_id": 108, "dep_city": "Bogota", "des_city": "Shanghai", "scheculed": "03:45 pm"},
        {"travel_id": 109, "dep_city": "Caracas", "des_city": "Lisboa", "scheculed": "08:00 am"}
    ]
}

def body():
    return {"name":None,"dni":None,"nacionality":None}