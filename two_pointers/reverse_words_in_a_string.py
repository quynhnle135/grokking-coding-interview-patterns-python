import re

def reverse_word(input_str, start, end):
    while start < end:
        temp = input_str[start]
        input_str[start] = input_str[end]
        input_str[end] = temp
        start += 1
        end -= 1

def reverse_words_in_a_string(sentence):
    sentence = re.sub(" +", " ", sentence.strip())
    sentence = list(sentence)
    str_len = len(sentence)
    reverse_word(sentence, 0, str_len - 1)
    start = end = 0
    while start < str_len:
        while end < str_len and sentence[end] != " ":
            end += 1
        reverse_word(sentence, start, end - 1)
        start = end = end + 1

    return "".join(sentence)


print(reverse_words_in_a_string("hello educative"))
print(reverse_words_in_a_string("the sky is blue"))