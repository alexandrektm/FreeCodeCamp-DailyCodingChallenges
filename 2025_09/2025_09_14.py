import os

def get_words(paragraph):

    paragraph=paragraph.split(" ")
    new_arr = []
    dict = {}

    for word in paragraph:
        if word == " ":
            new_arr=new_arr
        elif "," in word or "." in word or "!" in word:
            lword = list(word)
            lword.pop(len(lword)-1)
            word="".join(lword)
            new_arr.append(word.lower())
        else:
            new_arr.append(word.lower())

    for word in new_arr:

        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    ldict = list(dict)
    big = 0
    id = 0
    result = []


    for j in range(3):
        for i in range(len(ldict)):

            if dict[ldict[i]] > big:
                big = dict[ldict[i]]
                big_word = ldict[i]
                id = i

        result.append(big_word)
        big = 0
        ldict.pop(id)
        del dict[big_word]

    return result


os.system("cls")
print(get_words("I like coding. I like testing. I love debugging!"))