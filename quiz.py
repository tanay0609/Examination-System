import tkinter as Tk
from tkinter import *
import random
import time
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import numpy as np
def start():
    global root 
    root =Tk()
    root.title("START EXAM")
    canvas = Canvas(root,width = 600,height = 580)
    canvas.grid(column = 0, row = 1)
    img = PhotoImage(file="Exam-PNG-Pic.png")
    canvas.create_image(60,30,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage)
    button.configure(width = 112,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()

def loginPage():
    sup.destroy()         
    global login
    login = Tk()
    login.title("Login")
    
    prn_no1 = StringVar()
    password1 = StringVar()
    
    login_canvas = Canvas(login,width=760,height=500,bg="#101357")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="#f3e3de")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Examination Login",fg="#782a12",bg="#f3e3de",font=('calibri 40 underline bold'))
    heading.place(relx=0.18,rely=0.1)

    #PRN NO.
    ulabel = Label(login_frame,text="PRN NO. ",fg='black',bg='#f3e3de')
    ulabel.place(relx=0.21,rely=0.4)
    prnno2 = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = prn_no1,width=42)
    prnno2.place(relx=0.33,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="PASSWORD ",fg='black',bg='#f3e3de')
    plabel.place(relx=0.21,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password1,width=42)
    pas.place(relx=0.33,rely=0.5)

    print(prnno)
    def check():
        if (prnno == prnno2.get() and password == pas.get()):
                menu()
        else:
            messagebox.showerror("LOGIN FAILED",  "Wrong PRN NO or password")
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check,bg='#956719',fg='white')
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup           
    sup = Tk()
    sup.title("EXAM SIGNUP")

    fname= StringVar()
    prnno = StringVar()
    passW = StringVar()
    rollno = StringVar()
    
    
    sup_canvas = Canvas(width=760,height=500,bg="#101357")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#f3e3de")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Examination SignUp",fg="#782a12",bg="#f3e3de")
    heading.config(font=('calibri 40 underline bold'))
    heading.place(relx=0.15,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="ENTER FULL NAME: ",fg='brown',bg='#f3e3de')
    flabel.place(relx=0.16,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.34,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="ENTER PRN NO: ",fg='brown',bg='#f3e3de')
    ulabel.place(relx=0.16,rely=0.5)
    prno = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = prnno)
    prno.config(width=42)
    prno.place(relx=0.34,rely=0.5)
    
    #password
    plabel = Label(sup_frame,text="ENTER PASSWORD: ",fg='brown',bg='#f3e3de')
    plabel.place(relx=0.16,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.34,rely=0.6)
    
    #rollno
    clabel = Label(sup_frame,text="ENTER ROLL NO. ",fg='brown',bg='#f3e3de')
    clabel.place(relx=0.16,rely=0.7)
    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = rollno)
    c.config(width=42)
    c.place(relx=0.34,rely=0.7)
    def addUserToDataBase():
        messagebox.showinfo("SUCCESS",  "SIGNUP SUCCESSFUL")
        global fullname
        fullname = fname.get()
        global prnno
        prnno = prno.get()
        global rollno
        global password
        password = pas.get()
        rollno = c.get()
        loginPage()

    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='#d48f8f')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = loginPage,bg="#f3e3de",fg='blue')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()

def menu():
    login.destroy()
    global menu 
    menu = Tk()
    menu.title("EXAM")
    menu_canvas = Canvas(menu,width=790,height=500,bg="#101357")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="#e2cfc7",bd=5)
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    wel = Label(menu_canvas,text='Vishwakarma Institute of Information Technology',fg="white",bg="#101357",font=('Arial 22 bold underline'))
    wel.place(relx=0.068,rely=0.02)
    
    level = Label(menu_frame,text='---EXAM GUIDELINES---',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level.place(relx=0.32,rely=0.03)
    
    level1 = Label(menu_frame,text='Rules to follow during all online proctored exams:',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level1.place(relx=0.02,rely=0.15) 
    
    level2 = Label(menu_frame,text='1.You must use a functioning webcam and microphone',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level2.place(relx=0.02,rely=0.25) 
    
    level3 = Label(menu_frame,text='2.No cell phones or other secondary devices in the room',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level3.place(relx=0.02,rely=0.35) 
    
    level4 = Label(menu_frame,text='3.Your desk/table must be clear ',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level4.place(relx=0.02,rely=0.45) 
    
    level5 = Label(menu_frame,text='4.No one else can be in the room with you',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level5.place(relx=0.02,rely=0.55) 
    
    level6= Label(menu_frame,text='5.The testing room must be well-lit ',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level6.place(relx=0.02,rely=0.65) 
    
    level7= Label(menu_frame,text='6.No use of additional applications or internet',fg='#ff0a0a',bg="#e2cfc7",font="calibri 18 bold")
    level7.place(relx=0.02,rely=0.75)
    
    def isChecked():
        if var1.get() == 1:
            letsgo['state'] = NORMAL
        elif var1.get() == 0:
            letsgo['state'] = DISABLED
            messagebox.showwarning('ERROR', 'Please accept and continue')
        else:
            messagebox.showerror('PythonGuides', 'Something went wrong!')
   
    var1= IntVar()  
    var1.set(0)
    hardR = Checkbutton(menu_frame,text='I accept and continue',fg='black',bg="#e2cfc7",font="calibri 14 ",variable=var1,onvalue=1,offvalue=0,command=isChecked)
    hardR.place(relx=0.02,rely=0.85)
    letsgo = Button(menu_frame,text="Let's Begin--->",state=DISABLED,bg="#e9daca",font="calibri 12",command=easy)
    letsgo.place(relx=0.75,rely=0.9)
    menu.mainloop()
    
def easy():
    menu.destroy()
    global e
    e = Tk()
    e.title("EASY QUESTIONS")

    easy_canvas = Canvas(e, width=800, height=500, bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="#e2cfc7")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    global easyscore
    easyscore = np.zeros(10)

    def countDown():
        check = 0
        for k in range(15, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!")
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    score = 0
    easyQ = [[
        "Q. Who developed Python Programming Language?",
        "Wick van Rossum",
        "Rasmus Lerdorf",
        "Guido van Rossum",
        "Niene Stom"
    ], [
        "Q. What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []] \nlist(filter(bool, nl))",
        "[1, 0, 2, ‘hello’, '', []]",
        "Error",
        "[1, 2, ‘hello’]",
        "[1, 0, 2, 0, ‘hello’, '', []]"
    ], [
        "Q. What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)",
        "34.00",
        "34.000000",
        "34.0000",
        "34.00000000"

    ], [
        "Q. What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10",
        "30.8",
        "27.2",
        "28.4",
        "30.0"
    ], [
        "Q. Which of these in not a core data type?",
        "Tuples",
        "Dictionary",
        "Lists",
        "Class"
    ], [
        "Q. Which of the following represents the bitwise XOR operator?",
        "^",
        "&",
        "!",
        "|"
    ], [
        "Q. In which year was the Python language developed?",
        "1995",
        "1972",
        "1981",
        "1989"
    ], [
        "Q. Which character is used in Python to make a single line comment?",
        "#",
        "/",
        "//",
        "!",
    ], [
        "Q. What is the output of the following code?"
        "valueOne = 5 ** 2",
        "10",
        "15",
        "Error:invalid syntax",
        "25"
    ], [
        "Q. In which llanguage python is wriitten",
        "English",
        "PHP",
        "C",
        "All of the above",
    ]]
    answer = [
        "Guido van Rossum",
        "[1, 2, ‘hello’]",
        "34.000000",
        "27.2",
        "Class",
        "^",
        "1989",
        "#",
        "25",
        "C"
    ]
    li = ['', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = random.choice(li[1:])

    ques = Label(easy_frame, text=easyQ[x][0], font="calibri 13 bold", bg="#e2cfc7")
    ques.place(relx=0.5, rely=0.25, anchor=CENTER)

    var = StringVar()
    var.set(NONE)
    a = Radiobutton(easy_frame, text=easyQ[x][1], font="calibri 11", value=easyQ[x][1], variable=var, bg="#e2cfc7")
    a.place(relx=0.2, rely=0.4, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], font="calibri 11", value=easyQ[x][2], variable=var, bg="#e2cfc7")
    b.place(relx=0.2, rely=0.5, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], font="calibri 11", value=easyQ[x][3], variable=var, bg="#e2cfc7")
    c.place(relx=0.2, rely=0.6, anchor=CENTER)

    d = Radiobutton(easy_frame, text=easyQ[x][4], font="calibri 11", value=easyQ[x][4], variable=var, bg="#e2cfc7")
    d.place(relx=0.2, rely=0.7, anchor=CENTER)

    li.remove(x)

    timer = Label(e, font="calibri 14 bold", width=4)
    timer.place(relx=0.15, rely=0.18, anchor=CENTER)


    def display():
        if len(li) == 1:
            createplot()
            medium()
        if len(li) == 2:
            nextQuestion.configure(text='Next->', command=NONE)

        if li:
            x = random.choice(li[1:])
            global choice
            choice = x
            ques.configure(text=easyQ[x][0])

            a.configure(text=easyQ[x][1], value=easyQ[x][1])

            b.configure(text=easyQ[x][2], value=easyQ[x][2])

            c.configure(text=easyQ[x][3], value=easyQ[x][3])

            d.configure(text=easyQ[x][4], value=easyQ[x][4])

            nextQuestion.configure(text='Next->', command=calc)

            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

    def calc1():
        if (var.get() in answer):
                easyscore[x] = 1
                print(easyscore)
    def calc():
        global score
        if (var.get() in answer):
                easyscore[choice] = 1
                score += 1
                print(easyscore)

        display()

    nextQuestion = Button(easy_frame, command=calc1, text="Next", font=("ariel", 16, "bold"), width=5, bg="#3b4c8d", fg="black")
    nextQuestion.place(relx=0.84, rely=0.82, anchor=CENTER)

    quit_button = Button(easy_frame, text="Quit", command=e.destroy, font=("ariel", 16, "bold"))
    quit_button.place(x=570, y=16)

    def createplot():
        X = np.array(['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10'])
        plt.plot(X, easyscore)
        plt.title("EASY QUESTIONS \n Marks vs questions")
        plt.xlabel("Questions")
        plt.ylabel("Marks")
        plt.savefig("analysis1.png")

    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def medium():
    e.destroy()
    global m
    m = Tk()
    m.title("Medium Questions")
    
    med_canvas = Canvas(m,width=800,height=500,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="#e2cfc7")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)


    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    
    mediumQ = [
                [
                    "Which of the following is not an exception handling keyword in Python?",
                     "accept",
                     "finally",
                     "except",
                     "try"
                ],[
                    "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?",
                    "3",
                    "5",
                    "25",
                    "1"
                ],[
                    "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?",
                    "Error",
                    "None",
                    "25",
                    "2"
                ],[
                    "print(0xA + 0xB + 0xC):",
                    "0xA0xB0xC",
                    "Error",
                    "0x22",
                    "33"
                ],[
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ],[
                    "Which type of Programming does Python support?",
                    "object-oriented programming",
                    "structured programming",
                    "functional programming",
                    "all of the mentioned"
                    
                ],[
                    "Which keyword is used for function in Python language?",
                    "Function",
                    "Def",
                    "Fun",
                    "Define"

                ],[
                    "What will be the output of the following code snippet?"
                    "a = [1, 2]"
                    "print(a * 3)" ,
                    "Error",
                    "[1,2]",
                    "[1,2,1,2]",
                    "[1,2,1,2,1,2]"
                ],[
                    "Which of the following is the truncation division operator in Python?",
                    "|",
                    "//",
                    "/",
                    "%"
                ],[
                    "What will be the output of this function?"
                    "round(4.876)",
                    "4",
                    "4.5",
                    "576",
                    "5",
                ]]
    answer = [
             "accept",
             "1",
             "25",
             "33",
             "none of the mentioned",
             "all of the mentioned",
             "def",
             "[1,2,1,2,1,2]",
             "//",
             "5"
            ]
    
    li = ['',0,1,2,3,4,5,6,7,8,9]
    x = random.choice(li[1:])
    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 13 bold",bg="#e2cfc7")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    var.set(NONE)
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 11 ",value=mediumQ[x][1],variable = var,bg="#e2cfc7")
    a.place(relx=0.2,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 11",value=mediumQ[x][2],variable = var,bg="#e2cfc7")
    b.place(relx=0.2,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 11",value=mediumQ[x][3],variable = var,bg="#e2cfc7")
    c.place(relx=0.2,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 11",value=mediumQ[x][4],variable = var,bg="#e2cfc7")
    d.place(relx=0.2,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m,font="calibri 14 bold",width=4)
    timer.place(relx=0.15,rely=0.18,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
            createplot()
            difficult()
        if len(li) == 2:
            nextQuestion.configure(text='Next',command=NONE)
                
        if li:
            x = random.choice(li[1:])
            global choice1
            choice1=x
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])

            nextQuestion.configure(text='Next->', command=calc)
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()
    global score2
    score2 = np.zeros(10)
    def calc1():
        if (var.get() in answer):
                score2[x] = 1
                print(score2)
    def calc():
        if (var.get() in answer):
            score2[choice1] = 1
            print(score2)
        display()
    
    nextQuestion = Button(med_frame,command=calc1,text="Next",font=("ariel",16,"bold"),width=5,bg="#3b4c8d",fg="black")
    nextQuestion.place(relx=0.84,rely=0.82,anchor=CENTER)

    quit_button = Button(med_frame, text="Quit", command=m.destroy,font=("ariel",16,"bold"))
    quit_button.place(x=570,y=16)

    def createplot():
        X = np.arange(10)
        plt2.plot(X, score2)
        plt2.title("Medium QUESTIONS \n Marks vs Questions")
        plt2.xlabel("Questions")
        plt2.ylabel("Marks")
        plt2.savefig("analysis2.png")

    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
    m.destroy()
    global h
    h = Tk()
    h.title("Hard Questions")
    
    hard_canvas = Canvas(h,width=800,height=500,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="#e2cfc7")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(30, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    
    hardQ = [
      [
       "Q.All keywords in Python are in _________",
        "lower case",
        "UPPER CASE",
        "Capitalized",
        "None of the mentioned"
    ],[
        "Q.Which of the following cannot be a variable?",
        "__init__",
        "in",
        "it",
        "on"
    ],[
     "  Q.Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"   
    ],[
        "Q.What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],[
        "Q.What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ],[
        "Q.Is Python case sensitive when dealing with identifiers?",
        "no",
        "yes",
        "machine dependent",
        "none of the mentioned"
    ],[
        "Q.What will be the output of the following Python function?"
        "min(max(False,-3,-4), 2,7)",
        "-4",
        "-3",
        "2",
        "False"
    ],[
       "Q.Which of the following operators is the correct option for power(ab)?",
       "a ^ b",
       "a**b",
       "a ^ ^ b",
       "a ^ * b"
    ],[
       "Q.What happens when '2' == 2 is executed?",
       "False",
       "Ture",
       "ValueError occurs",
       "TypeError occurs",
    ],[
       "Q.Study the following program:"
       "print(6 + 5 - 4 * 3 / 2 % 1)",
       "11.0",
       "7.0",
       "15",
       "0"
    ]]
    answer = [
            "None of the mentioned",
            "in",
            "(1,2,3)",
            "4",
            "error",
            "no",
            "False",
            "a**b",
            "false",
            "11.0"
            ]
    
    li = ['',0,1,2,3,4,5,6,7,8,9]
    x = random.choice(li[1:])

    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 13 bold",bg="#e2cfc7")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    var.set(NONE)
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 11",value=hardQ[x][1],variable = var,bg="#e2cfc7")
    a.place(relx=0.2,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 11",value=hardQ[x][2],variable = var,bg="#e2cfc7")
    b.place(relx=0.2,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 11",value=hardQ[x][3],variable = var,bg="#e2cfc7")
    c.place(relx=0.2,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 11",value=hardQ[x][4],variable = var,bg="#e2cfc7")
    d.place(relx=0.2,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h,font="calibri 14 bold",width=4)
    timer.place(relx=0.15,rely=0.18,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                createplot()
                getresults()
        if len(li) == 2:
            nextQuestion.configure(text='Submit',command=NONE)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            global choice2
            choice2=x
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])

            nextQuestion.configure(text='Next->', command=calc)
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()
    global score3
    score3 = np.zeros(10)
    def calc1():
        if (var.get() in answer):
                score3[x] = 1
                print(score3)
    def calc():
        if (var.get() in answer):
            score3[choice2]=1
            print(score3)
        display()

    def createplot():
        X = np.array(['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10'])
        plt1.plot(X, score3)
        plt1.title("Hard QUESTIONS \n Marks vs Questions")
        plt1.xlabel("Questions")
        plt1.ylabel("Marks")
        plt1.savefig("analysis3.png")

    nextQuestion = Button(hard_frame,command=calc1,text="Next",font=("ariel",16,"bold"),width=5,bg="#3b4c8d",fg="black")
    nextQuestion.place(relx=0.84,rely=0.82,anchor=CENTER)

    quit_button = Button(hard_frame, text="Quit", command=h.destroy,font=("ariel",16,"bold"))
    quit_button.place(x=570,y=16)

    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def getresults():
    global root1
    h.destroy()
    root1 = Tk()
    root1.title("RESULTS")
    root1.geometry('1000x800')

    canvas = Canvas(root1, width=1000, height=700, bg='white')
    python_image = PhotoImage(file='logo.png')
    canvas.create_image((100, 100), image=python_image)
    canvas.grid(row=0, column=0)
    canvas.create_text((550, 120), text="VISHWAKARMA INSTITUTE OF INFORMATION TECHNOLOGY", fill="dark blue",
                       font='Calibri 24 underline')

    img1 = PhotoImage(file='img2.png')
    canvas.create_image((500, 400), image=img1)

    button = Button(root1, text='Get Results', command=geteasy)
    button.configure(width=122, height=2, activebackground="#33B5E5", bg='#fc862d', relief=RAISED)
    button.grid(column=0, row=1)
    root1.mainloop()

def geteasy() :
    global ge
    root1.destroy()
    ge=Tk()
    ge.title("RESULTS")
    ge.geometry('1000x800')

    canvas = Canvas(ge, width=1000, height=800, bg='#e0f5fe')
    canvas.grid(row=0, column=0)

    canvas.create_line((0, 20, 1000, 20), fill='#024562', width=3)
    canvas.create_text((55, 35), text="Full Name:", font='Calibri 12', anchor='n')
    label_text = ""+ fullname
    canvas.create_text((135, 35), text=label_text, font='Calibri 12', anchor='n')
    canvas.create_text((55, 55), text="PRN NO   :", font='Calibri 12', anchor='n')
    label_text1 = "" + str(prnno)
    canvas.create_text((135, 55), text=label_text1, font='Calibri 12', anchor='n')
    label_text2 = "" + str(rollno)
    canvas.create_text((55, 75), text="Roll NO   :", font='Calibri 12', anchor='n')
    canvas.create_text((135, 75), text=label_text2, font='Calibri 12', anchor='n')
    canvas.create_line((0, 105, 1000, 105), fill='#024562', width=3)
    canvas.create_text((500, 125), text='ANALYSIS ON EASY QUESTIONS', fill='dark blue',
                       font='calibri 20 bold underline')
    canvas.create_text((400, 165),
                       text="1.Your performance in easy section is very good. You have exhibited a remarkable performance.",
                       font="calibri 14", fill='dark red', justify='left')
    canvas.create_text((318, 185), text="2.Practice regularly in order to maintain this level of excellence throughout",
                       fill='dark red', font="calibri 14", justify='left')
    canvas.create_text((330, 205), text="3.Try to exceed your current level of performance by expanding your lexicon. ",
                       fill='dark red', font="calibri 14")
    canvas.create_text((255, 225), text='4.Try learning about subtleties of this wonderful language', font='calibri 14',
                       fill='dark red')

    img1 = PhotoImage(file='analysis1.png')
    canvas.create_image((500, 500), image=img1)

    button = Button(ge, text='Next', command=getmedium)
    button.configure(width=10, height=2, activebackground="#33B5E5", bg='#fc862d', relief=RAISED)
    button.place(x=900, y=725)
    ge.mainloop()

def getmedium():
    ge.destroy()
    global gm
    gm=Tk()
    gm.title("RESULTS")
    gm.geometry('1000x800')

    canvas = Canvas(gm, width=1000, height=800, bg='#e0f5fe')
    canvas.grid(row=0, column=0)

    canvas.create_line((0, 20, 1000, 20), fill='#024562', width=3)
    canvas.create_text((55, 35), text="Full Name:", font='Calibri 12', anchor='n')
    label_text = "" + fullname
    canvas.create_text((135, 35), text=label_text, font='Calibri 12', anchor='n')
    canvas.create_text((55, 55), text="PRN NO   :", font='Calibri 12', anchor='n')
    label_text1 = "" + str(prnno)
    canvas.create_text((135, 55), text=label_text1, font='Calibri 12', anchor='n')
    label_text2 = "" + str(rollno)
    canvas.create_text((55, 75), text="Roll NO   :", font='Calibri 12', anchor='n')
    canvas.create_text((135, 75), text=label_text2, font='Calibri 12', anchor='n')
    canvas.create_line((0, 105, 1000, 105), fill='#024562', width=3)

    canvas.create_text((500, 125), text='ANALYSIS ON MEDIUM QUESTIONS', fill='dark blue',
                       font='calibri 20 bold underline')
    canvas.create_text((400, 165),
                       text="1.Your performance in Medium section is very good. According to our analysis, .",
                       font="calibri 14", fill='dark red', justify='left')
    canvas.create_text((385, 185), text="2.you have a good understanding of all relevant areas of Quantitative Ability",
                       fill='dark red', font="calibri 14", justify='left')
    canvas.create_text((300, 205), text="3.You just need to practice enough to remain in touch ", fill='dark red',
                       font="calibri 14")
    canvas.create_text((315, 225), text='4.Try learning about subtleties of this wonderful language', font='calibri 14',
                       fill='dark red')

    img1 = PhotoImage(file='analysis2.png')
    canvas.create_image((500, 500), image=img1)

    button = Button(gm, text='Prev', command=geteasy)
    button.configure(width=10, height=2, activebackground="#33B5E5", bg='#fc862d', relief=RAISED)
    button.place(x=30, y=725)

    button = Button(gm, text='Next', command=getdifficult)
    button.configure(width=10, height=2, activebackground="#33B5E5", bg='#fc862d', relief=RAISED)
    button.place(x=850, y=725)
    gm.mainloop()

def getdifficult():
    global gd
    gm.destroy()
    gd= Tk()
    gd.title("RESULTS")
    gd.geometry('1000x800')

    canvas = Canvas(gd, width=1000, height=800, bg='#e0f5fe')
    canvas.grid(row=0, column=0)

    canvas.create_line((0, 20, 1000, 20), fill='#024562', width=3)
    canvas.create_text((55, 35), text="Full Name:", font='Calibri 12', anchor='n')
    label_text = "" + fullname
    canvas.create_text((135, 35), text=label_text, font='Calibri 12', anchor='n')
    canvas.create_text((55, 55), text="PRN NO   :", font='Calibri 12', anchor='n')
    label_text1 = "" + str(prnno)
    canvas.create_text((135, 55), text=label_text1, font='Calibri 12', anchor='n')
    label_text2 = "" + str(rollno)
    canvas.create_text((55, 75), text="Roll NO   :", font='Calibri 12', anchor='n')
    canvas.create_text((135, 75), text=label_text2, font='Calibri 12', anchor='n')
    canvas.create_line((0, 105, 1000, 105), fill='#024562', width=3)
    canvas.create_text((500, 125), text='ANALYSIS ON DIFFICULT QUESTIONS', fill='dark blue',
                       font='calibri 20 bold underline')
    canvas.create_text((300, 165), text="1.Your performance in Logical Ability is very good.", font="calibri 14",
                       fill='dark red', justify='left')
    canvas.create_text((413, 185),
                       text="2.You are an expert in drawing inferences, spotting patterns and solving puzzles",
                       fill='dark red', font="calibri 14", justify='left')
    canvas.create_text((402, 205), text="3.We are sure you know that the only way to sustain and improve this ability.",
                       fill='dark red', font="calibri 14")
    canvas.create_text((360, 225), text='4.regularly practice more and more difficult questions. All the best!',
                       font='calibri 14', fill='dark red')

    img1 = PhotoImage(file='analysis3.png')
    canvas.create_image((500, 500), image=img1)

    button = Button(gd, text='Prev', command=getmedium)
    button.configure(width=10, height=2, activebackground="#33B5E5", bg='#fc862d', relief=RAISED)
    button.place(x=100, y=725)

    button = Button(gd, text='Next', command=final)
    button.configure(width=10, height=2, activebackground="#33B5E5", bg='#fc862d', relief=RAISED)
    button.place(x=850, y=725)
    gd.mainloop()

def final():
    global sh1
    gd.destroy()
    sh1 = Tk()
    sh1.title("RESULTS")
    sh1.geometry("1000x800")
    show_canvas = Canvas(sh1, width=1000, height=800, bg="white")
    show_canvas.pack()
    ima = PhotoImage(file='logo.png')
    show_canvas.create_image((50, 100), image=ima)
    show_canvas.create_text((550, 120), text="VISHWAKARMA INSTITUTE OF INFORMATION TECHNOLOGY", fill="#075f8e",
                            font='Calibri 24 underline')
    scoreasy = 0
    scoremedium = 0
    scorehard = 0

    for x in easyscore:
        scoreasy += x
    for x in score2:
        scoremedium += x
    for x in score3:
        scorehard += x
    y1 = np.array([scoreasy, scoremedium, scorehard])
    mylabels = ["Easy", "Medium", "Hard"]
    plt.title("Marks distribution")
    plt.pie(y1, labels=mylabels)
    plt.savefig("piechart.png")
    show_canvas.create_line((0, 20, 1000, 20), fill='#024562', width=3)
    show_canvas.create_line((0, 280, 1000, 280), fill='#024562', width=3)
    show_canvas.create_line((0, 350, 1000, 350), fill='#024562', width=3)
    show_canvas.create_text((55, 205), text="Full Name :", font='Calibri 12', anchor='n')
    label_text = "" + fullname
    show_canvas.create_text((125, 205), text=label_text, font='Calibri 12', anchor='n')
    show_canvas.create_text((55, 225), text="PRN NO    :", font='Calibri 12', anchor='n')
    label_text1 = "" + str(prnno)
    show_canvas.create_text((125, 225), text=label_text1, font='Calibri 12', anchor='n')
    show_canvas.create_text((55, 245), text="Roll NO    :", font='Calibri 12', anchor='n')
    label_text2 = "" + str(rollno)
    show_canvas.create_text((125, 245), text=label_text2, font='Calibri 12', anchor='n')
    mark=scoreasy+scoremedium+scorehard
    st = "Your score is " + str(mark) + " out of 30"
    mlabel = Label(show_canvas, text=st, fg="black", font=("ariel", 16, "bold"))
    mlabel.place(x=500, y=320, anchor=CENTER)
    ima1 = PhotoImage(file='piechart.png')
    show_canvas.create_image((500, 600), image=ima1)
    button = Button(sh1, text='END', command=exit)
    button.configure(width=10, height=2, activebackground="#33B5E5", bg='RED', relief=RAISED)
    button.place(x=470, y=755)


    sh1.mainloop()

#if __name__=='__main__':
if(True):
    start()
