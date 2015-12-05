#include "PE_Problem12.h"
#include <iostream>
#include <math.h>

void problem12::getTriNumWithNDivisors(int divisorCount){
	int testNumber = 0;
	int counter = 1;

	while (getDivisorsCount(testNumber) < divisorCount){
		testNumber+= counter;
		counter++;
	}
	problem12::printTriWithNDivisors(testNumber, divisorCount);
}


int problem12::getDivisorsCount(int testNumber){
	int tempDivisorCount = 0;

	int rootOfTestNumber = sqrt(testNumber);

	//Check each perfect division and increment the divisor count if it is a division without residue. 
	//Add +2 to the division count. E.g. : 28 % 7 = 0 (28 has two roots : 7 and 4). 
	for (int i = 1; i < rootOfTestNumber; i++){
		if (testNumber % i == 0){
			tempDivisorCount += 2;
		}
	}

	//If it is a perfect root, we only want one divisor added. E.g. : 49 % 7 = 0 (49 has two identical roots : 7 and 7)
	if (pow(rootOfTestNumber, 2) == testNumber){
		tempDivisorCount--;
	}

	return tempDivisorCount;
}

void problem12::printTriWithNDivisors(int triNumber, int divisorCount){
	if (triNumber > 0){
		printf("The value of the first triangle number to have over %d divisors is : %d \n", divisorCount, triNumber);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");

}
