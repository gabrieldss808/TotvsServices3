"""Ttk Frame with rounded corners.

Based on an example by Bryan Oakley, found at: http://wiki.tcl.tk/20152"""
from tkinter import *
from tkinter.ttk import *
from utils.stylesInterface import StylesInterface

root = Tk()

Style = StylesInterface()

frame = Frame(root,style="RoundedFrame", padding=10)
frame.pack(fill='x')

frame2 = Frame(style="RoundedFrame", padding=10)
frame2.pack(fill='both', expand=1)

entry = Entry(frame, text='Test')
entry.pack(fill='x')
entry.bind("<FocusIn>", lambda evt: frame.state(["focus"]))
entry.bind("<FocusOut>", lambda evt: frame.state(["!focus"]))

text = Text(frame2, borderwidth=0, bg="white", highlightthickness=0)
text.pack(fill='both', expand=1)
text.bind("<FocusIn>", lambda evt: frame2.state(["focus"]))
text.bind("<FocusOut>", lambda evt: frame2.state(["!focus"]))

root.mainloop()