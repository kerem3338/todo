import os
import sys
import json

_config={
	"author": "Zoda",
	"version": "1.0",
	"repo": "https://github.com/kerem3338/todo"
}
try:
	f=open("note.json","r+",encoding="utf8")
	fjson=json.load(f)
except FileNotFoundError:
	if os.name == "nt":
		os.system(f"nul>{os.getcwd()}\\note.json")
	else:
		os.system("touch note.json")
	

try:
	if sys.argv[1] == "list":
		for i in  range(len(list(fjson.keys()))):
			print(list(fjson.keys())[i])

	elif sys.argv[1] == "new":
		title=sys.argv[2]
		content=sys.argv[3]

		f.seek(0)
		f.truncate()
		fjson[title]=content
		json.dump(fjson,f)
	elif sys.argv[1] == "get":
		if sys.argv[2] in fjson:
			print(fjson[sys.argv[2]])
		else:
			print(f"Note '{sys.argv[2]}' Not Found")

	elif sys.argv[1] == "del":
		if sys.argv[2] in fjson:
			del fjson[sys.argv[2]]
			f.seek(0)
			f.truncate()
			json.dump(fjson,f)
		else:
			print(f"Note '{sys.argv[2]}' Not Found")

	elif sys.argv[1] == "about" or sys.argv[1] == "info":
		print(f"""Zoda Todo
Version: {_config["version"]}
Repo: {_config["repo"]}
Author: {_config["author"]}

Todo app in your terminal!""")
	elif sys.argv[1] == "help" or sys.argv[1] == "-h":
		print("""
Commands
list - lists all notes
del <note> - deletes the note
new <note title> <note> - adds a note
get <note title> - shows the grade
about/info - About This App
help/-h - This Message
""")
except IndexError:
	print(f"Please use {__file__} -h")
