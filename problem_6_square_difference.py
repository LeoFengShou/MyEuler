s1 = ((1 + 100) * 50) ** 2
s2 = 0
for i in range(1, 101, 1):
	s2 += i ** 2
print(s1 - s2)