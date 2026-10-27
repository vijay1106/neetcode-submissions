class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #     for inner_index,inner_num in enumerate(nums):
    #         for outer_index,outer_num in enumerate(nums[inner_index + 1:]):
    #             print(f"inner_index:{inner_index} \t inner_num:{inner_num} \t outer_index : {outer_index} \t outer_num : {outer_num}")
    #             if inner_num == outer_num:
    #                 return True
    #     return False
        # print(nums)
        # print(set(nums))
        # print(len(nums))
        # print(len(set(nums)))
        # if len(nums) == len(set(nums)):
        #     return False
        # return True
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False