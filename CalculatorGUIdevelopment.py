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
