import googletrans as translate
import sys
import os
import platform

def docs():
	print("https://github.com/javid-aliyev/Translator-application")

def sinput(ps):
	"""Smart input. It handles errors but do not validate the input.
	:param ps: str
	:return: str
	"""
	try:
		npt = input(ps)
		return npt
	except (KeyboardInterrupt, EOFError):
		return

def clear_console():
	if platform.system().lower() == "windows":
		os.system("cls")
	else:
		os.system("clear")

def execute_command(command):
	global src_lang
	global dest_lang	

	if command == ":setdest":
		dest_lang = sinput("Destination language? ")
	elif command == ":setsrc":
		src_lang = sinput("Source language? ")
	elif command == ":getdest":
		print(dest_lang)
	elif command == ":getboth":
		print(f"Destination language: {dest_lang}")
		print(f"Source language: {src_lang}")
	elif command == ":getsrc":
		print(src_lang)
	elif command == ":reverse":
		dest_lang, src_lang = src_lang, dest_lang
	elif command == ":help":
		docs()
	elif command == ":clear":
		clear_console()
	elif command == ":quit":
		sys.exit()
	elif command == "":
		return
	else:
		print("Invalid command")

def translate_text(text, dest, src):
	"""Returns translated text
	:param text: str
	:param dest: str
	:param src: str
	:return: str
	"""

	translator = translate.Translator()
	try:
		translated_text = translator.translate(
			text,
			dest=dest,
			src=src
		)
		return translated_text.text
	except ValueError:
		return "Incorrect destination or source language"

def main():
	while True:
		npt = sinput("text/command: ")
		if npt[0] == ":":
			execute_command(npt)
		else:
			print(translate_text(npt, dest_lang, src_lang))

if __name__ == "__main__":
	src_lang = "en"
	dest_lang = "ru"
	main()
