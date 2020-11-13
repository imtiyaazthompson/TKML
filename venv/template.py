import tkinter as tk

def setup():
	widgets = {}
	widgets['myLabel'] = tk.Label(text='Hello, World',width=0,height=0)
	widgets['myLabel_2'] = tk.Label(text='Foo bar',width=0,height=0)
	widgets['myButton'] = tk.Button(text='my button',width=0,height=0)
	return widgets

def main():
	window = tk.Tk()
	widgets = setup()
	for key in widgets.keys():
		widgets[key].pack()
	window.mainloop()

if __name__ == '__main__':
	main()