class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = []
        l2 = []
        for i in range(len(nums)):
            if i < n:
                l1.append(nums[i])
            else:
                l2.append(nums[i])

        i = 0
        l = []
        while i < (len(nums)/2):
            l.append(l1[i])
            l.append(l2[i])
            i += 1

        return l
