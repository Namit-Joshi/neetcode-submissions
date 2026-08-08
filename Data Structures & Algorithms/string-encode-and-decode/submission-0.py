class Solution:

    def encode(self, strs: List[str]) -> str:
        str_list = []

        for s in strs:
            str_list.append(f"{len(s)}#{s}")

        return "".join(str_list)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length

            ans.append(s[i:j])
            i = j

        return ans