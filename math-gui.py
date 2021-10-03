import math
from tkinter import *
from tkinter import messagebox
import tkinter

#declaration of all UI components
okno = Tk()
okno.geometry('500x500')
okno.eval('tk::PlaceWindow . center')
okno.title="Matika"
choose = Label(text="Vyber tvar:")
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
obsah = Button(text="Obsah", padx=50, pady=10)
obvod = Button(text="Obvod", padx=50, pady=10)
vysledok = Button(text="Výsledok", padx=50, pady=10)
realna_dlzka = Button(text="Reálna dĺžka", padx=50, pady=10)
l1 = Label(text="Dĺžka strany:")
l2 = Label(text="a:")
l3 = Label(text="b:")
l4 = Label(text="Polomer:")
i = IntVar()
isdark = IntVar()
stvorec = Radiobutton(okno, text="Štvorec", variable=i, value=1)
obdlznik = Radiobutton(okno, text="Obdĺžnik", variable=i, value=2)
kruh = Radiobutton(okno, text="Kruh", variable=i, value=3)
pyveta = Radiobutton(okno, text="Pytagorova veta", variable=i, value=4)
mode = Checkbutton(okno, text="Tmavý režim", variable=isdark, onvalue=1, offvalue=0)
lang = Menu(okno)
#making them visible
mode.pack() #this actually does not do anything, because there are problems with switching foreground
choose.pack()
stvorec.pack()
obdlznik.pack()
kruh.pack()
pyveta.pack()

#and the functions belonging to the buttons, radiobuttons and checkbutton
def prvy(): 
    if i.get() == 1:
         try: 
          getside = dlzka.get()
          side = float(getside)
          obsah = side * side
          zapis = str(obsah)
          stav = "Obsah štvorca je " + zapis + "."
          l_obsahstvorca.pack_forget()
          l_obsahstvorca.pack()
          l_obsahstvorca.config(text=stav)
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 2:
         try:   
          geta = a.get()
          getb = b.get()
          sidea = float(geta)
          sideb = float(getb)
          obsah = sidea * sideb
          zapis = str(obsah)
          stav = "Obsah obdĺžnika je " + zapis + "."
          l_obsahobdlznika.pack_forget()
          l_obsahobdlznika.pack()
          l_obsahobdlznika.config(text=stav)
         except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 3:
          try:     
           getr = r.get()
           radius = float(getr)
           obsah = math.pi * radius*radius
           zapis = str(obsah)
           stav = "Obsah kruhu je " + zapis + "."
           l_obsahkruhu.pack_forget()
           l_obsahkruhu.pack()
           l_obsahkruhu.config(text=stav)
          except ValueError:
           messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 4:
          try:   
           geta = a.get()
           getb = b.get()
           sidea = float(geta)
           sideb = float(getb)
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
        try:  
          getside = dlzka.get()
          side = float(getside)
          obvod = side * 4
          zapis = str(obvod)
          stav = "Obvod štvorca je " + zapis + "."
          l_obvodstvorca.pack_forget()
          l_obvodstvorca.pack()
          l_obvodstvorca.config(text=stav)
        except ValueError:
          messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if i.get() == 2:
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

obsah.config(command=prvy)
obvod.config(command=druhy)
vysledok.config(command=prvy)
realna_dlzka.config(command=druhy)

def hide():
  #this function is only for better understanding what it does
  dlzka.delete(0)
  a.delete(0)
  b.delete(0)
  r.delete(0)
  dlzka.pack_forget()
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

stvorec.config(command=prepare)
obdlznik.config(command=prepare)
kruh.config(command=prepare)
pyveta.config(command=prepare)

okno.mainloop()