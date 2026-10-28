class Solution:
    #remove all non-alphanumeric and spaces
    #make everything lowercase
    #remove all the spaces 
    #split the string into a list of characters
    #move the 
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # print(f"clean_text : {clean_text}")

        str_list = list(clean_text)
        # print(f"str_list : {str_list}")

        str_len = len(str_list)
        print(f"str_len : {str_len}")

        if str_len <= 1:
            return True
        

        for i, c in enumerate(str_list):
            # print(str_list[i])
            # print(str_list[str_len - i])
            if str_list[i] != str_list[str_len - 1 - i]:
                return False
        return True