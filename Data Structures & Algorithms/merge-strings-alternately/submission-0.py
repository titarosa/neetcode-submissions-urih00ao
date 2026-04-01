class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        w1Len = len(word1)
        w2Len = len(word2)

        if w1Len == 0:
            return word2
        
        if w2Len == 0:
            return word1

        newString = []
        w1, w2 = 0, 0

        while w1 < len(word1) and w2 < len(word2):
            newString.append(word1[w1])
            w1 += 1
            newString.append(word2[w2])
            w2 += 1
        if w1 < len(word1):
            newString.extend(word1[w1:])
        elif w2 < len(word2):
            newString.extend(word2[w2:])
        return ''.join(newString)







           




        