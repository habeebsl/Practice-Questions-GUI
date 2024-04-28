import tkinter
import secrets

courses = [
    'Respiratory Physiology',
    'Embryology',
    'GIT Physiology', 
    'Cardiovascular Physiology', 
    'Neurophysiology', 
    'Renal Physiology', 
    'Introductory Physiology', 
    'Blood Physiology', 
    'Endocrinology', 
    'Reproductive Physiology'
]

def choose_question(course):
    with open(f"desktop/Practice questions/{course}.txt", "r") as file:  # Changed backslash to forward slash
        questions = file.readlines()
        random_question = secrets.SystemRandom().randint(0, len(questions)-1)
        return f"{course} - {questions[random_question]}"

def placeholder_remove(event):
    if choose_course.get() == "Type Index":
        choose_course.delete(0, tkinter.END)

def print_question(question):
    list.grid_forget()
    choose_course.grid_forget()
    choose_or_not.config(text=question)
    button.config(text="Generate new question")

def choose_option():
    if yes_var.get() == True:
        check_yes.grid_forget()
        check_no.grid_forget()
        for i in range(len(courses)):
            choose_or_not.config(text='Type the index of your course of choice')
            list.insert(tkinter.END, f"{i+1}. {courses[i]}")
            list.grid(row=3, column=0)
        choose_course.insert(0, "Type Index")
        choose_course.grid(row=4, column=0)
        empty = choose_course.bind("<FocusIn>", placeholder_remove)

        button.grid(row=4, column=1)
        button.bind("<Button-1>", lambda event: print_question(choose_question(courses[int(choose_course.get())-1])))
    else:
        check_no.grid_forget()
        check_yes.grid_forget()
        button.grid(row=4, column=1)
        choose_or_not.config(text=print_question(choose_question(random_course())))
        button.config(text="Generate new question")
        button.bind("<Button-1>", lambda event: print_question(choose_question(random_course())))

def random_course():
    random_course = secrets.SystemRandom().randint(0, len(courses)-1)
    return courses[random_course]



window = tkinter.Tk()
choose_or_not = tkinter.Label(window, text="Would you like to pick a course??")
choose_or_not.grid(row=0, column=0)

yes_var = tkinter.BooleanVar()
no_var = tkinter.BooleanVar()
check_yes = tkinter.Checkbutton(window, text="yes", variable=yes_var, command=choose_option)
check_no = tkinter.Checkbutton(window, text="no", variable=no_var, command=choose_option)

list = tkinter.Listbox(window)
list.grid_forget()

choose_course = tkinter.Entry(window)

check_yes.grid(row=1, column=0)
check_no.grid(row=1, column=1)

button = tkinter.Button(window, text='Enter')
button.grid_forget()

window.mainloop()









