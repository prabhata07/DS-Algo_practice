import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]
        ansStart, ansEnd = 0, 0
        start = 0
        arr_len = len(nums)

        for i in range(1, arr_len):
            if cur_sum < 0: # Edge case: For first negative value
                cur_sum = nums[i]
                start = i
            else:
                cur_sum += nums[i] 
            # cur_sum = nums[i] if cur_sum < 0 else cur_sum + nums[i] # Edge case: For first negative value

            if cur_sum > max_sum:
                max_sum = cur_sum
                ansStart = start
                ansEnd = i

        print("The subarray is: [", end="")
        for i in range(ansStart, ansEnd + 1):
            print(nums[i], end=" ")
        print("]")

        return max_sum
    
         
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-2,-3, -1, 0]
    # nums = [-2, 1]
    sol = Solution()

    print(f"Searching max sub array for: {nums}")
    op = sol.maxSubArray(nums)
    print(f"maximum sub array sum is: {op}")   