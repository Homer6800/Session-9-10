file_name = "x-file.txt.py"
fd = open(file_name)  # r is inplicit
print("here are the contents of the file:")


# another way is to read it line by line
for line in fd:
    #print(line, end="")
    #print(line.strip())
    print(line.replace("\n", ""), end="")
fd.close()

with open(file_name) as fd:
    print("Here are the three letter words!")
    for line in fd:
        words = line.split()
        for word in words:
            if len(word) == 3:
                print(word)



