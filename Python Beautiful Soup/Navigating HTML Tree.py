from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
# print(tbody) 
print(trs[0].next_sibling) #gets next sibling i.e. next table row
print(trs[1].previous_sibling) #gets previous sibling i.e. previous table row
#can look at next_siblings

print(trs[0].parent.name) #or .descendants #or .contents or .children
#if you get a generator object convert it to a list

prices = {}
for tr in trs:
    for td in tr.contents[2:4]: #lists all content and if u use [2:4] gives just name and price according to the position in contents
        print(td)
        print()

for tr in trs[:10]:
    name, price =  tr.contents[2:4]
    print(name.p) #prints name and if you use .p, prints name with p tag
    print(name.p.string) #just what is inside the string
    print()
