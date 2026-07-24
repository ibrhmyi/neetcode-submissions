class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        

        for word in strs:
            wordkey = [0] * 26
            for l in word:
                wordkey[ord(l) - ord('a')] +=1
            dic[tuple(wordkey)].append(word)
        return list(dic.values())
