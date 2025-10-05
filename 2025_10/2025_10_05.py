def has_exoplanet(readings):

    average_reading : float = 0
    sum_readings : int = 0
    does_have_exo : bool = False

    luminosity_catalog = {
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
        "G":16,
        "H":17,
        "I":18,
        "J":19,
        "K":21,
        "L":22,
        "M":23,
        "N":24,
        "O":25,
        "P":26,
        "Q":27,
        "R":28,
        "S":29,
        "T":30,
        "U":31,
        "V":32,
        "W":33,
        "X":34,
        "Y":35,
        "Z":36,
        }

    for read_unit in readings:

        if read_unit not in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return "Error!"
    
        sum_readings += luminosity_catalog[read_unit]

    average_reading = sum_readings / len(readings)

    for read_unit in readings:

        if luminosity_catalog[read_unit] <= (0.8*(average_reading)):
            does_have_exo = True
            break

    if does_have_exo:
        return True
    else:
        return False

print(has_exoplanet("9AB98AB9BC98A"))