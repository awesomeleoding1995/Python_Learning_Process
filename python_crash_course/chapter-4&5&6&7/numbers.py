# Updated date: 2/3/2020
# Author: Lee Ding
# Make a list of the numbers from one to one million, and then use a min() and max()
# to make sure your list actually starts at one and ends at one million. Also, use sum()
# function to see how quickly python can add a million numbers.

# numbers = list(range(1,1000001))
# start_num = min(numbers)
# end_num = max(numbers)
# sum_num = sum(numbers)
# print("the min number is " + str(start_num) + " and the max number is " + str(end_num))
# print("\nand the sum of them is " + str(sum_num))

# numbers = list(range(3,31,3))
# for number in numbers:
# 	print(number)

numbers = [number**3 for number in range(1,11)]
print(numbers)