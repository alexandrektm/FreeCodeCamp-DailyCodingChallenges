# Email Validator
# Given a string, determine if it is a valid email address using the following constraints:
# 
# It must contain exactly one @ symbol.
# The local part (before the @):
# Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
# Cannot start or end with a dot.
# The domain part (after the @):
# Must contain at least one dot.
# Must end with a dot followed by at least two letters.
# Neither the local or domain part can have two dots in a row.

# Check for @ to divide into local and domain. in domain, if check @, False. (V)
# In local, if check not in list, False. (V)
# In local, if starts with dot, False. If upon seeing @, last was dot, False. (V)
# In domain, needs at least one dot, or False. (V)
# Once done, check OG string for ending in dot followed by two letters. (V)
# If two dots in a row anywhere, False. (V)

def validate(email):


    if email[0] == ".":
        return False

    if "@" not in email:
        return False


    isDomain : bool = False

    for index, character in enumerate(email):

        if character == ".":
            if email[index-1] == ".":
                return False

        if character == "@":
            if isDomain == True:
                return False
            if email[index-1] == ".":
                return False
            isDomain = True
            continue
        
        if (isDomain == False) and character.lower() not in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9",".","_","-"):
            return False
        

    for index, character in enumerate(email[::-1]):
        
        if character == ".":
            if index >= 2:
                break
            return False

        if not (character.isalpha()):
            return False
        

    return True

print(validate("aslf.ewue@mail.m"))