from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('anagram', 'nagaram'))
    print(s.isAnagram('car', 'rac'))
    print(s.isAnagram('tom', 'mat'))
