# Introduction
This is a console program that allows you to quickly translate texts into different languages.
Written in Python 3.7.3 using the [googletrans](https://pypi.org/project/googletrans/) module.

# Documentation
### Theory
To control the program, text commands are used. If the input starts with ":", then the program considers it a command. Otherwise, the program considers this text to be translated.

**Destination language** - language to translate.

**Source language** - language to translate from.

*You can change **destination** and **source** language with some commands.*

---
#### Commands
##### Commands (9):
- :getdest;
- :getsrc;
- :getboth;
- :setdest;
- :setsrc;
- :reverse;
- :help;
- :clear;
- :exit.

##### What do these commands do?

1. **:getdest** - displays the language into which you want to translate.
2. **:getsrc** - displays the language from which you want to translate.
3. **:getboth** - returns dest and src together.
4. **:setdest** - changes the language you want to translate into.
5. **:setsrc** - changes the language from which you want to translate.
6. **:reverse** - changes the language from which you want to translate and the language into which you need to translate.
7. **:help** - displays a link to this documentation.
8. **:clear** - clears the console.
9. **:exit** - quits the program.

# More information
Written on Windows 7 x64 and then on Linux Ubuntu LTS 18.04.4 x64 by Javid Aliyev.
