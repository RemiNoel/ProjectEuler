#include "PE_Problem15.h"
#include <iostream>


void problem15::findNumberOfWaysInGrid(unsigned int gridN){
	__int64 numberOfWaysCount = 0;
	int K = gridN; //min of moves -> go from (0,0) to (n,k) in k moves.

	// There will always be 40 moves to make and 20 changes in X and Y. 
	// So the formula to use should be 40!/(20!)^2
	//That being said, to find the number of ways one can use in a SE lattice path is :

	numberOfWaysCount = problem15::getGridWaysCount(gridN * 2, K);

	problem15::printWaysCount(numberOfWaysCount);
}


__int64 problem15::getGridWaysCount(__int64 N, __int64 K){
	if (K == 0)
		return 1;

	//We could use for loops but the recursion is more logical in this context.
	return (N * problem15::getGridWaysCount(N - 1, K - 1)) / K;
}

void problem15::printWaysCount(__int64 count){
	if (count > 0){
		std::cout << "The number of routes in a SE/NE lattice 20 x 20 grid is : \n" << count << std::endl;
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");


}