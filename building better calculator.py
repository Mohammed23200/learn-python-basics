from math import *
def better_calc(num1,num2,op):
    if op == '+':
        print(num1+num2)
    elif op == '-':
        print(num1-num2)
    elif op == '*':
        print(num1*num2)
    elif op == '/':
        print(num1/num2)
    elif op == "**":
        print(pow(num1,num2))
    elif op == 'abs':
        print(abs(num1))
        print(abs(num2))
    elif op == 'sqrt':
        print(sqrt(num1))
        print(sqrt(num2))
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
op = input("enter the operator")
better_calc(num1,num2,op)
