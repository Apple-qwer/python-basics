class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = [] 
        for i in nums1: 
            if i in nums2: 
                x.append(i)

        y = list(set(x))
        return y 