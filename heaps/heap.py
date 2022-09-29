"""
parent: (index-1)/2
left:  2n - 1
right: 2n - 2
"""

class MaxBinaryHeap:

    def __init__(self, values=[]) -> None:
        self.values = values
    
    def insert(self, value):
        self.values.append(value)
    
    def bubbleUp(self):

        # currentIdx = len(self.values) - 1
        # parentIdx = int((currentIdx - 1)/2)

        # node = self.values[currentIdx]
        # parent = self.values[parentIdx]

        # if node > parent:
        #     self.values[parentIdx] = node 
        #     self.values[currentIdx] = parent
        #     currentIdx =  parentIdx
        #     parentIdx = int((currentIdx - 1)/2)