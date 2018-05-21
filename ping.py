import os
import subprocess
import re

import tkinter as tk
import tkinter.filedialog

from multiprocessing.dummy import Pool as ThreadPool

class Application(tk.Frame):
    def quit_app(event=None):
        root.quit()

    def __init__(self, master=None):
        super().__init__(master)
        root.title("Ping Game")
        self.pack()
        self.create_widgets()

        main = Main()
        main.start()

    def create_widgets(self):
        menubar   = tk.Menu(self)
        file_menu = tk.Menu(root,tearoff=0)

        file_menu.add_command(label="New")
        file_menu.add_command(label="Open", command=self.onOpen)
        file_menu.add_command(label="Exit", command=self.quit_app)

        menubar.add_cascade(label="File", menu=file_menu)

        toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)

        root.config(menu=menubar)

    def onOpen(self):
        dlg = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =[ ("All files","*.*")])
        
        print(dlg)
        self.readFile(dlg)

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
        print(item + " " + str(matches))

    def start(self):
        pool    = ThreadPool(self.NUM_THREADS)
        results = pool.map(self.pingServers, self.urls)

        pool.close() 
        pool.join()

    def parseFile(self, filename):
        file = open(filename, "r")
        return list(filter(None, (line.rstrip() for line in file)))

#################### START ####################
root = tk.Tk()
app = Application(master=root)
root.geometry("600x550")

root.mainloop()