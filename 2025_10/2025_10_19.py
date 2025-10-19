# HTML Attribute Extractor
# Given a string of a valid HTML element, return the attributes of the element using the following criteria:
# 
# You will only be given one element.
# Attributes will be in the format: attribute="value".
# Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
# Return attributes in the order they are given.
# If no attributes are found, return an empty array.

def extract_attributes(element):

    potential_attribute = []
    result_list = []
    inside_quotes : bool = False

    for character in element:

        if character == " " and not inside_quotes:
            potential_attribute = []
        elif character == "=":
            continue

        elif character == '"' and not inside_quotes:
            potential_attribute.append(", ")
            inside_quotes = True
        elif character == '"':
            result_list.append("".join(potential_attribute))
            inside_quotes = False

        else:
            potential_attribute.append(character)

    return result_list

print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))


# MAYBE BETTER VERSION, more COMPACT, less SIGHT-READABLE:


def extract_attributes(element):

    potential_attribute = []
    result_list = []
    inside_quotes : bool = False

    for character in element:

        if character == " " and not inside_quotes:
            potential_attribute = []

        elif character == '"':
            if inside_quotes:
                result_list.append("".join(potential_attribute))
            else:
                potential_attribute.pop()
                potential_attribute.append(", ")
            inside_quotes = not inside_quotes

        else:
            potential_attribute.append(character)

    return result_list

print(extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>'))
