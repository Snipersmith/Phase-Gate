words = "abecd"
words_2 = "efd"


def reverse_word(words):

    reversed_word = ""
    for char in words:
        reversed_word = char + reversed_word
    return reversed_word



def add_second_word(first, second):


    return reverse_word(first) + second

print(add_second_word(words, words_2))

