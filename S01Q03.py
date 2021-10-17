'''
This program will modify S01Q02 to print multiplication table
of any number input by user
'''


num = int(input("Please enter the number you want the table for:"))

for i in range(1,11):
    print(num,"*",i, "=",num*i)
