class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]: return mid
            if target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
        return -1