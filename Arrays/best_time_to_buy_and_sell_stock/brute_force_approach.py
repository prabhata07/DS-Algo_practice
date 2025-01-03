class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        arr_len = len(prices)
        max_pro = 0

        # Brute force approach.
        for i in range(arr_len):
            for j in range(i+1, arr_len):
                f_ele = prices[i]
                s_ele = prices[j]
                if f_ele < s_ele:
                    pro = s_ele - f_ele
                    if pro > max_pro:
                        max_pro = pro

        # Time complexity is O(n^2)
        return max_pro

if __name__ == "__main__":

    sol = Solution() 
    prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    print(f"stock input is: {prices}")
    out = sol.maxProfit(prices)
    print(f"output is: {out}")