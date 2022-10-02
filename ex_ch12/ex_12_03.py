from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_704793.html (Sum ends with 68)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
html = urlopen(url, context=ctx).read()
# 1st argument - string; 2nd - how you’d like the markup parsed
x = BeautifulSoup(html, 'html.parser')

# Retrieve all span elements
total = 0
elements = x('span') # Give a list of all span tags
for element in elements:
    num = element.contents[0]
    num = int(num)
    total = total + num

print(total)
