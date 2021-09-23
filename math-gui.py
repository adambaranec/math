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
l_obsahstvorca = Label(okno)
l_obsahobdlznika = Label(okno)
l_obsahkruhu = Label(okno)
l_vysledokvety = Label(okno)
l_obvodstvorca = Label(okno)
l_obvodobdlznika = Label(okno)
l_obvodkruhu = Label(okno)
l_dlzkaodvesny = Label(okno)
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
          stav = "Obsah štvorca je " + zapis + "."
          l_obsahstvorca.pack_forget()
          l_obsahstvorca.pack()
          l_obsahstvorca.config(text=stav)
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
          stav = "Obsah obdĺžnika je " + zapis + "."
          l_obsahobdlznika.pack_forget()
          l_obsahobdlznika.pack()
          l_obsahobdlznika.config(text=stav)
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 3:
        if strana1 != None:
          try:     
           getr = r.get()
           radius = int(getr)
           obsah = math.pi * radius*radius
           zapis = str(obsah)
           stav = "Obsah kruhu je " + zapis + "."
           l_obsahkruhu.pack_forget()
           l_obsahkruhu.pack()
           l_obsahkruhu.config(text=stav)
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
           stav = "Výsledok vety je " + zapis + "."
           l_vysledokvety.pack_forget()
           l_vysledokvety.pack()
           l_vysledokvety.config(text=stav)
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
          stav = "Obvod štvorca je " + zapis + "."
          l_obvodstvorca.pack_forget()
          l_obvodstvorca.pack()
          l_obvodstvorca.config(text=stav)
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
          stav = "Obvod obdĺžnika je " + zapis + "."
          l_obvodobdlznika.pack_forget()
          l_obvodobdlznika.pack()
          l_obvodobdlznika.config(text=stav)
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 3:
        if strana1 != None:
         try:
          getr = r.get()
          radius = int(getr)
          obvod = 2 * math.pi * radius
          zapis = str(obvod)
          stav = "Obvod kruhu je " + zapis + "."
          l_obvodkruhu.pack_forget()
          l_obvodkruhu.pack()
          l_obvodkruhu.config(text=stav)
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
          stav = "Dĺžka odvesny je " + zapis + "."
          l_dlzkaodvesny.pack_forget()
          l_dlzkaodvesny.pack()
          l_dlzkaodvesny.config(text=stav)
         except ValueError:               
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")

obsah = Button(text="Obsah", padx=50, pady=10, command=prvy)
obvod = Button(text="Obvod", padx=50, pady=10, command=druhy)
vysledok = Button(text="Výsledok", padx=50, pady=10, command=prvy)
realna_dlzka = Button(text="Reálna dĺžka", padx=50, pady=10, command=druhy)
l1 = Label(text="Dĺžka strany:")
l2 = Label(text="a:")
l3 = Label(text="b:")
l4 = Label(text="Polomer:")

def hide():
  #if someone clicked another radiobutton, the elements should not stay there
  a.pack_forget()
  b.pack_forget()
  r.pack_forget()
  obsah.pack_forget()
  obvod.pack_forget()
  vysledok.pack_forget()
  realna_dlzka.pack_forget()
  l1.pack_forget()
  l2.pack_forget()
  l3.pack_forget()
  l4.pack_forget()
  l_obsahstvorca.pack_forget()
  l_obsahobdlznika.pack_forget()
  l_obsahkruhu.pack_forget()
  l_vysledokvety.pack_forget()
  l_obvodstvorca.pack_forget()
  l_obvodobdlznika.pack_forget()
  l_obvodkruhu.pack_forget()
  l_dlzkaodvesny.pack_forget()

def prepare():
  hide()

  if i.get() == 1:
       l1.pack()
       dlzka.pack()
       obsah.pack()
       obvod.pack()
  if i.get() == 2:
       l2.pack()
       a.pack()
       l3.pack()
       b.pack()
       obsah.pack()
       obvod.pack()
  if i.get() == 3:
       l4.pack()
       r.pack()
       obsah.pack()
       obvod.pack()
  if i.get() == 4:
       l2.pack()
       a.pack()
       l3.pack()
       b.pack()
       vysledok.pack()
       realna_dlzka.pack()

Radiobutton(okno, text="Štvorec", variable=i, value=1, command=prepare).pack()
Radiobutton(okno, text="Obdĺžnik", variable=i, value=2, command=prepare).pack()
Radiobutton(okno, text="Kruh", variable=i, value=3, command=prepare).pack()
Radiobutton(okno, text="Pytagorova veta", variable=i, value=4, command=prepare).pack()

okno.mainloop()
