class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k
