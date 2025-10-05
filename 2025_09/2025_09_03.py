def is_pangram(sentence, letters):
    
    result=False
    skip=False
    letters=letters.upper()
    sentence=sentence.upper()
    letters=letters.strip()
    sentence=sentence.strip()
    
    
    for check_letter_a in sentence:
        if check_letter_a == " " or check_letter_a == "." or check_letter_a == "!" or check_letter_a == ",":
            result=True
        elif check_letter_a in letters:
            result=True
        else:
            result=False
            skip=True
            break
     
    for check_letter_b in letters:
        if check_letter_b in sentence and skip==False:
            result=True
        else:
            result=False
            break
            
    return result

print(is_pangram("Hello World!", "helowrd"))