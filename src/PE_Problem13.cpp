#include "PE_Problem13.h"
#include "Utilities.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <streambuf>

void problem13::findFirstNDigitsOfSum(int nDigits){
	int digitResidue = 0;
	std::string s_firstTenDigitsOfSumRev = "";

	//Fetch the information in the iput.txt file and put it in a temporary string
	std::ifstream file;
	file.open("input.txt", std::ifstream::in);
	
	std::string str((std::istreambuf_iterator<char>(file)),
						std::istreambuf_iterator<char>());

	if (file.is_open()){
		std::vector<std::string> s_ListOfNumber = utilities::splitString(str, '\n');
		file.close();

		for (int i = 49; i >= 0; i--){
			int tempSum = 0;
			
			for (int j = 0; j < 100; j++){
				tempSum += s_ListOfNumber[j][i] - '0';
			}
			s_firstTenDigitsOfSumRev += (utilities::intToString((tempSum + digitResidue) % nDigits));
			digitResidue = (digitResidue + tempSum) / nDigits;
		}
		//Reverse the string to correctly get the first digits of the sum
		s_firstTenDigitsOfSumRev = std::string(s_firstTenDigitsOfSumRev.rbegin(), s_firstTenDigitsOfSumRev.rend());

		std::string s_firstTenDigitsOfSum = utilities::intToString(digitResidue);
		s_firstTenDigitsOfSum += (s_firstTenDigitsOfSumRev);

		//Truncate the string to get only the first 10 digits to the sum. (long long or __int64)
		__int64 firstTenDigits = atoll(s_firstTenDigitsOfSum.substr(0, 10).c_str());

		problem13::printFirstNDigits(firstTenDigits);
	}

}

void problem13::printFirstNDigits(__int64 firstTenDigitsOfSum){
	if (firstTenDigitsOfSum > 0){
		std::cout << "the first ten digits of the sum of the one-hundred 50-digit numbers are : \n" << firstTenDigitsOfSum << std::endl;
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}
	//system("Pause");
}