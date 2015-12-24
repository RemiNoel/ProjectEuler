#include "PE_Problem6.h"
#include <iostream>


void problem6::findSquareDifference(){
	int computedDifference = 0;
	int sumOfSq = 0;
	int sqOfSum = 0;
	int sum = 0;

	for (int i = 1; i <= 100; i++){
		sum += i;
	}

	sqOfSum = pow(sum, 2);

	for (int j = 1; j <= 100; j++){
		sumOfSq = sumOfSq + pow(j, 2);
	}
	computedDifference = sqOfSum - sumOfSq;

	printSquareDifference(computedDifference);
}

void problem6::printSquareDifference(int difference){
	if (difference > 0){
		printf("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is : %u \n", difference);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	system("Pause");
}