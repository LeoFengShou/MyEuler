def have_factors(number):
	count = 0
	root = number ** 0.5
	int_root = int(root)
	# print(int_root)
	for i in range(1, int_root + 1, 1):
		if number % i == 0: count += 2
	if root == int_root: count -= 1
	return count


# print(have_factors(6))
# print(have_factors(8))
# print(have_factors(9))


tri_num = 1
i = 2
while have_factors(tri_num) < 501:
	tri_num += i
	i += 1
print(tri_num)