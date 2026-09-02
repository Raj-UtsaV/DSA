"""Canonical solution metadata.

Problem Number: 81
Problem Title: Search in Rotated Sorted Array II
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Duplicate Boundary Shrinking
Canonical URL: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1; right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
        return False
