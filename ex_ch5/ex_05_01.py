num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval  == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('ALL DONE')
print('Total:',tot,'Amount:',num,'Average:',tot/num)
#This will work to find average number.
