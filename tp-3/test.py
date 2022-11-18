a = {
    "===MEALS": {
        "codes": {"M02": {"name": "Beef Korean Noodle", "price": "56000"}},
        "names": {"Beef Korean Noodle": {"code": "M02", "price": "56000"}}
    },
    "===DRINKS": {
        "codes": {"D02": {"name": "Golden Glow", "price": "30000"}},
        "names": {"Golden Glow": {"code": "D02", "price": "30000"}}
    },
    "===TOPPINGS": {
        "codes": {"T02": {"name": "Edamame", "price": "10000"}},
        "names": {"Edamame": {"code": "T02", "price": "10000"}}
    }
}

merged = {}
for i in a.values():
    merged = {**merged, **i['names']}
print(merged)
