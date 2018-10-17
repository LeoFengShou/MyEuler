i = 3
j = 5
su = 0
while i < 1000:
	if i % 5 != 0:
		su += i 
	i += 3
	print(i, su)
while j < 1000:
	su += j 
	j += 5
	print(j, su)
print(su)
