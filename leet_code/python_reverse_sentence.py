# Solution #1

s="the sky is blue"
def reverse_sentence(s):
    print(s)
    array_words=s.split(" ")
   # print(array_words)
    reverse_array_words= array_words[::-1]
    #print(reverse_array_words)
    return " ".join(reverse_array_words)

#reverse_sentence(s)
print(reverse_sentence(s))

#==============================Solution 2=================================
