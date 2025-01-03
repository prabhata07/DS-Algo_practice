class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_prof = 0
        min_price = prices[0]

        # Optimal approach.
        for num in prices[1:]:
            if num > min_price:
                prof = num - min_price
                if prof > max_prof:
                    max_prof = prof
            else:
                min_price = num
            
        # Time complexity is O(n)
        return max_prof

if __name__ == "__main__":

    sol = Solution() 
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    print(f"stock input is: {prices}")
    out = sol.maxProfit(prices)
    print(f"output is: {out}")