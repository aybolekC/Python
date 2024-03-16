
print("======================================My Solution=====================================")
s="interview"
to_find="e"

def find_first_occurance(s,to_find):
    for i in range(len(s)):
        if(s[i]==to_find):
            return i    
    return -1

print(find_first_occurance(s, to_find))

s="kickstart"
to_find="n"

print(find_first_occurance(s, to_find))

print("======================================Trainer Solution=====================================")
s="interview"
to_find="e"

def find_first_occurance1(s,to_find):
    return s.find(to_find)
    
   
print(find_first_occurance1(s, to_find))