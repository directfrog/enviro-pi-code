from recipe_scrapers import scrape_me
import re, os, sys, time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
from web_scraping import WebScrape
running = True

data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Food Database.csv")
data = pd.read_csv(data_load)

text = 'hey I have some chicken that needs to be used'
text = text.split()
def obtain_input(text):
    possible_words = []
    found = []
    for x in range(0, 904):
        search = data.iloc[x, 0].split()
        for word in text:
            if (text.index(word)+1 <= (len(text)-1)) and (text.index(word)-1 >= 0):
                if word not in possible_words:
                    possible_words.append(word)
                if f'{text[text.index(word)]} {text[text.index(word)+1]}' == ' '.join(search):
                    f = f'{text[text.index(word)]} {text[text.index(word)+1]}'
                    if f not in found:
                        found.append(f)
                if f'{text[text.index(word)]} {text[text.index(word)-1]}' == ' '.join(search):
                    f = f'{text[text.index(word)]} {text[text.index(word)-1]}'
                    if f not in found:
                        found.append(f)
            if word in search:
                f = f'{word}'
                if f not in found:
                    found.append(f)
    if len(found) == 1:
        return ''.join(found)
    if len(found) > 1:
        base_name = found[0]
        for x in found:
            if len(x) > len(base_name):
                base_name = x
                print(f'base name: {base_name}')
                return base_name



while True:
    input = obtain_input(text)
    print(f'recognised food item: {input}')
    if input == None:
        print('do not recognise food item sorry. Try telling me the name of the food item only (eg cucumber or pepper)')

    scraper = WebScrape(input)
    scraper.scrape()
    result = scraper.run()
    print(result)
