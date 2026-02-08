class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.upper() == word else True if word.lower() == word else True if word.capitalize() == word else False