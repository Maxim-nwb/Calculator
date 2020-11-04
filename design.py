import tkinter as tk



#-----------------------------------------------GIU----------------------------------------------------------------
#------------------------------Main window
MainWindow = tk.Tk()
MainWindow.geometry('324x225')
MainWindow.resizable(width=False, height=False)
MainWindow.title('Calculator')
MainWindow.iconbitmap('icon.ico')

#----------------------------Input boxes
BoxHistory = tk.Entry(MainWindow, width = 23, font = 'Times 12', justify=tk.RIGHT)
BoxHistory.grid(column = 0, row = 0, columnspan = 4, sticky=tk.W+tk.E+tk.N+tk.S)

BoxMain = tk.Entry(MainWindow, width = 23, font = 'Times 20', justify=tk.RIGHT)
BoxMain.grid(column = 0, row = 1, columnspan = 4, sticky=tk.W+tk.E+tk.N+tk.S)
#----------------------------------Buttons

#---------------Numbers
btn0 = tk.Button(MainWindow, text="0")
btn0.grid(column=0, row=6, sticky=tk.W+tk.E+tk.N+tk.S)

btn1 = tk.Button(MainWindow, text="1")
btn1.grid(column=0, row=5, sticky=tk.W+tk.E+tk.N+tk.S)

btn2 = tk.Button(MainWindow, text="2")  
btn2.grid(column=1, row=5, sticky=tk.W+tk.E+tk.N+tk.S)

btn3 = tk.Button(MainWindow, text="3")
btn3.grid(column=2, row=5, sticky=tk.W+tk.E+tk.N+tk.S)

btn4 = tk.Button(MainWindow, text="4")
btn4.grid(column=0, row=4, sticky=tk.W+tk.E+tk.N+tk.S)

btn5 = tk.Button(MainWindow, text="5")  
btn5.grid(column=1, row=4, sticky=tk.W+tk.E+tk.N+tk.S)

btn6 = tk.Button(MainWindow, text="6")
btn6.grid(column=2, row=4, sticky=tk.W+tk.E+tk.N+tk.S)

btn7 = tk.Button(MainWindow, text="7")
btn7.grid(column=0, row=3, sticky=tk.W+tk.E+tk.N+tk.S)

btn8 = tk.Button(MainWindow, text="8")  
btn8.grid(column=1, row=3, sticky=tk.W+tk.E+tk.N+tk.S)

btn9 = tk.Button(MainWindow, text="9")
btn9.grid(column=2, row=3, sticky=tk.W+tk.E+tk.N+tk.S)

#-----------Functions
btn_plus = tk.Button(MainWindow, text="+")
btn_plus.grid(column=3, row=6, sticky=tk.W+tk.E+tk.N+tk.S)

btn_minus = tk.Button(MainWindow, text="-")  
btn_minus.grid(column=3, row=5, sticky=tk.W+tk.E+tk.N+tk.S)

btn_mult = tk.Button(MainWindow, text="*")
btn_mult.grid(column=3, row=4, sticky=tk.W+tk.E+tk.N+tk.S)

btn_div = tk.Button(MainWindow, text="/")  
btn_div.grid(column=3, row=3, sticky=tk.W+tk.E+tk.N+tk.S)

btn_equal = tk.Button(MainWindow, text="=")  
btn_equal.grid(column=2, row=6, sticky=tk.W+tk.E+tk.N+tk.S)

btn_dot = tk.Button(MainWindow, text=".")  
btn_dot.grid(column=1, row=6, sticky=tk.W+tk.E+tk.N+tk.S)

btn_del = tk.Button(MainWindow, text="⌫")  
btn_del.grid(column=3, row=2, sticky=tk.W+tk.E+tk.N+tk.S)

btn_clear = tk.Button(MainWindow, text="C")  
btn_clear.grid(column=2, row=2, sticky=tk.W+tk.E+tk.N+tk.S)

btn_pow = tk.Button(MainWindow, text="x²")  
btn_pow.grid(column=1, row=2, sticky=tk.W+tk.E+tk.N+tk.S)

btn_sqrt = tk.Button(MainWindow, text="√")  
btn_sqrt.grid(column=0, row=2, sticky=tk.W+tk.E+tk.N+tk.S)
