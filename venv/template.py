import tkinter as tk


widgets = {}

PACKING = ['myFrame', 'LabelFrame', 'myLabel', 'myLabel_2', 'ButtonFrame', 'myButton', 'myButton_2', 'EntryFrame', 'nameEntry', 'nameEntry_2']

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
	widgets["LabelFrame"] = tk.Frame(master=widgets["myFrame"])
	widgets['myLabel'] = tk.Label(master=widgets["LabelFrame"],text='Hello, World',width=0,height=0)
	widgets['myLabel_2'] = tk.Label(master=widgets["LabelFrame"],text='Foo bar',width=0,height=0)
	widgets["ButtonFrame"] = tk.Frame(master=widgets["myFrame"])
	widgets['myButton'] = tk.Button(master=widgets["ButtonFrame"],text='my button',width=0,height=0,command=lambda: myButton_callback('''Your arguments go here'''))
	widgets['myButton_2'] = tk.Button(master=widgets["ButtonFrame"],text='Press me!',width=0,height=0,command=lambda: myButton_2_callback('''Your arguments go here'''))
	widgets["EntryFrame"] = tk.Frame(master=widgets["myFrame"])
	widgets['nameEntry'] = tk.Entry(master=widgets["EntryFrame"],width=0)
	widgets['nameEntry'].insert(0,"default")
	widgets['nameEntry_2'] = tk.Entry(master=widgets["EntryFrame"],fg="yellow",bg="blue",width=50)
	widgets['nameEntry_2'].insert(0,"Name")
	return widgets

def main():
	window = tk.Tk()
	widgets = setup()
	for widget in PACKING:
		widgets[widget].pack()
	window.mainloop()

if __name__ == '__main__':
	main()

