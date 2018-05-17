import socket
import sys
import os

serverAdd = input('input server')

rep = os.system('ping ' + serverAdd + ' -t')

if rep == 0:
	print('server is up')
else:
	print('server is down')

