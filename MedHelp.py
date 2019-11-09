import json, os
from tkinter import *

os.system('clear')

class MedManager:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x500')

        self.windowCanvas = Canvas(self.root, bg='#292947')
        self.windowCanvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.addMedBtn = Button(self.root, text = 'Add Medication', bg = '#292947', fg = 'white', command = self.addMed)
        self.addMedBtn.place(relx = 0, rely = 0, relwidth = 1.0, relheight = 0.1)

    def addMed(self):
        addMedRoot = Tk()

        addMedCanvas = Canvas(addMedRoot, bg = '#292947')
        addMedCanvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        addBtn = Button(addMedCanvas, text = 'Add', bg = '#292957', fg = 'white', command = self.saveMed)
        addBtn.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)

        
        medNameTitle = Label(addMedCanvas, text = 'Name: ', bg = '#292947', fg = 'white', justify=LEFT)
        medNameTitle.place(relx = 0, rely = 0.1, relwidth = 0.4, relheight = 0.1)

        self.medNameEnt = Entry(addMedCanvas)
        self.medNameEnt.place(relx = 0.4, rely = 0.1, relwidth = 0.6, relheight = 0.1)
        

        
        medAmountTitle = Label(addMedCanvas, text = 'Amount: ', bg = '#292947', fg = 'white', justify=LEFT)
        medAmountTitle.place(relx = 0, rely = 0.2, relwidth = 0.4, relheight = 0.1)

        self.medAmountEnt = Entry(addMedCanvas)
        self.medAmountEnt.place(relx = 0.4, rely = 0.2, relwidth = 0.6, relheight = 0.1)

        

        medFrequencyTitle = Label(addMedCanvas, text = 'Frequency: ', bg = '#292947', fg = 'white', justify=LEFT)
        medFrequencyTitle.place(relx = 0, rely = 0.3, relwidth = 0.4, relheight = 0.1)

        self.medFrequencyEnt = Entry(addMedCanvas)
        self.medFrequencyEnt.place(relx = 0.4, rely = 0.3, relwidth = 0.6, relheight = 0.1)


        
        medOtherTitle = Label(addMedCanvas, text = 'Other: ', bg = '#292947', fg = 'white', justify=LEFT)
        medOtherTitle.place(relx = 0, rely = 0.4, relwidth = 0.4, relheight = 0.1)

        self.medOtherEnt = Entry(addMedCanvas)
        self.medOtherEnt.place(relx = 0.4, rely = 0.4, relwidth = 0.6, relheight = 0.1)
        
        
        addMedRoot.mainloop()

    def saveMed(self):
        with open('Medications.json', 'r') as medFile:
            medFile = medFile.read()
            medFile = json.loads(medFile)

            print(self.medNameEnt.get())
            print(self.medAmountEnt.get())
            print(self.medFrequencyEnt.get())
            print(self.medOtherEnt.get())
            
            medFile[self.medNameEnt.get()] = {
                "Amount": self.medAmountEnt.get(),
                "Frequency": self.medFrequencyEnt.get(),
                "Other": self.medOtherEnt.get()        
            }
            
            with open('Medications.json', 'w') as medSaveFile:
                medSaveFile.write(json.dumps(medFile))
            

    def start(self):
        self.root.mainloop()

userMM = MedManager()
userMM.start()

