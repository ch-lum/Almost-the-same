# Almost the same Readme

Fri Sep 2 10:57:00 2022
By Christopher Lum (cslum@ucsd.edu)

Two words are *almost the same* if they contain all but one letter in common, in the same order. IE *read* and *lead* are almost the same because they have three letters together.

This project focuses on networks of *n*-letter words (primarily four), creating edges when two words are almost the same.

graphs and gephi/ contains .graphml files of networks and .gephi files for visualization

words dataset/ contains a .txt dictionary from SCOWL (http://wordlist.aspell.net/) and a program to convert SCOWL .txts to .json because for some reason I decided to import the word lists as .json

makegraph creates a .graphml file for words of a given length

shortestpath takes a .graphml file and a source and target word to find the shortest path for two specific words

Word_to_word is a terrible piece of code I used before learning what graphs were and should never be used because it is so terrible. Honestly embarassing that it exists but I keep it up as a vestige of a pre-graph era.