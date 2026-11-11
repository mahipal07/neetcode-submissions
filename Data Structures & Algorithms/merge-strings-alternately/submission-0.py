class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)

        while i < n1 and j < n2:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from either string
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
