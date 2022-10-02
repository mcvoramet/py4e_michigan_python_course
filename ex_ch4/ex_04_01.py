def computepay(h,r):
    hr= float(h)
    ra = float(r)
    if h <= 40 :
        x = hr*ra
        return x
    elif h > 40 :
        y = ((40*ra)+((ra/2)+ra)*(hr-40))
        return y

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
