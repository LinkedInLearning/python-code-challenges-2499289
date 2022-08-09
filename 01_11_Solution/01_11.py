import time

from tkinter import *

# Objekt der Klasse Tk erstellt und Fensterüberschrift

fenster = Tk()

fenster.wm_title("Uhrzeit")

# Uhrzeit wird über ein Label angezeigt und mit pack im fenster gezeigt

uhr = Label(master=fenster,

            font=('Arial', 30),

            fg='blue',

            width=15)

uhr.pack()

zeit = ''

# Abfrage der Zeit vom laufenden Computer

# mit config wird das Label neu beschriftet

# mit after wird nach 0,2sek die Funktion tick neu aufgerufen


def tick():

    global zeit

    neuezeit = time.strftime('%H:%M:%S')

    if neuezeit != zeit:

        zeit = neuezeit

        uhr.config(text=zeit)

    uhr.after(1000, tick)


tick()

uhr.mainloop()  # Programm startet
