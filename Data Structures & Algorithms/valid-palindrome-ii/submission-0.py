class Solution:
    def validPalindrome(self, s: str) -> bool:
        def almostPalindrome( i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i +=1
                j -=1
            return True

        start, end = 0 , len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return almostPalindrome(start + 1, end) or almostPalindrome(start, end - 1)
            start +=1
            end -=1
        return True
        