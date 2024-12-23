import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialization
        arr_len = len(nums)
        max_sub_arr_sum = -sys.maxsize -1

        # Better Approach to bruteforce/ Enhanced BruteForce.

        for i in range(arr_len):
            sub_arr_sum = 0
            for j in range(i, arr_len):
                # Current subarray nums[i........j]
                
                # Add the current element nums[j] 
                # To the sum i.e. sum of nums[i......j-1]
                sub_arr_sum += nums[j]

                # Find maximum subarray sum.
                max_sub_arr_sum = max(max_sub_arr_sum, sub_arr_sum)

        # Time complexity O(N^2), Because we are using 2 for loops.
        # Space Complexity O(1)
        return max_sub_arr_sum
        
if __name__ == "__main__":

    nums = [-1, 0]
    # nums = [-1, 0, 1, 2, 3, -7]

    sol = Solution()
    max_sum = sol.maxSubArray(nums)
    print(f"The max_sum is : ", max_sum)