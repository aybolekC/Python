print("===========================My Solution=======================")
sentence="Interview Kickstart"

def length_of_last_word(sentence):

    if (len(sentence)>1):
        x= sentence.split()
        result=len(x[len(x)-1])
    elif sentence.isspace():
        #result=int(0)
        print("0")
    else:
        result=len(sentence)
    
    return result

print(length_of_last_word(sentence))

sentence=" Hello World  "
print(length_of_last_word(sentence))

print("===========================My Solution=======================")

sentence="Interview Kickstart"

def length_of_last_word2(sentence):
    if len(sentence.strip())==0:
        return 0
    words=sentence.strip().split()
    if len(words)==0:
        return 0
    return len(sentence.strip().split()[-1])
    

print(length_of_last_word2(sentence))   