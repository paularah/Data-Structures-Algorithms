def minRemoveToMakeValid(s: str) -> str:
    stack = []
    remove_indices = set()

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if not stack:
                remove_indices.add(i)
            else:
                stack.pop()
    # print(stack)
    # print(remove_indices)
    while stack:
        remove_indices.add(stack.pop())
    print(remove_indices)

    for index, char in enumerate(s):
        if index not in remove_indices:
            stack.append(char)

    return ''.join(stack)


minRemoveToMakeValid("ab(a(c)fg)9)")

"""
 L  R 
abcabcbb
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        currentWindow = set()
        for right in range(len(s)):
            print(right)
            while s[right] in currentWindow:
                left
            left += 1
            currentWindow.remove(s[left])
        return longest


print(Solution().lengthOfLongestSubstring("abcabcbb"))
