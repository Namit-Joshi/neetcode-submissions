class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        rev = word[::-1]
        if(word == rev):
            return True
        return False