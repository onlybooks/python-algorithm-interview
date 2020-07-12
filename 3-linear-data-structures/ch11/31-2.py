import collections


class Solution:
    def topKFrequent(self, nums, k):
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
