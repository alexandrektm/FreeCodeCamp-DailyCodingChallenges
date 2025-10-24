# Speak Wisely, You Must
# Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:
# 
# Words are separated by a single space.
# Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
# Move all words before and including that word to the end of the sentence and:
# Preserve the order of the words when you move them.
# Make them all lowercase.
# And add a comma and space before them.
# Capitalize the first letter of the new first word of the sentence.
# All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
# Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
# For example, given "You must speak wisely." return "Speak wisely, you must."

def wise_speak(sentence):

        words = sentence.strip(".").strip("!").strip("?").split(" ")
        punctuation = sentence[len(sentence)-1]
        key_triggers = ["have","must","are","will","can"]
        cached_list = []

        for index, word in enumerate(words):

                cached_list.append(word.lower())

                if word in key_triggers:

                        result_list = words[index+1:]
                        result_list[len(result_list)-1] = result_list[len(result_list)-1]+","
                        for late_word in cached_list:
                                result_list.append(late_word)
                        result_list[len(result_list)-1] = result_list[len(result_list)-1]+f"{punctuation}"
                        break

        result = " ".join(result_list).capitalize()

        return result

print(wise_speak("You can do it!"))