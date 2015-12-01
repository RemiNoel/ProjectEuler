#include "PE_Problem6.h"
#include <iostream>

void problem6::findLowestValue(){
	
}
void problem6::printLowerValue(unsigned int lowestValue){
	if (lowestValue > 0){
		printf("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is : %u \n", lowestValue);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}

	system("Pause");
}