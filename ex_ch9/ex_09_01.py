#Use filename mbox-short.txt
fname = input("Enter file name: ")
han = open(fname)
counts = dict()
lst = list()
#Search email follow with "From." (From is in position[0])
for line in han:
    line = line.rstrip()
    wds = line.split()
    #Guardian in a compound statement. (From email)(email is in position[1])
    if len(wds) < 2 or wds[0] != 'From':
        continue
    mails = wds[1].split()
    #Store all email in one list
    for word in mails:
         lst.append(word)
#Store all email in dict() and count each email
for name in lst:
    counts[name] = counts.get(name, 0) + 1
#Find the most repeated email in the dict().
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)