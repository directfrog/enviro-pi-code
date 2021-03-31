import re, os, sys, time
import pandas as pd

class word_processer(object):
  def __init__(self, text):
    self.text = text
    self.data = data = pd.read_csv('Recipe Collection.csv')
    self.found = []
    self.search_found = []
    self.results = []

  def obtain_input(self, text):
    true_double_word = None
    for x in range(0, len(self.data)-1):
      self.search = self.data.iloc[x, 0].split()
      for word in self.text:
        ### Processes Commas ###
        if word[-1] == ',':
          self.wrd = [w for w in word]
          self.wrd.remove(',')
          self.text[self.text.index(word)] = ''.join(self.wrd)

        ### Gets double words ###
        if (self.text.index(word)+1) < len(self.text):
          double_word = f'{self.text[self.text.index(word)]} {self.text[self.text.index(word)+1]}'
          if double_word in ' '.join(self.search) or double_word == ' '.join(self.search):
            if double_word not in self.results:
              true_double_word = double_word
              self.results.append(true_double_word)

    ##### Deals with single letter words (outside of loop to compare to double letter word that is found in the search) #####              
    for x in range(0, len(self.data)-1):
     self.search = self.data.iloc[x, 0].split()
     for word in self.text:
      if word in self.search or word == self.search:
        if word not in self.results:
        #if self.search[-1] == word:
          if true_double_word == None:
            self.results.append(word)
          else:
            if word not in true_double_word.split():
              self.results.append(word)
      else:
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
    print(f'TDW: {true_double_word}')
    return self.results
