# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 22:56:53 2018

@author: Anastasiia
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pygame import mixer
import pandas as pd
import numpy as np
import random
import csv
import os
import re

class WindowMain(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)             
        self.master = master 
        self.master.iconbitmap('owl.ico')
        self.init_window()
        
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Lære Norsk")
         
        mixer.init()
        mixer.music.load('anthem.mp3')
        mixer.music.play()
        
        imgPath = "norway.png"
        background_image = PhotoImage(file=imgPath)
        background_label = ttk.Label(self, image=background_image)
        #background_label.place(x=50, y=50, relwidth=10, relheight=10)
        background_label.image = background_image
        background_label.bind("<Button-1>", self.showWindow)
        background_label.pack(side=TOP,fill=BOTH, expand=YES)
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=YES) 
        
        
    def showWindow(self, event):
        mixer.music.stop()
        self.newWindow = Toplevel(self.master)
        self.newWindow.geometry("450x300+400+150")
        self.app = Window(self.newWindow)
        #self.master.deiconify()
        self.master.withdraw()
        #root.tkraise()


        
        

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)               
        self.master = master
        self.master.iconbitmap('owl.ico')
        self.tabs = ttk.Notebook(self)
        self.num_words = 25
        self.dict = list()
        
        self.question_quiz = StringVar()
        self.choiceA = StringVar()
        self.choiceB = StringVar()
        self.choiceC = StringVar()
        self.choiceD = StringVar()
        self.lib_name = StringVar()
        self.combo_choice_quiz = StringVar()

        self.i = IntVar()
        self.correct_answer = ""
        self.score = 0
        
        self.page1 = Frame(self.tabs)
        self.page2 = Frame(self.tabs)
        self.page3 = Frame(self.tabs)
        
        self.tabs.add(self.page1, text='Learn')
        self.tabs.add(self.page2, text='Quiz')
        self.tabs.add(self.page3, text='Write')
        self.tabs.bind("<Button-1>", self.set_words_used)
        self.tabs.pack(expand=1, fill="both")
        
        self.words_used = list()
        self.words_left = StringVar()
        
        #FlashCards
        self.norsk = StringVar()
        self.english = StringVar()
        self.details = StringVar()
        self.combo_choice_card = StringVar()
        self.i_card = IntVar()
        self.labelNorsk = ttk.Label(self.page1, textvariable = self.norsk,  font = "Times 14 bold", padding=15, width = 30)
        self.labelNorsk.grid(column=1, row=2, stick=W, columnspan=2)
        self.labelEnglish = ttk.Label(self.page1, textvariable = self.english,  font = "Times 14", padding=15, width = 30, wraplength=300, justify=LEFT)
        self.labelEnglish.grid(column=1, row=3, stick=W, columnspan=2, rowspan=1)
        self.labelDetails = ttk.Label(self.page1, textvariable = self.details,  font = "Times 14", padding=15, width = 35, wraplength=300, justify=LEFT)
        self.labelDetails.grid(column=1, row=4, stick=W, columnspan=3, rowspan=2)
        
        #Quiz
        self.EngNor = StringVar()
        self.labelQ = ttk.Label(self.page2, textvariable = self.question_quiz,  font = "Times 14 bold", padding=15, width=25, anchor= CENTER)
        self.labelQ.grid(column=0, row=2, columnspan=6)
        self.answered = False
        
        self.labelA = ttk.Label(self.page2, textvariable = self.choiceA, font = "Times 14", padding=15, width=21, anchor=CENTER)
        self.labelA.grid(column=0, row=3, stick=W, columnspan=2)
        self.labelA.bind("<Button-1>", lambda event:self.check(event,0))
        self.labelB = ttk.Label(self.page2, textvariable = self.choiceB,  font = "Times 14", padding=15, width=20, anchor=CENTER)
        self.labelB.grid(column=1, row=3, stick=E, columnspan=2)
        self.labelB.bind("<Button-1>", lambda event: self.check(event,1))
        self.labelC = ttk.Label(self.page2, textvariable = self.choiceC,  font = "Times 14", padding=15, width=21, anchor=CENTER)
        self.labelC.grid(column=0, row=4, stick=W, columnspan=2)
        self.labelC.bind("<Button-1>", lambda event: self.check(event,2))
        self.labelD = ttk.Label(self.page2, textvariable = self.choiceD,  font = "Times 14", padding=15, width=20, anchor=CENTER)
        self.labelD.grid(column=1, row=4, stick=E,columnspan=2)
        self.labelD.bind("<Button-1>", lambda event: self.check(event,3))

        
        #Write
        self.question_write = StringVar()
        self.infinitive = StringVar()
        self.present = StringVar()
        self.preteritum = StringVar()
        self.perfect = StringVar()

        self.answ_infinitive = StringVar()
        self.answ_present = StringVar()
        self.answ_preteritum = StringVar()
        self.answ_perfect = StringVar()
       
        
        
        style = ttk.Style()
        style.configure("Red.TLabel", background="red") 
        style.configure("Green.TLabel", background="green") 
             
        self.init_window()

        
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Lære Norsk")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=YES)
        
        self.labelCaption = ttk.Label(self.page1, text= "Category:",  font = "Times 12", padding=10, width=10).grid(column=0, row=0)
        listBox_card = ttk.Combobox(self.page1, textvariable=self.combo_choice_card, values = ['verbs', 'adj', 'adv','pron_prep', 'nouns', 'house','food', 'city','world', 'body',  'animals', 'people'])
        listBox_card.grid(column=1, row=0, stick=W)
        listBox_card.bind("<<ComboboxSelected>>", self.FlashCards)
        
        
        
        self.labelChoice = ttk.Label(self.page2, textvariable=self.EngNor,  font = "Times 12", padding=10, width=20)
        self.labelChoice.grid(column=0, row=0)
        self.EngNor.set("Norwegian -> English")
        self.labelChoice.bind("<Button-1>", self.LangDir)
        listBox_quiz = ttk.Combobox(self.page2, textvariable=self.combo_choice_quiz, values = ['verbs', 'adj', 'adv','pron_prep', 'nouns', 'house','food', 'city','world', 'body',  'animals', 'people'])
        listBox_quiz.grid(column=1, row=0, stick=W)
        listBox_quiz.bind("<<ComboboxSelected>>", self.Quiz)
        
        
        self.labelCaption2 = ttk.Label(self.page3, text= "Category:",  font = "Times 12", padding=10, width=10).grid(column=0, row=0)
        listBox_card2 = ttk.Combobox(self.page3, textvariable=self.combo_choice_card, values = ['verbs'])
        listBox_card2.grid(column=1, row=0, stick=W)
        listBox_card2.bind("<<ComboboxSelected>>", self.Write)
        
        

    def FlashCards(self, event): 
        self.labelWords_left1 = ttk.Label(self.page1, textvariable = self.words_left,  font = "Times 14 bold", width=10, foreground='green').grid(column=2, row=0)
        labelNorsk = ttk.Label(self.page1, text="nowegian:", font = "Times 12", padding=15).grid(column=0, row=2, stick=E)
        labelEnglish = ttk.Label(self.page1, text="english:", font = "Times 12", padding=15).grid(column=0, row=3, stick=E)
        labelDetails = ttk.Label(self.page1, text="comment:", font = "Times 12",  padding=15).grid(column=0, row=4, stick=E)
        quitButton = ttk.Button(self.page1, text="Quit",command=root.destroy)
        quitButton.place(relx=0.05, rely=1.0, anchor=SW) #grid(column=0, row=7, rowspan=2, anchor=S)
        file = self.combo_choice_card.get() +'.csv'
        dictionary = self.openLibrary(file)
        

        if self.dict:
            if self.dict[-1]!=self.combo_choice_card.get():
                self.words_used = list()
                self.words_left.set('')
        self.dict.append(self.combo_choice_card.get())
       
        game = self.Game(dictionary)
        # norwegian-english
        game = np.array(game)
        # eng 1, norw 0
        english_correct = game[:, 1]
        norwegian = game[:, 0]
        self.words_used = list(self.words_used) + list(norwegian)
        #print("GAME", norwegian)
        #print("USED", self.words_used)

        comment = game[:, 2]
        self.i_card.set(-1)
        self.nextCard(norwegian, english_correct, comment)
        nextcardButton = ttk.Button(self.page1, text="Next",command=lambda: self.nextCard(norwegian, english_correct, comment))
        nextcardButton.place(relx=0.6, rely=1.0, anchor=SW)#.grid(column=1, row=7, columnspan=4)
        previouscardButton = ttk.Button(self.page1, text="Previous",command=lambda: self.previousCard(norwegian, english_correct, comment))
        previouscardButton.place(relx=0.4, rely=1.0, anchor=SW)#.grid(column=0, row=7, columnspan=2)
        
        continueButton_cards = ttk.Button(self.page1, text="Continue")
        continueButton_cards.bind("<Button-1>", self.FlashCards)
        continueButton_cards.place(relx=0.8, rely=1.0, anchor=SW)

      
    def nextCard(self, norwegian, english_correct, comment):  
        i = self.i_card.get()
        if i<self.num_words-1:
            self.i_card.set(i+1)
            self.norsk.set(norwegian[self.i_card.get()])
            self.english.set(english_correct[self.i_card.get()])
            self.details.set(comment[self.i_card.get()])
        
            
    def previousCard(self, norwegian, english_correct, comment): 
        i = self.i_card.get()
        if i>0:
            self.i_card.set(i-1)
            self.norsk.set(norwegian[self.i_card.get()])
            self.english.set(english_correct[self.i_card.get()])
            self.details.set(comment[self.i_card.get()])

            
        
        
    def Quiz(self, event):
        self.labelWords_left2 = ttk.Label(self.page2, textvariable = self.words_left,  font = "Times 14 bold", width=10, foreground='green', anchor=E).grid(column=2, row=0)
        
        self.score = 0
        quitButton = ttk.Button(self.page2, text="Quit",command=root.destroy)
        quitButton.place(relx=0.2, rely=1.0, anchor=SW) #.grid(column=0, row=7)
        file = self.combo_choice_quiz.get() +'.csv'
        dictionary = self.openLibrary(file)
        
        if self.dict:
            if self.dict[-1]!=self.combo_choice_quiz.get():
                self.words_used = list()
                self.words_left.set('')
        self.dict.append(self.combo_choice_quiz.get())
        
        game = self.Game(dictionary)

        game = np.array(game)
        direction = self.EngNor.get()
        if direction=="Norwegian -> English":
            # norwegian-english
            english_correct = game[:, 1]
            norwegian = game[:, 0]
            comment = game[:, 2]
            english_choices = [dictionary[i][1] for i in list(dictionary.keys())] 
            self.words_used = list(self.words_used) + list(norwegian)
            #print("GAME", norwegian)
            #print("USED", self.words_used)
        else:
            # english-norwegian
            english_correct = game[:, 0]
            norwegian = game[:, 1]
            comment = game[:, 2]
            english_choices = [dictionary[i][0] for i in list(dictionary.keys())] 
            # because of this line - while dictionary[d] in game or str(dictionary[d][0]) in p:
            # in words_used list norwegian tranlation should be added
            self.words_used = list(self.words_used) + list(english_correct)
            #print("GAME", english_correct)
            #print("USED", self.words_used)
        
        self.i.set(-1)
        
        self.nextQ(norwegian, english_correct, english_choices)
        
        nextQButton = ttk.Button(self.page2, text="Next",command=lambda: self.nextQ(norwegian, english_correct, english_choices))
        nextQButton.place(relx=0.6, rely=1.0, anchor=SW) #.grid(column=1, row=7)
        self.labelQ.bind("<Button-1>", lambda event: self.AnswerQuiz(event, english_correct, comment))
        
        continueButton_quiz = ttk.Button(self.page2, text="Continue")
        continueButton_quiz.place(relx=0.8, rely=1.0, anchor=SW)
        continueButton_quiz.bind("<Button-1>", self.Quiz)

    def Write(self, event):
        self.labelWords_left3 = ttk.Label(self.page3, textvariable = self.words_left,  font = "Times 14 bold", width=10, foreground='green').grid(column=3, row=0)
        self.labelQ_write = ttk.Label(self.page3, textvariable=self.question_write, font = "Times 14 bold", padding=15, width=25, anchor=CENTER)
        self.labelQ_write.grid(column=1, row=2, stick=W, columnspan=6)
        labelIndef = ttk.Label(self.page3, text="indefinite:", font = "Times 12", padding=5).grid(column=0, row=3, stick=E)
        labelPres = ttk.Label(self.page3, text="present:", font = "Times 12", padding=5).grid(column=0, row=4, stick=E)
        labelPret = ttk.Label(self.page3, text="preteritum:", font = "Times 12",  padding=5).grid(column=0, row=5, stick=E)
        labelPerf = ttk.Label(self.page3, text="perfectum:", font = "Times 12",  padding=5).grid(column=0, row=6, stick=E)
        
        self.entryInfinitive = Entry(self.page3, textvariable = self.infinitive,  font = "Times 14 bold",  width = 20, justify=LEFT)
        self.entryInfinitive.grid(column=1, row=3, stick=W, columnspan=2, rowspan=1)
        self.entryPresent = Entry(self.page3, textvariable = self.present,  font = "Times 14 bold",  width = 20, justify=LEFT)
        self.entryPresent.grid(column=1, row=4, stick=W, columnspan=2, rowspan=1)
        self.entryPreteritum = Entry(self.page3, textvariable = self.preteritum, font = "Times 14 bold",  width = 20, justify=LEFT)
        self.entryPreteritum.grid(column=1, row=5, stick=W, columnspan=2, rowspan=1)
        self.entryPerfect = Entry(self.page3, textvariable = self.perfect,  font = "Times 14 bold",  width = 20, justify=LEFT)
        self.entryPerfect.grid(column=1, row=6, stick=W, columnspan=2, rowspan=1)  
        
        
        labelIndef_answ = ttk.Label(self.page3, textvariable=self.answ_infinitive, font = "Times 12", padding=5, width=20, anchor=W).grid(column=3, row=3, columnspan=1, stick=W)
        labelPres_answ = ttk.Label(self.page3, textvariable=self.answ_present, font = "Times 12", padding=5, width=20, anchor=W).grid(column=3, row=4, columnspan=1,stick=W)
        labelPret_answ = ttk.Label(self.page3, textvariable=self.answ_preteritum, font = "Times 12",  padding=5, width=20, anchor=W).grid(column=3, row=5, columnspan=1, stick=W)
        labelPerf_answ = ttk.Label(self.page3, textvariable=self.answ_perfect, font = "Times 12",  padding=5, width=20, anchor=W).grid(column=3, row=6, columnspan=1, stick=W)
         
        
        
        
        file = self.combo_choice_card.get() +'.csv'
        dictionary = self.openLibrary(file)
        #print(dictionary)
        game = self.Game(dictionary)
        game = np.array(game)
        english_correct = game[:, 1]
        norwegian = game[:, 0]
        self.words_used = list(self.words_used) + list(norwegian)
        #print("GAME", norwegian)
        #print("USED", self.words_used)
        comment = game[:, 2]

        self.i.set(-1)
        self.nextSpell(english_correct)
        nextButton = ttk.Button(self.page3, text="Next",command=lambda: self.nextSpell(english_correct))
        nextButton.place(relx=0.6, rely=1.0, anchor=SW)
        checkButton = ttk.Button(self.page3, text="Check",command=lambda: self.CheckSpellingVerbs(norwegian, english_correct, comment))
        checkButton.place(relx=0.4, rely=1.0, anchor=SW)
        quitButton = ttk.Button(self.page3, text="Quit",command=root.destroy)
        quitButton.place(relx=0.05, rely=1.0, anchor=SW)
        self.labelQ_write.bind("<Button-1>", lambda event: self.AnswerWriting(event, norwegian, comment))
        
        continueButton_write = ttk.Button(self.page3, text="Continue")
        continueButton_write.place(relx=0.8, rely=1.0, anchor=SW)
        continueButton_write.bind("<Button-1>", self.Write)

    def CheckSpellingVerbs(self, norwegian, english_correct, comment):
        i = self.i.get()
        wordList = re.sub("[^\w-]", " ",  comment[i]).split()
        ind = [i for i,val in enumerate(wordList) if val=='-']
        pres = wordList[:ind[0]]
        pret = wordList[ind[0]+1:ind[1]]
        perf = wordList[ind[1]+1:]
        perf.pop(0)
        
        if self.infinitive.get()==norwegian[i]:
            self.entryInfinitive.configure(background="Green")
        else:
            self.entryInfinitive.configure(background="Red")
            
        if self.present.get() in list(pres):
            self.entryPresent.configure(background="Green")
        else:
            self.entryPresent.configure(background="Red")  
            
        if self.preteritum.get() in list(pret):
            self.entryPreteritum.configure(background="Green")
        else:
            self.entryPreteritum.configure(background="Red") 
            
        if self.perfect.get() in list(perf):
            self.entryPerfect.configure(background="Green")
        else:
            self.entryPerfect.configure(background="Red")   
            
        self.answ_infinitive.set(norwegian[i])
        self.answ_present.set(pres)
        self.answ_preteritum.set(pret)
        self.answ_perfect.set(perf)
        
          


    def nextSpell(self, english_correct):
        self.labelQ_write.configure(style="TLabel")
        self.entryInfinitive.configure(background="white")
        self.infinitive.set('')
        self.entryPresent.configure(background="white")
        self.present.set('')
        self.entryPreteritum.configure(background="white")
        self.preteritum.set('')
        self.entryPerfect.configure(background="white")
        self.perfect.set('')
        self.answ_infinitive.set('')
        self.answ_present.set('')
        self.answ_preteritum.set('')
        self.answ_perfect.set('')
        i = self.i.get()
        if i<self.num_words-1:
            self.i.set(i+1)
            self.question_write.set(english_correct[self.i.get()])
        else:
            end = "Your score is " + str(self.score) + " out of " + str(self.num_words)+ "!"
            messagebox.showinfo("Results", end)
            

    def LangDir(self, event):
        a = self.EngNor.get()
        if a == "Norwegian -> English":
           self.EngNor.set("English -> Norwegian") 
           self.words_used = list()
        else:
           self.EngNor.set("Norwegian -> English") 
           self.words_used = list()
           
           
    def set_words_used(self, event):
        self.words_used = list()
        self.words_left.set('')
        self.dict = list()
           

    def check(self, event, num):
        if self.answered == False:
            c = [self.labelA, self.labelB, self.labelC, self.labelD]
            if num == self.correct_answer:
                c[self.correct_answer].configure(style="Green.TLabel")
                self.score +=1
                self.answered = True
            else:
                c[self.correct_answer].configure(style="Green.TLabel")
                c[num].configure(style="Red.TLabel")
           
        

    def allocateQ(self, question, correct, answers, others):
        self.question_quiz.set(question)
        self.choiceA.set(answers[0])
        self.choiceB.set(answers[1])
        self.choiceC.set(answers[2])
        self.choiceD.set(answers[3])
        self.correct_answer = correct
        
      
        
    def nextQ(self, norwegian, english_correct, english_choices):
        self.answered = False
        self.labelQ.configure(style="TLabel")
        self.labelA.configure(style="TLabel")
        self.labelB.configure(style="TLabel")
        self.labelC.configure(style="TLabel")
        self.labelD.configure(style="TLabel")
        g = self.i.get()
        if g<self.num_words-1:
            self.i.set(g+1)
            [question, correct, answers, others] = self.nextWord(self.i.get(), norwegian, english_correct, english_choices)
            #print("QA", question, correct)
            #print("others", answers, others)
            self.allocateQ(question, correct, answers, others)
        else:
            #print("The end")
            end = "Your score is " + str(self.score) + " out of " + str(self.num_words)+ "!"
            messagebox.showinfo("Results", end)
    
        
 
    def AnswerQuiz(self, event, english_correct, comment):
        i = self.i.get()
        self.question_quiz.set(english_correct[i])
        self.labelQ.configure(style="Red.TLabel")
        
        
    def AnswerWriting(self, event, english_correct, comment):
        i = self.i.get()
        self.question_write.set(english_correct[i])
        self.labelQ_write.configure(style="Red.TLabel")    


    def get_library(self, event):
        self.combo_choice.get()
        

    def openLibrary(self, file): 
        #file = str(self.combo_choice.get()+'.csv')

        #print(file)
        df = pd.read_csv(file, na_values=['nan'], keep_default_na=False)
        dictionary = df.set_index('ID').T.to_dict('list')
        return(dictionary)
        
    def Game(self, dictionary):
        #print(len(dictionary) - len(self.words_used))
        
        if len(dictionary) - len(self.words_used) < self.num_words:
            self.words_used = list()
            self.words_left.set('    left '+str(len(dictionary) - self.num_words))
        else:
            self.words_left.set('    left '+str(len(dictionary) - len(self.words_used) - self.num_words))
        p = list(self.words_used)    
        #print("USED", p)
        game = [0 for i in range(0,self.num_words)]
        for j in range(0, self.num_words):
            d =random.choice(list(dictionary.keys())) 
            #print(dictionary[d])
            
            while dictionary[d] in game or str(dictionary[d][0]) in p:
                d =random.choice(list(dictionary.keys()))
                #print(dictionary[d])
            game[j] = dictionary[d]
            #print(j)
                     
        #print(game)
        return(game)
  
        
    def nextWord(self, i, norwegian, english_correct, english_choices):

        question = norwegian[i]
        answers = [0,0,0,0]
        correct = random.choice([0, 1, 2, 3])
        answers[correct] = english_correct[i]
        others = [x for x in [0, 1, 2, 3] if x not in [correct]]
        selected = [answers[correct]]
        for j in range(0,3):
            
            not_selected = [x for x in english_choices if x not in selected]
            #print("not selected", not_selected)
            answers[others[j]] = random.choice(not_selected)
            selected = selected + [answers[others[j]]]
            #print("selected", selected)
    
        
        #print("Question", question)
        #print("Correct", answers[correct], correct)
        #print("Other1", answers[others[0]], others[0])
        #print("Other2", answers[others[1]], others[1])
        #print("Other3", answers[others[2]], others[2])
         
        return(question, correct, answers, others)   
        
        

    def addEntry(self,dictionary, file):
        norwegian_choices = [dictionary[i][0] for i in list(dictionary.keys())]
        new_entry_list = [1,'D','DD','DDD']
        if new_entry_list[1] not in norwegian_choices:
            
            new_entry = pd.DataFrame(new_entry_list).T
            new_entry = new_entry.rename(index=str, columns={0: "ID", 1: "N", 2: "E", 3: "C"})
            #print(new_entry)
            lib_file = open(file,'a')
            new_entry.to_csv(lib_file, header=False, index=False)
            lib_file.close()
        else:
            print("already exists!")

    
                
        
root = Tk()
root.geometry("450x300+400+150")
app = WindowMain(root)
root.mainloop()        
        


