from tkinter import * 
from tkinter import messagebox #To work with messagesPopup
import numpy as np # numpy for maths operations.
import matplotlib.pyplot as plt # MatplotLib & PyPlot for plotting graph.
import re # Regular expressions

#python function_plotter.py

root = Tk()
root.title("Function plotter")
root.iconbitmap('./mm_logo.ico')
root.geometry("700x250")
	

#padding here is internally within the frame
bigFrame = LabelFrame(root, text="Enter f(x)", padx=10, pady=10, font = "bold")
#padding here is externally within the root
bigFrame.grid(row=0, column=0, padx=30, pady=30)
fun = Entry(bigFrame,  width=100, borderwidth = 5)
fun.grid(row=0, column=0, columnspan=3)

minFrame = LabelFrame(bigFrame, text="Enter min value of x", padx=10, pady=10)
minFrame.grid(row=1, column=0, padx=20, pady=20)
min  = Entry(minFrame , width=30, borderwidth = 2)
min.grid(row=0, column=0)

maxFrame = LabelFrame(bigFrame, text="Enter max value of x", padx=10, pady=10)
maxFrame.grid(row=1, column=1, padx=20, pady=20)
max  = Entry(maxFrame , width=30, borderwidth = 2)
max.grid(row=0, column=0)


def popup_validInput():
	messagebox.showerror("Take care", "Enter a valid input function please!")

def popup_emptyFields():
	messagebox.showwarning("Take care", "Enter all filelds please!")
	
	

def string2func(string):
	global f 
	replacements = {'^': '**'}
	allowed_words = ['x']

	# evaluates the string and returns a function of x 
	# find all words and check if all are allowed:
	
	for word in re.findall('[a-zA-Z]+', string):
			if word not in allowed_words:
				#raise ValueError(
				#    '"{}" is forbidden to use in math expression'.format(word)
				#)
				popup_validInput()

	for old, new in replacements.items():
		string = string.replace(old, new)

	def func(x):
		return eval(string)
	return func
	


def plot():

	#'5*x**3 + 2*x'
	
	if (len(fun.get()) != 0 and len(min.get()) != 0 and len(max.get()) != 0):
		f = string2func(str(fun.get()))
		a = float(min.get())
		b = float(max.get())
		x = np.linspace(a, b, 250)
		
		fig, ax = plt.subplots()
		
		ax.grid()
		fig.canvas.manager.set_window_title("Function plotter")
		ax.set_title("Your function Plot ^_^" ,fontsize = 12, fontweight ='bold')
		ax.plot(x, f(x))
		plt.xlim(a, b)
		plt.show()
		return True
	else :
		popup_emptyFields()
		return False
	

buttonFrame = LabelFrame(bigFrame, text="", padx=10, pady=10)
buttonFrame.grid(row=1, column=2, padx=20, pady=20)
plotButton = Button(buttonFrame, text="plot", command=plot)
plotButton.grid(row=0, column=0)



root.mainloop()