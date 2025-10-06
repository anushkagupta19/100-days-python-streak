# Write a Python program to swap two variables.

a = int(input("enter the value of a:"))
b= int(input("enter the value of b:"))
print(f"enter the original value: a={a} , b={b}")

temp=a 
a=b
b=temp
print(f"after swapping the value: a={a},b={b}")
