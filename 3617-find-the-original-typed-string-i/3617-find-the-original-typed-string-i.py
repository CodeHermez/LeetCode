class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        counter,i = (1,0)
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            group_len = j - i
            if group_len > 1:
                counter += group_len - 1
            i = j
        return counter
        