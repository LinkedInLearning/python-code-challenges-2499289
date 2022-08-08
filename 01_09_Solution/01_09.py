from tkinter import *

class Application(Frame):
   
    def __init__(self,master=None):
        Frame.__init__(self, master)
        Label(master,text="Dezimal").grid(row=0)
        
        Label(master,text="Oktal").grid(row=1)
        Label(master,text="Binär").grid(row=2)
        Label(master,text="Hexadezimal").grid(row=3)
        
        self.d = Entry(master)
        self.d.grid(row=0, column=1)
        self.o = Label(master,text="#")
        self.o.grid(row=1, column=1)
        self.b = Label(master,text="#")
        self.b.grid(row=2, column=1)
        self.h = Label(master,text="#")
        self.h.grid(row=3, column=1)

        Button(master,text='OK',width=20,command=self.action).grid(
            row=4, column=0)
        Button(master,text='Abbrechen',width=20,command=root.destroy).grid(
            row=4, column=1)
        

    def action(self):
        try:
            int(self.d.get())
            d = int(self.d.get())
            print(d, oct(d), hex(d), bin(d))
            self.b.config(text= str(bin(d)))
            self.o.config(text= str(oct(d)))
            self.h.config(text=str(hex(d)))
        except:
            pass
            
        

root=Tk()
app=Application(master=root)
app.mainloop()
















