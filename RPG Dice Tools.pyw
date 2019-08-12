import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from random import randint
import tkinter.ttk
from ttkthemes import ThemedTk
import sys
import os
from tkinter.font import Font
from Tab1 import DiceRoller
from Tab2 import CombatTracker

class Main(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        tab1 = DiceRoller(self.notebook)
        tab2 = CombatTracker(self.notebook)

        self.notebook.add(tab1, text = "Dice Roller")
        self.notebook.add(tab2, text = "Party Sheet")
        
if __name__ == '__main__':

    root = ThemedTk("equilux")
    root.set_theme("equilux")
    root.wm_title("RPG Tools")
    root.geometry("285x480")
    root.resizable(0,0)
    Main(root).pack(fill="both", expand=True)
    root.mainloop()
