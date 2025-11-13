

def verify(message, key, signature):

    dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26

    }

    message_value = []
    key_value = []

    for char in message:
        
        if char.lower() not in ("abcdefghijklmnopqrstuvwxyz"):
            continue

        value = dictionary[char.lower()]
        if char.isupper():
            value += 26
        message_value.append(value)
        
    m_value = sum(message_value)

    for char in key:

        if char.lower() not in ("abcdefghijklmnopqrstuvwxyz"):
            continue
        
        value = dictionary[char.lower()]
        if char.isupper():
            value += 26
        key_value.append(value)
        
    k_value = sum(key_value)

    signature_calculated = m_value + k_value

    if signature_calculated == signature:
        return True
    else:
        return False