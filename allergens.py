import datetime
import numpy as np
import pandas as pd
today = datetime.date.today()
today.month


if today.month == 1:
  month = 'january'
elif today.month == 2:
  month = 'february'
elif today.month == 3:
  month = 'march'
elif today.month == 4:
  month = 'april'
elif today.month == 5:
  month = 'may'
elif today.month == 6:
  month = 'june'
elif today.month == 7:
  month = 'july'
elif today.month == 8:
  month = 'august'
elif today.month == 9:
  month = 'september'
elif today.month == 10:
  month = 'october'
elif today.month == 11:
  month = 'november'
else:
  month = 'december'



from recipe_scrapers import scrape_me
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re 
import pandas as pd
import time

import csv
import re

seasonal_food_data = pd.read_excel('seasonal fruit and veg_.xlsx')

start_time = time.time()
link_list = []
data = pd.read_excel('Recipe Collection.xlsx')  
alpha = input("What is your main ingredient you've wasted:  ")

for x in range(len(data)):
  food_data = data.iloc[x]["Wasted Food"]
  found = re.search(alpha, str(food_data))
  if found != None:
    link = data.iloc[x]["BBCGoodFood link"]
alpha = input("What other ingredient do you want to find: ")
print(" ")

list_RECIPES = []
list_1 = []
list_2 = []
list_3 = []

req = Request(str(link)) #Or any link
html_page = urlopen(req)
soup = BeautifulSoup(html_page, "lxml")

links = []

for link in soup.findAll('a'):
  main_link = link.get('href')
  x = re.search("recipes/", str(main_link))
  z = re.search("https", str(main_link))
  a = re.search("collection", str(main_link))
  if x != None and z != None and a == None:
    from recipe_scrapers import scrape_me
    scrape_me = scrape_me(main_link)
    z = str(scrape_me.ingredients())
    x = re.search(alpha, z)
    if x != None:
      list_RECIPES.append(main_link)
      title1 = scrape_me.title()
      instructions = str(scrape_me.instructions())
      list_1.append(z)
      list_2.append(title1)
      list_3.append(str(instructions))
        # This is the cool bit. It gets the title, instructions, and ingredients of the recipes with the ingredient in it. 

duration = time.time() - start_time

print(duration)

counterotherthing = 0
counterothernextthing = 0
allergens_results = [ ]
allergens_results_counter = []
length_of_allergens = 1

for num in range(len(list_2)):
  if num % 2 == 0:
    print(str(num//2+1)+ ". "+list_2[num])
    with open('FoodData.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      variable = 0
      while counterotherthing < num//2+1: 
        allergens_counter = 0
        counterotherthing += 1
        ingredients_thing = list_1[counterotherthing*2-1]
        ingredients_thing1 = ingredients_thing.title()
        for x in range(len(ingredients_thing)):
            for row in csv_reader:
              a = row[3]
              b = a.title()
              line_count += 1
              posativething = re.search(b, ingredients_thing1)
              posative_cherry = re.search('Cherry',  ingredients_thing1)
              posative_tomato = re.search('Tomato', ingredients_thing1)
              if posativething and b != 'Cherry':
                allergens_results.append(b) 
              elif posativething and posative_cherry and posative_tomato == None:
                allergens_results.append('Cherry') 
    print('Warning, contains:', allergens_results[length_of_allergens -1: -1])
    length_of_allergens = len(allergens_results)
  
    while counterothernextthing < 1:
              for x in range(0, 396):
                food = seasonal_food_data.iloc[x,0]
                food1 = food.title()
                month_in_season = seasonal_food_data.iloc[x,1]
                line_count += 1
                allergens_counter += 1
                posativething1 = re.search(food1, ingredients_thing1)
                if posativething1:
                  if month_in_season == month:
                   counterothernextthing += 1
              if allergens_counter >= 397:
                break
              break
    if counterothernextthing >= 2:
      print('Reccomended: Contains', counterothernextthing, 'in-season ingredients')
    else: 
      print('Reccomended: Contains:', counterothernextthing, 'in-season ingredient')

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

print("  ")

instructions = list_3[choose*2-1]
instructions = instructions.split(".")
for x in range(len(instructions)):
  press = input("Press ENTER to continue: ")
  print(instructions[x])
  
# This whole bit just presents the ouptut to the user. 
