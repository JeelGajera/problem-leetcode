class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def bin_search(arr, val):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left+right)//2
                mid_val = nums[mid]
                if mid_val == val:
                    return mid
                elif val < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        return bin_search(nums, target)