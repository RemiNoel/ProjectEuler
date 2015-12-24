#ifndef PE_PROBLEM10
#define PE_PROBLEM10
/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

namespace problem10{

	void findSumOfPrimes(const unsigned long primeSumLimit);
	void printSumOfPrimes(double sumOfPrimes);

	const unsigned long primeCountLimit = 2000000;
}

#endif