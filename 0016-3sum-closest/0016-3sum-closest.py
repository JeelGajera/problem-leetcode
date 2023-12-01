class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        current_dif = float('inf')
        closest = 0
        for i in range(len(nums)-1):
            left = i + 1
            right = len(nums)-1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res == target:
                    return res
                elif res < target:
                    if current_dif > target - res:
                        current_dif = target - res
                        closest = res
                    left += 1
                else:
                    if current_dif > res - target:
                        current_dif = res - target
                        closest = res
                    right -= 1
        return closest