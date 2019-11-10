'''
二分查找的变形
改变选择左右的规则，注意理解二分查找的边界条件。
#也可以先用二分查找找出最小值，再用二分找出搜索target
'''
class Solution:
    testing = False
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<1:
            return -1
        r = len(nums)-1;
        l = 0
        mid = (r+l)//2
        while True:
            if Solution.testing:    #######################################
                print(l,mid,r)
            if nums[mid]==target:    #查找成功
                return mid
            if l>=r:
                return -1
            
            if nums[mid] < nums[r]:
                if target>nums[mid]and target<=nums[r]:    #在右侧
                    l = mid+1
                    mid =(r+l)//2
                else:
                    r = mid-1
                    mid =(r+l)//2
            else:
                if target<nums[mid] and target>=nums[l]:    #在左侧
                    r = mid-1
                    mid =(r+l)//2
                else:
                    l = mid+1
                    mid =(r+l)//2
        return mid