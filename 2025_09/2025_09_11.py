import os

def reverse_sentence(sentence):

    wordlist = sentence.split(" ")
    sanit_wlist = []

    o = 1
    for elem in wordlist:

        if o < len(wordlist):

            if (elem == " " or elem == "") and (wordlist[o] == "" or wordlist[o] == " "):
                sanit_wlist=sanit_wlist
            else:
                sanit_wlist.append(elem)

        else:
            sanit_wlist.append(elem)

    finalist = []

    i = (len(sanit_wlist)-1)
    for elem in sanit_wlist:

        finalist.append(sanit_wlist[i])
        finalist.append(" ")
        i -= 1

    finalist.pop(len(finalist)-1)
    result="".join(finalist)
    return result

os.system("cls")
print(reverse_sentence("! world hello"))