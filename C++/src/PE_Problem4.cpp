#include "PE_Problem4.h"

#include <algorithm>
#include <vector>
#include <iostream>

bool problem4::isPalindrome(int testNum) {
	int temp = testNum;
	int revNum = 0;
	int restDigit;
	while (temp) {
		restDigit = temp % 10;
		temp = temp / 10;
		revNum = revNum * 10 + restDigit;
	}
	return testNum == revNum;
}

void problem4::getLargestPalindrome() {
	int largestPalindrome = 0;

	std::vector<int> list;
	const int x1 = 999;
	const int x2 = 999;
	for (int i = x1; i > 99; i--) {
		for (int j = i; j > 99; j--) {
			if (isPalindrome(i * j)) {
				list.push_back(i * j);
			}
		}
	}

	//Find the largest palindrome in the list 
	largestPalindrome = list[std::distance(list.begin(), max_element(std::begin(list), std::end(list)))];
	printLargestPalindrome(largestPalindrome);
}

void problem4::printLargestPalindrome(int palindrome){
	if (palindrome > 0){
		printf("The largest 3-digit product palindrome is : %u \n", palindrome);
	}
	else{
		printf("There as been an error! Reevaluate your code. \n");
	}

	system("Pause");

}