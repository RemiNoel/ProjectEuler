#include "PE_Problem16.h"
#include <iostream>
#include <string>

void problem16::findPowerSumDigits(int base, int n){
	int sumOfDigits = 0;
	std::string tempDigitString;
	int residue = 0;

	long double veryLargeNumber = pow(base, n);
	tempDigitString = std::to_string(veryLargeNumber);

	for (int i = 0; i < tempDigitString.size() - 7 ; i++){
		sumOfDigits += tempDigitString[i] - '0';
	}

	problem16::printPowerSumDigits(sumOfDigits);
}

void problem16::printPowerSumDigits(int sumOfDigits){
	if (sumOfDigits > 0){
		std::cout << "The sum of the digits of the number 2^1000 is : \n" << sumOfDigits << std::endl;
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");
}