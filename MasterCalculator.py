from tkinter import *

expression = ""

def input_val(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
  
def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ") 
		expression = ""
    
def clear():
	global expression
	expression = ""
	equation.set("")

def backspace():
	global expression
	expression = expression[:-1]
	equation.set(expression)

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="light blue")
	gui.title("Simple Calculator")
	gui.geometry("280x199")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)

button1 = Button(gui, text =' 1 ', font="lucida 10 bold",
command = lambda: input_val(1), height = 1, width = 7)
button1.grid(row = 4, column = 0, ipady = 4 , ipadx = 2)

button2 = Button(gui, text = ' 2 ', font="lucida 10 bold",
command = lambda: input_val(2), height = 1, width = 7)
button2.grid(row = 4, column = 1, ipady = 4 , ipadx = 2)

button3 = Button(gui, text = ' 3 ', font="lucida 10 bold",
command = lambda: input_val(3), height = 1, width = 7)
button3.grid(row = 4, column = 2, ipady = 4 , ipadx = 2)

button4 = Button(gui, text = ' 4 ', font="lucida 10 bold",
command = lambda: input_val(4), height = 1, width = 7)
button4.grid(row = 3, column = 0, ipady = 4 , ipadx = 2)

button5 = Button(gui, text = ' 5 ', font="lucida 10 bold",
command = lambda: input_val(5), height = 1, width = 7)
button5.grid(row = 3, column = 1, ipady = 4 , ipadx = 2)

button6 = Button(gui, text = ' 6 ', font="lucida 10 bold",
command = lambda: input_val(6), height = 1, width = 7)
button6.grid(row = 3, column = 2, ipady = 4 , ipadx = 2)

button7 = Button(gui, text = ' 7 ', font="lucida 10 bold",
command = lambda: input_val(7), height = 1, width = 7)
button7.grid(row = 2, column = 0, ipady = 4 , ipadx = 2)

button8 = Button(gui, text = ' 8 ', font="lucida 10 bold",
command = lambda: input_val(8), height = 1, width = 7)
button8.grid(row = 2, column = 1, ipady = 4 , ipadx = 2)

button9 = Button(gui, text = ' 9 ', font="lucida 10 bold",
command = lambda: input_val(9), height = 1, width = 7)
button9.grid(row = 2, column = 2, ipady = 4 , ipadx = 2)

button10 = Button(gui, text = ' 0 ', font="lucida 10 bold",
command = lambda: input_val(0), height = 1, width = 7)
button10.grid(row = 5, column = '1', ipady = 4 , ipadx = 2)

plus = Button(gui, text=' + ', font="lucida 10 bold",
command = lambda: input_val("+"), height=1, width=7)
plus.grid(row = 2, column = 3, ipady = 4 , ipadx = 2)

minus = Button(gui, text = ' - ', font="lucida 10 bold",
command = lambda: input_val("-"), height = 1, width = 7)
minus.grid(row = 3, column = 3, ipady = 4 , ipadx = 2)

multiply = Button(gui, text = ' * ', font="lucida 10 bold",
command = lambda: input_val("*"), height = 1, width = 7)
multiply.grid(row = 4, column = 3, ipady = 4 , ipadx = 2)

divide = Button(gui, text=' / ', font="lucida 10 bold",
command = lambda: input_val("/"), height = 1, width = 7)
divide.grid(row = 5, column = 3, ipady = 4 , ipadx = 2)

equal = Button(gui, text=' = ', font="lucida 10 bold",
command = equalpress, height = 1, width = 7)
equal.grid(row = 6, column = '1', ipady = 4 , ipadx = 2)

clear = Button(gui, text = 'C', font="lucida 10 bold",
command = clear, height = 1, width = 7)
clear.grid(row = 6, column = 0, ipady = 4 , ipadx = 2)

backspace = Button(gui, text = 'delete', font="lucida 10 bold",
command = backspace, height = 1, width = 7)
backspace.grid(row = 5, column = 0, ipady = 4 , ipadx = 2)

Decimal = Button(gui, text='.', font="lucida 10 bold",
command = lambda: input_val('.'), height = 1, width = 7)
Decimal.grid(row = 5, column = 2, ipady = 4 , ipadx = 2)


gui.mainloop()
