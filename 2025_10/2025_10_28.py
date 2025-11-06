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

print(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]))