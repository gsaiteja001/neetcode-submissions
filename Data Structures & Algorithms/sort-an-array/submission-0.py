class Solution:
    # 1. Added 'self' parameter
    def merge_sort(self, left, right):
        result = []
        i = 0
        j = 0
        
        # 3. Changed '<=' to '<'
        while i < len(left) and j < len(right):
            # 2. Changed parentheses () to brackets [] for indexing
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        
        # 4. Added the missing return statement
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # 1. Added 'self.' to call the class method
        return self.merge_sort(left, right)