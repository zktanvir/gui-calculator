import tkinter
from tkinter import *
import parser

equation = ""

def onclick_btn_1():
    global equation
    equation += '1'
    screen.config(text=equation)

    
def onclick_btn_2():
    global equation
    equation += '2'
    screen.config(text=equation)
    
def onclick_btn_3():
    global equation
    equation += '3'
    screen.config(text=equation)

def onclick_btn_4():
    global equation
    equation += '4'
    screen.config(text=equation)
    
def onclick_btn_5():
    global equation
    equation += '5'
    screen.config(text=equation)
    
def onclick_btn_6():
    global equation
    equation += '6'
    screen.config(text=equation)
    
def onclick_btn_7():
    global equation
    equation += '7'
    screen.config(text=equation)
    
def onclick_btn_8():
    global equation
    equation += '8'
    screen.config(text=equation)
    
def onclick_btn_9():
    global equation
    equation += '9'
    screen.config(text=equation)
    

def onclick_btn_0():
    global equation
    equation += '0'
    screen.config(text=equation)
    

def onclick_btn_00():
    global equation
    equation += '00'
    screen.config(text=equation)
    

def onclick_btn_plus():
    global equation
    equation += '+'
    screen.config(text=equation)
    
def onclick_btn_minus():
    global equation
    equation += '-'
    screen.config(text=equation)
    
def onclick_btn_multi():
    global equation
    equation += '*'
    screen.config(text=equation)
    
def onclick_btn_devide():
    global equation
    equation += '/'
    screen.config(text=equation)
    
def clear():
    global equation
    equation = ""
    screen.config(text=equation)
    
def onclick_btn_dot():
    global equation
    equation += '.'
    screen.config(text=equation)
    
def onclick_btn_br_open():
    global equation
    equation += '('
    screen.config(text=equation)

def onclick_btn_br_close():
    global equation
    equation += ')'
    screen.config(text=equation)
    

def equals():
    global equation
    try:
        equation = parser.expr(equation).compile()
        equation = str(eval(equation))
        ans = equation
    except Exception:
        ans = 'ERROR!'
    screen.config(text=ans)
    equation = ""
    

    

root = Tk()
root.config(
    bg='#080404',
)
root.geometry('250x400+300+300')
root.resizable(0,0)
root.title('Calculator')

screen = Label(
    root,
    text='',
    font=(
        'Helvetica',
        22
    ),
    anchor=SE,
    bg='#080404',
    fg='#70ff70'
)
screen.pack(
    expand=True,fill='both'
)

btn_row_0 = Frame(root,bg='#080404')
btn_row_0.pack(expand=True,fill='both')



btn_row_1 = Frame(root,bg='#080404')
btn_row_1.pack(expand=True,fill='both')



btn_row_2 = Frame(root,bg='#080404')
btn_row_2.pack(expand=True,fill='both')



btn_row_3 = Frame(root,bg='#080404')
btn_row_3.pack(expand=True,fill='both')



btn_row_4 = Frame(root,bg='#080404')
btn_row_4.pack(expand=True,fill='both')


btn_7 = Button(
    btn_row_1,
    text='7',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_7,
    activebackground='#FFF'
)
btn_7.pack(side=LEFT, expand=True, fill='both')


btn_8 = Button(
    btn_row_1,
    text='8',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_8,
    activebackground='#FFF'
)
btn_8.pack(side=LEFT, expand=True, fill='both')


btn_9 = Button(
    btn_row_1,
    text='9',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_9,
    activebackground='#FFF'
)
btn_9.pack(side=LEFT, expand=True, fill='both')


btn_4 = Button(
    btn_row_2,
    text='4',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_4,
    activebackground='#FFF'
)
btn_4.pack(side=LEFT, expand=True, fill='both')


btn_5 = Button(
    btn_row_2,
    text='5',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_5,
    activebackground='#FFF'
)
btn_5.pack(side=LEFT, expand=True, fill='both')


btn_6 = Button(
    btn_row_2,
    text='6',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_6,
    activebackground='#FFF'
)
btn_6.pack(side=LEFT, expand=True, fill='both')


btn_minus = Button(
    btn_row_1,
    text='- ',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=onclick_btn_minus,
    activebackground='#FFF'
)
btn_minus.pack(side=LEFT, expand=True, fill='both')


btn_1 = Button(
    btn_row_3,
    text='1',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_1,
    activebackground='#FFF'
)
btn_1.pack(side=LEFT, expand=True, fill='both')


btn_2 = Button(
    btn_row_3,
    text='2',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_2,
    activebackground='#FFF'
)
btn_2.pack(side=LEFT, expand=True, fill='both')


btn_3 = Button(
    btn_row_3,
    text='3',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_3,
    activebackground='#FFF'
)
btn_3.pack(side=LEFT, expand=True, fill='both')



btn_multi = Button(
    btn_row_2,
    text='×',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=onclick_btn_multi,
    activebackground='#FFF'
)
btn_multi.pack(side=LEFT, expand=True, fill='both')


btn_clear = Button(
    btn_row_0,
    text='C',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#F00',
    command=clear,
    activebackground='#FFF'
)
btn_clear.pack(side=LEFT, expand=True, fill='both')


btn_bracket_open = Button(
    btn_row_0,
    text='(',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=onclick_btn_br_open,
    activebackground='#FFF'
)
btn_bracket_open.pack(side=LEFT, expand=True, fill='both')


btn_bracket_close = Button(
    btn_row_0,
    text=')',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=onclick_btn_br_close,
    activebackground='#FFF'
)
btn_bracket_close.pack(side=LEFT, expand=True, fill='both')



btn_plus = Button(
    btn_row_0,
    text='+',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=onclick_btn_plus,
    activebackground='#FFF'
    
)
btn_plus.pack(side=LEFT, expand=True, fill='both')



btn_00 = Button(
    btn_row_4,
    text='00',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_00,
    activebackground='#FFF'
)
btn_00.pack(side=LEFT, expand=True, fill='both')


btn_0 = Button(
    btn_row_4,
    text='0',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_0,
    activebackground='#FFF'
)
btn_0.pack(side=LEFT, expand=True, fill='both')


btn_dot = Button(
    btn_row_4,
    text='.',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#FFF',
    command=onclick_btn_dot,
    activebackground='#FFF'
)
btn_dot.pack(side=LEFT, expand=True, fill='both')


btn_devide = Button(
    btn_row_3,
    text='÷',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=onclick_btn_devide,
    activebackground='#FFF'
)
btn_devide.pack(side=LEFT, expand=True, fill='both')


btn_equal = Button(
    btn_row_4,
    text='=',
    font=('Helvetica', 18),
    bd = 0,
    highlightthickness = 0,
    bg='#080404',
    fg='#448404',
    command=equals,
    activebackground='#FFF'
)
btn_equal.pack(side=LEFT, expand=True, fill='both')





root.mainloop()