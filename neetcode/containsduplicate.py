#Contains Duplicate

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         myDict = {}
         for n in range(len(nums)):
            if nums[n] in myDict:
                return True
            myDict[nums[n]] = n
         return False