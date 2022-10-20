# https://leetcode.com/discuss/interview-question/380650/Bloomberg-or-Phone-Screen-or-Candy-Crush-1D

"""
* loop through every char in the string
* add or increment of pair indicating the character and its count
* if the count is greater than or equals to 3, pop the stack 
* Build the result the char and count
"""


def candyCrush(string):
    stack = []
    for char in string:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])

        if stack[-1][1] == 3:
            stack.pop()
    res = ""
    for char, count in stack:
        res += (char * count)
    return res


# assert candyCrush("aaabbbc") == "c"


# https://leetcode.com/problems/decode-string/description/
"""
* create a stack 
* loop through every character in the string
* if the character is not a closing bracket, add it to the stack 
* if the char is a closing bracket, pop everything for the stack until you find 
the last correspondinfg opening bracket. 
* Pop everything from the stack that is a digit to get the number 
* create the substring n time and add it to the stack  
"""


def decodeString(s):
    stack = []
    for c in s:
        if stack and c == ']':
            subStr = ''
            while stack[-1] != '[':
                subStr = stack.pop() + subStr
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            print(num)
            stack.append(subStr * int(num))
        else:
            stack.append(c)
    return "".join(stack)


# assert decodeString("3[a]2[bc]") == "aaabcbc"

'''
* loop  trough the chars 
* if the character is a closing bracket and the top of the stack is an opening, 
pop the stack 
* 
'''


def minAddToMakeValid(s: str) -> int:
    stack = []

    for c in s:
        if c == ")" and stack[-1] == "(":
            stack.pop()
        elif c == "(":
            stack.append(c)
        else:
            stack.append(c)
    return len(stack)


# https://leetcode.com/problems/min-stack/
'''
* The trick to this is maintaing another stack to keep track of the min values
* when we push a new item to the stack, we compare the current min val in the min stack 
the item and push the lesser of them to the min stack. 
* when we pop from the stack we also pop from the min stack. 
# '''
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []


#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         minVal = 0
#         if self.minStack:
#             minVal = self.minStack[-1]
#             minVal = min(val, minVal)
#         else:
#             minVal = val
#         self.minStack.append(minVal)


#     def pop(self) -> None:
#         if self.stack:
#             self.stack.pop()
#             self.minStack.pop()


#     def top(self) -> int:
#         return self.stack[-1]


#     def getMin(self) -> int:


def reverseWords(s: str) -> str:
    stack = []
    res = ""

    print(s)

    for i in range(len(s)-1, -1, -1):
        if i == " ":
            while stack:
                res = stack.pop() + res
                res = " " + res
        else:
            stack.append(s[i])
    print(res)
    return res


print(reverseWords("the sky is blue"))
