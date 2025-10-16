# HTML Tag Stripper
# Given a string of HTML code, remove the tags and return the plain text content.
# 
# The input string will contain only valid HTML.
# HTML tags may be nested.
# Remove the tags and any attributes.
# For example, '<a href="#">Click here</a>' should return "Click here".

def strip_tags(html):

    isReading : bool = True
    result_register = []

    for character in html:

        if character == "<":
            print(character)
            print("opening")
            isReading = False
        elif character == ">":
            print(character)
            print("closing")
            isReading = True
        else:

            if isReading == True:
                result_register.append(character)

    result = "".join(result_register)

    return result


print(strip_tags('<img src="cat.jpg" alt="Cat">'))