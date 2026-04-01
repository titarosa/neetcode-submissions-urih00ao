class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            start, end = 0, len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True

        start, end = 0, len(s) -1

        while start < end:
            if s[start] != s[end]:
                return isPalindrome(s[start+1:end+1]) or isPalindrome(s[start:end])
            else:
                start +=1
                end -=1
        return True
        
        

        
 
