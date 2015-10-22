import os

def run(**args):

	print "[*] In dirlister module."
	files = os.listdir(".")

	# list all the files of a directory
	return str(files)
