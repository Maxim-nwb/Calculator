import tkinter as tk
import math

#----------------Main window
MainWindow = tk.Tk()
MainWindow.geometry('350x225')
MainWindow.resizable(width=False, height=False)
MainWindow.title('Calculator')
MainWindow.iconbitmap('icon.ico')
#----------------

LabelBoxMain = tk.StringVar() # tracing to update BoxMain (line 19)
LabelBoxHistory = tk.StringVar() # tracing to update BoxHistory (line 17)
Expression = '' # variable to store an expression
HistoryExpression = '' # variable to store an history expression
NumberOne = None # variable to store an first digit
NumberTwo = None # variable to store an second digit


#----------------------------Input boxes
BoxHistory = tk.Label(MainWindow, width = 23, font = 'Times 12', textvariable = LabelBoxHistory, anchor = tk.E, bg='#AFEEEE')
BoxHistory.grid(column = 0, row = 0, columnspan = 4, sticky=tk.W+tk.E+tk.N+tk.S)

BoxMain = tk.Label(MainWindow, width = 23, font = 'Times 20', textvariable = LabelBoxMain, anchor = tk.E, bg='#40E0D0')
BoxMain.grid(column = 0, row = 1, columnspan = 4, sticky=tk.W+tk.E+tk.N+tk.S)
#----------------------------

#------------------Function

def clear():
    # function clear BoxMain and BoxHistory
    global Expression
    global HistoryExpression
    global NumberOne
    global NumberTwo
    # changing the trace variable
    HistoryExpression = ''
    Expression = ''
    # setting the variables to their initial position
    NumberOne = None
    NumberTwo = None
    # set changes
    LabelBoxMain.set(Expression)
    LabelBoxHistory.set(HistoryExpression)

def delete(event='<KeyPress event state=Mod1|0x40000 keysym=Delete keycode=46 x=221 y=-52>'):
    # function delete last char in BoxMain
    global Expression
    Expression = Expression[:-1]
    LabelBoxMain.set(Expression)

def pow_actions():
    global Expression
    global HistoryExpression
    # checks whether the values to convert to float are correct
    if Expression == "." or Expression == "":
        pass
    # adding an entry to BoxHistory
    else:
        HistoryExpression = '{0}²'.format(Expression)
        LabelBoxHistory.set(HistoryExpression)
    # count
        Expression = str(float(Expression)**2)
        LabelBoxMain.set(Expression)

def sqrt_actions():
    global Expression
    global HistoryExpression
    # checks whether the values to convert to float are correct
    if Expression == "." or Expression == "":
        pass
    # adding an entry to BoxHistory
    else:
        HistoryExpression = '√ {0}'.format(Expression)
        LabelBoxHistory.set(HistoryExpression)
    # count
        Expression = str(math.sqrt(float(Expression)))
        LabelBoxMain.set(Expression)

def equal(x,y,act):
    solution = None
    # check what action needs to be performed
    if act == " + ":
        solution = x + y
    if act == " - ":
        solution = x - y
    if act == " * ":
        solution = x * y
    if act == " / ":
        solution = x / y
    return solution

def get_actions(event, i):
    global Expression
    global HistoryExpression
    global NumberOne
    global NumberTwo

    # if the user accidentally clicks on the same sign several times in a row, no action will be performed
    if str(NumberOne) == Expression and HistoryExpression[-3:] == i:
        pass
    # checking for correct use of "="
    elif (HistoryExpression == "" or "√" in HistoryExpression or "²" in HistoryExpression) and i == " = ":
        pass
    # clear memory for new expression after getting the result
    elif "=" in HistoryExpression and i != " = ":
        HistoryExpression = str(NumberOne) + i
        LabelBoxHistory.set(HistoryExpression)
        Expression = ""
        LabelBoxMain.set(Expression)
    # if the user selected an action and then changed it, change the sign
    elif str(NumberOne) == Expression and HistoryExpression[-3:] != i and i != " = ":
        HistoryExpression = HistoryExpression[:-3] + i
        LabelBoxHistory.set(HistoryExpression)
    # checks whether the values to convert to float are correct
    elif Expression == "." or Expression == "":
        pass
    else:
        # work with complex expressions
        if "√" in HistoryExpression or "²" in HistoryExpression:
            HistoryExpression = ""
            LabelBoxHistory.set(HistoryExpression)
            NumberOne = None
        LastExpression = Expression
        # checking for variables
        if NumberOne is not None:
            NumberTwo = float(Expression)
        else:
            NumberOne = float(Expression)
        # if there are two variables and there is an action we perform it
        if (NumberOne and NumberTwo) is not None:
            NumberOne = equal(NumberOne, NumberTwo, HistoryExpression[-3:])
            # recording the result for entering in BoxMain
            Expression = str(NumberOne)
            # update variables
            NumberTwo = None
        else:
            Expression = ''
            # get actions in BoxHistory
        HistoryExpression += LastExpression + i
        LabelBoxHistory.set(HistoryExpression)
        LabelBoxMain.set(Expression)

def get_numbers(event, i):
    # get numbers in BoxMain
    global Expression
    global NumberOne
    #chek ..
    if i == "." and Expression.count(".") == 1: i = ""
    # clear memory for new expression
    if "=" in LabelBoxHistory.get() or "√" in LabelBoxHistory.get() or "²" in LabelBoxHistory.get():
        clear()
    # if the answer to the last calculation is in BoxMain then we clear it
    if str(NumberOne) == Expression:
        Expression = ''
    Expression += i
    LabelBoxMain.set(Expression)


#---------------Buttons Numbers
btn0 = tk.Button(MainWindow, text="0")
btn0.grid(column=0, row=6, sticky=tk.W+tk.E+tk.N+tk.S)
btn0.bind('<Button-1>', lambda event, numb ='0': get_numbers(event, numb))

btn1 = tk.Button(MainWindow, text="1")
btn1.grid(column=0, row=5, sticky=tk.W+tk.E+tk.N+tk.S)
btn1.bind('<Button-1>', lambda event, numb ='1': get_numbers(event, numb))

btn2 = tk.Button(MainWindow, text="2")  
btn2.grid(column=1, row=5, sticky=tk.W+tk.E+tk.N+tk.S)
btn2.bind('<Button-1>', lambda event, numb ='2': get_numbers(event, numb))

btn3 = tk.Button(MainWindow, text="3")
btn3.grid(column=2, row=5, sticky=tk.W+tk.E+tk.N+tk.S)
btn3.bind('<Button-1>', lambda event, numb ='3': get_numbers(event, numb))

btn4 = tk.Button(MainWindow, text="4")
btn4.grid(column=0, row=4, sticky=tk.W+tk.E+tk.N+tk.S)
btn4.bind('<Button-1>', lambda event, numb ='4': get_numbers(event, numb))

btn5 = tk.Button(MainWindow, text="5")  
btn5.grid(column=1, row=4, sticky=tk.W+tk.E+tk.N+tk.S)
btn5.bind('<Button-1>', lambda event, numb ='5': get_numbers(event, numb))

btn6 = tk.Button(MainWindow, text="6")
btn6.grid(column=2, row=4, sticky=tk.W+tk.E+tk.N+tk.S)
btn6.bind('<Button-1>', lambda event, numb ='6': get_numbers(event, numb))

btn7 = tk.Button(MainWindow, text="7")
btn7.grid(column=0, row=3, sticky=tk.W+tk.E+tk.N+tk.S)
btn7.bind('<Button-1>', lambda event, numb ='7': get_numbers(event, numb))

btn8 = tk.Button(MainWindow, text="8")  
btn8.grid(column=1, row=3, sticky=tk.W+tk.E+tk.N+tk.S)
btn8.bind('<Button-1>', lambda event, numb ='8': get_numbers(event, numb))

btn9 = tk.Button(MainWindow, text="9")
btn9.grid(column=2, row=3, sticky=tk.W+tk.E+tk.N+tk.S)
btn9.bind('<Button-1>', lambda event, numb ='9': get_numbers(event, numb))
#---------------

#-----------Buttons Functions
btn_plus = tk.Button(MainWindow, text="+")
btn_plus.grid(column=3, row=6, sticky=tk.W+tk.E+tk.N+tk.S)
btn_plus.bind('<Button-1>', lambda event, numb =' + ': get_actions(event, numb))

btn_minus = tk.Button(MainWindow, text="-")  
btn_minus.grid(column=3, row=5, sticky=tk.W+tk.E+tk.N+tk.S)
btn_minus.bind('<Button-1>', lambda event, numb =' - ': get_actions(event, numb))

btn_mult = tk.Button(MainWindow, text="*")
btn_mult.grid(column=3, row=4, sticky=tk.W+tk.E+tk.N+tk.S)
btn_mult.bind('<Button-1>', lambda event, numb =' * ': get_actions(event, numb))

btn_div = tk.Button(MainWindow, text="/")  
btn_div.grid(column=3, row=3, sticky=tk.W+tk.E+tk.N+tk.S)
btn_div.bind('<Button-1>', lambda event, numb =' / ': get_actions(event, numb))

btn_equal = tk.Button(MainWindow, text="=")  
btn_equal.grid(column=2, row=6, sticky=tk.W+tk.E+tk.N+tk.S)
btn_equal.bind('<Button-1>', lambda event, numb =' = ': get_actions(event, numb))

btn_dot = tk.Button(MainWindow, text=".")  
btn_dot.grid(column=1, row=6, sticky=tk.W+tk.E+tk.N+tk.S)
btn_dot.bind('<Button-1>', lambda event, numb ='.': get_numbers(event, numb))

btn_del = tk.Button(MainWindow, text="⌫", command = delete)  
btn_del.grid(column=3, row=2, sticky=tk.W+tk.E+tk.N+tk.S)


btn_clear = tk.Button(MainWindow, text="C", command = clear)  
btn_clear.grid(column=2, row=2, sticky=tk.W+tk.E+tk.N+tk.S)

btn_pow = tk.Button(MainWindow, text="x²", command = pow_actions)  
btn_pow.grid(column=1, row=2, sticky=tk.W+tk.E+tk.N+tk.S)

btn_sqrt = tk.Button(MainWindow, text="√", command = sqrt_actions)  
btn_sqrt.grid(column=0, row=2, sticky=tk.W+tk.E+tk.N+tk.S)
#-----------

#-----------------------Processing keystrokes
#-------Numbers
MainWindow.bind('<Key-0>', lambda event, numb ='0': get_numbers(event, numb))

MainWindow.bind('<Key-1>', lambda event, numb ='1': get_numbers(event, numb))

MainWindow.bind('<Key-2>', lambda event, numb ='2': get_numbers(event, numb))

MainWindow.bind('<Key-3>', lambda event, numb ='3': get_numbers(event, numb))

MainWindow.bind('<Key-4>', lambda event, numb ='4': get_numbers(event, numb))

MainWindow.bind('<Key-5>', lambda event, numb ='5': get_numbers(event, numb))

MainWindow.bind('<Key-6>', lambda event, numb ='6': get_numbers(event, numb))

MainWindow.bind('<Key-7>', lambda event, numb ='7': get_numbers(event, numb))

MainWindow.bind('<Key-8>', lambda event, numb ='8': get_numbers(event, numb))

MainWindow.bind('<Key-9>', lambda event, numb ='9': get_numbers(event, numb))
#--------Actions
MainWindow.bind('<Key-+>', lambda event, numb =' + ': get_actions(event, numb))

MainWindow.bind('<Key-->', lambda event, numb =' - ': get_actions(event, numb))

MainWindow.bind('<Key-*>', lambda event, numb =' * ': get_actions(event, numb))

MainWindow.bind('<Key-/>', lambda event, numb =' / ': get_actions(event, numb))

MainWindow.bind('<Key-.>', lambda event, numb ='.': get_numbers(event, numb))

MainWindow.bind('<Key-Return>', lambda event, numb =' = ': get_actions(event, numb))

MainWindow.bind('<Key-BackSpace>', delete)
MainWindow.bind('<Key-Delete>', delete)

#-----------------------

#-------Main
MainWindow.mainloop()