class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        n = len(s)

        while i < n:
            # Find delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract length and the string itself
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Move pointer to the start of the next encoded chunk
            i = end

        return res
