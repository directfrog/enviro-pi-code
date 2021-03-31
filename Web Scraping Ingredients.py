from recipe_scrapers import scrape_me
import re, os, sys, time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import random

class scraper(object):
  def __init__(self, alpha, beta):
    self.start_time = time.time()
    self.link_list = [] 
    self.data = pd.read_csv('Recipe Collection.csv')
    self.list_RECIPES = []
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.links = []
    self.shortest_links = []
    self.choose = 0
    self.alpha = alpha
    self.beta = beta

  def scrape(self):
      for x in range(len(self.data)):
        self.food_data = self.data.iloc[x, 0]
        self.found = re.search(self.alpha, self.food_data)
        if self.found != None:
          self.link = self.data.iloc[x, 1]
          self.link_list.append(self.link)

      if len(self.link_list) == 0:
        print(f'System ERROR: couldnt find food item: {self.alpha}')
        sys.exit()

      ### Create choice option here ###
      self.link_list_choice = self.link_list[0]
      self.req = Request(str(self.link_list_choice)) #Or any link

      self.html_page = urlopen(self.req)
      self.soup = BeautifulSoup(self.html_page, "lxml")

      def get_scrape(self, list_1, list_2, list_3, z):
        #This is the cool bit. It gets the title, instructions, and ingredients of the recipes with the ingredient in it.
        self.title = self.scrape_me.title()
        self.instructions = str(self.scrape_me.instructions())
        self.formatting_is_shit = ''.join([x for x in z])
        self.list_1.append(self.formatting_is_shit)
        print(f'List1: {list_1}')
        self.list_2.append(self.title)  
        self.list_3.append(str(self.instructions)) 
        return self.list_1, self.list_2, self.list_3


      def format(self, array):
        self.arr = []
        for x in array:
          self.arr.append(x)
        return ''.join(self.arr)

      #please ask no questions about the function naming
      def return_scrape(self, list_1, list_2, list_3, start_time):
        self.duration = time.time() - start_time
        for num in range(len(self.list_2)):
          if num % 2 == 0:
            print(str(num//2+1)+ ". "+self.list_2[num])
        self.choose = 1#int(input("Choose a recipe (number):  "))

        if len(self.list_2) == 1:
          self.choose = 0
          print("Let's cook",self.list_2[self.choose])
          self.ingredients = self.list_1[0]
          self.instructions = self.list_3[0]
        else:
          print("Let's cook",self.list_2[(self.choose*2)-1])
        self.instructions = self.list_3[(self.choose*2)-1]
        self.instructions = self.instructions.split(".")
        return self.ingredients 


      ### Sorts the links and returns the ingredients ###
      for link in self.soup.findAll('a'):
        self.main_link = link.get('href')
        self.x = re.search("recipes/", str(self.main_link))
        self.z = re.search("https", str(self.main_link))
        self.a = re.search("collection", str(self.main_link))
        if self.x != None and self.z != None and self.a == None:
          from recipe_scrapers import scrape_me
          self.scrape_me = scrape_me(self.main_link)
          self.z = list(self.scrape_me.ingredients())
          #x = re.search(beta, z)
          #if x != None:
          self.list_RECIPES.append(self.main_link)    
          self.list_1, self.list_2, self.list_3 = get_scrape(self, self.list_1, self.list_2, self.list_3, self.z)
          self.ingreds = return_scrape(self, self.list_1, self.list_2, self.list_3, self.start_time)
          return self.ingreds
