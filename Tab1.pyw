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

# There's got to be a better way to do this but eh =/
class DiceRoller(ttk.Frame):
    def __init__(self,root):
        ttk.Frame.__init__(self, root)
        
        #Declaring variables(In order d4, d6, d8, d10, d12, d20, d100)

        self.var1 = IntVar()
        self.Num1 = IntVar()
        self.Mod1 = IntVar()

        self.var2 = IntVar()
        self.Num2 = IntVar()
        self.Mod2 = IntVar()

        self.var3 = IntVar()
        self.Num3 = IntVar()
        self.Mod3 = IntVar()

        self.var4 = IntVar()
        self.Num4 = IntVar()
        self.Mod4 = IntVar()

        self.var5 = IntVar()
        self.Num5 = IntVar()
        self.Mod5 = IntVar()

        self.var6 = IntVar()
        self.Num6 = IntVar()
        self.Mod6 = IntVar()

        self.var7 = IntVar()
        self.Num7 = IntVar()
        self.Mod7 = IntVar()
      
        #Declaring references
        self.Num1 = ttk.Entry(self, width = 5)
        self.Num1.insert("1", '1')
        self.Mod1 = ttk.Entry(self, width = 3)
        self.Mod1.insert("1", '0')
   

        self.Num2 = ttk.Entry(self, width = 5)
        self.Num2.insert("1", '1')
        self.Mod2 = ttk.Entry(self, width = 3)
        self.Mod2.insert("1", '0')

        self.Num3 = ttk.Entry(self, width = 5)
        self.Num3.insert("1", '1')
        self.Mod3 = ttk.Entry(self, width = 3)
        self.Mod3.insert("1", '0')

        self.Num4 = ttk.Entry(self, width = 5)
        self.Num4.insert("1", '1')
        self.Mod4 = ttk.Entry(self, width = 3)
        self.Mod4.insert("1", '0')

        self.Num5 = ttk.Entry(self, width = 5)
        self.Num5.insert("1", '1')
        self.Mod5 = ttk.Entry(self, width = 3)
        self.Mod5.insert("1", '0')

        self.Num6 = ttk.Entry(self, width = 5)
        self.Num6.insert("1", '1')
        self.Mod6 = ttk.Entry(self, width = 3)
        self.Mod6.insert("1", '0')

        self.Num7 = ttk.Entry(self, width = 5)
        self.Num7.insert("1", '1')
        self.Mod7 = ttk.Entry(self, width = 3)
        self.Mod7.insert("1", '0')

        self.text = tk.Text(self)
        self.text.config(state=DISABLED, bg = "gray20", foreground = "gray63", bd = "0", relief = RAISED, font = "Courier")
        self.text.config(height = 11, width = 25)

        #Technically incorrect radiobutton behaviour (as per TKinter documentation), but it allows user to choose a polyhedral.
        d4 = ttk.Radiobutton(self, text = "d4", variable = self.var1, value = 4)
        d6 = ttk.Radiobutton(self, text = "d6", variable = self.var2, value = 6)
        d8 = ttk.Radiobutton(self, text = "d8", variable = self.var3, value = 8)
        d10 = ttk.Radiobutton(self, text = "d10", variable = self.var4, value = 10)
        d12 = ttk.Radiobutton(self, text = 'd12', variable = self.var5, value = 12)
        d20 = ttk.Radiobutton(self, text = 'd20', variable = self.var6, value = 20)
        d100 = ttk.Radiobutton(self, text = 'd100', variable = self.var7, value = 100)

        rolld4 = ttk.Button(self, text = 'Roll', command = self.Rolld4)
        rolld6 = ttk.Button(self, text = 'Roll', command = self.Rolld6)
        rolld8 = ttk.Button(self, text = 'Roll', command = self.Rolld8)
        rolld10 = ttk.Button(self, text = 'Roll', command = self.Rolld10)
        rolld12 = ttk.Button(self, text = 'Roll', command = self.Rolld12)
        rolld20 = ttk.Button(self, text = 'Roll', command = self.Rolld20)
        rolld100 = ttk.Button(self, text = 'Roll', command = self.Rolld100)

        #Grid Placement
        numbers = ttk.Label(self, text = '# of Dice')
        numbers.grid(column=1, row=0, sticky = E)

        modifiers = ttk.Label (self, text = "Modifier")
        modifiers.grid(column=4, row = 0, sticky = W)

        diceTypes = ttk.Label (self, text = "Type")
        diceTypes.grid(column = 2, row = 0)
      
        self.Num1.grid(column = 1, row = 1)
        self.Mod1.grid(column = 4, row = 1)
        
        self.Num2.grid(column = 1, row = 2)
        self.Mod2.grid(column = 4, row = 2)

        self.Num3.grid(column = 1, row = 3)
        self.Mod3.grid(column = 4, row = 3)

        self.Num4.grid(column = 1, row = 4)
        self.Mod4.grid(column = 4, row = 4)

        self.Num5.grid(column = 1, row = 5)
        self.Mod5.grid(column = 4, row = 5)

        self.Num6.grid(column = 1, row = 6)
        self.Mod6.grid(column = 4, row = 6)

        self.Num7.grid(column = 1, row = 7)
        self.Mod7.grid(column = 4, row = 7)
        
        d4.grid(row = 1, column = 2)
        d6.grid(row = 2, column = 2)
        d8.grid(row = 3, column = 2)
        d10.grid(row = 4, column = 2)
        d12.grid(row = 5, column = 2)
        d20.grid(row = 6, column = 2)
        d100.grid(row = 7, column = 2)

        rolld4.grid(row = 1, column = 5)
        rolld6.grid(row = 2, column = 5)
        rolld8.grid(row = 3, column = 5)
        rolld10.grid(row = 4, column = 5)
        rolld12.grid(row = 5, column = 5)
        rolld20.grid(row = 6, column = 5)
        rolld100.grid(row = 7, column = 5)

        self.text.grid(column = 1, row=8, columnspan = 5, rowspan=6, sticky = EW, ipadx=15, pady = 15)
 
        #Function
    def Rolld4(self):
        
        if(self.Num1.get()):
            if(self.Mod1.get()):
                diceNumber = self.Num1.get()
                modifier = self.Mod1.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var1.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in D4 the modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the Number of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D4 modifier field')
        else:
            showerror('Error', 'Whoops')

    def Rolld6(self):
        
        if(self.Num2.get()):
            if(self.Mod2.get()):
                diceNumber = self.Num2.get()
                modifier = self.Mod2.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var2.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the D6 modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the # of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D6 modifier field')
        else:
            showerror('Error', 'Whoops')
                       
    def Rolld8(self):
            
        if(self.Num3.get()):
            if(self.Mod3.get()):
                diceNumber = self.Num3.get()
                modifier = self.Mod3.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var3.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the D8 modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the # of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D8 modifier field')
        else:
            showerror('Error', 'Whoops')

    def Rolld10(self):
        
        if(self.Num4.get()):
            if(self.Mod4.get()):
                diceNumber = self.Num4.get()
                modifier = self.Mod4.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var4.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the D10 modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the # of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D10 modifier field')
        else:
            showerror('Error', 'Whoops')

    def Rolld12(self):
        
        if(self.Num5.get()):
            if(self.Mod5.get()):
                diceNumber = self.Num5.get()
                modifier = self.Mod5.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var5.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the D12 modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the # of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D12 modifier field')
        else:
            showerror('Error', 'Whoops')

    def Rolld20(self):
        
        if(self.Num6.get()):
            if(self.Mod6.get()):
                diceNumber = self.Num6.get()
                modifier = self.Mod6.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var6.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the D20 modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the # of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D20 modifier field')
        else:
            showerror('Error', 'Whoops!')

    def Rolld100(self):
        
        if(self.Num7.get()):
            if(self.Mod7.get()):
                diceNumber = self.Num7.get()
                modifier = self.Mod7.get()
                if(diceNumber.isdigit()):
                    try:
                        modifier = int(modifier)
                        diceNumber = int(diceNumber)
                        diceType = self.var7.get()
                        if(diceType):
                            dice = 0
                            diceTotal = 0
                            stringResult = ''
                            for dice in range(0, diceNumber):
                                diceRoll = randint(1, diceType)
                                diceTotal = diceTotal + diceRoll
                                stringResult = stringResult + 'Dice number ' + str(dice+1) + ' result = ' + str(diceRoll) + '\n'

                            self.text.config(state=NORMAL)
                            self.text.delete(1.0, END)
                            self.text.insert(INSERT, stringResult + '= %d, plus modifier = %d' % (diceTotal,diceTotal+modifier))
                            self.text.config(state=DISABLED)
                        else:
                            showerror('Error', 'Please choose a dice type')
                    except:
                        showerror('Error', 'Please insert a numeric value in the D100 modifier field')
                else:
                    showerror('Error', 'Please insert a numeric value in the D100 # of Dice field')

            else:
                showerror('Error', 'Please insert a numeric value in the D100 modifier field')