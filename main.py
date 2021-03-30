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
    #ingredients list
    self.list_1 = []
    #title list
    self.list_2 = []
    #instructions list
    self.list_3 = []
    self.links = []
    self.choose = 0
    self.alpha = alpha
    self.beta = beta

  def scrape(self):
      for x in range(len(self.data)):
        self.food_data = self.data.iloc[x, 0]
        self.found = re.search(self.alpha, self.food_data)
        if self.found != None:
          self.link = self.data.iloc[x, 1]
          print(f'link found: {self.link}')
          self.link_list.append(self.link)

      if len(self.link_list) == 0:
        print(f'EnvrioBot ERROR: couldnt find food item: {self.alpha}')
        sys.exit()

      ### Create choice option here ###
      self.link_list_choice = self.link_list[0]
      self.req = Request(str(self.link_list_choice)) #Or any link

      self.html_page = urlopen(self.req)
      self.soup = BeautifulSoup(self.html_page, "lxml")

      def get_the_shit(self, list_1, list_2, list_3, z):
        #This is the cool bit. It gets the title, instructions, and ingredients of the recipes with the ingredient in it.
        self.title = self.scrape_me.title()
        print(f'Title: {self.title}')
        self.instructions = str(self.scrape_me.instructions())
        self.formatting_is_shit = ''.join([x for x in z])
        self.list_1.append(self.formatting_is_shit)
        self.list_2.append(self.title)
        self.list_3.append(str(self.instructions)) 
        return self.list_1, self.list_2, self.list_3


      def format(self, array):
        self.arr = []
        for x in array:
          self.arr.append(x)
        return ''.join(self.arr)

      #please ask no questions about the function naming
      def return_the_shit(self, list_1, list_2, list_3, start_time):
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
        formatted = format(self, self.ingredients)
        return formatted


      ### Sorts the links and returns the ingredients ###
      for link in self.soup.findAll('a'):
        self.main_link = link.get('href')
        self.x = re.search("recipes/", str(self.main_link))
        self.z = re.search("https", str(self.main_link))
        self.a = re.search("collection", str(self.main_link))
        if self.x != None and self.z != None and self.a == None:
          from recipe_scrapers import scrape_me
          self.scrape_me = scrape_me(self.main_link)
          self.z = str(self.scrape_me.ingredients())
          #x = re.search(beta, z)
          #if x != None:
          self.list_RECIPES.append(self.main_link)    
          self.list_1, self.list_2, self.list_3 = get_the_shit(self, self.list_1, self.list_2, self.list_3, self.z)
          self.ingreds = return_the_shit(self, self.list_1, self.list_2, self.list_3, self.start_time)
          return self.ingreds
          
        


### INTRODUCTION ###

print('---Welcome to the enviro bot---')
print('Please enter your main food item so we can get an idea of what you might be able to cook')

text = 'Hey Joe, what are some recipes for bread'
text = text.split()
comma_debug_mode = False

class word_processer(object):
  def __init__(self, text):
    self.text = text
    self.data = data = pd.read_csv('Food Database.csv')
    self.found = []
    self.search_found = []
    self.results = []

  def comma_process(self):
    for word in self.text:
      if word[-1] == ',':
        self.wrd = [w for w in word]
        self.wrd.remove(',')
        self.text[self.text.index(word)] = ''.join(self.wrd)
    return text


  def adjective_process(self):
    for x in range(0, 904):
      self.search = self.data.iloc[x, 0].split()
      for word in self.text:
        #checks for double letter foods like 'wheat bread' or 'white cabbage' and deletes the pre-word
        if self.text.index(word)+1 < len(self.text):
          if [self.text[self.text.index(word)], self.text[self.text.index(word)+1]] == self.search:
            self.text.pop(text.index(word))
    return text

  def obtain_input(self, text):
    text = self
    for x in range(0, 904):
      self.search = self.data.iloc[x, 0].split()
      for word in self.text:
        if word in self.search or word == self.search:
          if self.search[-1] == word:
            if word not in self.results:
              self.results.append(word)
                    
        if word[-1] == 's':  
          self.wrd = [x for x in word]
          self.wrd.pop()
          if ''.join(self.wrd) in self.search:
            if ''.join(self.wrd) not in self.results:
              self.results.append(''.join(self.wrd))
        if word[-1] != 's':
          self.wrd = [x for x in word]
          self.wrd.append('s')
          if ''.join(self.wrd) in self.search:
            if ''.join(self.wrd) not in self.results:
              self.results.append(''.join(self.wrd))
    return self.results

beta = None
def run(beta):
  wp = word_processer(text)
  out = wp.obtain_input(text)
  web_scraper = scraper(out[0], beta)
  if len(out) == 0:
    print('didnt find the food item')
    sys.exit()
  else:
    print(f'Found word: {out[0]}')
    print('---------------')
    print('---------------')
    if len(out) == 1:
      beta = None
    else:
      beta = out[1]
    print(f'out: {out[0]}')
    ingreds = web_scraper.scrape()
    print(ingreds)

while True:
  run(beta)
  sys.exit()
