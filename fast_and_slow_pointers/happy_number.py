def sum_of_squared_digits(n):
    total_sum = 0
    while n > 0:
        digit = n % 10
        n //= 10
        total_sum += digit ** 2
    return total_sum


def is_happy_number(n):
    slow = n
    fast = sum_of_squared_digits(n)
    while fast != 1 and slow != fast:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))

    if fast == 1:
        return True
    return False


def happy_number_hashset(n):
    seen = set()
    while n != 1:
        n = sum_of_squared_digits(n)
        if n in seen:
            return False
        else:
            seen.add(n)
    return True



print(is_happy_number(1))
print(happy_number_hashset(1))
print("---")
print(is_happy_number(5))
print(happy_number_hashset(5))
print("---")
print(is_happy_number(19))
print(happy_number_hashset(19))
print("---")
print(is_happy_number(25))
print(happy_number_hashset(25))
print("---")
print(is_happy_number(7))
print(happy_number_hashset(7))

