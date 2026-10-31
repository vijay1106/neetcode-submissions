class Solution:
    def isValid(self, s: str) -> bool:

        #when going through the string
        #check if the current character closed 
        #has the most recent element in the stack should be an open one
        
        closeToOpen = {
            ')' : '(',
            '}' : '{', 
            ']' : '['
        }

        # print(closeToOpen[')'])

        stack = []


        for p in s:

            print(f'p : {p}')

            if p in  closeToOpen:
                if stack and stack[-1]  ==  closeToOpen[p]:
                    stack.pop()
                    # print(f'stack : {stack}')
                else:
                    return False

            else:
                stack.append(p)

                # print(f'stack : {stack}')

        return True if not stack else False