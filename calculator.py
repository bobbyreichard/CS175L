#Simple Calculator

import tkinter

window = tkinter.Tk()
window.title("Calculator")

#Functions
def add(value):
    print(value)


#GUI
#Row 1
final_result = tkinter.Label(window, text = "")
final_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(window, text = "1", command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(window, text = "2", command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(window, text = "3", command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(window, text = "/", command=lambda: add("/"))
button_divide.grid(row=1, column=3)

#Row 2

button_4 = tkinter.Button(window, text = "4", command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(window, text = "5", command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(window, text = "6", command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(window, text = "*", command=lambda: add("*"))
button_multiply.grid(row=2, column=3)





#last line of program
root.mainloop()
