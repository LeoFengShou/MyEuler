for i in range(1, 500, 1):
	for j2 in range(1, 500, 1):
		c = 1000 - i - j2
		if i ** 2 + j2 ** 2 == c ** 2:
			print(i * j2 * c)