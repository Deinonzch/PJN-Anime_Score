#!/usr/bin/python3
import sys
import re

bone = 'https://myanimelist.net/anime/genre/4/Comedy?page='

url = ''

for x in range(0, 47):
	url = url + bone + str(x+1) + "\n"

print(url)
