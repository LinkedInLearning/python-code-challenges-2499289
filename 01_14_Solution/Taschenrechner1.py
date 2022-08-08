from tkinter import *
import tkinter.font as tkFont

# Feld mit der Anzeige leeren
def leere():
    feld.configure(state=NORMAL)
    feld.delete(0,"end")
    feld.configure(state=DISABLED)

# Letztes Zeichen in dem Anzeigefeld wegnehmen
def back():
    pos = len(feld.get())
    feld.configure(state=NORMAL)
    feld.delete(pos-1,pos)
    feld.configure(state=DISABLED)
# Zahl oder Operator in das Anzeigefeld setzen    
def setze(x):
    pos = len(feld.get())
    feld.configure(state=NORMAL)
    feld.insert(pos,str(x))  
    feld.configure(state=DISABLED)
# Ausdruck in dem Anzeigefeld berechnen und dort das Ergebnis anzeigen    
def berechne():
    erg = eval(feld.get())
    feld.configure(state=NORMAL)
    feld.delete(0,"end")
    feld.insert(0,str(erg))  
    feld.configure(state=DISABLED)

root = Tk()
root.title("Taschenrechner")
ft1 = tkFont.Font(family='Times',size=16)
# Anzeigefeld - auf die Breite von 4 Spalten verteilt
feld = Entry(root,width=25, state=DISABLED, font=ft1)
feld.grid (column=0, row=0, columnspan="4")

# Die Button des Taschenrechners in Zellen eines Grids
Button(root,text='<-',width=7,height=2,command=back,bg="gray").grid(row=1, column=0) 
Button(root,text='%',width=7,height=2,bg="gray",command=lambda : setze('%')).grid(row=1, column=1) 
Button(root,text='**',width=7,height=2,bg="gray",command=lambda : setze('**')).grid(row=1, column=2) 
Button(root,text='/',width=7,height=2,bg="gray",command=lambda : setze('/')).grid(row=1, column=3) 

Button(root,text='7',width=7,height=2,command=lambda : setze(7)).grid(row=2, column=0) 
Button(root,text='8',width=7,height=2,command=lambda : setze(8)).grid(row=2, column=1) 
Button(root,text='9',width=7,height=2,command=lambda : setze(9)).grid(row=2, column=2) 
Button(root,text='x',width=7,height=2,bg="gray",command=lambda : setze('*')).grid(row=2, column=3) 

Button(root,text='4',width=7,height=2,command=lambda : setze(4)).grid(row=3, column=0) 
Button(root,text='5',width=7,height=2,command=lambda : setze(5)).grid(row=3, column=1) 
Button(root,text='6',width=7,height=2,command=lambda : setze(6)).grid(row=3, column=2) 
Button(root,text='-',width=7,height=2,bg="gray",command=lambda : setze('-')).grid(row=3, column=3) 

Button(root,text='1',width=7,height=2,command=lambda : setze(1)).grid(row=4, column=0) 
Button(root,text='2',width=7,height=2,command=lambda : setze(2)).grid(row=4, column=1) 
Button(root,text='3',width=7,height=2,command=lambda : setze(3)).grid(row=4, column=2) 
Button(root,text='+',width=7,height=2,bg="gray",command=lambda : setze('+')).grid(row=4, column=3) 

Button(root,text='C',width=7,height=2,command=leere,bg="gray").grid(row=5, column=0) 
Button(root,text='0',width=7,height=2,command=lambda : setze(0)).grid(row=5, column=1) 
Button(root,text=',',width=7,height=2,bg="gray",command=lambda : setze(".")).grid(row=5, column=2) 
Button(root,text='=',width=7,height=2,bg="blue",command=lambda : berechne()).grid(row=5, column=3) 

root.mainloop()