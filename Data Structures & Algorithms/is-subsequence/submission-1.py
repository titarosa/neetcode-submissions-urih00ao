class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        if not t:
            return False

        s_len, t_len = len(s), len(t)

        i_s, i_t = 0, 0

        while i_s < s_len and i_t < t_len:
            if s[i_s] == t[i_t]:
                i_s += 1
            i_t += 1
        return i_s == s_len
