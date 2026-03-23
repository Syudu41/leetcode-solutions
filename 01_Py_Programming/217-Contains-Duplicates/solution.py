from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return True
        
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4,5]))
