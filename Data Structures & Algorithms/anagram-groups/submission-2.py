class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} 
        for str in strs:
           str_sort =  "".join(sorted(str)) #sorted version of the string
        #    print(f"str : {str} , str_sort : {str_sort}")
           dict[str_sort] = dict.get(str_sort,[])+[str]
        #    print(dict.values())
        grp_ana = list(dict.values())
        return grp_ana

        
            
 