import os
import subprocess
import re
import tkinter as tk
import tkinter.filedialog
from tkinter import StringVar
from tkinter import *

from multiprocessing.dummy import Pool as ThreadPool

root = tk.Tk()
serversList= tk.StringVar()

class Application(tk.Frame):

    def quit_app(event=None):
        root.quit()

    def __init__(self, master=None):
        super().__init__(master)
        root.title("Ping Game")   
        self.pack()
        self.create_widgets()
        self.pingButton()

        root.minsize(width=50,height=50)
    def create_widgets(self):

        menubar   = tk.Menu(self)
        file_menu = tk.Menu(root,tearoff=0)

        file_menu.add_command(label="Add",command=self.popAdd)
        file_menu.add_command(label="Delete")
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menubar)

    def pingButton(self):

        pingButton = tk.Button(self,text="Ping",width=10,command=self.printPing)
        pingButton.pack(side="bottom")


    def printPing(self):
        serverList= []
        main          = Main()
        serverList    = main.start()
        text          = tk.Text(root)
       
        # i=0
        empty=''
        serverDisplay['text'] = empty
        # serverDisplay.delete(1.0,tk.END)
        servers = ''
        for items in serverList:
            servers += str(items)+'\n'
            print(items)
        serversList.set(servers)

        # print(serverList)

    def popAdd(self):
        # f = tk.Frame(None, height=300, width=300)
        toplevel = tk.Toplevel()
        # frame = tk.Frame(toplevel)
        toplevel.maxsize(width=300, height=300)
        toplevel.minsize(width=300, height=300)
        toplevel.title("Add Server")
        label1 = tk.Label(toplevel, text="Add Server")
        e1 = tk.Entry(toplevel, bd =5)
        
        
        def addServer():
             file = open("games.txt", "a")
             file.write("\n"+e1.get())
             file.close()
             
        
        button = tk.Button(toplevel, text="Add", command=addServer)
        label1.pack()
        e1.pack()
        button.pack()
 
class Main:
    # consts
    NUM_THREADS  = 2
    NUM_REQUESTS = 5

    def __init__(self, master=None):
        self.urls = self.parseFile("games.txt")

    def pingServers(self, item):
        
        serverAdd    = "ping -n " + str(self.NUM_REQUESTS) + " " + item
        output       = subprocess.check_output(serverAdd, shell=True)
        decoded      = output.decode('utf-8')
        matches      = re.findall("Average = ([\\d.]+)ms",decoded)
        pingAdd = item + " " + str(matches)
   
        print(pingAdd)
        return pingAdd


    def start(self):
        pool    = ThreadPool(self.NUM_THREADS)
        results=pool.map(self.pingServers, self.urls)
        # returnVal=pingServers.get()
        pool.close() 
        pool.join()
        print(len(results))
        return results

    def parseFile(self, filename):
        file = open(filename, "r")
        return list(filter(None, (line.rstrip() for line in file)))
        file.close()

#################### START ####################

app = Application(master=root)
serverDisplay = tk.Label(root,textvariable=serversList)
serverDisplay.pack()
root.maxsize(300,300)
root.minsize(300,300)
root.mainloop()