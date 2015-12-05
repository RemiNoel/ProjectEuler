#include "Utilities.h"

#include <algorithm>
#include <iostream>
#include <math.h>
#include <sstream>

bool utilities::isPrime(int testNumber){
	if (testNumber < 0)
		return false;
	if ((testNumber & 1) == 0)
		return testNumber == 2;

	/*
	If both a and b were greater than the square root of n, a*b would be greater than n. 
	So at least one of those factors must be less or equal to the square root of n, and to check if n is prime, 
	we only need to test for factors less than or equal to the square root.
	*/

	double root = sqrt(testNumber) + 1;

	for (int i = 3; i <= root; i+=2) {
		if (testNumber % i == 0) {
			return false;
		}
	}
	return true;
}

std::vector<std::string> utilities::splitString(std::string stringIn, char character){
	std::stringstream ss(stringIn);
	std::vector<std::string> listOut;

	std::string tempString;

	while (std::getline(ss, tempString, character)){
		listOut.push_back(tempString); 
	}
	return listOut;
}

std::string utilities::intToString(int numberToTransform){
	std::stringstream ss;
	ss << numberToTransform;

	return ss.str();
}