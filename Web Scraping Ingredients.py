from recipe_scrapers import scrape_me
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

alpha = input("What ingredient do you want to find: ")
print(" ")

list_RECIPES = []
list_1 = []
list_2 = []
list_3 = []

req = Request("https://www.bbcgoodfood.com/recipes/collection/top-20-winter-recipes") #Or any link (right now only on BBCGoodFood)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
  links.append(link.get('href'))
for y in range(len(links)):
   x = re.search("recipes/", str(links[y]))
   z = re.search("https", str(links[y]))
   a = re.search("collection", str(links[y]))
   if x != None and z != None and a == None:
      from recipe_scrapers import scrape_me
      scrape_me = scrape_me(links[y])
      z = str(scrape_me.ingredients())
      x = re.search(alpha, z)
      if x != None:
        list_RECIPES.append(links[y])
        
        title = scrape_me.title()
        instructions = str(scrape_me.instructions())
        list_1.append(z)
        list_2.append(title)
        list_3.append(str(instructions))

for num in range(len(list_2)):
  if num % 2 == 0:

    print(str(num//2+1)+ ". "+list_2[num])

print(" ")
choose = int(input("Choose a recipe (number):  "))

print("  ")
print("Let's cook",list_2[choose*2-1])
print("")
print("Here are the ingredients you need: \n")

ingredients = list_1[choose*2-1]
ingredients = ingredients.split("'")

for x in range(len(ingredients)):
  if x % 2 == 1:
    print(ingredients[x])

press = input("Type START to continue: ")

instructions = list_3[choose*2-1]
instructions = instructions.split(".")
for x in range(len(instructions)):
  if x % 2 == 1:
    print(instructions[x])
