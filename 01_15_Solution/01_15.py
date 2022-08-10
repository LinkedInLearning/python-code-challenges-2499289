from tkinter import *
from tkinter import filedialog

from tkinter import messagebox
import os.path
'''
Ein neues Dokument anlegen
'''
'''
Datei öffnen
'''    
def openFile():
    global dat
    inhalt = textfeld1.get(1.0, END)
    dat = filedialog.askopenfilename(initialdir = "/",title = "Dateiauswahl",filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*")))
    if dat=="":
        return
    try:
        fp = open(dat,"r",encoding='utf8')
        inhalt = fp.read()
        fp.close()
        textfeld1.delete(1.0,'end') # Bestehenden Inhalt leeren
        textfeld1.insert(CURRENT,inhalt)
        root.title("RJS-Editor - " + dat)
    except IOError:
        messagebox.showerror('Fehler',"Fehler beim Zugriff auf die Datei")

root = Tk()
root.title("Editor - no file")
root.minsize(width=600, height=400)
dat = "" # Dateiname

textfeld1 = Text(master=root,  wrap='word')
textfeld1.pack(expand=1, fill='both',side=LEFT)
scrollbar1 = Scrollbar(master=root)
scrollbar1.pack(expand=1, fill='both',side=LEFT)
textfeld1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=textfeld1.yview)


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Öffnen...", command=openFile)


mainloop()

