class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = {}
        for i in nums:
            collection[i] = collection.get(i, 0) + 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num, freq in collection.items():
            buckets[freq].append(num)

        results = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                results.append(num)
                if len(results) == k:
                    return results