#include "PE_Problem10.h"
#include "Utilities.h"
#include <iostream>

void problem10::findSumOfPrimes(const unsigned long primeSumLimit){
	double primeSum = 0;

	for (double  i = 2; i < primeSumLimit; i++){
		if (utilities::isPrime(i)){
			primeSum += i;
		}
	}
	problem10::printSumOfPrimes(primeSum);
}

void problem10::printSumOfPrimes(double sumOfPrimes){
	if (sumOfPrimes > 0){
		printf("The sum of all the primes below two million is : %f \n", sumOfPrimes);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");
}
