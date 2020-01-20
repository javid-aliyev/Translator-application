from googletrans import Translator
from sys import exit
from os import system

def docs():
	pass

def main():
	translator = Translator()
	src = "en"
	dest = "ru"

	run = True
	while run:
		try:
			user_input = input("~ ").strip()
		except KeyboardInterrupt:
			run = False

		# commands
		if user_input == ":setdest":
			try:
				d = input("Destination(en/ru/..)? ").strip().lower()
				dest = d
			except KeyboardInterrupt: exit()
		elif user_input == ":setsrc":
			try:
				s = input("Source(en/ru/..)? ").strip().lower()
				src = s
			except KeyboardInterrupt: exit()
		elif user_input == ":getdest": print(dest)
		elif user_input == ":getsrc": print(src)
		elif user_input == ":help": docs()
		elif user_input == ":clear":
			system("clear")
			system("cls")
		elif user_input == ":exit":	exit()
		elif user_input.strip() == "": continue
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