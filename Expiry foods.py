from datetime import date
import datetime

list_dates = []
list_item= []

number_items = int(input(say("How many items do you want to input?")))

# Adding ingredients, might need to add to csv?

for x in range(number_items):

  say("Enter the name of the item.")

  item = listen()
  list_item.append(item)

  say("Enter the expirt date of the item.")

  date_input = listen()
  if "th" in date_input:
    date_input = date_input.replace("th","/")
  if "st" in date_input:
    date_input = date_input.replace("st","/")
  if "nd" in date_input:
    date_input = date_input.replace("nd","/")
  if "rd" in date_input:
    date_input = date_input.replace("rd","/")
  if "of" in date_input:
    date_input = date_input.replace("of","")
  
  date_input = date_input.replace(" ","")
  list_dates.append(date_input)

# Checking ingredients for expiry date, this only gets one ingredient. 
today = date.today()
x = datetime.datetime(today.year, today.month, today.day + 1)
x = x.strftime("%d/%m/%Y")

for num in range(number_items):
  if str(x) == list_dates[num]:
    self.alpha = list_items[num]
    break

# Roman, not quite sure if I got the self.alpha bit right. Sorry. 
# Also, can you add another option to the bot to both add ingredients & to make recipes using the ingreidents that will go off. Thanks so much.
