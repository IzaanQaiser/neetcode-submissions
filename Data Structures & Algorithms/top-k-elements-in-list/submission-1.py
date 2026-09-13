class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = {}
        for i in nums:
            collection[i] = collection.get(i, 0) + 1
        sorted_dict = sorted(collection.items(), key=lambda x: x[1], reverse=True)
        result = [sorted_dict[i][0] for i in range(k)]
        return result