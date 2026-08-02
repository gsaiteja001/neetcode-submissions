class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       res = curSum = 0
       prefixsums = { 0 : 1 }

       for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixsums.get(diff,0)
            prefixsums[curSum] = 1 + prefixsums.get(curSum,0)
       return res