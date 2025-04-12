import heapq 
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        x = 0 
        while sum(nums) != 0: 
            y = heapq.heappop(nums)  
            for i in range(len(nums)): 
                nums[i] = nums[i] - y 
            if y != 0: 
                x += 1
        return x