import qiskit
import tkinter

# window
root = tkinter.Tk()
root.title("Quantum Glasses")

# colours n fonts
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 32)

# def layout + frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root, bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

# def display frame layout
display = tkinter.Entry(display_frame, width=35, font=display_font, bg=background, borderwidth=10, justify=tkinter.LEFT)
display.pack(padx=3, pady=4)

root.mainloop()