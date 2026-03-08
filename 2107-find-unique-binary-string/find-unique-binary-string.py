class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans=""
        for i , ch in enumerate(nums):
            if ch[i] == "1":
                ans+="0"
            else:
                ans+="1"
        return ans