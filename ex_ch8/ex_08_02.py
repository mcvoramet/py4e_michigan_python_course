#Use file name  mbox-short.txt
fname = input("Enter file name: ")
han = open(fname)
count = 0
for line in han:
    line = line.rstrip()
    wds = line.split()
    #Guardian in a compound statement
    if len(wds) < 2 or wds[0] != 'From':
        continue
    print(wds[1])
    count = count + 1
print("There were",count, "lines in the file with From as the first word")
