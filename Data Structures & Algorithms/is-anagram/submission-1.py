class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # counter_s = Counter(s)
        # print(counter_s)
        # counter_t = Counter(t)
        # if counter_s == counter_t:
        #     return True
        
        # else:
        #     return False
        char_dict = {}
        for c in s:
            # if c in char_dict:
            #     char_dict[c] = char_dict[c]+1
            # else :
            #    char_dict[c] = 1
            char_dict[c] = char_dict.get(c,0)+1
        print(char_dict)
        char_dict_comp = {}
        for c in t:
            # if c in char_dict_comp:
            #     char_dict_comp[c] = char_dict_comp[c]+1
            # else :
            #    char_dict_comp[c] = 1 
            char_dict[c] = char_dict.get(c,0)-1
        print(char_dict)
        for val in char_dict.values():
            if val != 0:
                return False
        return True
        
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # # print(s)
        # # print(t)
        # s = "".join(s)
        # t = "".join(t)
        # # print(s)
        # # print(t)
        # if s == t:
        #     return True
        # else:
        #     return False