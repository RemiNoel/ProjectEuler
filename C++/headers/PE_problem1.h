#ifndef PE_PROBLEM1
#define PE_PROBLEM1

/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

namespace problem1{
	void calculateSum(int multipleA, int multipleB, int limit);
	void printSumAnswer(int answer);

	const int m_multipleA = 3;
	const int m_multipleB = 5;
	const int m_limit = 1000;
};

#endif
