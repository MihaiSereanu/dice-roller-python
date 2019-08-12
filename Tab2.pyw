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

# Combat Tracker without automated support for initiative - might revisit in the future to add.
class CombatTracker(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)


        #Declaring References
        # Not the best practice to hardcode a set number of players into this so I will definitely come back to this and create an Add PC / Enemy button (somehow)
        ## Binding a function to a Button to add more tkinter objects isn't the issue, as much as writing my Roll functions better, without hardcoded values

        # Group Labels
        pclabel = ttk.Label(self, text="Players")
        pclabel.config(font=("Courier", 15))
        pclabel.grid(column=2, row = 0, columnspan =3, sticky=NSEW)
        monsterlabel = ttk.Label(self, text="Monster")
        monsterlabel.config(font=("Courier", 15))
        monsterlabel.grid(column=2, row = 7, columnspan=3, sticky=NSEW)


        # Player Info Labels
        pcname = ttk.Label(self, text = "Name")
        pcAC = ttk.Label(self, text = "AC")
        pcHP = ttk.Label(self, text = "HP")
        pcInsp = ttk.Label(self, text = "Insp.")
        monstertarget = ttk.Label(self, text = "Target")

        targetchoose1 = ttk.Button(self, text = "Attack", width=6, command = self.RollAttack1)

        targetchoose2 = ttk.Button(self, text = "Attack", width = 6, command = self.RollAttack2)
        targetchoose3 = ttk.Button(self, text = "Attack", width = 6, command = self.RollAttack3)
        targetchoose4 = ttk.Button(self, text = "Attack", width = 6, command = self.RollAttack4)
        targetchoose5 = ttk.Button(self, text = "Attack", width = 6, command = self.RollAttack5)

        # Player Labels
        self.pc1 = ttk.Label(self, text = "#1")
        self.pc1name = ttk.Entry(self, width=6)
        self.pc1AC = ttk.Entry(self, width=3)
        self.pc1HP = ttk.Entry(self, width=3)
        self.pc1Insp = ttk.Entry(self, width=3)


        self.pc2 = ttk.Label(self, text = "#2")
        self.pc2name = ttk.Entry(self, width=6)
        self.pc2AC = ttk.Entry(self, width=3)
        self.pc2HP = ttk.Entry(self, width=3)
        self.pc2Insp = ttk.Entry(self, width=3)

        self.pc3 = ttk.Label(self, text = "#3")
        self.pc3name = ttk.Entry(self, width=6)
        self.pc3AC = ttk.Entry(self, width=3)
        self.pc3HP = ttk.Entry(self, width=3)
        self.pc3Insp = ttk.Entry(self, width=3)

        self.pc4 = ttk.Label(self, text = "#4")
        self.pc4name = ttk.Entry(self, width=6)
        self.pc4AC = ttk.Entry(self, width=3)
        self.pc4HP = ttk.Entry(self, width=3)
        self.pc4Insp = ttk.Entry(self, width=3)

        self.pc5 = ttk.Label(self, text = "#5")
        self.pc5name = ttk.Entry(self, width=6)
        self.pc5AC = ttk.Entry(self, width=3)
        self.pc5HP = ttk.Entry(self, width=3)
        self.pc5Insp = ttk.Entry(self, width=3)


        # Monster Labels
        monsternumber1 = ttk.Label(self, text = "#1")
        monstername = ttk.Label (self, text = "Name")
        monsterAC = ttk.Label(self, text = "AC")
        monsterHP = ttk.Label(self, text = "HP")
        monsterBonus = ttk.Label(self, text = "HIT")
        monsterDamage= ttk.Label(self, text = "Damage")

        # Monster Entries
        mname1 = ttk.Entry(self, width = 6)
        mAC1 = ttk.Entry(self, width = 3)
        mHP1 = ttk.Entry(self, width = 3)

        #Damage Labels
        numofdice = ttk.Label(self, text = " Num")
        numofdice.config(font=("Arial", 8))
        polyhedral = ttk.Label(self, text = "   d#")
        polyhedral.config(font=("Arial", 8))
        damageplus = ttk.Label(self, text = "+")
        damageplus.config(font=("Arial", 8))

        #Damage Entries
        self.bonus1 = ttk.Entry(self, width = 3)
        self.numDice = ttk.Entry(self, width=3)
        self.mPlus = ttk.Entry(self, width=4)
        self.diceType = ttk.Entry(self, width=3)

        # Textbox
        self.text = tk.Text(self)
        self.text.config(state=DISABLED, bg = "gray20", foreground = "gray63", bd = "0", relief = RAISED, font = "Courier")
        self.text.config(height = 10, width = 25)

        # Grid Placement
        pcname.grid(column=1, row = 1)
        pcAC.grid(column=2, row = 1)
        pcHP.grid(column=3, row = 1)
        pcInsp.grid(column=4, row = 1, sticky=W)
        monstertarget.grid(column=5, row=1)

        self.pc1.grid(column = 0, row = 2)
        self.pc1name.grid(column=1, row = 2)
        self.pc1AC.grid(column=2, row =2)
        self.pc1HP.grid(column=3, row = 2)
        self.pc1Insp.grid(column=4, row = 2, columnspan=2, sticky=W)
        targetchoose1.grid(column=5, row =2)

        self.pc2.grid(column = 0, row = 3)
        self.pc2name.grid(column=1, row = 3)
        self.pc2AC.grid(column=2, row =3)
        self.pc2HP.grid(column=3, row = 3)
        self.pc2Insp.grid(column=4, row = 3, columnspan=2, sticky=W)
        targetchoose2.grid(column=5, row = 3)

        self.pc3.grid(column = 0, row = 4)
        self.pc3name.grid(column=1, row = 4)
        self.pc3AC.grid(column=2, row =4)
        self.pc3HP.grid(column=3, row = 4)
        self.pc3Insp.grid(column=4, row = 4, columnspan=2, sticky=W)
        targetchoose3.grid(column=5, row = 4)

        self.pc4.grid(column = 0, row = 5)
        self.pc4name.grid(column=1, row = 5)
        self.pc4AC.grid(column=2, row =5)
        self.pc4HP.grid(column=3, row = 5)
        self.pc4Insp.grid(column=4, row = 5, columnspan=2, sticky=W)
        targetchoose4.grid(column=5, row = 5)

        self.pc5.grid(column = 0, row = 6)
        self.pc5name.grid(column=1, row = 6)
        self.pc5AC.grid(column=2, row =6)
        self.pc5HP.grid(column=3, row = 6)
        self.pc5Insp.grid(column=4, row = 6, columnspan=2, sticky=W)
        targetchoose5.grid(column=5, row = 6)

        monsternumber1.grid(column =0, row = 10)

        monstername.grid(column =1, row = 8)
        monsterAC.grid(column = 2, row = 8)
        monsterHP.grid(column=3, row = 8)
        monsterBonus.grid(column =4, row = 8)
        monsterDamage.grid(column = 5, row = 8)

        mname1.grid(column=1, row = 10)
        mAC1.grid(column=2, row = 10)
        mHP1.grid(column=3, row = 10)
        self.bonus1.grid(column=4, row = 10, sticky=W)
        self.numDice.grid(column=5, row=10, sticky=W)
        self.diceType.grid(column=5, row=10, columnspan=3)
        self.mPlus.grid(column=5, row=10, columnspan=4, sticky=E)

        numofdice.grid(column=5, row=9,sticky=W)
        polyhedral.grid(column=5, row=9)
        damageplus.grid(column=5, row=9, sticky=E)

        self.text.grid(column = 0, row=11, columnspan = 10, rowspan=10, sticky = EW, ipadx=15, pady = 15)

    #Functions

    def RollAttack1(self):

        if(self.pc1AC.get()):
            if(self.bonus1.get()):
                modifier = self.bonus1.get()
                modifier = int(modifier)
                dieTotal=0
                dieRoll = randint(1,20)
                dieTotal = dieTotal + dieRoll
                result = dieTotal + modifier
                stringResult= ""
                stringResult = stringResult + "Unmodified Roll=" + str(dieRoll) + "\n" + "\n" + "Modified Roll=" + str(result) + '\n' + '\n'
                if result >= int(self.pc1AC.get()):
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack hits!' + '\n')
                    self.text.config(state=DISABLED)
                    if (self.pc1HP.get()):
                        if (self.numDice.get()):
                            if (self.diceType.get()):
                                if (self.mPlus.get()):
                                    diceNumber = self.numDice.get()
                                    modifier = self.mPlus.get()
                                    if (diceNumber.isdigit()):
                                        modifier = int(modifier)
                                        diceNumber = int(diceNumber)
                                        dType = self.diceType.get()
                                        if (dType):
                                            dice = 0
                                            diceTotal = 0
                                            dType = int(dType)
                                            stringResult = ''
                                            for dice in range(0, diceNumber):
                                                diceRoll = randint(1, dType)
                                                diceTotal = diceTotal + diceRoll
                                                damageDone = diceTotal + modifier
                                                HP = self.pc1HP.get()
                                                HP = int(HP)
                                                damageDone = int(damageDone)
                                                remainingHP = HP - damageDone
                                                self.pc1HP.delete(0, END)
                                                self.pc1HP.insert(0, remainingHP)
                                            self.text.config(state=NORMAL)
                                            self.text.insert(INSERT, stringResult + "Damage done is " + str(damageDone) + '\n')
                                            self.text.insert(INSERT, stringResult + "Reduced Player 1's HP")
                                            self.text.config(state=DISABLED)
                                else:
                                    showerror('Error', 'Please insert a damage bonus')
                            else:
                                showerror('Error', 'Please specify which damage dice to roll')
                        else:
                            showerror('Error', 'Please specify the number of damage dice to roll')
                    else:
                        showerror('Error', 'Please insert an HP value for Player1!')
                else:
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack misses!')
                    self.text.config(state=DISABLED)
            else:
                showerror('Error', 'Please insert the Hit Modifier!')
        else:
            showerror('Error', 'Please insert an AC value for PC1!')

    def RollAttack2(self):

        if(self.pc2AC.get()):
            if(self.bonus1.get()):
                modifier = self.bonus1.get()
                modifier = int(modifier)
                dieTotal=0
                dieRoll = randint(1,20)
                dieTotal = dieTotal + dieRoll
                result = dieTotal + modifier
                stringResult= ""
                stringResult = stringResult + "Unmodified Roll=" + str(dieRoll) + "\n" + "\n" + "Modified Roll=" + str(result) + '\n' + '\n'
                if result >= int(self.pc2AC.get()):
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack hits!' + '\n')
                    self.text.config(state=DISABLED)
                    if (self.pc2HP.get()):
                        if (self.numDice.get()):
                            if (self.diceType.get()):
                                if (self.mPlus.get()):
                                    diceNumber = self.numDice.get()
                                    modifier = self.mPlus.get()
                                    if (diceNumber.isdigit()):
                                        modifier = int(modifier)
                                        diceNumber = int(diceNumber)
                                        dType = self.diceType.get()
                                        if (dType):
                                            dice = 0
                                            diceTotal = 0
                                            dType = int(dType)
                                            stringResult = ''
                                            for dice in range(0, diceNumber):
                                                diceRoll = randint(1, dType)
                                                diceTotal = diceTotal + diceRoll
                                                damageDone = diceTotal + modifier
                                                HP = self.pc2HP.get()
                                                HP = int(HP)
                                                damageDone = int(damageDone)
                                                remainingHP = HP - damageDone
                                                self.pc2HP.delete(0, END)
                                                self.pc2HP.insert(0, remainingHP)
                                            self.text.config(state=NORMAL)
                                            self.text.insert(INSERT, stringResult + "Damage done is " + str(damageDone) + '\n')
                                            self.text.insert(INSERT, stringResult + "Reduced Player 2's HP")
                                            self.text.config(state=DISABLED)
                                else:
                                    showerror('Error', 'Please insert a damage bonus')
                            else:
                                showerror('Error', 'Please specify which damage dice to roll')
                        else:
                            showerror('Error', 'Please specify the number of damage dice to roll')
                    else:
                        showerror('Error', 'Please insert an HP value for Player2!')
                else:
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack misses!')
                    self.text.config(state=DISABLED)
            else:
                showerror('Error', 'Please insert the Hit Modifier!')
        else:
            showerror('Error', 'Please insert an AC value for PC2!')

    def RollAttack3(self):

        if(self.pc3AC.get()):
            if(self.bonus1.get()):
                modifier = self.bonus1.get()
                modifier = int(modifier)
                dieTotal=0
                dieRoll = randint(1,20)
                dieTotal = dieTotal + dieRoll
                result = dieTotal + modifier
                stringResult= ""
                stringResult = stringResult + "Unmodified Roll=" + str(dieRoll) + "\n" + "\n" + "Modified Roll=" + str(result) + '\n' + '\n'
                if result >= int(self.pc3AC.get()):
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack hits!' + '\n')
                    self.text.config(state=DISABLED)
                    if (self.pc3HP.get()):
                        if (self.numDice.get()):
                            if (self.diceType.get()):
                                if (self.mPlus.get()):
                                    diceNumber = self.numDice.get()
                                    modifier = self.mPlus.get()
                                    if (diceNumber.isdigit()):
                                        modifier = int(modifier)
                                        diceNumber = int(diceNumber)
                                        dType = self.diceType.get()
                                        if (dType):
                                            dice = 0
                                            diceTotal = 0
                                            dType = int(dType)
                                            stringResult = ''
                                            for dice in range(0, diceNumber):
                                                diceRoll = randint(1, dType)
                                                diceTotal = diceTotal + diceRoll
                                                damageDone = diceTotal + modifier
                                                HP = self.pc3HP.get()
                                                HP = int(HP)
                                                damageDone = int(damageDone)
                                                remainingHP = HP - damageDone
                                                self.pc3HP.delete(0, END)
                                                self.pc3HP.insert(0, remainingHP)
                                            self.text.config(state=NORMAL)
                                            self.text.insert(INSERT, stringResult + "Damage done is " + str(damageDone) + '\n')
                                            self.text.insert(INSERT, stringResult + "Reduced Player 3's HP")
                                            self.text.config(state=DISABLED)
                                else:
                                    showerror('Error', 'Please insert a damage bonus')
                            else:
                                showerror('Error', 'Please specify which damage dice to roll')
                        else:
                            showerror('Error', 'Please specify the number of damage dice to roll')
                    else:
                        showerror('Error', 'Please insert an HP value for Player3!')
                else:
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack misses!')
                    self.text.config(state=DISABLED)
            else:
                showerror('Error', 'Please insert the Hit Modifier!')
        else:
            showerror('Error', 'Please insert an AC value for PC3!')

    def RollAttack4(self):

        if(self.pc4AC.get()):
            if(self.bonus1.get()):
                modifier = self.bonus1.get()
                modifier = int(modifier)
                dieTotal=0
                dieRoll = randint(1,20)
                dieTotal = dieTotal + dieRoll
                result = dieTotal + modifier
                stringResult= ""
                stringResult = stringResult + "Unmodified Roll=" + str(dieRoll) + "\n" + "\n" + "Modified Roll=" + str(result) + '\n' + '\n'
                if result >= int(self.pc4AC.get()):
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack hits!' + '\n')
                    self.text.config(state=DISABLED)
                    if (self.pc4HP.get()):
                        if (self.numDice.get()):
                            if (self.diceType.get()):
                                if (self.mPlus.get()):
                                    diceNumber = self.numDice.get()
                                    modifier = self.mPlus.get()
                                    if (diceNumber.isdigit()):
                                        modifier = int(modifier)
                                        diceNumber = int(diceNumber)
                                        dType = self.diceType.get()
                                        if (dType):
                                            dice = 0
                                            diceTotal = 0
                                            dType = int(dType)
                                            stringResult = ''
                                            for dice in range(0, diceNumber):
                                                diceRoll = randint(1, dType)
                                                diceTotal = diceTotal + diceRoll
                                                damageDone = diceTotal + modifier
                                                HP = self.pc4HP.get()
                                                HP = int(HP)
                                                damageDone = int(damageDone)
                                                remainingHP = HP - damageDone
                                                self.pc4HP.delete(0, END)
                                                self.pc4HP.insert(0, remainingHP)
                                            self.text.config(state=NORMAL)
                                            self.text.insert(INSERT, stringResult + "Damage done is " + str(damageDone) + '\n')
                                            self.text.insert(INSERT, stringResult + "Reduced Player 4's HP")
                                            self.text.config(state=DISABLED)
                                else:
                                    showerror('Error', 'Please insert a damage bonus')
                            else:
                                showerror('Error', 'Please specify which damage dice to roll')
                        else:
                            showerror('Error', 'Please specify the number of damage dice to roll')
                    else:
                        showerror('Error', 'Please insert an HP value for Player4!')
                else:
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack misses!')
                    self.text.config(state=DISABLED)
            else:
                showerror('Error', 'Please insert the Hit Modifier!')
        else:
            showerror('Error', 'Please insert an AC value for PC4!')

    def RollAttack5(self):

        if(self.pc5AC.get()):
            if(self.bonus1.get()):
                modifier = self.bonus1.get()
                modifier = int(modifier)
                dieTotal=0
                dieRoll = randint(1,20)
                dieTotal = dieTotal + dieRoll
                result = dieTotal + modifier
                stringResult= ""
                stringResult = stringResult + "Unmodified Roll=" + str(dieRoll) + "\n" + "\n" + "Modified Roll=" + str(result) + '\n' + '\n'
                if result >= int(self.pc5AC.get()):
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack hits!' + '\n')
                    self.text.config(state=DISABLED)
                    if (self.pc5HP.get()):
                        if (self.numDice.get()):
                            if (self.diceType.get()):
                                if (self.mPlus.get()):
                                    diceNumber = self.numDice.get()
                                    modifier = self.mPlus.get()
                                    if (diceNumber.isdigit()):
                                        modifier = int(modifier)
                                        diceNumber = int(diceNumber)
                                        dType = self.diceType.get()
                                        if (dType):
                                            dice = 0
                                            diceTotal = 0
                                            dType = int(dType)
                                            stringResult = ''
                                            for dice in range(0, diceNumber):
                                                diceRoll = randint(1, dType)
                                                diceTotal = diceTotal + diceRoll
                                                damageDone = diceTotal + modifier
                                                HP = self.pc5HP.get()
                                                HP = int(HP)
                                                damageDone = int(damageDone)
                                                remainingHP = HP - damageDone
                                                self.pc5HP.delete(0, END)
                                                self.pc5HP.insert(0, remainingHP)
                                            self.text.config(state=NORMAL)
                                            self.text.insert(INSERT, stringResult + "Damage done is " + str(damageDone) + '\n')
                                            self.text.insert(INSERT, stringResult + "Reduced Player 5's HP")
                                            self.text.config(state=DISABLED)
                                else:
                                    showerror('Error', 'Please insert a damage bonus')
                            else:
                                showerror('Error', 'Please specify which damage dice to roll')
                        else:
                            showerror('Error', 'Please specify the number of damage dice to roll')
                    else:
                        showerror('Error', 'Please insert an HP value for Player5!')
                else:
                    self.text.config(state=NORMAL)
                    self.text.delete(1.0, END)
                    self.text.insert(INSERT, stringResult + 'Attack misses!')
                    self.text.config(state=DISABLED)
            else:
                showerror('Error', 'Please insert the Hit Modifier!')
        else:
            showerror('Error', 'Please insert an AC value for PC5!')
