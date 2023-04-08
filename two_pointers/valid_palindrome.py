def validPalindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA", "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test case #", i +1)
        print("-" * 100)
        print("\tThe input string is ", test_cases[i], "ang the length of the string is ", len(test_cases[i]))
        print("\nIs it a palindrome? ", validPalindrome(test_cases[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()


# s1 = "abba"
# print(validPalindrome(s1))
#
# s2 = "abcd"
# print(validPalindrome(s2))
