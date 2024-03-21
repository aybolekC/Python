# file = open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/my_file.txt", "w")
# file.write("I love Python\n")
# file.write("Python is my favorite\n")
# file.close

# with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/my_file.txt", "a") as file:
#     file.write("Yes! Python is great!")    

# with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/my_file.txt", "r") as file:
#     while True:
#         cur_line=file.readline()
#         for ch in cur_line:
#             if ch=='P':
#                 print(cur_line.index(ch))

print("=================================== instructors solution =============================================================")               

# with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/my_file1.txt", "w") as file:
#     L=["I love Python.\n","Python is my favorite" ]
#     file.writelines(L)

# with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/my_file1.txt", "a") as file:
#     file.write("\nYes! Python is great!")    

with open("C:/Users/12816/Python/python_fundamentals_ik_live/week_3/my_file1.txt", "r") as file:
    lines=file.readlines()

idx=[]

for line in lines:
    idx.append(line.index("Python"))

print(idx)