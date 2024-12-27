import sys

# This is kadanes algorithm.
# It is based on global and local memory concept.
# Global will keep the highest sum and local will keep the running max sum.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialization
        arr_len = len(nums)
        max_sub_arr_sum = -sys.maxsize - 1 # this is Global Memory to keep max value.
        max_neg_num = -sys.maxsize - 1

        # Optimal approach.
        sub_arr_sum = 0 #local memory
        for num in arr_len:
            sub_arr_sum += num

            # if -ve local sum, make it 0
            if sub_arr_sum < 0:
                sub_arr_sum = 0

            # Find maximum subarray sum.
            max_sub_arr_sum = max(max_sub_arr_sum, sub_arr_sum)

            # Finding maximum -ve number.
            if num <= 0:
                max_neg_num = max(max_neg_num, nums)

        if max_sub_arr_sum == 0:
            max_sub_arr_sum = max_neg_num

        # Time complexity O(N), Because we are using 1 for loops.
        # Space Complexity O(1)
        return max_sub_arr_sum
        
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,-3, -1, 0]
    sol = Solution()

    op = sol.maxSubArray(nums)
    print(f"maximum sub array sum is: {op}")