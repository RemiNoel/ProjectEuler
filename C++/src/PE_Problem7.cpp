#include "PE_Problem7.h"
#include <iostream>


void problem7::findPrimeNumberAt(int primeNumberPosition){
	unsigned long primeNum = 0;
	
	for (int i = 2 ; i != primeNumberPosition; primeNum++){
		for (int j = 2; j <= primeNum; j++){
			if (primeNum % j == 0 && j != primeNum){
				break;
			}
			else if (j == primeNum){
				i++;
			}
				
		}
	}
	printPrimeNumber(primeNum, primeNumberPosition);
}



void problem7::printPrimeNumber(unsigned long primeNumber, int primeNumberPosition){
	if (primeNumber > 0){
		printf("The %u th prime number is : %u \n", primeNumberPosition, primeNumber);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	system("Pause");

}