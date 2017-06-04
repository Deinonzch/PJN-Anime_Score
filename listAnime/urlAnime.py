#!/usr/bin/python3
import sys
import re

bone = 'https://myanimelist.net/anime/'

i=0
j=0

idAnime = []
nameAnime = []

for line in sys.stdin:
	words = re.findall(r'((?<=\<series_animedb_id\>)[0-9]+)',line)
	words2 = re.findall(r'((?<=\<series_title\>\<!\[CDATA\[)[^\]]+)',line)
	if words:
		i += 1
		idAnime.append(words[0])
	if words2:
		j += 1
		nameAnime.append(words2[0].replace(' ', '_'))

urlAnime = []
for index, value in enumerate(nameAnime):
	urlAnime.append(bone + idAnime[index] + '/' + value + '/characters')

url = ''
for index, value in enumerate(urlAnime):
	url = value + '\n' + url

print(url)
