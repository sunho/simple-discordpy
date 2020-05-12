# Simple Discordpy

Targetting students who learn python for the first time, this library wraps discord.py to eliminate the complex syntaxes such as await and class. 

The library was able to motivate the students by enabling them to use python for applications in real world without learning extra notions.

## Example

As the features of this libray is limited, almost all of them can be covered just by the following example.

```
from sd import *
sdstart('discord token') # start the bot

sdprint("input a") # send discord message
a=sdinput() # receive a string from user through discord
sdprint("a", a)
sdstop() # stops the bot
```
