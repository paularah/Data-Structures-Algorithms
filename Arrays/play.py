from collections import Counter


def productExceptSelf(nums):
    res = [0] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i]
    print(res)

    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i] * postfix
        postfix = postfix * nums[i]
    print(res)
    return res


class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for i, c in count.items():
            print(i, c)
            freq[c].append(i)
        print(freq)

        res = []

        for f in range(len(freq), -1, -1):
            print(f)
            for i in freq[f]:
                res.append(i)
                if len(res) == k:
                    return res


# Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)


class Solution:
    def longestConsecutive(self, nums):
        """
        create a set from the nums
        for every value in the set, 
        check if that value is a start of sequence, if it is, 
        create an array and start append, its sequences until theres
        none left
        """

        sequenceSet = set(nums)
        sequences = []
        for i in sequenceSet:
            if i - 1 in sequenceSet:
                continue
            sequences.append([i])
            n = 1
            while i + n in sequenceSet:
                sequences[-1].append(i + n)
                n += 1
        longest = 0

        for seq in sequences:
            longest = max(longest, len(seq))
        return longest


Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
