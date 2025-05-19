# Problem 1 : Ugly Number II
# Time Complexity : 
'''
Using Heap - O(nlog k) where n is the n ugly number and k is the size of the priority queue
Using pointers - O(n) where n is the n ugly number
'''
# Space Complexity : 
'''
Using Heap - O(n) where n is the nth ugly number
Using pointers - O(n) where n is the n ugly number
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Using heap 
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # define seen hash set which will store the number which is already seen
        seen = set()
        # define min heap which will store the number 
        heap = []
        # define primes array whih will have allowed prime number
        primes = [2, 3, 5]

        # add the number 1 to heap and seen set
        heapq.heappush(heap, 1)
        seen.add(1)

        # define variable to count and set to 1 and currUgly number and set to 1
        count = 1
        currUgly = 1
        # loop till count is less than or equal to n
        while count <= n:
            # get the top number from the heap which will be the current ugly number
            currUgly = heapq.heappop(heap)
            # increment the count which will count the ugly number
            count += 1
            # loop through primes array
            for prime in primes:
                # get new ugly number by multiplying the prime with current ugly number
                newUgly = currUgly * prime
                # check if the new ugly number is not in seen hash set
                if newUgly not in seen:
                    # if the number is not in set then add the number in the set and heap
                    seen.add(newUgly)
                    heapq.heappush(heap, newUgly)
        # return current ugly number
        return currUgly

# Using pointers

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # define array with size n and fill with 0
        arr = [0] * n
        # set the arr[0] to 1
        arr[0] = 1
        # define variable p2, p3, p5 and set to 0 
        p2 = p3 = p5 = 0
        # define variable n2, n3, n5 and set to 2, 3, 5 ie number for each prime 
        n2, n3, n5 = 2, 3, 5

        # loop from 1 to n
        for i in range(1, n):
            # get the minimum between n2, n3 and n5
            minVal = min(n2, n3, n5)
            # set the value of arr[i] to minimum value
            arr[i] = minVal

            # check if miVal is n2
            if minVal == n2:
                # increment p2
                p2 += 1
                # get the n2 as 2 * arr[p2]
                n2 = 2 * arr[p2]

            # check if miVal is n3
            if minVal == n3:
                # increment p3
                p3 += 1
                # get the n3 as 3 * arr[p3]
                n3 = 3 * arr[p3]
            
            # check if miVal is n5
            if minVal == n5:
                # increment p5
                p5 += 1
                # get the n5 as 5 * arr[p5]
                n5 = 5 * arr[p5]
        # return the last element of array
        return arr[-1]
            