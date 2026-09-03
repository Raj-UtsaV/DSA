class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return (min(nums1) % 2 != 0) or all(x % 2 == 0 for x in nums1)