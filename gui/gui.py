from tkinter import *


mainWindow = Tk()


# create main widow and configure it
def create_main_windo():
    mainWindow.title("Circuit Analysis ")
    mainWindow.geometry("1300x550+200+200")

def create_solve_button(func):
    # create button and active it
    solveButton = Button(mainWindow, text="solve problem", command=func, font=('vendor', 18, 'bold'), height=1,
                         width=13)
    solveButton.place(x=350, y=450)

# creae entery flied to get input

def createTieSetLabel():
    B = Label(font=('vendor', 18), fg='black')
    B.place(x=50, y=150)
    B.configure(text='B')

    ZB = Label(font=('vendor', 18), fg='black')
    ZB.place(x=50, y=200)
    ZB.configure(text='ZB')

    EB = Label(font=('vendor', 18), fg='black')
    EB.place(x=50, y=250)
    EB.configure(text='EB')

    IB = Label(font=('vendor', 18), fg='black')
    IB.place(x=50, y=300)
    IB.configure(text='IB')
    return

def createCutSetLabel():
    B = Label(font=('vendor', 18), fg='black')
    B.place(x=50, y=150)
    B.configure(text='C')

    ZB = Label(font=('vendor', 18), fg='black')
    ZB.place(x=50, y=200)
    ZB.configure(text='YB')

    EB = Label(font=('vendor', 18), fg='black')
    EB.place(x=50, y=250)
    EB.configure(text='EB')

    IB = Label(font=('vendor', 18), fg='black')
    IB.place(x=50, y=300)
    IB.configure(text='IB')
    return

def tieLabel():
    if (choices.get() == 1):
        createTieSetLabel()
    return

def cutLabel():
    if (choices.get() == 2):
        createCutSetLabel()
    return

# create radio button to choices tie set or cut set

choices = IntVar()

def create_readio_button():
    radioButton1 = Radiobutton(mainWindow, text='Tie Set ', font=('vendor', 18, 'bold'), variable=choices, value=1,
                               command=tieLabel)
    radioButton1.place(x=60, y=60)
    radioButton1.pack()
    radioButton2 = Radiobutton(mainWindow, text='Cut Set ', font=('vendor', 18, 'bold'), variable=choices, value=2,
                               command=cutLabel)
    radioButton2.place(x=60, y=60)
    radioButton2.pack()
    return


