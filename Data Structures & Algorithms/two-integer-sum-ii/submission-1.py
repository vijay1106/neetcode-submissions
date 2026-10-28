class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #iterate through the list
        # get a dict {number, index}
        # iterate through the list 
        # look for target - number and if exists return the first index
        # add a if loop to ensure current index is not the same as the dict index 
        # to optimize will try to do in single loop

        dict = {}
        #iterate through the list
        for i, n in enumerate(numbers): 
            # print(f"i : {i}, n : {n}")

            diff = target - n
            # print(f"diff : {diff}")

            if dict.get(diff) is not None:
                if dict.get(diff) != i:
                    return [dict[diff]+ 1, i+1 ]
            
            dict[n] = dict.get(n, i) 
            # print(f"dict : {dict}")    