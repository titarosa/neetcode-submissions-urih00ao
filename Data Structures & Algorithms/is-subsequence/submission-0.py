class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t or not s:
            return True

        if not t:
            return False      

        s_len = len(s) 
        t_len = len(t) 

        if s_len > t_len: 
            s, t = t, s

        n = s_len 
        i_s = 0
        i_t = 0

        while i_s < s_len and i_t < t_len: 
            if s[i_s] == t[i_t]:
                i_s += 1
                i_t += 1
                n -= 1
            else:
                i_t += 1 
        return n == 0