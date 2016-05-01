import os
import urllib2

dictionary = open("support/dictionary", "r")
lines = map(lambda l: l.strip(), list(dictionary.read().splitlines()))

with open("blockedservers", "w+") as file:

    for line in urllib2.urlopen("https://sessionserver.mojang.com/blockedservers"):
        line = line.strip()
        found = False
        for dict_line in lines:
            if line in dict_line:
                file.write(dict_line + "\n")
                found = True

        if not found:
            file.write(line + "\n")
