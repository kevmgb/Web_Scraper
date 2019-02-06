from tkinter import *

'======================================Setup====================================================='
root = Tk()
root.geometry("400x400+0+0")
root.title("Web Scraper for Headlines")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

'====================================The Actual Function=========================================='

def Ref():

    import requests
    r = requests.get("http://www.nation.co.ke")
    rraw = r.text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(rraw, 'html.parser')

    filename = "HeadLinesGUI.txt"

    with open(filename, 'w') as f:
        for x in soup.find_all('p'):
            if x.string != None:
                f.write(x.string)
            else:
                f.write(x.get_text())


'======================================Info========================================================='

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text="Internet Web Scraper", fg="Steel Blue",
                bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

'===================================Only one button=================================================='

btnTotal = Button(f1, padx=16, pady=6, bd=12, fg="black", font=('arial', 14, 'bold'), width=29,
                  text="Get Today's Headlines, Now !", bg="powder blue", command=Ref).grid(row=7, column=1)

'===================================================================================================='

root.mainloop()