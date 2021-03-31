from recipe_scrapers import scrape_me
import re, os, sys, time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import random

from web_scraping import *
from word_processing import *
          
### INTRODUCTION      
print('---Welcome to the enviro bot---')
print('Please enter your main food item so we can get an idea of what you might be able to cook')

class EnviroBot:
  def __init__(self, beta, text):
    self.beta = beta
    self.text = text
    self.wp = word_processer(self.text)
    self.out = self.wp.obtain_input(self.text)
    if len(self.out) != 0:
      self.web_scraper = scraper(self.out[0], self.beta)
  
  def return_out(self):
    return self.out

  def run(self, alpha):
    if len(self.out) == 0:
      print(f'didnt find the food item')
      sys.exit()
    else:
      #print(f'Found word: {self.out[0]}')
      print('---------------')
      print('---------------')
      if len(self.out) == 1:
        self.beta = None
      else:
        self.beta = self.out[1]
      print(f'out: {self.out[0]}')
      self.ingreds = self.web_scraper.scrape()
      print(self.ingreds)


text = 'Find recipes using rice'
text = text.split() 
beta = None

while True:
  system = EnviroBot(beta, text)
  out = system.return_out()
  print(f'out: {out}')
  system.run(out)
  sys.exit()

