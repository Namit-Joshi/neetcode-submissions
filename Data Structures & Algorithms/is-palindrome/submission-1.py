class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        st = ""

        for ch in s:
            if (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9'):
                st += ch

        rev = st[::-1]

        if st == rev:
            return True
        
        return False
        