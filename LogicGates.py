from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Logic Gates Program")
window.geometry("350x250")

finalVal = Label(window, text="", font="Helvetica 32")
finalVal.grid(column=0, row=0, columnspan=3)

def runGate():
    gate = chosen.get()
    tf = ""
    i1 = True if inputOne.get() == 'True' else False
    i2 = True if inputTwo.get() == 'True' else False
    if gate == 1:
        tf = orGate(i1, i2)
    elif gate == 2:
        tf = andGate(i1, i2)
    elif gate == 3:
        tf = xorGate(i1, i2)
    elif gate == 4:
        tf = nandGate(i1, i2)
    elif gate == 5:
        tf = norGate(i1, i2)

    finalVal.configure(text=str(bool(tf)))
    finalVal.update()
    window.update()

def orGate(val1, val2):
    print (val1, val2)
    if val1 or val2:
        return True
    else:
        return False


def andGate(val1, val2):
    if val1 and val2:
        return True
    else:
        return False


def xorGate(val1, val2):
    if val1 and not val2:
        return True
    elif val2 and not val1:
        return True
    else:
        return False


def nandGate(val1, val2):
    if not val1 and not val2:
        return True
    else:
        return False


def norGate(val1, val2):
    if val1 or val2:
        return False
    else:
        return True



chosen = IntVar()
OR = Radiobutton(window, text="OR", value=1, variable=chosen)
AND = Radiobutton(window, text="AND", value=2, variable=chosen)
XOR = Radiobutton(window, text="XOR", value=3, variable=chosen)
NAND = Radiobutton(window, text='NAND', value=4, variable=chosen)
NOR = Radiobutton(window, text="NOR", value=5, variable=chosen)

OR.grid(column=0, row=1, sticky=W, pady=2, padx=4)
AND.grid(column=1, row=1, sticky=W, pady=2, padx=4)
XOR.grid(column=0, row=2, sticky=W, pady=2, padx=4)
NAND.grid(column=1, row=2, sticky=W, pady=2, padx=4)
NOR.grid(column=0, row=3, sticky=W, pady=2, padx=4)

inputOneLabel = Label(window, text="Input A")
inputOneLabel.grid(column=0, row=4, sticky=W, pady=2)

inputOne = Combobox(window)
inputOne['values'] = (True, False)
inputOne.current(0)
inputOne.grid(column=1, row=4, sticky=W, pady=2)

inputTwoLabel = Label(window, text="Input B")
inputTwoLabel.grid(column=0, row=5, sticky=W)

inputTwo = Combobox(window)
inputTwo['values'] = (True, False)
inputTwo.current(0)
inputTwo.grid(column=1, row=5, sticky=W)

run = Button(window, text="Run", command=runGate)
run.grid(column=0, row=6, columnspan=2)

window.mainloop()
