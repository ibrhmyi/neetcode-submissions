class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        i = 0
        j = n-1

        for _ in range(n//2):
            char = s[i]
            s[i] = s[j] 
            s[j] = char
            i+= 1
            j-= 1


        