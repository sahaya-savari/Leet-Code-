class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        rev_num = 0

        while x > 0:
            digit = x % 10
            rev_num = rev_num * 10 + digit
            x = x // 10

        return original == rev_num

