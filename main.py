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
    self.data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Recipe Collection.csv")
    self.data = pd.read_csv(self.data_load)
    self.list_RECIPES = []
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.links = []
    self.choose = 0
    self.alpha = alpha
    self.beta = beta
    self.food_data_list = []
    self.short_sort = []

  def scrape(self):
    for x in range(len(self.data)):
      self.food_data = self.data.iloc[x, 0]
      self.found = re.search(self.alpha, self.food_data)
      if self.found != None:
        self.link = self.data.iloc[x, 1]
        self.link_list.append(self.link)

    ######## Checks for empty list (food words not mentioned or recognised) ########
    if len(self.link_list) == 0:
      print(f'System ERROR: couldnt find food item: {self.alpha}')
      sys.exit()

    ######## Opens the page with soup #########
    for self.link_list_choice in self.link_list:
      self.req = Request(str(self.link_list_choice)) #Or any link
      self.html_page = urlopen(self.req)
      self.soup = BeautifulSoup(self.html_page, "lxml")


      ######## Sorts the links and returns the ingredients ########
      for link in self.soup.findAll('a'):
        self.main_link = link.get('href')
        self.x = re.search("recipes/", str(self.main_link))
        self.z = re.search("https", str(self.main_link))
        self.a = re.search("collection", str(self.main_link))
        if self.x != None and self.z != None and self.a == None:
          from recipe_scrapers import scrape_me
          try:
            self.scrape_me = scrape_me(self.main_link)
            ####### Gets the ingredients using scrape_me #######
            self.z = list(self.scrape_me.ingredients())
            
            ######## checks for second ingredient in ingredients ########
            #note that beta != None is because beta is already None, it just changes if a second food word is detected in the beginning text
            if self.beta != None:
              x = re.search(self.beta, z)

            if x != None:
              try:
                ######## Gets all of the data from the page ########
                self.title = self.scrape_me.title()
                self.instructions = str(self.scrape_me.instructions())
                self.list_1 = [x for x in self.z]
                self.list_2 = self.title  
                self.list_3 = str(self.instructions) 

                food_list = [self.list_1, self.list_2, self.list_3]
                if food_list not in self.food_data_list:
                  self.food_data_list.append(food_list)
              except:
                continue

            else:
              print('Sorry, couldnt find the second ingredient, but i still found recipes with the first ingredient')
              try:
                ######## Gets all of the data from the page ########
                self.title = self.scrape_me.title()
                self.instructions = str(self.scrape_me.instructions())
                self.list_1 = [x for x in self.z]
                self.list_2 = self.title  
                self.list_3 = str(self.instructions) 

                food_list = [self.list_1, self.list_2, self.list_3]
                if food_list not in self.food_data_list:
                  self.food_data_list.append(food_list)
              except:
                continue
                print('Continued')
          except:
            continue
    
  def sort_shortest(self):
    for num in range(len(self.food_data_list)):
      current_lowest = self.food_data_list[0]
      for i in self.food_data_list:
        if len(i[0]) < len(current_lowest[0]):
          current_lowest = i 
      self.short_sort.append(current_lowest)
      self.food_data_list.pop(self.food_data_list.index(current_lowest))
    return self.short_sort



    


