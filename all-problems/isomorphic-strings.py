
# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping_s = {}
        mapping_t = {}
        n = len(s)
        for i in range(n):
            ch_s = s[i]
            ch_t = t[i]
            mp_s = mapping_s.get(ch_s, '')
            mp_t = mapping_t.get(ch_t, '')

            if mp_s == '' and mp_t == '':
                mapping_s[ch_s] = ch_t
                mapping_t[ch_t] = ch_s
            elif mp_s != '' and mp_t != '':
                if mp_s != ch_t:
                    print(mapping_s, mapping_t)
                    return False
            else:
                return False
            
        return True
        
