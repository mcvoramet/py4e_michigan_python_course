#Use filename regex_sum_42.txt for sample (sum=445833)
#Use filename regex_sum_704791.txt for assignment (sum=ends with 313)
fname = input("Enter file name: ")
han = open(fname)
counts = dict()
lst = list()
new_lst = list()
newer_lst = list()
import re

for line in han:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)

    if num not in lst:
        lst.append(num)
for i in lst:
    new_lst.extend(i)
for j in new_lst:
    newer_lst.append(float(j))
print(sum(newer_lst))
#Here is a redacted version of 2 line version of this program using list comprehension
#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
#List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.
