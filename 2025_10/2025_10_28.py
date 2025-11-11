# Navigator
# On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.
# 
# Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:
# 
# You always start on the "Home" page, which will not be included in the commands array.
# Valid commands are:
# "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
# "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
# "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".

def navigate(commands):

        place = "Home"
        back = ""
        forward = ""

        for element in commands:

                if element == "Back":
                        if back != "":
                                forward = place
                                place = back

                elif element == "Forward":
                        if forward != "":
                                back = place
                                place = forward

                place_command = element.split()

                if place_command[0] == "Visit":
                        forward = ""
                        back = place
                        place = " ".join(place_command[1::])
                        continue


        return place


def navigate(commands):

        place_list = ["Home"]
        pointer = 0

        for element in commands:

                if element == "Back":
                        if pointer > 0:
                                pointer -= 1

                if element == "Forward":
                        if pointer < (len(place_list)-1):
                                pointer += 1

                place_command = element.split()

                if place_command[0] == "Visit":

                        place_list = place_list[0:(pointer+1)]

                        place_list.append(" ".join(place_command[1::]))
                        pointer = (len(place_list)-1)

        result = place_list[pointer]

        return result


print(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]))