# Project-1
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
