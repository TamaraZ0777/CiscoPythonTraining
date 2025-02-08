def is_prime(num):
	num_is_prime = True
	if num == 2:
		return num_is_prime
	else:
		for n in range(2, num):
			if num % n == 0:
				num_is_prime = False
		return num_is_prime
	

#
# Write your code here.
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

