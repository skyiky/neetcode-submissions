class Solution:
    
    def encode(self, strs: List[str]) -> str:
        x = [str(len(strs)).zfill(2)]
        for n in strs:
            x.append(str(len(n)).zfill(3))
        x.extend(strs)
        return "".join(x)

    def decode(self, s: str) -> List[str]:
        result = []
        x = int(s[0:2])
        i = 2 + (3 * x)
        j = 2
        for _ in range(x):
            size = int(s[j:j+3])
            word = s[i:i+size]
            result.append(word)
            i += size
            j += 3
        return result