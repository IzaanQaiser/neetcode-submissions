class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for i in strs:
            length = len(i)
            parts.append(f"{length}#{i}")
        encoding = "".join(parts)
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1 # will increment j till it's point at "#"
            length = int(s[i:j]) # not including j
            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end
        return result
            


