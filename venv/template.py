import tkinter as tk


widgets = {}

PACKING = ['myFrame', 'myLabel', 'myLabel_2', 'myButton', 'myButton_2', 'nameEntry', 'nameEntry_2']

def myButton_callback():
	# Callback for this button when clicked
	pass

def myButton_2_callback():
	# Callback for this button when clicked
	pass

def get_text_from(entry):
	return entry.get()

def setup():
	widgets["myFrame"] = tk.Frame()
	widgets['myLabel'] = tk.Label(master=widgets["myFrame"],text='Hello, World',width=0,height=0)
	widgets['myLabel_2'] = tk.Label(master=widgets["myFrame"],text='Foo bar',width=0,height=0)
	widgets['nameEntry'] = tk.Entry(master=widgets["myFrame"],width=0)
	widgets['nameEntry'].insert(0,"default")
	widgets['nameEntry_2'] = tk.Entry(master=widgets["myFrame"],fg="yellow",bg="blue",width=50)
	widgets['nameEntry_2'].insert(0,"Name")
	widgets['myButton'] = tk.Button(master=widgets["myFrame"],text='my button',width=50,height=0,bg="blue",fg="yellow",command=lambda: myButton_callback('''Your arguments go here'''))
	widgets['myButton_2'] = tk.Button(master=widgets["myFrame"],text='Press me!',width=50,height=0,bg="blue",fg="yellow",command=lambda: myButton_2_callback('''Your arguments go here'''))
	return widgets

def main():
	window = tk.Tk()
	widgets = setup()
	for widget in PACKING:
		widgets[widget].pack()
	window.mainloop()

if __name__ == '__main__':
	main()

