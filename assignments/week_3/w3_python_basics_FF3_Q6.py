num1=input()
num2=input()

try:
    int(num1)/int(num2)
except:
    print("division by zero is not acceptable")
finally:
    print("will be printed anyway")