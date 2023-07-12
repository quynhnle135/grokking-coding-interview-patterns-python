def check_valid_palindrome(input):
    start = 0
    end = len(input) - 1
    while start < end:
        if input[start] != input[end]:
            return False
        start += 1
        end -= 1
    return True

