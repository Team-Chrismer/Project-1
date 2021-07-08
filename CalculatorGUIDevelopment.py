from tkinter import *

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="light blue")
	gui.title("Simple Calculator")
	gui.geometry("280x199")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)

gui.mainloop()
