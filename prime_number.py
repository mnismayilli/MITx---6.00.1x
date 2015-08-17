# 1
import sys

def prime_number(number):
	"""
	take a number, return True if it's a prime number,return False if it's not
	"""
	for num in range(2, number):
		if number % num == 0:
			return False
	return True	


def prime(number):
	"""
	take a number n, return all the prime number from 1 to n
	"""
	answer = []
	for num in range(2, number):
		if prime_number(num) == True:
			answer.append(num)
	return answer

print prime(int(sys.argv[1]))



# 2    Sieve of Eratosthenes
import sys

def sieve(num):
    results = []
    primes = [True for _ in range(num + 1)]
    for i in range(2, num + 1):
        if primes[i]:
            results.append(i)
            for n in range(i * 2, num + 1, i):
                primes[n] = False
    return results

print sieve(int(sys.argv[1]))
