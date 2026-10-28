class Solution:
    #remove all non-alphanumeric and spaces
    #make everything lowercase
    #remove all the spaces 
    #split the string into a list of characters
    #move the 
    def isPalindrome(self, s: str) -> bool:
        # clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # # print(f"clean_text : {clean_text}")

        # str_list = list(clean_text)
        # # print(f"str_list : {str_list}")

        # str_len = len(str_list)
        # print(f"str_len : {str_len}")

        # if str_len <= 1:
        #     return True
        

        # for i, c in enumerate(str_list):
        #     # print(str_list[i])
        #     # print(str_list[str_len - i])
        #     if str_list[i] != str_list[str_len - 1 - i]:
        #         return False
        # return True

        l = 0
        r = len(s) - 1

        while l < r :
            print(l, r)

            while l < r and not self.isAplhanum(s[l]):
                l = l + 1

            while r > l and not self.isAplhanum(s[r]):
                r = r -1 
            
            print(s[l].lower(), s[r].lower())

            if s[l].lower() != s[r].lower():
                print("did not match")
                return False
            
            l, r = l+1, r-1
            print(l, r)
        
        return True

    def isAplhanum(self, c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or  
        ord("a") <= ord(c) <= ord("z") or 
        ord("0") <= ord(c) <= ord("9") )