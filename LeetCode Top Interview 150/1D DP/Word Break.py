class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            if dp[i]:
                for w in wordSet:
                    if s.startswith(w, i):
                        dp[i + len(w)] = True

        return dp[len(s)]
