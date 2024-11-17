def test(a):
	print(f"test: {a}")

def test2(b):
	print(f"test2: {b}")

def test3(a, b, c):
	test(b)
	print(f"test2: {c}")
	test2(a)

test3(1, 2, 3)
