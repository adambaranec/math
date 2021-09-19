import math
from tkinter import *
from tkinter import messagebox
import tkinter

okno = Tk()
okno.geometry('500x500')
okno.eval('tk::PlaceWindow . center')
okno.title="Matika"
Label(text="Vyber tvar:").pack()
strana1 = StringVar()
strana2 = StringVar()
dlzka = Entry(okno, textvariable=strana1)
a = Entry(okno, textvariable=strana1)
b = Entry(okno, textvariable=strana2)
r = Entry(okno, textvariable=strana1)

i = IntVar()
i.set(1)

def prvy(): 
    if i.get() == 1:
       if strana1 != None: 
         try: 
          getside = dlzka.get()
          side = int(getside)
          obsah = side * side
          zapis = str(obsah)
          Label(okno, text="Obsah štvorca je " + zapis + ".").pack()
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 2:
        if strana1 and strana2 != None: 
         try:   
          geta = a.get()
          getb = b.get()
          sidea = int(geta)
          sideb = int(getb)
          obsah = sidea * sideb
          zapis = str(obsah)
          Label(okno, text="Obsah obdĺžnika je " + zapis + ".").pack()
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 3:
        if strana1 != None:
          try:     
           getr = r.get()
           radius = int(getr)
           obsah = math.pi * radius*radius
           zapis = str(obsah)
           Label(okno, text="Obsah kruhu je " + zapis + ".").pack()
          except ValueError:
           messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 4:
        if strana1 and strana2 != None:
          try:   
           geta = a.get()
           getb = b.get()
           sidea = int(geta)
           sideb = int(getb)
           vysledok = sidea*sidea + sideb*sideb
           zapis = str(vysledok)
           Label(okno, text="Výsledok vety je " + zapis + ".").pack()
          except ValueError:
           messagebox.showerror("Pozor", "Akceptujeme len čísla.")


def druhy():
    if i.get() == 1:
       if strana1 != None: 
        try:  
          getside = dlzka.get()
          side = int(getside)
          obvod = side * 4
          zapis = str(obvod)
          Label(okno, text="Obvod štvorca je " + zapis + ".").pack()
        except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 2:
        if strana1 and strana2 != None: 
         try: 
          geta = a.get()
          getb = b.get()
          sidea = int(geta)
          sideb = int(getb)
          obvod = 2 * (sidea + sideb)
          zapis = str(obvod)
          Label(okno, text="Obvod obdĺžnika je " + zapis + ".").pack()
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 3:
        if strana1 != None:
         try:
          getr = r.get()
          radius = int(getr)
          obvod = 2 * math.pi * radius
          zapis = str(obvod)
          Label(okno, text="Obvod kruhu je " + zapis + ".").pack()
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 4:
        if strana1 and strana2 != None:
         try:     
          geta = a.get()
          getb = b.get()
          sidea = int(geta)
          sideb = int(getb)
          vypocet = sidea*sidea + sideb*sideb
          vysledok = math.sqrt(vypocet)
          zapis = str(vysledok)
          Label(okno, text="Dĺžka odvesny je " + zapis + ".").pack()
         except ValueError:               
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")

obsah = Button(text="Obsah", padx=50, pady=10, command=prvy)
obvod = Button(text="Obvod", padx=50, pady=10, command=druhy)
vysledok = Button(text="Výsledok", padx=50, pady=10, command=prvy)
realna_dlzka = Button(text="Reálna dĺžka", padx=50, pady=10, command=druhy)

def prepare():
    if i.get() == 1:
       Label(text="Dĺžka strany:").pack()
       dlzka.pack()
       obsah.pack()
       obvod.pack()
    if i.get() == 2:
       Label(text="a:").pack()
       a.pack()
       Label(text="b:").pack()
       b.pack()
       obsah.pack()
       obvod.pack()
    if i.get() == 3:
       Label(text="Polomer:").pack()
       r.pack()
       obsah.pack()
       obvod.pack()
    if i.get() == 4:
       Label(text="a:").pack()
       a.pack()
       Label(text="b:").pack()
       b.pack()
       vysledok.pack()
       realna_dlzka.pack()

Radiobutton(okno, text="Štvorec", variable=i, value=1, command=prepare).pack()
Radiobutton(okno, text="Obdĺžnik", variable=i, value=2, command=prepare).pack()
Radiobutton(okno, text="Kruh", variable=i, value=3, command=prepare).pack()
Radiobutton(okno, text="Pytagorova veta", variable=i, value=4, command=prepare).pack()

okno.mainloop()