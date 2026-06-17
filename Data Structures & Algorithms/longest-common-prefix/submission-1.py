class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=lambda x: len(x))
        output = ""

        for i in range(len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i]:
                    return output
            output += strs[0][i]
        return output



        
        