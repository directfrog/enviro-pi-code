from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from system import *
from WordProcessor import *

#Define different screens
class TextEnterWindow(Screen):
	def button_on(self):
		self.ids.button_image.source = 'button1.png'

	def button_off(self):
		self.ids.button_image.source = 'button2.png' 
		main_ingred = ProcessWords(self.ids.main_ingred.text)
		other_ingreds = ProcessWords(self.ids.other_ingred.text)

		print(main_ingred, other_ingreds)

		self.ids.main_ingred.text = ''
		self.ids.other_ingred.text = '' 

		results = get_foods(main_ingred, other_ingreds)

class TextEnterWindow(Screen):
	pass

class ResultsWindow(Screen):
	pass
	
class WindowManager(ScreenManager):
	pass

kv = Builder.load_file('RockettApp.kv')
	

class TheApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	TheApp().run()