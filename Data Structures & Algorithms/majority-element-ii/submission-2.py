class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        return [num for num, cnt in count.items() if cnt > math.floor(len(nums)/3)]