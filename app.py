from googletrans import Translator
from sys import exit
from os import system

def main():
	translator = Translator()
	src = "en"
	dest = "ru"

	run = True
	while run:
		try:
			user_input = input("~ ").strip().lower()
		except KeyboardInterrupt:
			run = False

		if user_input == ":dest":
			# set destination
			pass
		elif user_input == ":src":
			# set source
			pass
		elif user_input == ":help":
			# help
			pass
		elif user_input == ":clear":
			system("clear") # TODO: ADD windows/linux/osx condition
			system("cls")
		elif user_input == ":exit":	exit()
		else:
			try:
				translated = translator.translate(
					user_input, dest=dest, src=src
				)
				print(translated.text)
			except ValueError:
				print("Destination or source language is not correct.")

if __name__ == "__main__":
	main()