#include "PE_Problem5.h"
#include <iostream>

void problem5::getSmallestNumberDividedByRange(int begin, int end) {
	long c = 1;
	int successes = 0;
	while (true) {
		for (long i = begin; i < end; i++) {
			if (c % i != 0)
				break;
			else
				successes++;
		}
		if (successes != end - begin) {
			successes = 0;
			c++;
		}
		else {
			problem5::printLowerValue(c);
		}
	}
}

void problem5::printLowerValue(unsigned int lowestValue){
	if (lowestValue > 0){
		printf("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is : %u \n", lowestValue);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}

	system("Pause");
}