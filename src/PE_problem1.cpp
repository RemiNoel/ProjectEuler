#include "PE_problem1.h"
#include <iostream>


void problem1::calculateSum(int multipleA, int multipleB, int limit){
	auto tempSum = 0;

	for (int i = 0; i < limit; i++){
		if (i % m_multipleA == 0){
			tempSum += i;
		}
		else if (i % m_multipleB == 0){
			tempSum += i;
		}
	}
	problem1::printSumAnswer(tempSum);
}

void problem1::printSumAnswer(int answer){
	if (answer > 0){
		printf("The sum of all the multiples of %d and %d is %d. \n", problem1::m_multipleA, problem1::m_multipleB, answer);
	}
	else{
		printf("There as been an error! Reevaluate your code.");
	}

	system("Pause");
}