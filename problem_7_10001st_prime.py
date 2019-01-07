def is_prime(num):
	i = 2
	while i ** 2 <= num:
		if num % i == 0: return False
		i += 1
	return True

count = 1
last_prime = 2
while count < 10001:
	last_prime += 1
	while not is_prime(last_prime):
		last_prime += 1
	count += 1
print(last_prime)

# print(is_prime(2))
# print(is_prime(29))
# print(is_prime(27) == False)