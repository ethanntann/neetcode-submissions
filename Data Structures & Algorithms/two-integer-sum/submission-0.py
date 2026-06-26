class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = {} # value : index
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in numList:
                return [numList[compliment],i]
            numList[nums[i]] = i
      