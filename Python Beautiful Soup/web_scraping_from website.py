from bs4 import BeautifulSoup
import requests

url = ""

result = requests.get(url)
doc = BeautifulSoup(result.text, "html parser")
print(doc.prettify())

prices = doc.find_all(text="$")
print(prices)
parent = prices[0].parent
print(parent)
strong = parent.find("strong")
print(strong.string)
