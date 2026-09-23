class Solution:
    def canPermutePalindrome(self, s):
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        odd = 0

        for count in counts.values():
            if count % 2 == 1:
                odd += 1

        return odd <= 1
