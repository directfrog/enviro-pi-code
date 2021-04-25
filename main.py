from recipe_scrapers import scrape_me
import re, os, sys, time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
import random
import math
import time
from speech_recog_owo import *
import pyttsx3
from web_scraping import *
from word_processing import *
import csv
from gtts import gTTS
import pygame
from pygame import mixer
time.sleep(20)

debug_mode = True

def say(text):
    tts = gTTS(text)
    tts.save('tts_output.mp3')
    pygame.mixer.init(30000)
    pygame.mixer.music.load('tts_output.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    
class EnviroBot:
  def __init__(self, beta, text):
    self.beta = beta
    self.text = text
    self.wp = word_processer(self.text)
    self.out = self.wp.obtain_input(self.text)
    print(f'results from word processor: {self.out}')
    say('searching for recipes using the ingredient. This might take a minute or two')

  def return_scraper_data(self):
    if len(self.out) > 0:
      web_scraper_object = scraper(self.out[0], self.beta)
      web_scraper_object.scrape()
      recipes = web_scraper_object.sort_shortest()
      return recipes
    else:
      return None
def openRecipesListen():
  text = 'open recipes'
  patterns = ['Oops didn\'t recognize what you said, please say again', 'sorry, didint quite catch that, can you repeat yourself?', 'Oh it seems that i didnt really hear what you said, can you please repeat yourself?']
  text = None
  fault_count = 0
  while text == None:
    if fault_count > 0:
      say(random.choice(patterns))
    say('i\'m listening')
    recogniser = speech_recog_object()
    text = recogniser.speech_recog_run()
    print(f'Heard: {text}')
    if text != None:
      if 'power off' in text or 'power down' in text or 'shut down' in text or 'turn off' in text:
        say('powering off')
        sys.exit()
      search = re.search('open recipes', text.lower())
      if search != None:
        return True
      if search == None:
          search = re.search('open', text.lower())
          if search != None:
            return True
          if search == None:
            return False
    fault_count += 1

def sort_clean(result):
    for x in result:
        if isinstance(x, list):
            copy = x.copy()
            result.pop(result.index(x))
            for i in copy:
                result.append(i)
    return result

def listen(find):
  patterns = ['Oops didn\'t recognize what you said, please say again', 'sorry, didint quite catch that, can you repeat yourself?', 'Oh it seems that i didnt really hear what you said, can you please repeat yourself?']
  text = None
  fault_count = 0
  while text == None:
    if fault_count > 0:
      say(random.choice(patterns))
    say('i\'m listening')
    recogniser = speech_recog_object()
    text = recogniser.speech_recog_run()
    print(f'Heard: {text}')
    if text != None:
      if 'power off' in text or 'power down' in text or 'shut down' in text or 'turn off' in text:
        say('powering off')
        sys.exit()
      search = re.search(find, text.lower())
      if search != None:
        return True
      if search == None:
        return False
    fault_count += 1

     
def find_recipe_interface(system):
  recipes = system.return_scraper_data()
  if recipes != None:
    try:
        say('I found some recipes based on the ingredient')
    except:
        say('oh i just lost signal to the internet. Maybe move me closer to the router. Ill boot again ')
    say('Do you want me to also say the other ingredients of the recipe?')
    result = listen('yes')
    if result:
      list_ingredients = True
    else:
      list_ingredients = False

    patterns = ['Ok', 'Cool', 'Alright, lets get started then']
    say(random.choice(patterns))
    
    ######## Gets groups of two recipes ########
    recipe_groups = []
    count = 0
    for x in range(len(recipes)):
      if list_ingredients == True:
        result = ['Recipe ', str(x+1), ': ', str(recipes[x][1]), ' with the ingredients :', [re.sub(r"\([^()]*\)", "", ingredient) for ingredient in recipes[x][0]]]
        result = sort_clean(result)
        say(''.join(list(result)))
        
      else:
        result = ['Recipe ', str(x+1), ': ', str(recipes[x][1]),'. The amount of ingredients is: ', str(len([re.sub(r"\([^()]*\)", "", ingredient) for ingredient in recipes[x][0]]))]
        result = sort_clean(result)
        say(''.join(result))
 
      ##### Asks to chose recipe #####
      patterns = ['Do you want to choose this recipe?', 'Do you want me to log this recipe?', 'Do you want to make this dish?']
      say(random.choice(patterns))
      result = listen('yes')
      if result:
        say(f'Ok, you chose the recipe: {recipes[x][1]}')
        ##### creates list of chosen recipce #####
        chosen_recipe = recipes[x]


        ######## Adding recipes data to run_data csv ########
        run_data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_data.csv")
        with open(run_data_load, mode='w') as file:
          writer = csv.writer(file)

          ingredients = [re.sub(r"\([^()]*\)", "", x) for x in chosen_recipe[0]]
          title = chosen_recipe[1]
          instructions = chosen_recipe[2]
          print(f'title: {title}')
          print(f'ingredients: {ingredients}')
          print(f'instructions: {instructions}')
          writer.writerow(['title', 'ingredients', 'instructions'])
          writer.writerow([title, ingredients, instructions])
          
          ##### program ending here/ adding runtimes to program_data file #####
          say('I have stored the recipe that you want to use, so next time I boot up, just say: open recipes')
          program_data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "program_data.csv")
          program_data = pd.read_csv(program_data_load)
          run_times = program_data.iloc[0, 0]
          run_times += 1
          with open(program_data_load, mode='w') as file:
              file.truncate(0)
              writer = csv.writer(file)
              writer.writerow(['run_times'])
              writer.writerow([run_times])
          say('should i power off')
          result = listen('yes')
          if result:
              say('powering off. remember to hit the off button.')
              sys.exit()
          else:
              say('ok, restarting.')
              run()
      else:
        continue
  else:
    say('Didnt find anything for that food')
    say('Do you want to try another one?')
    result = listen('yes')
    if result:
      text = None
      fault_count = 0
      while text == None:
        if fault_count > 0:
          say('didn\'t recognise what you said, try again')
        say('i\'m listening')
        recogniser = speech_recog_object()
        text = recogniser.speech_recog_run()
        print(f'recognised: {text}')
        if text != None:
          text = text.lower()
          if len(text) > 1:
            text = text.split()
          system = EnviroBot(beta=None, text=text)
          find_recipe_interface(system)
          sys.exit()
        fault_count += 1
    else:
      say('ok powering off then')
      sys.exit()

def get_run_times():
  program_data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Program Data.csv")
  program_data = pd.read_csv(program_data_load)
  run_times = program_data.iloc[0, 0]
  return run_times

def open_recipes_file():
  say('opening recipes file')
  data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run_data.csv")

  with open(data_load, mode='r') as file:
    data_read = pd.read_csv(file)
    if data_read.empty:
      say('the recipes file seems to be empty, try find a recipe first and try again')
      run()
    else:
      say(f'the recipe: {data_read.iloc[0, 0]}  is currently in the file')
      say('do you want me to read out the ingredients')
      result = listen('yes')
      if result:
        say('here are the ingredients')
        ##### Find and say the ingredients #####
        ingreds = data_read.iloc[0, 1]
        res = ingreds.strip('[]').split(', ')
        for index in res:
            #note that we dont change the actual file, we run this code to read someting
            result = index.strip("'")
            say(result)

        ##### ask to say the instructions #####
        say('do you want me to say the instructions')
        result = listen('yes')
        if result:
          instructions = data_read.iloc[0, 2]
          say(f'The instructions are {instructions}')
          say('do you want me to power off?')
          result = listen('yes')
          if result:
              say('ok, remember to press the off button')
              sys.exit()
          else:
              say('ok, rebooting then')
              run()
              
        else:
          say('powering off then')
          sys.exit()
      else:
        say('ok, powering off then')
        sys.exit()

  sys.exit()

def run():
  text = None
  while True:
    data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Recipe Collection.csv")
    data = pd.read_csv(data_load)

    ###### introduction #####
    if debug_mode == False:
      say('hi, i\'m the enviro bot')
      say('you can say: find recipes to find a recipe or: open recipes to open the file where I have stored your past recipes')
    print('PROGRAM START')
    result = openRecipesListen()
    if result:
      open_recipes_file()
    else:
      say('alright, tell me your main ingredient')
      fault_count = 0
      while text == None:
        if fault_count > 0:
          say('didn\'t recognise what you said, try again')
        say('i\'m listening')
        recogniser = speech_recog_object()
        text = recogniser.speech_recog_run()
        print(f'recognised: {text}')
        if text != None:
          text = text.lower()
          if len(text) > 1:
            text = text.split()
          system = EnviroBot(beta=None, text=text)
          find_recipe_interface(system)
          sys.exit()
        fault_count += 1

run()
