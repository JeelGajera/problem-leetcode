class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()

        for i in range(n-3):
            for  j in range(i+1,n-2):
                left, right = j+1, n-1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        quadruplets = [nums[i], nums[j], nums[left], nums[right]]
                        res.add(tuple(quadruplets))
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1

        return [list(quadruplets) for quadruplets in res]