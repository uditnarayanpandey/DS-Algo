##Maximum subarray with k distinct cahracters : Sliding window O(n)

##problem of finding the longest subsequence with k distinct characters.
##for example : "abcbdbdbbdcdabd"
##Output is : "bdbdbbd"

'''
Explanation : The window (substring) is stable for the current problem if it contains k distinct characters at any point. If the window has less than k distinct characters, it expands by adding characters to it from the right; otherwise, if the window contains more than k distinct characters, it shrinks by removing characters from the left until it becomes stable again.
'''
# abcbdbdbbdcdabd -> bdbdbbd
# abccbbccbccbbbcbcbdbdbbdcdabd -> bccbbccbccbbbcbcb


sample_string = "abccbbccbccbbbcbcbdbdbbdcdabd"
k = int(input("Please enter the number of distinct characters: "))
pointer, win_high, win_low = 0,0,0
sub_string = ""
calc_dict = dict()


print('\n\n','+-'*15, ' ' , sample_string, ' ', '+-'*15, '\n\n')


while pointer < len(sample_string):

	print('Pointer: {}  high: {}  low: {}'.format(pointer, win_high, win_low))
	
	if (sample_string[pointer] in calc_dict):
		calc_dict[sample_string[pointer]] += 1
	else:
		calc_dict.setdefault(sample_string[pointer], 1)


	if(len(calc_dict.keys()) <= k):
		print(calc_dict)
		win_high += 1
	else:
		sub = sample_string[win_low : win_high]
		print('Potential substring : ', sub )
		
		if(len(sub) > len(sub_string)):
			sub_string = sub
			
		while(len(calc_dict) != k):
			print(calc_dict)
			rem = sample_string[win_low]
			print('>'*15, f'removing {rem}')

			if (calc_dict[rem] > 0 ):
				calc_dict[rem] -= 1 
				win_low += 1
				
			if (calc_dict[rem] == 0):
				del calc_dict[rem]
				print('current length of the calc_dict is : ', len(calc_dict), '>'*20)
				
		win_high += 1
	pointer += 1
if(len(sample_string[win_low : win_high])> len(sub_string)):
	sub_string = sample_string[win_low : win_high]
print(sub_string)

			

	
