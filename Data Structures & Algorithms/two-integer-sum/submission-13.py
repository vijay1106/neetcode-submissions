class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if dict.get(diff) is None:
                dict[num] = index
            else :
                return [dict.get(diff), index]
        
        # print(dict)
        
        # for i,num in enumerate(nums):
        #     print(f"i,num : {i},{num}")
        #     diff = target-num
        #     if diff > 0:
        #         if dict.get(diff):
        #             j = dict[diff]
        #             print(f"j : {j}")
        #             if i != j:
        #                 return [i,j]
        #         else:
        #             return [0]     