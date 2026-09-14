class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        left_product_list = []
        right_product = 1
        right_product_list = [1] * len(nums)
        result_list = []
        for i in nums:
            left_product_list.append(left_product)
            left_product *= i
        for i in range(len(nums)-1, -1, -1):
            right_product_list[i] = right_product
            right_product *= nums[i]
        for i in range(len(nums)):
            result_list.append(right_product_list[i] * left_product_list[i])
        
        return result_list

        


        

