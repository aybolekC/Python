with open("C:/Users/12816/Python/assignments/week_3/example1.txt", "r") as file:
    lines=file.readlines()

    max_len=0
    longest_word=" "

    for line in lines:
        words=line.split()
        for ch in words:
            if len(ch)> max_len:
                max_len=len(ch)
                longest_word=ch

    print(max_len)
    print(longest_word)