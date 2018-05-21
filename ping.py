import os
import subprocess
import re
import tkinter as tk
import tkinter.filedialog
# import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    "24.105.62.129",
    "sgp-1.valve.net"
]

class Application(tk.Frame):
    def quit_app(event=None):
        root.quit()

    

    def __init__(self, master=None):
        super().__init__(master)
        root.title("Ping Game")
        self.pack()
        self.create_widgets()
        # self.create_widgetss()
    def create_widgets(self):
     
        menubar                     = tk.Menu(self)
        file_menu                   = tk.Menu(root,tearoff=0)
        file_menu.add_command(label ="New")
        file_menu.add_command(label ="Open" ,command=self.onOpen)
        file_menu.add_command(label ="Exit" ,command=self.quit_app)
        menubar.add_cascade(label   ="File", menu=file_menu)
        toolbar                     = tk.Frame(root, bd=1, relief=tk.RAISED)

        root.config(menu=menubar)

    def onOpen(self):

     
        dlg = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes =[ ("All files","*.*")])
        
        print(dlg)
        self.readFile(dlg)

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.readlines()
        pool = ThreadPool(2)
        results = pool.map(self.pingServer, text)
        print(results)

        pool.close() 
        pool.join()

    def pingServer(self,item):
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


    # pingServer(content_1)



    # def create_widgetss(self):
    #     self.hi_there = tk.Button(self)
    #     self.hi_there["text"] = "Hello World\n(click me)"
    #     self.hi_there.pack(side="top")

    #     self.quit = tk.Button(self, text="QUIT", fg="red",
    #                           command=root.destroy)
    #     self.quit.pack(side="bottom")
   
        # self.createWidgets()

root = tk.Tk()
app = Application(master=root)
root.geometry("600x550")

root.mainloop()

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