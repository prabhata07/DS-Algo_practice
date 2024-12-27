import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
                # if cur_sum < 0: # Edge case: For first negative value
                # 	cur_sum = num
                # else:
                # 	cur_sum += num 
                cur_sum = num if cur_sum < 0 else cur_sum + num # Edge case: For first negative value

                if cur_sum > max_sum:
                    max_sum = cur_sum

        return max_sum
    
         
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-2,-3, -1, 0]
    nums = [-2, 1]
    sol = Solution()

    op = sol.maxSubArray(nums)
    print(f"maximum sub array sum is: {op}")   