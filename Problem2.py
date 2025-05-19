# Problem 2 : Longest Palindromic Substring
# Time Complexity : 
'''
DP 2-d array - O(n^2) where n is the length of the string s
Two Pointer - O(n^2) where n is the length of the string s
'''
# Space Complexity : 
'''
DP 2-d array - O(n^2) where n is the length of the string s
Two Pointer - O(1)
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# DP 2-d array

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # get the length of the string of s
        n = len(s)
        # if the length is 0 then return empty string 
        if n == 0:
            return ""
        # define dp matrix with size(n*n) and fill with 0
        dp = [[False] * n for _ in range(n)]
        # set the dp[0][0] to True
        dp[0][0] = True
        # define start and end which will store the index of subsequence 
        start = 0
        end = 0
        # loop from 1 to n length
        for j in range(1, n):
            # loop from j to 0
            for i in range(j, -1, -1):
                # if character at jth and ith position is not equal then set dp[i][j] to False
                if s[j] != s[i]:
                    dp[i][j] = False
                else:
                    # else check if (j-1) is less than 2 or the value of dp at (i+1)(j-1)th position is True
                    if j - i < 2 or dp[i+1][j-1]:
                        # set the value of dp at i and jth position as True
                        dp[i][j] = True
                        # check if (j-i) is greater than (end - start)
                        if j - i > end - start:
                            # if it is then set start to i and end to j
                            start = i
                            end = j
        # return the sub sequence from start to end index
        return s[start:end+1]

# Dp 1-d array
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # get the length of the string of s
        n = len(s)
        # define dp array with size n and fill with 0
        dp = [False] * n 
        # set the 0th element True
        dp[0] = True
        # define start and end which will store the index of subsequence 
        start = 0
        end = 0

        # loop from 1 to n length
        for i in range(1, n):
            # define diagUp to store the diaginal Up value of the array and initially set to False
            diagUp = False
            # loop from i to 0
            for j in range(i, -1, -1):
                # store dp[j] value in the temp
                temp = dp[j]
                # check if the character ith and jth position is not equal
                if s[i] != s[j]:
                    # if it is not then set the dp[j] to False
                    dp[j] = False
                else:
                    # else check if (j-1) is less than 2 or the value of diagUp is True 
                    if i - j <= 2 or diagUp:
                        # set the value of jth position of dp as True
                        dp[j] = True
                        # check if (j-i) is greater than (end - start)
                        if i - j > end - start:
                            # if it is then set start to i and end to j
                            start = j 
                            end = i 
                    else:
                        # else set the jth position of dp as False
                        dp[j] = False
                # store value of temp in diagUp
                diagUp = temp
        # return the sub sequence from start to end index
        return s[start:end+1]        


# Two Pointer

class Solution:
    def __init__(self):
        # define start and end pointer for stroing the start and end index of subsequence
        self.start = 0
        self.end = 0

    def longestPalindrome(self, s: str) -> str:
        # get the length of the string of s
        n = len(s)
        # loop from 0 to length of the string s
        for i in range(n):
            # call the function for odd length of the string
            self.extendAroundCenter(s, i, i)
            # check if i is less than (n-1) and the character at i and (i+1)th position are equal then call the function for even length 
            if i < n - 1 and s[i] == s[i+1]:
                self.extendAroundCenter(s, i, i+1)
        # return the sub sequence from start to end index
        return s[self.start:self.end+1]
    
    def extendAroundCenter(self, s: str, l: int, r: int) -> None:
        # loop till l is greater than or equal to 0 and r is less than the length and characters at l and rth position are equal
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # decrement l and increment r
            l -= 1
            r += 1
        # increment l and decrement r to get the correct index
        l += 1
        r -= 1
        # check if (r-l) is less than (end - start) and if it is then set start to l and end to r
        if r - l > self.end - self.start:
            self.start = l
            self.end = r