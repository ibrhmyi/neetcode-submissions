class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] +=1
        buckets = [[] for i in range(len(nums)+1)]
        for key, val in dic.items():
            buckets[val].append(key)
        return sum(buckets, [])[-k:]







        