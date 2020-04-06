#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item = {}
        for i, n  in enumerate(nums):
            if target - n in item:
                return [item[target-n], i]
            item[n] = i


        
# @lc code=end

