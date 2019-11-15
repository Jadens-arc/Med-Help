import json, os
from tkinter import *

os.system('clear')

class MedManager:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x500')
        self.root.title('Med Help')

        self.windowCanvas = Canvas(self.root, bg='#292947')
        self.windowCanvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.addMedBtn = Button(self.windowCanvas, text = 'Add Medication', bg = '#292947', fg = 'white', command = self.addMed)
        self.addMedBtn.place(relx = 0, rely = 0, relwidth = 0.7, relheight = 0.1)

        self.deleteMedBtn = Button(self.windowCanvas, text = 'Delete', bg = '#292947', fg = 'white', command = self.deleteMed)
        self.deleteMedBtn.place(relx = 0.7,rely = 0, relwidth = 0.3, relheight = 0.1)

        self.medText = Text(self.windowCanvas, bg = '#292947', fg = 'white', wrap = WORD)
        
        self.rewritePage()

        self.medText.config(state = DISABLED)
        self.medText.place(relx = 0, rely = 0.1, relwidth = 1.0, relheight = 0.9)
        
    def rewritePage(self):
        self.medText.config(state = NORMAL)
        self.medText.delete(1.0, END)
        with open('Medications.json') as medFile:
            medFile = json.loads(medFile.read())
            for key in medFile:
                self.medText.insert(INSERT, str(key) + '\n')
                for medKey in medFile[key]:
                    self.medText.insert(INSERT, '    ' + str(medFile[key][medKey]) + '\n')
        self.medText.config(state = DISABLED)

    def deleteMed(self):
        deleteMedRoot = Tk()
        deleteMedRoot.title('Delete Medication')

        deleteMedCanvas = Canvas(deleteMedRoot, bg = '#292947')
        deleteMedCanvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        deleteMedTitle = Label(deleteMedRoot, bg = '#292947', fg = 'white', text = 'Name of Medication')
        deleteMedTitle.pack()

        self.deleteMedEnt = Entry(deleteMedRoot)
        self.deleteMedEnt.pack()

        def deleteUserMed():
            selectedMed = self.deleteMedEnt.get()
            print(selectedMed)
            with open('Medications.json', 'r') as medFile:
                medFile = medFile.read()
                medFile = json.loads(medFile)
                medFile.pop(selectedMed)
                with open('Medications.json', 'w') as medSaveFile:
                    medSaveFile.write(json.dumps(medFile))
            self.rewritePage()

        deleteMedBtn = Button(deleteMedRoot, bg = '#ff0000', fg = 'white', text = 'Delete', command = deleteUserMed)
        deleteMedBtn.pack()

        deleteMedRoot.mainloop()

    def addMed(self):
        addMedRoot = Tk()
        addMedRoot.title('Add Med')

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



        medUseTitle = Label(addMedCanvas, text = 'Use:', bg = '#292947', fg = 'white', justify=LEFT)
        medUseTitle.place(relx = 0, rely = 0.4, relwidth = 0.4, relheight = 0.1)

        self.medUseEnt = Entry(addMedCanvas)
        self.medUseEnt.place(relx = 0.4, rely = 0.4, relwidth = 0.6, relheight = 0.1)


        
        medOtherTitle = Label(addMedCanvas, text = 'Other: ', bg = '#292947', fg = 'white', justify=LEFT)
        medOtherTitle.place(relx = 0, rely = 0.5, relwidth = 0.4, relheight = 0.1)

        self.medOtherEnt = Entry(addMedCanvas)
        self.medOtherEnt.place(relx = 0.4, rely = 0.5, relwidth = 0.6, relheight = 0.1)
        
        
        addMedRoot.mainloop()

    def saveMed(self):
        with open('Medications.json', 'r') as medFile:
            medFile = medFile.read()
            medFile = json.loads(medFile)

            print(self.medNameEnt.get())
            print(self.medAmountEnt.get())
            print(self.medFrequencyEnt.get())
            print(self.medUseEnt.get())
            print(self.medOtherEnt.get())
            
            medFile[self.medNameEnt.get()] = {
                "Amount": self.medAmountEnt.get(),
                "Frequency": self.medFrequencyEnt.get(),
                "Use": self.medUseEnt.get(),
                "Other": self.medOtherEnt.get()
            }
            
            with open('Medications.json', 'w') as medSaveFile:
                medSaveFile.write(json.dumps(medFile))

            self.rewritePage()
            

    def start(self):
        self.root.mainloop()

userMM = MedManager()
userMM.start()

