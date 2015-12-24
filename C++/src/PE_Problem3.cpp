#include "PE_Problem3.h"
#include <vector>
#include <math.h>


void problem3::findLargestPrimeFactor(unsigned long long Number){
	unsigned int i = 2;
	while (pow(i, 2) < Number){
		while(Number % i == 0){
			Number /= i;
			printf("current largest prime factor is : %u\n", i);
		}
		i++;
	}
	problem3::printLargestPrimeFactor(Number);
}

void problem3::printLargestPrimeFactor(unsigned long long Number){
	if (Number > 0){
		printf("The largest prime factor of this number 600 854 475 143 is : %u \n", Number);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}

	system("Pause");

}

