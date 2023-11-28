class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        for i in range(n-2):
            left,right = i+1, n-1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    res.add(tuple(triplet))

                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in res]