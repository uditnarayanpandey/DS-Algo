##Longest substring without repeating characters

##Given a string s, find the length of the longest substring without repeating characters.
'''
Example: 

s = "abcabcbb"
Output = 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Objective: to find the longest subs with no repeating character
        input[string]: string from which the subs has to be found
        output[string]: The longest substring with no repeating characters 
        '''
        pointer = 0
        substring_len = 0
        low = 0
        calc_set = set()

        while pointer < (len(s)):
            if s[pointer] not in calc_set:
                calc_set.add(s[pointer])
            else:
                while(s[pointer] in calc_set):
                    calc_set.remove(s[low])
                    low += 1
                calc_set.add(s[pointer])
            pointer += 1
            substring_len = max((pointer-low), substring_len)
        print('longest substring with non repeating characters has a length of : {}'.format(substring_len))


if __name__ == '__main__':

    a = Solution()
    a.lengthOfLongestSubstring('abcabcbb')