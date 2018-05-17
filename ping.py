import os
import subprocess
import re


def pingServer(games):
	for item in games:
		serverAdd = "ping -n 5 "+ item  # the shell command
		output = subprocess.check_output(serverAdd, shell=True)
		decoded = output.decode('utf-8')
		matches = re.findall("Average = ([\\d.]+)ms",decoded)
		print(item+" "+str(matches))

filename1 = "games.txt"
file1 = open(filename1, "r")

with open(filename1) as f:
    content_1 = f.readlines()
    pingServer(content_1)

