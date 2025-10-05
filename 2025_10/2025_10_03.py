def check_strength(password):


    check_count : int = 0
    contains_special_character : bool = False
    contains_digit : bool = False


    if len(password) >= 8:
        check_count += 1


    upper_password : str = password.upper()
    lower_password : str = password.lower()
    if (password != upper_password) and (password != lower_password):
        check_count += 1


    for character in password:
        if character.isdigit():
            contains_digit : bool = True
        if character in ["!","@","#","$","%","^","&","*"]:
            contains_special_character : bool = True


    if contains_digit:
        check_count += 1
    if contains_special_character:
        check_count += 1


    if check_count < 2:

        return "weak"

    elif 1 < check_count < 4:

        return "medium"

    else:

        return "strong"

print(check_strength("123456"))