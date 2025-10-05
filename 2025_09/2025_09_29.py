def get_longest_word(sentence):

    templ : list = sentence.split(" ")
    big : int = 0
    bigw : str = ""

    for word in templ:

        if big < len(word.strip(".")):
            big = len(word.strip("."))
            bigw = word.strip(".")

    return bigw

print(get_longest_word("This sentence has multiple long words."))