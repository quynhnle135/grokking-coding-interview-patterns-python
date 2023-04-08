# import re
#
# s = "I am a human being"
#
# res1 = re.sub('a', '_', s)
# print(res1)
#
# s1 = "   hello educative   good morning"
# res2 = re.sub(" +", " ", s1.strip())
# print(res2)
# # print(s1.strip())
# res2 = list(res2)
# print(res2)

my_string = "hello educative"
reversed_string = my_string[::-1]
word = reversed_string[0:3]
print(word)
start = 0
end = len(reversed_string) - 1
stack = []
# while start < len(reversed_string):
#     while reversed_string[end] != " " and end < len(reversed_string):
#         end += 1
#     words =