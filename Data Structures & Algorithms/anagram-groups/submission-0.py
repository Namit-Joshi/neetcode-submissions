class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            lex = ''.join(sorted(word))

            if lex in dic:
                dic[lex].append(word)
            else:
                dic[lex] = [word]
        ans = []
        for value in dic.values():
            ans.append(value)
        return ans
            