class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        splice = 0

        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:splice]
            splice += 1

        return strs[0][:splice]