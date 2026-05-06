class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = [] # This is where we save our matches

        # i, j, left, and right are your d, c, b, and a
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]: continue # Skip duplicates
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                
                # These two pointers (left/right) act as a 'smart' while loop
                left, right = j + 1, n - 1
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        # Found a match! Save it and CONTINUE the search
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move both to find new potential matches for this i and j
                        while left < right and nums[left] == nums[left+1]: left += 1
                        while left < right and nums[right] == nums[right-1]: right -= 1
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1 # Sum too small, move left pointer forward
                    else:
                        right -= 1 # Sum too large, move right pointer backward
        
        return ans