class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search
        #Two pointers left of matrix and right of matrix 
        #get the middle list and with in middle intialize two pointers 
        #binary search for the target
        #check if the first element and last element of the array and compare to target 
        #if the target is less than first element then move the out right to the left of the out middle 
        #else move the left to the right of the middle and repeat until out _ left is less than right 

        out_left, out_right = 0 , len(matrix) - 1 

        

        while out_left <= out_right : 
            print(f'out_left : {out_left}, out_right : {out_right}')
            mid = (out_left + out_right) // 2 

            inner_left , inner_right = 0 , len(matrix[mid]) - 1 

            print(f'inner_left : {inner_left}, inner_right : {inner_right}')
            
            

            if target < matrix[mid][0] :
                out_right  = mid - 1
            
            elif target > matrix[mid][inner_right] :
                out_left  = mid + 1 

            elif matrix[mid][0]  <= target <=  matrix[mid][inner_right] :
                
                while inner_left <= inner_right : 
                    inner_mid = (inner_left + inner_right) // 2 
                    if matrix[mid][inner_mid] == target : 
                        return True
                    elif matrix[mid][inner_mid] < target : 
                        inner_left = inner_mid + 1 

                    else : 
                        inner_right = inner_mid - 1

                return False


        return False
        