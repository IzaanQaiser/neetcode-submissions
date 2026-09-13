class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        return_list = []
        for i in strs:
            key = "".join(sorted(i))
            if key not in collection:
                collection[key] = []
            collection[key].append(i)
        for i in collection.values():
            return_list.append(i)
        return return_list
