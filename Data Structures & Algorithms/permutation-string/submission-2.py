class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        for i in range(len(s2)):
            keys = s1
            count = 0

            for j in range(i, len(s2)):
                if s2[j] in keys:
                    keys = keys.replace(s2[j], "", 1)
                    count += 1

                    if count == n:
                        return True
                else:
                    break

        return False