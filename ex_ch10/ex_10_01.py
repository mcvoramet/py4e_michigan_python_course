#Use filename mbox-short.txt
fname = input("Enter file name: ")
han = open(fname)
counts = dict()
lst = list()

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 5 or wds[0] != "From":
        continue
#Time 09:12:43 is located in position [5]
    x = wds[5].split(":")
    time = x[0]             #Extracted just hour 09:xx:xx ---> 09
    counts[time] = counts.get(time, 0) + 1     #Count each hour
#.items() use for tuple
for v,k in counts.items():          #Pull out v and k from each tuple
    rslt = (v, k)
    lst.append(rslt)                #then add to the list

lst = sorted(lst)                   #Sort hour from low to high

for v, k in lst:
    print(v, k)
