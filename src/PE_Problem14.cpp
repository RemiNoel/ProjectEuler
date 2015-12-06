#include "PE_Problem14.h"
#include <iostream>
#include <vector>


void problem14::findLargestChainNumberUnderN(int N){
	__int64 startingChainNumber = 2;
	__int64 longestChainCount = 1;
	__int64 tempChainCount;
	__int64 tempNumber;

	for (int i = 2; i < N; i++){
		tempNumber = i;
		tempChainCount = 1;

		while (tempNumber > 1){
			tempNumber = problem14::findCollatzNextSeq(tempNumber);
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

__int64 problem14::findCollatzNextSeq(__int64 testNumber){
	if (testNumber % 2 == 0){
		return testNumber / 2;
	}
	else{
		return (3 * testNumber) + 1;
	}
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