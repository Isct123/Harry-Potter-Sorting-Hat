from tkinter import *					
from tkinter import ttk
import tkinter.font as font
import json
import operator as op
import os

try:
    import pyglet
    from pygame import mixer
except:
    #Installing dependencies
    os.system("py -m pip install pyglet")
    os.system("py -m pip install pygame")
    import pyglet
    from pygame import mixer



pyglet.font.add_file('magic-school.one.ttf')
pyglet.font.add_file('magic-school.two.ttf')
  
# Starting the mixer
def asdf(song, x, volume = 0.5):
    mixer.init()
    
    # Loading the song
    mixer.music.load(song)
    
    # Setting the volume
    mixer.music.set_volume(volume)
    
    # Start playing the song
    if x == 0:
        mixer.music.play()
    else:
        mixer.music.play(-1)

asdf("e.mp3", -1)

with open("question_bank.json") as f:
    data = json.load(f)

gryffindor, hufflepuff, slytherin, ravenclaw = 0, 0, 0, 0 
i=0

root = Tk()
root.title("Computer Science Authentic Task- Harry Potter Sorting Hat")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Home')
tabControl.add(tab2, text ='Quiz')
tabControl.pack(expand = 1, fill ="both")

def begin():
    tabControl.select(tab2)
    
heading = Label(tab1, text = "Authentic Task- Sorting Hat Project", bg='yellow')
heading['font']=font.Font(weight="bold", family="Roboto", size = 35)
heading.grid(row=0, column=0)
done_by = Label(tab1, text = "Done by: Rishikesh, Nihal, Avyay, Bhargav", bg='white')
done_by['font'] = font.Font(family="Roboto", size= 24)
done_by.grid()
start_quiz = Button(tab1, text = "Start Quiz", width=10, height=2, bg="green", command=begin)
start_quiz['font']=font.Font(family='Roboto', size=20)
start_quiz.grid()
exit_quiz = Button(tab1, text = "Exit Quiz", width=10, height=2, bg = "red", command=root.destroy)
exit_quiz['font']=font.Font(family='Roboto', size=20)
exit_quiz.grid()

heading = Label(tab2, text = "SORTING HAT", bg='orange')
heading['font']=font.Font(weight="bold", family="magic school two", size = 35)
heading.grid()

def option_letter(x, l):
    global gryffindor, hufflepuff, slytherin, ravenclaw
    o = l[["a", "b", "c", "d"].index(x)]
    if  o== "h":
        hufflepuff += 1
    elif o == "g":
        gryffindor +=1
    elif o == "s":
        slytherin+=1
    else:
        ravenclaw +=1
    pass

def create_questions(dic):
    for i in dic:
        askQuestion(i, dic[i][0], dic[i][1])

def choose_house():
    global gryffindor, slytherin, hufflepuff, ravenclaw
    g="You are %s%s %s"%(round(gryffindor/11*100, 2), "%", "Gryffindor")
    s="You are %s%s %s"%(round(slytherin/11*100, 2), "%", "Slytherin")
    h="You are %s%s %s"%(round(hufflepuff/11*100, 2), "%", "Hufflepuff")
    r="You are %s%s %s"%(round(ravenclaw/11*100, 2), "%", "Ravenclaw")
    root = Tk()
    root.title("Results")
    a=Label(root, text=g, bg='white')
    a.pack()
    b=Label(root, text=s, bg='white')
    b.pack()
    c=Label(root, text=h, bg='white')
    c.pack()
    d=Label(root, text=r, bg='white')
    a['font']=font.Font(family="sans serif", size=18)
    b['font']=font.Font(family="sans serif", size=18)
    c['font']=font.Font(family="sans serif", size=18)
    d['font']=font.Font(family="sans serif", size=18)
    d.pack()
    
    x = [gryffindor, slytherin, hufflepuff, ravenclaw]
    a=max(x)
    if op.countOf(x, a) > 1:
        print("There has been a tie between the houses that you are eligible for. Hence, we are choosing the house based on house hierarchy, this is to encourage sparsely populated houses to get more members")
    else:
        pass
    if a == slytherin:
        d= Label(root, text="You are chosen into Slytherin")
        d['font']=font.Font(family="sans serif", size=18)
        d.pack()
        asdf("Slytherin.mp3", 0, 1)

    elif a == gryffindor:
        d= Label(root, text="You are chosen into Gryffindor")
        d['font']=font.Font(family="sans serif", size=18)
        d.pack()
        asdf("Gryffindor.mp3", 0, 1)
    elif a == hufflepuff:
        d= Label(root, text="You are chosen into Hufflepuff")
        d['font']=font.Font(family="sans serif", size=18)
        d.pack()
        asdf("Hufflepuff.mp3", 0, 1)
    else:
        d= Label(root, text="You are chosen into Ravenclaw")
        d['font']=font.Font(family="sans serif", size=18, weight='bold')
        d.pack()
        asdf("Ravenclaw.mp3", 0, 1)
    root.mainloop()

def e(t, w, a, b, c, d):
    global data
    global i
    dic = list(data.values())
        
    option_letter(t, dic[i][1])
    
    
    w.destroy()
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    i+=1
    if i == len(data):
        return choose_house()
    askQuestion()

def askQuestion():
    global i
    qu = Label(tab2, text = "Question %i: %s"%(i+1, list(data.keys())[i]), bg='yellow')
    qu['font']=font.Font(family="magic school one", size = 30)
    qu.grid(row=2, column=0)
    options = list(data.values())[i][0]
    a = Button(tab2, text= "A: %s" %(options[0]), bg='white', command=lambda:e("a", qu, a, b, c, d))
    a['font']=font.Font(family="sans serif", size=18)
    a.grid(row=3, column=0)
    b = Button(tab2, text= "B: %s" %(options[1]), bg = 'white', command=lambda:e("b", qu, a, b, c, d))
    b['font']=font.Font(family="sans serif", size=18)
    b.grid(row=4, column=0)
    c = Button(tab2, text= "C: %s" %(options[2]), bg='white', command=lambda:e("c", qu, a, b, c, d))
    c['font']=font.Font(family="sans serif", size=18)
    c.grid(row=5, column=0)
    d = Button(tab2, text= "D: %s" %(options[3]), bg='white', command=lambda:e("d", qu, a, b, c, d))
    d['font']=font.Font(family="sans serif", size=18)
    d.grid(row=6, column=0)

askQuestion()

root.mainloop()
