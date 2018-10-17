def find_even_sum_of_fib(lim):
	a = 1
	b = 2
	nex = a + b
	su = 2
	while nex < lim:
		if nex % 2 == 0:
			su += nex
		a = b
		b = nex
		nex = a + b
	return su


if __name__ == '__main__':
	print(find_even_sum_of_fib(4000000))