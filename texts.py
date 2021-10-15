from tkinter import StringVar
import ui, count
from translate import Translator
'''declaration of all words used there (default in english,
they will be translated to other languages)'''
#name of the app
appname = "Matika"
#text of the first label
chooseshape = "Choose a shape"
#texts of the radiobuttons
square = "square"
rect = "rectangle"
circle = "circle"
pytheorem = "Pythagoras Theorem"
#texts of buttons
area = "area"
perimeter = "perimeter"
result = "result"
reallength = "real length"
#to tell the result
writesqarea = "Area of the square is"
writesqper = "Perimeter of the square is"
writerectarea = "Area of the rectangle is"
writerectper = "Perimeter of the rectangle is"
writecircler = "Area of the circle is"
writecirclep = "Perimeter of the circle is"
writepytres = "Result of the theorem is"
writepytlen = "Length of the side c is"
#the dialog box
attention = "Attention"
accept = "We accept only numbers"
#the one checkbutton
darkmode = "Dark mode"
#and finally the labels...
sidelength = "length of the side"
radiuscircle = "radius"

slovak = Translator('sk')
chooseshape_sk = slovak.translate(chooseshape)
square_sk = slovak.translate(square)
rect_sk= slovak.translate(rect)
circle_sk= slovak.translate(circle)
pytheorem_sk= slovak.translate(pytheorem)
area_sk= slovak.translate(area)
perimeter_sk= slovak.translate(perimeter)
result_sk= slovak.translate(result)
reallength_sk= slovak.translate(reallength)
attention_sk= slovak.translate(attention)
accept_sk= slovak.translate(accept)
darkmode_sk= slovak.translate(darkmode)
sidelength_sk= slovak.translate(sidelength)
radiuscircle_sk= slovak.translate(radiuscircle)
writesqarea_sk = slovak.translate(writesqarea)
writesqper_sk = slovak.translate(writesqper)
writerectarea_sk = slovak.translate(writerectarea)
writerectper_sk = slovak.translate(writerectper)
writecircler = slovak.translate(writecircler)
writecirclep = slovak.translate(writecirclep)
writepytres_sk = slovak.translate(writepytres)
writepytlen_sk = slovak.translate(writepytlen)

def toslovak():
 ui.choose.config(text=chooseshape_sk)
 ui.obsah.config(text=area_sk)
 ui.obvod.config(text=perimeter_sk)
 ui.vysledok.config(text=result_sk)
 ui.realna_dlzka.config(text=reallength_sk)
 ui.stvorec.config(text=square_sk)
 ui.obdlznik.config(text=rect_sk)
 ui.kruh.config(circle_sk)
 ui.pyveta.config(pytheorem_sk)
 ui.l1.config(sidelength_sk)
 ui.l4.config(radiuscircle_sk)
 '''ui.l_obsahstvorca.config()
 ui.l_obsahobdlznika.config()
 ui.l_obsahkruhu.config()
 ui.l_vysledokvety.config()
 ui.l_obvodstvorca.config()
 ui.l_obvodobdlznika.config()
 ui.l_obvodkruhu.config()
 ui.l_dlzkaodvesny.config()'''
 
def toenglish():
 ui.choose.config(text=chooseshape)
 ui.obsah.config(text=area)
 ui.obvod.config(text=perimeter)
 ui.vysledok.config(text=result)
 ui.realna_dlzka.config(text=reallength)
 ui.stvorec.config(text=square)
 ui.obdlznik.config(text=rect)
 ui.kruh.config(circle)
 ui.pyveta.config(pytheorem)
 ui.l1.config(sidelength)
 ui.l4.config(radiuscircle)
 '''ui.l_obsahstvorca.config()
 ui.l_obsahobdlznika.config()
 ui.l_obsahkruhu.config()
 ui.l_vysledokvety.config()
 ui.l_obvodstvorca.config()
 ui.l_obvodobdlznika.config()
 ui.l_obvodkruhu.config()
 ui.l_dlzkaodvesny.config()'''
