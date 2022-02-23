##Maximum subarray sum : Kadane's Algorithm

##Given an integers, the task is to find the maximum subarray sum possible of all the non-empty subarrays
##for example : [-3, -4, 5, -1, 2, -4, 6, -1]
##Output is : 8 
##Explanation : Subarray [5, -1, 2, -4, 6]  is the max sum contiguous subarray with sum 8

array = [-2, 2, 5, -1, 6]

curr_sum = 0
max_sum = float('-inf')
neg_val = float('-inf')
for val in array:
	curr_sum = curr_sum + val
	if curr_sum < 0:
		if curr_sum > neg_val:
			neg_val = curr_sum
		curr_sum = 0
		continue
	if curr_sum > max_sum:
		max_sum = curr_sum 
	else: 
		continue
if(max_sum == float('-inf')):
	print('Largest subarray sum : {}'.format(neg_val))
else:
	print('Largest subarray sum : {}'.format(max_sum))
	
	

