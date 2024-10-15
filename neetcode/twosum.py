#Two Integer Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range (len(nums)):
            diff = target - nums[i]
            if (diff in myDict):
                return [myDict.get(diff), i]
            myDict[nums[i]] = i
        return False