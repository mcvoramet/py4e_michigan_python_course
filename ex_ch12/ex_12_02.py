from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
#Last name in sequence: Anayah
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Alva.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: J
#url = input("Enter url: ")
#count = int(input("Enter count: "))
#position = int(input("Enter position: "))

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Retrieving:", url)

for i in range(count):
    html = urlopen(url, context=ctx).read()
    # 1st argument - string; 2nd - how you’d like the markup parsed
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a') # Give a list of all anchor tags
    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)
