class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        for c in s:
            if c in smap:
                smap[c] += 1
            else:
                smap[c] = 1
        
        tmap = {}
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else:
                 tmap[c] = 1
        
        return smap == tmap

        