from tkinter import Tk, Label, IntVar
from tkinter.ttk import Radiobutton, W, Combobox, Button

window = Tk()

window.title("Logic Gates Program")
window.geometry("350x250")

finalVal = Label(window, text="", font="Helvetica 32")
finalVal.grid(column=0, row=0, columnspan=3)


def runGate():
    gate = chosen.get()
    tf = ""
    a = inputOne.get() == 'True'
    b = inputTwo.get() == 'True'
    if gate == 1:
        tf = a or b
    elif gate == 2:
        tf = a and b
    elif gate == 3:
        tf = a and not b or b and not a
    elif gate == 4:
        tf = not a and not b
    elif gate == 5:
        tf = not a or b

    finalVal.configure(text=str(bool(tf)))
    finalVal.update()
    window.update()


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
