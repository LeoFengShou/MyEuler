def find_largest_prime_factor(num):
	factors = find_all_factors_of(num)
	for i in range(len(factors) - 1, -1, -1):
		if is_prime(factors[i]):
			return factors[i]


def find_all_factors_of(num):
	factors_f = []
	factors_r = []
	for i in range(1, int(num**0.5), 1):
		if num % i == 0:
			factors_r.append(num / i)
			factors_f.append(i)
	return factors_f + factors_r


def is_prime(num):
	if num <= 1:
		return False
	elif num <= 3:
		return True
	elif num % 2 == 0 and num % 3 == 0:
		return False
	i = 5
	while i * i < num:
		if num % i == 0 or num % (i + 2) == 0:
			return False
		i += 6
	return True


if __name__ == '__main__':
 	print(find_largest_prime_factor(600851475143))