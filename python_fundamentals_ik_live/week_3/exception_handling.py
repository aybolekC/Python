# SyntaxError - Missing closing parenthesis
# print("Hello world"

# Type Error - Trying to add a string with an integer
#result="5" +3

# ValueError - Converting a non-numeric string to an integer
# number_str="abc"
# result=int(number_str)

# FileNotFoundError - Trying to open a non-existent file
# file_path="non_existent_file.txt"
# with open(file_path, "r") as file:
#     content=file.read()

print("========================================Practice - 1======================================================")
a=5
b=0

try:
    print(a/b)
except:
    print("Cannot divide by zero!")

print("Completed")

print("========================================Practice - 2======================================================")

x=2

try:
   #y+=3
   #x+="abc"
    x+=2
    print(x)
except Exception as e:
    print("Oops! Something went wrong")
    print(type(e))
    print(e)

print("\n This line is printed anyways")    

print("========================================Practice - 3======================================================")

def divide(a,b):
    if b==0:
        raise Exception("Cannot divide by zero")
    return a/b



try:
    #result=divide(10,0)
    result=divide(10,2)
    print(result)
except Exception as e:
    print(e)   

print("========================================Practice - 4======================================================")
# Catching Specific Exceptions in Python

try:
    #Case 1
    even_number=[2,4,6,8]
    print(even_number[5])

    #Case 2
    x=5/0
except IndexError:
    print("Index out of Bound")
except ZeroDivisionError:
    print("Denominator cannot be 0.")

print("========================================Practice - 5======================================================")

# Use else after except
try:
    num=int(input("Enter a number: "))
    assert num%2==0
except:
    print("\n Not an even number!")
else:
    reciprocal=1/num
    print()
    print(reciprocal)
finally:
    print("\n Run Completed!")

print("========================================Practice - 6 ======================================================")    
# Create custom exception

class CustomError(Exception):
    def __init__(self, message):
        self.message=message


try:
    raise CustomError("This is a custom error!")
except Exception as e:
    print(e.message)