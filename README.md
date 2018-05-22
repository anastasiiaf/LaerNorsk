# LaereNorsk
This app helps me to learn norwegian :) (works but still under construction)

This application is written in Python, interface is done via Tkinter library

1. Run gui.py 
2. Application will start with a "greeting" picture of fjords and will play a national anthem of Norway 
3. Click somewhere in this picture - main working window will appear
4. In the main window you will see three tabs: Learn, Quiz and Write

In each tab you need to choose a category in a drop list. Program will select randomly 25 words from a particular category.
At the same time, program keeps a track of which words you have seen during one game, so each 25 randomly selected words have no 
repetition (this is true for all 3 tabs). In the upper right corner you will see how many words are left in this category. 
Categories: "verbs", "adj" (adjectives), "adv" (adverbs), "pron_prep" (prepositions, pronouns), "nouns" (general), "house" (nouns),
"food" (nouns), "city" (nouns), "world" (nouns), "body" (nouns), "animals" (nouns), "people" (nouns).

 Tab Learn: 
    Created for learning/repeating words. 
    Below there are norwegian word, english translation and in the comments row there are either forms of verbs or plural/singular
    noun/adjective forms.
    Navigate via buttons Next and Previous. Button Continue will select next 25 words from this category. 
    Button Quit will exit the program.
    
 Tab Quiz:
   Choose a category in drop list and the language of quiz: "Norwegian -> English" means that a word in question will be in norwegian, 
   while 4 choices (where one is correct) will be in english, and "English -> Norwegian" is the other way around. So in this quiz you
   have to find a correct translation.  
   If you click on the question field, it will turn red and show the right answer. If you select a correct answer among 4 choices,
   its background color will turn green. If your answer is not correct, its field will turn red and the background color of correct 
   answer will turn green. At the end, a message box will show how many questions out of 25 were answered.
   Navigate via a button Next. Button Continue will select next 25 words from this category. Button Quit will exit the program.
   
 Tab Write:
   Created for checking the verbs spelling. Again select a category (which is only verbs). In the upper right corner you will see 
   how many words are left in this category. 
   Below you will see a verb in english. Your task is to translate it to norwegian and write its forms in the corresponding fields:
   indefinite, present, preteritum and perfectum. Button Check is checking your spelling and to the right from the corresponding fields 
   you will see correct answers.  
   Navigate via button Next. Button Continue will select next 25 words from this category. Button Quit will exit the program.
   
