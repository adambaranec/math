import ui, math
def prvy(): 
    if ui.shape.get() == 1:
         try: 
          getside = ui.dlzka.get()
          side = float(getside)
          obsah = side * side
          zapis = str(obsah)
          stav = f"Obsah štvorca je {zapis}."
          ui.l_obsahstvorca.pack_forget()
          ui.l_obsahstvorca.pack()
          ui.l_obsahstvorca.config(text=stav)
         except ValueError:
          ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if ui.shape.get() == 2:
         try:   
          geta = ui.a.get()
          getb = ui.b.get()
          sidea = float(geta)
          sideb = float(getb)
          obsah = sidea * sideb
          zapis = str(obsah)
          stav = f"Obsah obdĺžnika je {zapis}."
          ui.l_obsahobdlznika.pack_forget()
          ui.l_obsahobdlznika.pack()
          ui.l_obsahobdlznika.config(text=stav)
         except ValueError:
          ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if ui.shape.get() == 3:
          try:     
           getr = ui.r.get()
           radius = float(getr)
           obsah = math.pi * radius*radius
           zapis = str(obsah)
           stav = f"Obsah kruhu je {zapis}."
           ui.l_obsahkruhu.pack_forget()
           ui.l_obsahkruhu.pack()
           ui.l_obsahkruhu.config(text=stav)
          except ValueError:
           ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if ui.shape.get() == 4:
          try:   
           geta = ui.a.get()
           getb = ui.b.get()
           sidea = float(geta)
           sideb = float(getb)
           vysledok = sidea*sidea + sideb*sideb
           zapis = str(vysledok)
           stav = f"Výsledok vety je {zapis}."
           ui.l_vysledokvety.pack_forget()
           ui.l_vysledokvety.pack()
           ui.l_vysledokvety.config(text=stav)
          except ValueError:
           ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")

def druhy():
    if ui.shape.get() == 1:
        try:  
          getside = ui.dlzka.get()
          side = float(getside)
          obvod = side * 4
          zapis = str(obvod)
          stav = f"Obvod štvorca je {zapis}."
          ui.l_obvodstvorca.pack_forget()
          ui.l_obvodstvorca.pack()
          ui.l_obvodstvorca.config(text=stav)
        except ValueError:
          ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if ui.shape.get() == 2:
         try: 
          geta = ui.a.get()
          getb = ui.b.get()
          sidea = int(geta)
          sideb = int(getb)
          obvod = 2 * (sidea + sideb)
          zapis = str(obvod)
          stav = f"Obvod obdĺžnika je {zapis}."
          ui.l_obvodobdlznika.pack_forget()
          ui.l_obvodobdlznika.pack()
          ui.l_obvodobdlznika.config(text=stav)
         except ValueError:
          ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if ui.shape.get() == 3:
         try:
          getr = ui.r.get()
          radius = int(getr)
          obvod = 2 * math.pi * radius
          zapis = str(obvod)
          stav = f"Obvod kruhu je {zapis}."
          ui.l_obvodkruhu.pack_forget()
          ui.l_obvodkruhu.pack()
          ui.l_obvodkruhu.config(text=stav)
         except ValueError:
          ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")
    if ui.shape.get() == 4:
         try:     
          geta = ui.a.get()
          getb = ui.b.get()
          sidea = int(geta)
          sideb = int(getb)
          vypocet = sidea*sidea + sideb*sideb
          vysledok = math.sqrt(vypocet)
          zapis = str(vysledok)
          stav = f"Dĺžka odvesny je {zapis}."
          ui.l_dlzkaodvesny.pack_forget()
          ui.l_dlzkaodvesny.pack()
          ui.l_dlzkaodvesny.config(text=stav)
         except ValueError:               
          ui.messagebox.showerror("Pozor", "Akceptujeme len čísla.")

ui.obsah.config(command=prvy)
ui.obvod.config(command=druhy)
ui.vysledok.config(command=prvy)
ui.realna_dlzka.config(command=druhy)