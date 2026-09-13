class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                idx_i = seen[complement]
                idx_j = idx
                return [idx_i, idx_j]
            else:
                seen[value] = idx
