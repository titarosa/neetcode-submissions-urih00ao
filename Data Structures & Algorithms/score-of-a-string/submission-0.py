class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        charSum = 0
        i = 0

        while i < len(s) - 1:
           diff = ord(s[i]) - ord(s[i+1])
           charSum += abs(diff)
           i += 1
        return charSum


        