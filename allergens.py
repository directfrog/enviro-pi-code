import re

specifications = []

allergens = ["almond", "brazil", "cashew", "celery", "egg", "fish", "hazelnut", "macadamia", "milk", "mussels", "mustard",  "oysters", "peanut", "pecan", "pistachio", "prawns", "sesame", "soybeans", "walnut"]
vegetarian = ["lamb", "beef", "chicken", "pork", "sausage", "parmesan", "fish"]
vegan = ["lamb", "beef", "chicken", "pork", "sausage", "parmesan", "fish", "milk", "cheddar", "cheese", "egg"]
lactose_intolerant = ["milk","cheese", "cheddar", "parmesan", "feta"]
for x in range(len(allergens)):
  positive = re.search(allergens[x],str(ingredients))
  if positive != None:
    specifications.append(allergens[x])

for x in range(len(vegetarian)):
  positive = re.search(vegetarian[x],str(ingredients))
  if positive != None:
    print("This recipe is not vegetarian")
    break

for x in range(len(vegan)):
  positive = re.search(vegan[x],str(ingredients))
  if positive != None:
    print("This recipe is not vegan")
    break
print(" ")
print("Allergens:")
for x in range(len(specifications)):
  print(specifications[x])

