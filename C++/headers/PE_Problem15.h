#ifndef PE_PROBLEM15
#define PE_PROBLEM15

/*
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

*/


namespace problem15{

	void findNumberOfWaysInGrid(unsigned int gridN);
	__int64 getGridWaysCount(__int64 N, __int64 K);
	void printWaysCount(__int64 count);
}

#endif