#include "PE_Problem2.h"
#include <iostream>

void problem2::calculateEvenFiboSeq(){
	auto temp = 2;
	auto tempTemp = 1;
	int tempFiboSum = 0;
	int evenFiboSum = 2;
	int i = 2;

	//Calculate the Fibonacci sequence
	while(evenFiboSum <= problem2::m_limit){
		tempFiboSum = temp + tempTemp;
		tempTemp = temp;
		temp = tempFiboSum;

		//Check if the Fibonacci sum is even
		if (tempFiboSum % 2 == 0){
			evenFiboSum += tempFiboSum;
		}
	}

	problem2::printAnswer(evenFiboSum);
}

void problem2::printAnswer(int answer){
	if (answer > 0){
		printf("The sum of the even-valued terms of the Fibonacci sequence with a value limit of %d is : %d \n", problem2::m_limit, answer);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}

	system("Pause");
}