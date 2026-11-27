class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatTime(rate) :
            eat_time = 0
            for i in range(len(piles)) : 
                eat_time = eat_time + (piles[i] + rate - 1) // rate
            
            return eat_time

        left = 1
        right = max(piles) 

        while left < right : 
            mid = (left + right) // 2 
            
            if eatTime (mid) > h : 
                left = mid + 1

            else :
                right = mid 
            
        return left           