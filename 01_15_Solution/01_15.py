from tkinter import *
from tkinter import filedialog

from tkinter import messagebox
import hashlib
import os.path
'''
Überprüfung, ob sich ein Inhalt geändert hat
'''
def getSignatur(inhalt):
    return hashlib.sha224(inhalt.encode("UTF-8")).hexdigest()
'''
Ein neues Dokument anlegen
'''
def newFile():
    global dat
    global signatur
    inhalt = textfeld1.get(1.0, END)
    if signatur != getSignatur(inhalt):
        if messagebox.askokcancel('Achtung Änderungen','Es gibt nicht gespeicherte Änderungen.\nDatei dennoch neu?')==False:
            return
    dat=""
    root.title("Editor - no file")
    textfeld1.delete(1.0,END)
    signatur = getSignatur(textfeld1.get(1.0, END))
'''
Datei öffnen
'''    
def openFile():
    global dat
    global signatur
    inhalt = textfeld1.get(1.0, END)
    if signatur != getSignatur(inhalt):
        if messagebox.askokcancel('Achtung Änderungen','Es gibt nicht gespeicherte Änderungen.\nDatei dennoch neu öffnen?')==False:
            return
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
        signatur = getSignatur(textfeld1.get(1.0, END))
    except IOError:
        messagebox.showerror('Fehler',"Fehler beim Zugriff auf die Datei")
'''
Vorhandene Datei speichern
'''
def saveFile():
    global dat
    global signatur
    if os.path.exists(dat):
        try:
            fp = open(dat,"w",encoding='utf8')
            inhalt = textfeld1.get(1.0, END)
            fp.write(inhalt)
            fp.close()
            signatur = getSignatur(textfeld1.get(1.0, END))
        except IOError:
            messagebox.showerror('Achtung Fehler',"Fehler beim Zugriff auf die Datei")
    else:
        saveAsFile()
'''
Neues Dokument speichern
'''
def saveAsFile():
    global dat
    global signatur
    dat = filedialog.asksaveasfilename(initialdir = "/",title = "Dateiauswahl",filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*")))
    if dat=="":
        return
    try:
        fp = open(dat,"w",encoding='utf8')
        inhalt = textfeld1.get(1.0, END)
        fp.write(inhalt)
        fp.close()
        signatur = getSignatur(textfeld1.get(1.0, END))
        root.title("RJS-Editor - " + dat)
    except IOError:
        messagebox.showerror('Achtung Fehler',"Fehler beim Zugriff auf die Datei")

'''
Kleine Info zum Programm
'''
def about():
    messagebox.showinfo('About',"Ein kleiner Texteditor")
'''
Programm beenden
'''    
def ende():
    if messagebox.askokcancel('Ende','Programm beenden?')==False:
        return
    inhalt = textfeld1.get(1.0, END)
    global signatur
    
    if signatur != getSignatur(inhalt):
        if messagebox.askokcancel('Achtung Änderungen','Es gibt nicht gespeicherte Änderungen.\nProgramm dennoch beenden?')==False:
            return
    root.destroy()

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

signatur = getSignatur(textfeld1.get(1.0, END)) # Anfangssignatur bestimmen

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Datei", menu=filemenu)
filemenu.add_command(label="Neu", command=newFile)
filemenu.add_command(label="Öffnen...", command=openFile)
filemenu.add_command(label="Speichern", command=saveFile)
filemenu.add_command(label="Speichern unter...", command=saveAsFile)

filemenu.add_separator()
filemenu.add_command(label="Beenden", command=ende)

helpmenu = Menu(menu)
menu.add_cascade(label="?", menu=helpmenu)
helpmenu.add_command(label="Info...", command=about)

mainloop()
