from bs4 import BeautifulSoup
import re #module for regular expression

with open("C:/Users/Vyom/Desktop/Python more like ahhhhh/Python Beautiful Soup/index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#modifying attributes of a tag  
tag = doc.find("option") #find tags
tag['value'] = 'new value' #changing
tag['color'] = 'blue' #adding
print(tag)
print(tag.attrs) #prints out all attributes of a tag in a dictionary

tags = doc.find_all(["p","div","li"]) #finds tags and gives everything inside tags
#another thing to do
tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
#also
tags = doc.find_all(class_ = "btn-item")
print(tags)

#regular expression
#look for syntax xof dollar sign on your own
tags = doc.find_all(text=re.compile("\$.*")) #gives any text after dollar sign
for tag in tags:
    print(tag.strip())

#limiting number of results while searching
tags = doc.find_all(text=re.compile("\$.*"), limit=1) #gives any text after dollar sign
for tag in tags:
    print(tag.strip())

#save modified file
tags = doc.find_all("input", type="text") #gives any text after dollar sign
for tag in tags:
    tag['placeholder'] = "I changed you"

with open("changed.html", "w") as new_file:
    new_file.write(str(doc))
