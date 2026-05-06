class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        for i in range(0,len(nums)):
            if nums[i] > 0:
                if nums[i] == ans:
                    ans += 1
        return ans
        