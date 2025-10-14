# Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:
# 
# The given sentences will always contain the same number of words.
# Words are separated by a single space and will only contain letters.
# The value of each word is the sum of its letters.
# Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
# A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
# Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
# A word wins if its value is greater than the opposing word's value.
# The team with more winning words is the winner.
# Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.


def battle(our_team, opponent):

    our_words = our_team.split(" ")
    their_words = opponent.split(" ")

    our_strength = {}
    their_strength = {}

    our_wins : int = 0
    their_wins : int = 0

    i = 0

    character_values = {
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
        "z": 26,
    }

    def clash(words, strengths,i):

        for word in words:

            word_value : int = 0

            for character in word:

                character_value = character_values[(character).lower()]
                if character == character.upper():
                    character_value *= 2

                word_value += character_value

            strengths[i] = word_value
            i += 1


    clash(our_words,our_strength,i)
    i = 0
    clash(their_words,their_strength,i)
    i = len(list(our_strength))


    for index in list(range(i)):
        if our_strength[index] > their_strength[index]:
            our_wins += 1
        elif our_strength[index] < their_strength[index]:
            their_wins += 1


    if our_wins > their_wins:
        return "We win"
    elif our_wins < their_wins:
        return "We lose"
    else:
        return "Draw"


print(battle("Hello World", "hello word"))