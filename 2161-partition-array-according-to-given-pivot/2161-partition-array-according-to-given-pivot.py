class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        equal = []
        greater = []
        for i in nums:
            if i < pivot:
                lesser.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)

        return lesser + equal + greater