# Use the file name mbox-short.txt as the file name
x = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    a = line.rstrip()
    b = a.find("0")
    c = a[b : ]
    num = float(c)
    np = []
    np.append(num)

    for i in np:
       x = x + i
tot = (len(a) + 1)
avg = x/tot
print("Average spam confidence:", avg)
