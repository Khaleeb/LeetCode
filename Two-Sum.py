class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            f = nums[i]
            for j in range(i+1, len(nums)):
                s = nums[j]
                if (s + f == target):
                    return [i, (j)]
