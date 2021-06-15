class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_pos = {}
        curr_length = 0
        start = 0
        for i, char in enumerate(s):
            if char not in char_pos:
                curr_length += 1
            else:
                start = max(start, char_pos[char])
                curr_length = i - start
            char_pos[char] = i
            if curr_length > max_length:
                max_length = curr_length
        return max_length
