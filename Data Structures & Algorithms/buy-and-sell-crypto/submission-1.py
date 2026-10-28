class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force approach
        #loop through each element and check if the next elementes are higher then decide to buy else move to the next element
        #store the value and get a max of earlier difference
        #by the end of the loop we would have the best combination to buy and sell
        
        best_sale = 0
        for i in range(0, len(prices)):
            
            print(f"i : {i}, price : {prices[i]}")
            
            for j in range(i+1, len(prices)):
                
                print(f"j : {j}, price : {prices[j]}")
                
                current_sale = prices[j] - prices[i]

                print(f"current_sale : {current_sale}")
                
                if  current_sale > best_sale:

                    best_sale = current_sale

                print(f"best_sale : {best_sale}")
        
        return best_sale