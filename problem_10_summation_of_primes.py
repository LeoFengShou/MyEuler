def is_prime(number):
	for i in range(2, int(number ** 0.5) + 1, 1):
		if number % i == 0: return False
	return True

# print(is_prime(1800))

su = 0
for i in range(2, 2000000, 1):
	if is_prime(i): 
		su += i
		print(i)
	print(su)
print(su)