#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 GUI
# Tkinter

# 快速打印
from tkinter import messagebox

from util import p
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.nameInput = Entry(self)
        self.hello_label = Label(self, text='Hello,World!')
        self.quit_button = Button(self, text='Hello', command=self.hello)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nameInput.pack()
        # self.hello_label.pack()
        self.quit_button.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello,%s!' % name)


app = Application()
app.master.title("Hello,World!")
app.mainloop()
