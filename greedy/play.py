"""
https://leetcode.com/problems/two-city-scheduling/description/
"""
def twoCitySchedule(costs):

    diffs = []

    for costA, costB in costs:
        diffs.append([costB-costA, costA, costB])
    diffs.sort()
    
    minCost = 0
    for i in range(len(diffs)):
        if i < len(diffs)//2:
            minCost += diffs[2]
        else:
            minCost += diffs[1]
    
    return minCost

assert twoCitySchedule([[10,20],[30,200],[400,50],[30,20]]) == 110
        
