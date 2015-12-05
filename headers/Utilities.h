#ifndef UTILITIES_H
#define UTILITIES_H

#include <string>
#include <vector>

namespace utilities{
	
	//Checks if a number is prime. Returns if the number is prime or not.
	bool isPrime(int testNumber);
	
	//Split a string of a certain character. Returns a list of string with the character removed from the stream.
	std::vector<std::string> splitString(std::string string, char character);

	//Change a integer into a string
	std::string intToString(int numberToTransform);

}

#endif