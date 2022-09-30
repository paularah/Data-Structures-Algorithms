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


