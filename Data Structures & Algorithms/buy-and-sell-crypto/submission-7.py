class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force approach
        #loop through each element and check if the next elementes are higher then decide to buy else move to the next element
        #store the value and get a max of earlier difference
        #by the end of the loop we would have the best combination to buy and sell
        
        best_sale = 0

        # for i in range(0, len(prices)):
            
        #     print(f"i : {i}, price : {prices[i]}")
            
        #     for j in range(i+1, len(prices)):
                
        #         print(f"j : {j}, price : {prices[j]}")
                
        #         current_sale = prices[j] - prices[i]

        #         print(f"current_sale : {current_sale}")
                
        #         if  current_sale > best_sale:

        #             best_sale = current_sale

        #         print(f"best_sale : {best_sale}")

        lowest_price = 100
        highest_price = 0


        # for i in range(0, len(prices)):

        #     if prices[i] <= lowest_price:
        #         lowest_price = prices[i] 
        #         print(f"lowest_price : {lowest_price}")
        
        # for j in range(len(prices)-1, -1, -1):
        #     print (f" j : {j}")

        #     if prices[j] >= highest_price:
        #         highest_price = prices[j] 
        #         print(f"highest_price : {highest_price}")

        # i, j = 0, len(prices) - 1

        # while i <= j:

        #     # print(f"i : {i}, price : {prices[i]}")
        #     # print(f"j : {j}, price : {prices[j]}")

        #     if prices[i] <= lowest_price:
                
        #         lowest_price = prices[i] 
        #         # print(f"lowest_price : {lowest_price}")
        #         i = i + 1 

        #     if prices[j] >= highest_price:
        #         highest_price = prices[j] 
        #         # print(f"highest_price : {highest_price}")
        #         j = j - 1 


        for i in range(0, len(prices)):

            if prices[i] < lowest_price:
                lowest_price = prices[i]

            current_profit = prices[i] - lowest_price 

            if best_sale < current_profit:
                best_sale = current_profit
        
        return best_sale