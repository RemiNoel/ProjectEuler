#Using names.txt (right click and 'Save Link/Target As...'), 
#a 46K text file containing over five-thousand first names, 
#begin by sorting it into alphabetical order. 
#Then working out the alphabetical value for each name, multiply this value by 
#its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, 
#COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
#What is the total of all the name scores in the file?

d_lettersValue = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10, 
				'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19, 
				'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

totalScores = 0
names = []

# Fetch the data from names.txt then store it in names(List)
# Sort the list so the names will corespond to their correct value
names = open('names.txt', 'r')
names = sorted(names.read().replace('"','').split(','), key = str)


def main():
	sumOfLetters = 0
	for i in range(1, len(names) + 1): 
		for letter in names[i - 1]:
			sumOfLetters += d_lettersValue[letter] * i
	print (sumOfLetters)
	
if __name__ == '__main__':
	main()