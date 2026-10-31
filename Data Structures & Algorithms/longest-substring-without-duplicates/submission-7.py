class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #have a dictoinary of all the characs as we keep going through the string
        #go through the list until we hit an existing charatcter in dictionary
        #keep a counter to measure the longest string

        #start a loop to go through the string 
        #for each char we come across compare to a set that we keep adding. 
        #if it does not exist we will move to next character 
        #increase our length of the current substring 
        #if the char exists in the set we pop the first element added in set until we dont see the char
        #then we reset the substring length counter and start again from the next char 

        str_set = set()
        max_len = 0 
        l = 0

        for r in range(len(s)):

            c = s[r]

            # print (f'l : {l}, r : {r}, c : {c}')

            while c in str_set:

                str_set.remove(s[l])

                # print(f'duplicate \n str_set : {str_set}')

                l = l + 1

            str_set.add(c)

            # print(f'str_set : {str_set}')

            max_len = max(max_len, r-l + 1 )
            
            # print(f'max_len : {max_len}')

        return max_len




            




        # dict = {}
        # cur_max_len = 0 
        # max_len = 0

        # l = 0 

        # for i in range(l, len(s)):
        #     c = s[i]

        #     print(f'c : {c}')

        #     if dict.get(c) is None:
        #         dict[c] = dict.get(c,0) + 1
        #         # print(dict)
        #         i = i + 1
        #         # print(f'i:{i}')
        #         cur_max_len = cur_max_len + 1
        #         # print(f'cur_max_len:{cur_max_len}')
            
        #     else:
        #         if cur_max_len > max_len:
        #             max_len = cur_max_len 
        #             # print(f'max_len:{cur_max_len}')
                
        #         l = l + 1
        #         dict = {}
        #         cur_max_len = 0


        # return max(max_len, cur_max_len)



        


        