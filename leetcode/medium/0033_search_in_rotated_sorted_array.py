"""Canonical solution metadata.

Problem Number: 33
Problem Title: Search in Rotated Sorted Array
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search
Study Tags: Sorted-Half Detection
Canonical URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: left = mid + 1
                else: right = mid - 1
        return -1
