if __name__ == "__main__":
	from p1 import fizzbuzz_sum
	if fizzbuzz_sum(10) != 23:
		print "Test #1 FAIL"
	else:
		print "Test #1 PASS"

	if fizzbuzz_sum(1000) != 233168:
		print "Test #2 FAIL"
	else:
		print "Test #2 PASS"
