"https://leetcode.com/problems/contains-duplicate/submissions/"
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a ={}
        for _ in nums:
            if _ in a:
                return True
            else:
                a[_]=_
        return False