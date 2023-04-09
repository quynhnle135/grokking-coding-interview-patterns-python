class Solution:
    def validPalindrome(self, s):
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.verify(s, low + 1, high) or self.verify(s, low, high - 1)
        return True

    def verify(self, s,  low, high):
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False
        return True


my_solution = Solution()
print(my_solution.validPalindrome(s="abcda"))

