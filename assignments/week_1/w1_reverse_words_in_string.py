
str="Best technical interview prep courses."

def reverse_words(s):
    words=s.strip().split()
    words.reverse()
    return " ".join(words)


print(reverse_words(str))