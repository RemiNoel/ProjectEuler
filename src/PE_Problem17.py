
#	If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
#	then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
#	how many letters would be used?
#
#import pdb #(debugger)

D = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
T = [0,3,6,6,5,5,5,7,6,6]
H = 7
Th = 8

sumOfLetter = 0

for i in range(1, 1000) :
    #Access the lists based on i
    
    #singles digit
    digit = i % 10
    
    #tens digit
    tens = ((i % 100) - digit) / 10
    
    #hundreds digit
    hundreds = ((i % 1000) - (10 * int(tens)) - digit) / 100
    #pdb.set_trace() #(debugger callout)
    if hundreds != 0:
        sumOfLetter += D[int(hundreds)] + H                  #D[hundreds] hundred 
        if tens != 0 or digit != 0 : sumOfLetter += 3   #add "and"
        
    if tens == 0 or tens == 1 : 
        sumOfLetter += D[int((10 * tens) + digit)]
    else : sumOfLetter += T[int(tens)] + D[int(digit)]       	       
        
sumOfLetter += D[1] + Th

print(sumOfLetter)
