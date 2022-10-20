"""
parent: (index-1)//2
left:  2n + 1
right: 2n + 2
"""


class MaxBinaryHeap:

    def __init__(self, values=[]) -> None:
        self.values = values

    def insert(self, value):
        self.values.append(value)

    def getParentIndex(self, index):
        return (index - 1)//2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 1

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index)

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
