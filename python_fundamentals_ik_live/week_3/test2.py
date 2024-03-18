
numbers=[4,2,9,1,5,]

sorted(numbers) # does not make any change to original list
print(numbers)

sorted_numbers=sorted(numbers)
print(sorted_numbers)

print(numbers)

numbers.sort()
print(numbers)

words=["apple", "banana", "cherry", "date", "fig", "bananas"]
soreted_words=sorted(words, key=len)
print(soreted_words)

soreted_words=sorted(words, key=len, reverse=True)
print(soreted_words)

soreted_words2=sorted(words, key=lambda x: x[1])
print(soreted_words2)