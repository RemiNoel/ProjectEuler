#include "PE_Problem14.h"
#include <iostream>


void problem14::findLargestChainNumberUnderN(int N){
	__int64 startingChainNumber = 2;
	__int64 longestChainCount = 1;
	__int64 tempChainCount;
	__int64 tempNumber;

	for (int i = 2; i < N; i++){
		tempNumber = i;
		tempChainCount = 1;

		while (tempNumber > 1){
			//Collatz chain sequence
			if (tempNumber % 2 == 0){
				tempNumber = tempNumber / 2;
			}
			else{
				tempNumber = (3 * tempNumber) + 1;
			}

			tempChainCount++;
		}

		if (tempNumber == 1){
			if (tempChainCount >= longestChainCount){
				longestChainCount = tempChainCount;
				startingChainNumber = i;
			}
		}
	}
	problem14::printLargestNumberChain(startingChainNumber, N);
}

void problem14::printLargestNumberChain(__int64 largestChainNumber, int N){
	if (largestChainNumber > 0){
		std::cout << "The starting number, under " << N << ", which produces the longest chain is : \n" << largestChainNumber << std::endl;
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");


}