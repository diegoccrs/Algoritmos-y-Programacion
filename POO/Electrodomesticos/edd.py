def inventory():
    return {
"washer":
[
{"cod_p": "AEX-200918", "price": 551.99, "brand": "Whirlpool",

"color": "Blanca", "capacity": 17},

{"cod_p": "GHT-191214", "price": 409.00, "brand": "LG", "color":

"Gris", "capacity": 15}
],
"microwave":
[
{"cod_p": "FGE-220708", "price": 109.01, "brand": "Daewoo", "color":

"Blanco", "digital": False},

{"cod_p": "PEP-210123", "price": 201.50, "brand": "Frigilux",

"color": "Negro", "digital": True}
],
"fridge":
[
{"cod_p": "HYW-180909", "price": 280.98, "brand": "Electrolux",

"color": "Plateado", "cooler": False, "comp": 5},
{"cod_p": "IUO-201020", "price": 405.99, "brand": "Samsung", "color":
"Azul pastel y rosado", "cooler": True, "comp": 8}
],
"blender":
[
{"cod_p": "OWO-191111", "price": 42.05, "brand": "Oster", "color":

"Plateado", "cup": "Cristal", "speeds": 3},

{"cod_p": "XAT-221230", "price": 17.99, "brand": "Philips", "color":

"Blanco", "cup": "Plastico", "speeds": 2}
]
}

def body():
    return {"cod_p": None, "price": None, "brand": None, "color": None}