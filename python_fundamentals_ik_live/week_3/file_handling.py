

print("===================================Practice 1 ===========================================")
file = open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example.txt", "r")
content=file.read()

print(type(content))
print()
print(content)

file.close()

#content=file.read()

print("===================================Practice 2 - using with ===========================================")
with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/tell.txt", "r") as file:
    content=file.read()
    print(content)

print("===================================Practice 3 -reading single line ===========================================")

with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/tell.txt", "r") as file:
    cur_file=file.readline()
    print(cur_file)

    cur_file=file.readline()
    print(cur_file)

print("===================================Practice 4 -using while loop to read file line by line ===========================================")
with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example.txt", "r") as file:
    while True:
        cur_line=file.readline()
        if cur_line:
            print(cur_line)
        else:
            break

print("===================================Practice 5 -using readlines - reading file as list of string ===========================================")
with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example.txt", "r") as file:
    lines=file.readlines()
    print(lines)

for line in lines:
    print(line)


print("===================================Practice 6 -starting from certain index and counting total chars+spaces ===========================================")
with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example.txt", "r") as file:
    file.seek(5)
    print(file.read())  

    print()

    position=file.tell()
    print(position) 

print("===================================Practice 7 - writing to a file by creating new one ===========================================")
file = open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example1.txt", "w")
file.write("Hello John!\n How are you?")
file.close

print("===================================Practice 8 - writing to a file overwriting ===========================================")
with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example.txt", "w") as file:
    file.write("Programming is fun!\n")
    file.write("Python for beginners")

print("===================================Practice 9 - writing to a file adding/append===========================================")
with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/example.txt", "a") as file:
    file.write("\nThis is the end of the document")    