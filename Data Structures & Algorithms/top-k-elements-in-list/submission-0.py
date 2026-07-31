class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums))]

        for i in set(nums):
            arr[nums.count(i)-1].append(i)
        stack = []
        for i in arr:
            for j in i:
                stack.append(j)

        res = []

        for i in range(k):
            res.append(stack.pop())

        return res