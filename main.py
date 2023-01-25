


 #[[1,0,-1,-1],[0,1,1,1]] C
 #[[2,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,4]] YP
 #[0,0,0,0] EP
 #[10,0,0,0] IP


from data.tie_set_model import TieSetData
from operation.tie_set_oprations import TieSetOperations
from data.cut_set_model import CutSetData
from operation.cut_set_operations import CutSetOperations
from tkinter import *
from gui.gui import *

def draw(jb, vb, is_user_selected):
    if is_user_selected:
        outputLabel.configure(
            text='out put : \n' + 'Branches Current: ' +
                 str(jb) + '\nBranches Volt: ' + str(vb)
            , padx=20, pady=20, background="grey",
            justify="left", border=10, borderwidth=20, )
    else:
        outputLabel.configure(
            text='Please choice Tie Set or Cut Set Matrix '

            , padx=20, pady=20, background="grey",
            justify="left", border=10, borderwidth=20, )
    pass

def func():
    # entry_input_b
    # entry_input_zb
    # entry_input_eb
    # entry_input_ib
    # global choices

    if choices.get() == 1:
        data_b = eval(entry_input_b.get())
        data_zb = eval(entry_input_zb.get())
        data_eb = eval(entry_input_eb.get())
        data_ib = eval(entry_inbut_ib.get())
        t_model = TieSetData(data_b, data_zb, data_eb, data_ib)
        tso = TieSetOperations(t_model)
        output_jb = tso.get_jb()
        output_vb = tso.get_vb()
        draw(output_jb, output_vb, True)
    elif choices.get() == 2:
        data_c = eval(entry_input_b.get())
        data_yb = eval(entry_input_zb.get())
        data_eb = eval(entry_input_eb.get())
        data_ib = eval(entry_inbut_ib.get())
        c_model = CutSetData(data_c, data_yb, data_eb, data_ib)
        cso = CutSetOperations(c_model)
        output_jb = cso.get_jb()
        output_vb = cso.get_vb()
        draw(output_jb,output_vb, True)
    else:
        draw([], [], False)
    return



# [[1,1,0,1,0],[-1,0,1,0,1]] B
# [[2,0,0,0,0],[0,5,0,0,0],[0,0,4,0,0],[0,0,0,3,0],[0,0,0,0,1]] Zb
# [4,0,-2,2,6]
# [0,0,0,-3,4]

# [[1,0,-1,-1],[0,1,1,1]]
# [[2,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,4],]
# [0,0,0,0]
# [10,0,0,0]

# funcation to get value form input and do funcation

# create main widow and configure it
create_main_windo()

# creae entery flied to get inpu
def createInputFiled():
    global entry_input_b
    global entry_input_zb
    global entry_input_eb
    global entry_inbut_ib

    entry_input_b = Entry(mainWindow, font=('Verdana', 16), width=20)
    entry_input_b.place(x=100, y=150)

    entry_input_zb = Entry(mainWindow, font=('Verdana', 16), width=20)
    entry_input_zb.place(x=100, y=200)

    entry_input_eb = Entry(mainWindow, font=('Verdana', 16), width=20)
    entry_input_eb.place(x=100, y=250)

    entry_inbut_ib = Entry(mainWindow, font=('Verdana', 16), width=20)
    entry_inbut_ib.place(x=100, y=300)
    return
create_solve_button(func)
createInputFiled()

# create label to tie set
# create radio button to choices tie set or cut set
create_readio_button()
# create label to show output
# create label to show output

def create_label_output():
    global outputLabel
    outputLabel = Label(font=('vendor', 14, 'bold'), fg='black')
    outputLabel.place(x=500, y=150)
    outputLabel.configure(text='out put: ')
create_label_output()

mainWindow.mainloop()
