from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        left = 0
        right = len(s1)

        while left < right and right < len(s2):
            windowCount = Counter(s2[left:right])
            print(windowCount, s1Count)
            if windowCount == s1Count:
                return True
            left += 1
            right += 1
        return False


assert Solution().checkInclusion("adc", "dcda") == True
