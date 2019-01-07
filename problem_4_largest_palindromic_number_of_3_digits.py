def is_symmetric(string):
	for i in range( int(len(string) / 2) ):
		if string[i] != string[len(string) - 1 - i]: return False
	return True

nums = []
for i in range(100, 1000, 1):
	for j2 in range(100, 1000, 1):
		nums.append(i * j2)
nums = sorted(nums)

for i in range(len(nums) - 1, -1, -1):
	if is_symmetric(str(nums[i])): 
		print("result:", nums[i])
		break

# print(is_symmetric("1"))
# print(is_symmetric("12") == False)
# print(is_symmetric("121"))
# print(is_symmetric("1221"))
# print(is_symmetric("123") == False)
