import re, os, sys, time
import pandas as pd

class word_processer(object):
  def __init__(self, text):
    self.text = text
    self.data_load = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Recipe Collection.csv")
    self.data = pd.read_csv(self.data_load)
    
    self.found = []
    self.search_found = []
    self.results = []

  def obtain_input(self, text):
    true_double_word = None
    print(f'word being used: {text}')
    for x in range(0, len(self.data)-1):
      self.search = self.data.iloc[x, 0].split()
      for word in self.text:
        ### Processes Commas ###
        if word[-1] == ',':
          self.wrd = [w for w in word]
          self.wrd.remove(',')
          self.text[self.text.index(word)] = ''.join(self.wrd)
    for x in range(0, len(self.data)-1):
      self.search = self.data.iloc[x, 0].split()
      for word in self.text:

        ### Gets double words ###
        if (self.text.index(word)+1) < len(self.text):
          double_word = f'{self.text[self.text.index(word)]} {self.text[self.text.index(word)+1]}'
          if double_word in ' '.join(self.search) or double_word == ' '.join(self.search):
            if double_word not in self.results:
              true_double_word = double_word
              self.results.append(true_double_word)
              return self.results 
              break
    #print(f'results unchanged: {self.results}')

    for x in range(0, len(self.data)-1):
     self.search = self.data.iloc[x, 0].split()
     for word in self.text:

      ######## processes singulars ########
      if word in self.search or word == self.search:
        if word not in self.results:
          if true_double_word == None:
            self.results.append(word)
          else:
            if word not in true_double_word.split():
              self.results.append(word)
      
      else:
        ######## Processes plurals ########
        if word[-1] == 's':
          wrd = [x for x in word]
          wrd.pop()
          if ''.join(wrd) in self.search:
            if ''.join(wrd) not in self.results:
              if true_double_word == None:
                self.results.append(''.join(wrd))
              else:
                if ''.join(wrd) not in true_double_word.split():
                  self.results.append(''.join(wrd))

        ######## Processes 'es' plurals (like potatoes) ########
        if word[-1] == 's' and word[-2] == 'e':
          wrd = [x for x in word]
          wrd.pop()
          wrd.pop()
          if ''.join(wrd) in self.search:
            if ''.join(wrd) not in self.results:
              if true_double_word == None:
                self.results.append(''.join(wrd))
              else:
                if ''.join(wrd) not in true_double_word.split():
                  self.results.append(''.join(wrd))
                  return self.results
                  break

        ######## Processes 'ies' plurals
        if word[-1] == 's' and word[-2] == 'e' and word[-3] == 'i':
          wrd = [x for x in word]
          for x in range(3):
            wrd.pop()
          wrd.append('y')
          if ''.join(wrd) in self.search:
            if ''.join(wrd) not in self.results:
              if true_double_word == None:
                self.results.append(''.join(wrd))
              else:
                if ''.join(wrd) not in true_double_word.split():
                  self.results.append(''.join(wrd))

        ######## processes singulars ########
        if word[-1] != 's':
          wrd = [x for x in word]
          wrd.append('s')
          if ''.join(wrd) in self.search:
            if ''.join(wrd) not in self.results:
              if true_double_word == None:
                self.results.append(''.join(wrd))
              else:
                if ''.join(wrd) not in true_double_word.split():
                  self.results.append(''.join(wrd))

    ######## process plurals that exist in singular form in double word ########
    if true_double_word != None:
      for food in self.results:
        if food != true_double_word:
          wrd = [x for x in food]
          if wrd[-1] == 's':
            wrd.pop()
            if ''.join(wrd) in true_double_word.split():
              self.results.pop(self.results.index(food))

    if len(self.results) > 1:
      self.results = self.results.pop()

    return self.results
