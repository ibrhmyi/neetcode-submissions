class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        m = len(s1)
        need = Counter(s1)
        window = Counter()

        for i in range(len(s2)):
            window[s2[i]] += 1

            if i >= m:
                window[s2[i - m]] -= 1
                if window[s2[i - m]] == 0:
                    del window[s2[i - m]]

            if window == need:
                return True

        return False