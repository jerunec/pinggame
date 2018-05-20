import os
import subprocess
import re
# import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
	"24.105.62.129",
	"sgp-1.valve.net"
]


def pingServer(item):
	# for item in games:
	print("ping -n 5 "+ item)
	serverAdd    = "ping -n 5 "+ item  # the shell command
	output       = subprocess.check_output(serverAdd, shell=True)
	decoded      = output.decode('utf-8')
	matches      = re.findall("Average = ([\\d.]+)ms",decoded)
	print(item + " " + str(matches))

filename1 = "games.txt"
file1 = open(filename1, "r")
content_1 = []

with open(filename1) as f:
    content_1.append(f.readlines())
    # pingServer(content_1)

pool = ThreadPool(2)
results = pool.map(pingServer, urls)
print(results)

pool.close() 
pool.join()


#     import urllib2 
# from multiprocessing.dummy import Pool as ThreadPool 

# urls = [
#   'http://www.python.org', 
#   'http://www.python.org/about/',
#   'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
#   'http://www.python.org/doc/',
#   'http://www.python.org/download/',
#   'http://www.python.org/getit/',
#   'http://www.python.org/community/',
#   'https://wiki.python.org/moin/',
# ]

# # make the Pool of workers
# pool = ThreadPool(4) 

# # open the urls in their own threads
# # and return the results
# results = pool.map(urllib2.urlopen, urls)

# # close the pool and wait for the work to finish 
# pool.close() 
# pool.join()