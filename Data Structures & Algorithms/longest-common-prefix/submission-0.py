class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Compare with the corresponding character in the other strings
            for s in strs[1:]:
                # Check out of bounds or character mismatch
                if i == len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
