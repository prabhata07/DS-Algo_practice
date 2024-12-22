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

        # Brute Force logic
        for i in range(arr_len):
            for j in range(i, arr_len):

                # sub_arr = nums[i......j]
                sub_arr_sum = 0

                # add all the elements of subarray
                for k in range(i, j+1):
                    sub_arr_sum += nums[k]

                max_sub_arr_sum = max(max_sub_arr_sum, sub_arr_sum)


        return max_sub_arr_sum

if __name__ == "__main__":
    nums = [-1, 0]

    sol = Solution()
    max_sum = sol.maxSubArray(nums)
    print("The maximum sum is:", max_sum)