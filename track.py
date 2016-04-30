import os
import urllib2

file = open("files/blockedservers", "w")

for line in urllib2.urlopen("https://sessionserver.mojang.com/blockedservers"):
	found = False
	for dict_line in open("files/dictionary.txt", "r"):
		if line.strip() in dict_line.strip():
			file.write(dict_line.strip() + "\n")
			found = True

	if not found:
		file.write(line.strip() + "\n")
