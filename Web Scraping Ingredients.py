from recipe_scrapers import scrape_me
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class WebScrape:
  def __init__(self):
    #alpha = input("What ingredient do you want to find: ")
    self.alpha = input('enter an ingredient: ')

    self.list_RECIPES = []
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.req = Request("https://www.bbcgoodfood.com/recipes/collection/top-20-winter-recipes") #Or any link (right now only on BBCGoodFood)
    self.html_page = urlopen(self.req)
    self.soup = BeautifulSoup(self.html_page, "lxml")
    self.links = []

  def scrape(self):
    for link in self.soup.findAll('a'):
      self.links.append(link.get('href'))
    for y in range(len(self.links)):
       x = re.search("recipes/", str(self.links[y]))
       z = re.search("https", str(self.links[y]))
       a = re.search("collection", str(self.links[y]))
       if x != None and z != None and a == None:
          self.scrape = scrape_me(self.links[y])
          z = str(self.scrape.ingredients())
          x = re.search(self.alpha, z)
          if x != None:
            self.list_RECIPES.append(self.links[y])
            self.title = self.scrape.title()
            self.instructions = str(self.scrape.instructions())
            self.list_1.append(z)
            self.list_2.append(self.title)
            self.list_3.append(str(self.instructions))

  def run(self):
    for num in range(len(self.list_2)):
      if num % 2 == 0:

        print(str(num//2+1)+ ". "+self.list_2[num])

    print(" ")
    self.choose = int(input("Choose a recipe (number):  "))

    print("  ")
    print("Let's cook",self.list_2[self.choose*2-1])
    print("")
    print("Here are the ingredients you need: \n")

    self.ingredients = self.list_1[self.choose*2-1]
    self.ingredients = self.ingredients.split("'")

    for x in range(len(self.ingredients)):
      if x % 2 == 1:
        print(self.ingredients[x])

    self.press = input("Type START to continue: ")

    self.instructions = self.list_3[self.choose*2-1]
    self.instructions = self.instructions.split(".")
    for x in range(len(self.instructions)):
      if x % 2 == 1:
        return self.instructions[x]
    









