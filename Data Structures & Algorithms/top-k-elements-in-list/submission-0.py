class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] +=1
        return heapq.nlargest(k, dic, key=dic.get)




        