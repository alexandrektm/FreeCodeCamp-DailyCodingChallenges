def classification(temp):

    star_catalog : dict = {
        "M": 0,
        "K": 3700,
        "G": 5200,
        "F": 6000,
        "A": 7500,
        "B": 10000,
        "O": 3000,
    }

    for star_type in list(star_catalog.keys()):
        if temp >= star_catalog[star_type]:
            classification : str = star_type

    return classification

print(classification(2000))