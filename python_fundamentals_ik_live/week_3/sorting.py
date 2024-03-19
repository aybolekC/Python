points=[[1,2], [0,4], [6,3,2], [1,3,1]]

sorted_points1=sorted(points)
print(sorted_points1)

sorted_points2=sorted(points, key=lambda x: (x[1]))
print(sorted_points2)

sorted_points3=sorted(points, key=lambda x: (x[1], x[0]))
print(sorted_points3)

#==============================Sorting continue================================================


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