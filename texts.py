import ui
from translate import Translator
'''declaration of all words used there (default in english,
they will be translated to other languages)'''
#name of the app
appname = "Matika"
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
#the dialog box
attention = "attention"
accept = "accept"
#the one checkbutton
darkmode = "Dark mode"
#and finally the labels...
sidelength = "length of the side"
radiuscircle = "radius"

slovak = Translator('sk')
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

def toslovak():
    pass

def toenglish():
    pass
