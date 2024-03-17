print("=================================My Solution==========================")
s="#aBdj12C"

def count_alphabets(s):
    count=0
    for char in s:
        if(char.isalpha()):
            count+=1
    return count

print(count_alphabets(s))

s="123 !@#$"
print(count_alphabets(s))

print("=================================Trainer Solution==========================")


