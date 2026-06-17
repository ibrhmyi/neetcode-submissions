class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {i: num for i, num in enumerate(nums)}
        sorted_items = sorted(num_map.items(), key=lambda x: x[1])
        
        i = 0
        j = len(sorted_items) - 1
        
        while i < j:
            current_sum = sorted_items[i][1] + sorted_items[j][1]
            
            if current_sum == target:
                return sorted([sorted_items[i][0], sorted_items[j][0]])
            elif current_sum > target:
                j -= 1 
            else:
                i += 1                
        return []