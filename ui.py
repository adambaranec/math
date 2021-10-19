from tkinter import *
import texts as tx

#declaration of all UI elements of this app
okno = Tk()
okno.geometry('500x500')
okno.eval('tk::PlaceWindow . center')
okno.title="Matika"""
choose = Label(text=tx.chooseshape)
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
obsah = Button(text=tx.area, padx=50, pady=10)
obvod = Button(text=tx.perimeter, padx=50, pady=10)
vysledok = Button(text=tx.result, padx=50, pady=10)
realna_dlzka = Button(text=tx.reallength, padx=50, pady=10)
l1 = Label(text=tx.sidelength)
l2 = Label(text="a:")
l3 = Label(text="b:")
l4 = Label(text=tx.radiuscircle)
shape = IntVar()
isdark = IntVar()
stvorec = Radiobutton(okno, text=tx.square, variable=shape, value=1)
obdlznik = Radiobutton(okno, text=tx.rect, variable=shape, value=2)
kruh = Radiobutton(okno, text=tx.circle, variable=shape, value=3)
pyveta = Radiobutton(okno, text=tx.pytheorem, variable=shape, value=4)
mode = Checkbutton(okno, text=tx.darkmode, variable=isdark, onvalue=1, offvalue=0)
lang = Menu(okno)

def toslovak():
 choose.config(text=tx.chooseshape_sk)
 obsah.config(text=tx.area_sk)
 obvod.config(text=tx.perimeter_sk)
 vysledok.config(text=tx.result_sk)
 realna_dlzka.config(text=tx.reallength_sk)
 stvorec.config(text=tx.square_sk)
 obdlznik.config(text=tx.rect_sk)
 kruh.config(text=tx.circle_sk)
 pyveta.config(text=tx.pytheorem_sk)
 l1.config(text=tx.sidelength_sk)
 l4.config(text=tx.radiuscircle_sk)
 l_obsahstvorca.config(text=tx.writesqarea_sk)
 l_obsahobdlznika.config(text=tx.writerectarea_sk)
 l_obsahkruhu.config(text=tx.writecirclea_sk)
 l_vysledokvety.config(text=tx.writepytres_sk)
 l_obvodstvorca.config(text=tx.writesqper_sk)
 l_obvodobdlznika.config(text=tx.writerectper_sk)
 l_obvodkruhu.config(text=tx.writecirclep_sk)
 l_dlzkaodvesny.config(text=tx.writepytlen_sk)
 
def toenglish():
 choose.config(text=tx.chooseshape)
 obsah.config(text=tx.area)
 obvod.config(text=tx.perimeter)
 vysledok.config(text=tx.result)
 realna_dlzka.config(text=tx.reallength)
 stvorec.config(text=tx.square)
 obdlznik.config(text=tx.rect)
 kruh.config(text=tx.circle)
 pyveta.config(text=tx.pytheorem)
 l1.config(text=tx.sidelength)
 l4.config(text=tx.radiuscircle)
 l_obsahstvorca.config(text=tx.writesqarea)
 l_obsahobdlznika.config(text=tx.writerectarea)
 l_obsahkruhu.config(text=tx.writecirclea)
 l_vysledokvety.config(text=tx.writepytres)
 l_obvodstvorca.config(text=tx.writesqper)
 l_obvodobdlznika.config(text=tx.writerectper)
 l_obvodkruhu.config(text=tx.writecirclep)
 l_dlzkaodvesny.config(text=tx.writepytlen)

