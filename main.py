from recipe_scrapers import scrape_me
import re, os, sys, time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import random

def scrape(alpha):
    start_time = time.time()
    link_list = []
    data = pd.read_csv('Recipe Collection.csv')  
    for x in range(len(data)):
      food_data = data.iloc[x, 0]
      found = re.search(alpha, food_data)
      if found != None:
        link = data.iloc[x, 1]
        print(f'link found: {link}')
        link_list.append(link)

        
data = pd.read_csv('Food Database.csv')

### INTRODUCTION ###

print('---Welcome to the enviro bot---')
print('Please enter your first item so we can get an idea of what you might be able to cook')

text = 'Are there any recipes for rice'
text = text.split()
comma_debug_mode = False

##### Processing any Commas ###
for word in text:
  if word[-1] == ',':
    wrd = [w for w in word]
    wrd.remove(',')
    text[text.index(word)] = ''.join(wrd)

show = []
for x in range(0, 904):
  search = data.iloc[x, 0].split()
  for word in text:
    #checks for double letter foods like 'wheat bread' or 'white cabbage' and deletes the pre-word
    if text.index(word)+1 < len(text):
      if [text[text.index(word)], text[text.index(word)+1]] == search:
        text.pop(text.index(word))

def obtain_input(text):
    found = []
    search_found = []
    results = []
    for x in range(0, 904):

      search = data.iloc[x, 0].split()
      
      for word in text:
        if word in search or word == search:
          if search[-1] == word:
            if word not in results:
              results.append(word)
                  
        if word[-1] == 's':  
          wrd = [x for x in word]
          wrd.pop()
          if ''.join(wrd) in search:
            if ''.join(wrd) not in results:
              results.append(''.join(wrd))
        if word[-1] != 's':
          wrd = [x for x in word]
          wrd.append('s')
          if ''.join(wrd) in search:
            if ''.join(wrd) not in results:
              results.append(''.join(wrd))
    return results

while True:
  #unsorted_result = obtain_input(text)
  out = obtain_input(text)
  #out = sort_input(unsorted_result)
  print(f'output: {out}')
  if len(out) == 0:
    print('didnt find the food item')
  else:
    print(f'Found word: {out[0]}')
    print('---------------')
    print('---------------')
    scrape(out[0])
  sys.exit()
























'''
        if found != None:
            link = data.iloc[x]["BBCGoodFood link"]
            print(data.iloc[x]['Wasted Food'])
            link_list.append(link)
        else:
            print(f'failed to find food item: {alpha}')
            print('Ending Process')
            sys.exit()
                  
    #alpha = input("What other ingredient do you want to find: ")
    alpha = beta
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
          title = scrape_me.title()
          instructions = str(scrape_me.instructions())
          list_1.append(z)
          list_2.append(title)
          list_3.append(str(instructions))
            # This is the cool bit. It gets the title, instructions, and ingredients of the recipes with the ingredient in it. 

    duration = time.time() - start_time

    print(duration)

    for num in range(len(list_2)):
      if num % 2 == 0:
        print(str(num//2+1)+ ". "+list_2[num])

       

    print(" ")
    choose = 1#int(input("Choose a recipe (number):  "))


    print("  ")
    print("Let's cook",list_2[choose*2-1])
    print("")
    print("Here are the ingredients you need: \n")

    ingredients = list_1[choose*2-1]
    ingredients = ingredients.split("'")

    for x in range(len(ingredients)):
      if x % 2 == 1:
        ingreds = ingredients[x]

    print("  ")

    
    instructions = list_3[choose*2-1]
    instructions = instructions.split(".")
    for x in range(len(instructions)):
      press = input("Press ENTER to continue: ")
      instr = instructions[x]

    return ingreds
'''
