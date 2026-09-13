class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            ptr_one = nums[i]
            for j in range(i+1, len(nums)):
                ptr_two = nums[j]
                if ptr_one + ptr_two == target:
                    return [i, j]