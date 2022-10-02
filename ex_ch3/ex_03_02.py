hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric number")
    quit()

if h <= 40 :
    print(h*r)
if h > 40 :
    print("Pay:",(40*r)+((h-40)*(r*1.5)))
