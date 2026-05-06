class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float('inf')

        for i in range(len(nums)):
            num = abs(nums[i])
            if num <= len(nums) and nums[num-1] > 0:
                nums[num-1] = nums[num-1] * -1
        
        ans = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                ans+=1
            else:
                break
        return ans
            

        