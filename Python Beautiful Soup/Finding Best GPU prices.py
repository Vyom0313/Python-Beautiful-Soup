from bs4 import BeautifulSoup
import re
import requests

gpu = input("What product do you want to search for? ")

url = ""

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

#figuring out number of pages of results
page_text = doc.find(class_ = "list-tool-pagination-text")
print(page_text)

pages = str(page_text).split("/")[-2].split(">")[-1][:-1] # splits at "/" and gets the second last element

for page in range(1, pages+1):
    url = f""
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells")

    items = div.find_all(text=re.compile("search_term")) #any text that contains this
    # "3080" "3080 FTW" wouldnt match but if you use above query it will match
    for item in items:
        print(item) #huh