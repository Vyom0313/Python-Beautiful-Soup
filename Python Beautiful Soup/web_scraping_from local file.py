from bs4 import BeautifulSoup

#how to read an html file and modify in it
#then later read an html webpage


# to open the file from the same directory aas your py file in read mode
with open("C:/Users/Vyom/Desktop/Python more like ahhhhh/Python Beautiful Soup/index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# print(doc) 
#to prettify as it prints with proper indentation
print(doc.prettify()) 

#to find something using tag name
tag = doc.title #title is the tag name
print(tag) #prints out title tag
print(tag.string) #prints out whatever is in the tag

#modification
tag.string = "Hello"
print(tag.string)
print(doc.prettify())

#finding
tag = doc.find("a") #gives first tag that has a inside of it
tags = doc.find_all("p") #gives all tags that have p
print(tags)
print(tags[0])

#accessing nested tags
tags = doc.find_all("p")[0]
print(tags.find_all("b"))
