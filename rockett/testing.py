arr = '''https://schema.org","@type":"ItemList","numberOfItems":9,"itemListElement":[{"@type":"ListItem","position":1,"url":"https://www.bbcgoodfood.com/recipes/eggy-bread"},{"@type":"ListItem","position":2,"url":"https://www.bbcgoodfood.com/recipes/mexican-eggy-bread"},{"@type":"ListItem","position":3,"url":"https://www.bbcgoodfood.com/recipes/ham-eggy-bread-salsa"},{"@type":"ListItem","position":4,"url":"https://www.bbcgoodfood.com/recipes/eggy-spelt-bread-orange-cheese-raspberries"},{"@type":"ListItem","position":5,"url":"https://www.bbcgoodfood.com/recipes/french-toast"},{"@type":"ListItem","position":6,"url":"https://www.bbcgoodfood.com/recipes/leek-tomato-eggy-bread-bake"},{"@type":"ListItem","position":7,"url":"https://www.bbcgoodfood.com/recipes/smoky-bean-bacon-eggy-bread-bake"},{"@type":"ListItem","position":8,"url":"https://www.bbcgoodfood.com/recipes/french-toast-bacon-butties"},{"@type":"ListItem","position":9,"url":"https://www.bbcgoodfood.com/recipes/cinnamon-blueberry-french-toast"}]}</script><scripthttps://images.immediate.co.uk/production/volatile/sites/30/2020/08/french-toast-dbe2eea.jpg","width":440}}],"prevItems":[],"nextUrl":null,"nextPageQueryString":null,"carouselSchema":{"@context":"https://schema.org","@type":"ItemList","numberOfItems":9,"itemListElement":[{"@type":"ListItem","position":1,"url":"https://www.bbcgoodfood.com/recipes/eggy-bread"},{"@type":"ListItem","position":2,"url":"https://www.bbcgoodfood.com/recipes/mexican-eggy-bread"},{"@type":"ListItem","position":3,"url":"https://www.bbcgoodfood.com/recipes/ham-eggy-bread-salsa"},{"@type":"ListItem","position":4,"url":"https://www.bbcgoodfood.com/recipes/eggy-spelt-bread-orange-cheese-raspberries"},{"@type":"ListItem","position":5,"url":"https://www.bbcgoodfood.com/recipes/french-toast"},{"@type":"ListItem","position":6,"url":"https://www.bbcgoodfood.com/recipes/leek-tomato-eggy-bread-bake"},{"@type":"ListItem","position":7,"url":"https://www.bbcgoodfood.com/recipes/smoky-bean-bacon-eggy-bread-bake"},{"@type":"ListItem","position":8,"url":"https://www.bbcgoodfood.com/recipes/french-toast-bacon-butties"},{"@type":"ListItem","position":9,"url":"https://www.bbcgoodfood.com/recipes/cinnamon-blueberry-french-toast"}]},"limit":24,"pockets"
:{"listContentBottom":[],"listFooter":[{"componentId":"dynamicRelatedContent","props":{"data":{"title":"Related'''

print(type(arr))

def get_links(arr):
	links = []
	for x in range(len(arr)):
		if arr[x] == 'h' and arr[x+1] == 't' and arr[x+2] == 't' and arr[x+3] == 'p' and arr[x+8] == 'w':
			for extension in range(x, x+80):
				if arr[extension] == '}':
					links.append(str(arr[x:extension-1]))
	return links

links = get_links(arr)
print(links)