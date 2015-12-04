#include "PE_Problem9.h"
#include <iostream>
#include <math.h>

void problem9::findPythTriplet(){
	int termA, termB;
	double termC;

	// termA + termB + termC = 1000;
	// pow(termA, 2) + pow(termB, 2) = pow(termC, 2) --> termC = sqrt(pow(termA, 2) + pow(termB, 2))
	// termA < termB < termC

	for (termA = 1; termA < 499; termA++){
		for (termB = 1; termB < 499; termB++){
			termC = sqrt(pow(termA, 2) + pow(termB, 2));
			if ((termA + termB + termC == 1000) && (termA < termB) && (termB < termC)){
				problem9::printPythTriplet(termA * termB * termC);
			}
		}
	}
}

void problem9::printPythTriplet(double product){
	if (product > 0){
		printf("The Pythagorean triplet product is : %f \n", product);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");
}