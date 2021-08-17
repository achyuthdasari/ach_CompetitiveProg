# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	sett=set()
	strin=""
	for i in text:
		if i not in sett:
			strin+=i
		sett.add(i)
	return strin


