#https://leetcode.com/discuss/interview-question/380650/Bloomberg-or-Phone-Screen-or-Candy-Crush-1D

"""
aaabbbc
[[b, ,]]
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

assert candyCrush("aaabbbc") == "c"


#https://leetcode.com/problems/decode-string/description/
"""
* create a stack 
* loop through every character in the stack 
* if the character is not a closing bracket, add it to the stack 
* if the char is a closing bracket, pop everything for the stack until you find 
the last correspondinfg opening bracket. 
* Pop everything from the stack that is a digit to get the number 
* create the substring n time and add it to the stack  
"""
def decodeString(s):
    stack = []
    for c in  s:
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


assert decodeString("3[a]2[bc]") == "aaabcbc"






