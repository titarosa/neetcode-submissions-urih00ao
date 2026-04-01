class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        currentWindow = 0
        result = currentWindow

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            if s[right] not in seen:
                seen.add(s[right])
                currentWindow = right - left + 1
                result = max(result, currentWindow)
          
        return result 



        