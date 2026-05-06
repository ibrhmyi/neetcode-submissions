class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        results = []
        num = ""
        j = 0
        while j < (len(s)):
            if s[j] == '#':
                j += 1
                num = int(num)
                results.append(s[j:j+num])
                j += num
                num = ""
            else:
                num += s[j]
                j += 1
        return results