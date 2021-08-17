from tkinter import *
import tkinter.ttk as ttk

# Creating the app`s window and display slot
root = Tk()
root.wm_title("Calculator")
display_slot = Entry(root, width=35, borderwidth=5)
display_slot.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Adding display_slot functionality - referring it as a string


def button_click(num):
    curr = display_slot.get()
    display_slot.delete(0, END)
    #global other =num
    display_slot.insert(0, str(curr)+str(num))
    return


def clear_button():
    display_slot.delete(0, END)


def addition_button():
    global first_num
    num = display_slot.get()
    global math_operation
    add_operator = '+'
    str_addition = "addition"
    #first_num = num
    #display_slot.delete(0, END)
    display_slot.insert(END, add_operator)
    #print(display_slot.get())
    #display_slot.delete(0, END)


def subtraction_button():
    sub_operator = '-'
    str_subtraction = 'subtraction'
    display_slot.insert(END, sub_operator)

# equal method will be the one that we`ll recognize and calculate the math operator
#def equal_button():
#    match operator:



# Adding buttons widget of the app


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=addition_button)
button_sub = Button(root, text="-", padx=40, pady=20, command=subtraction_button)
#button_equal = Button(root, text="=", padx=90, pady=20, command=equal_button)
button_clear = Button(root, text="Clear", padx=29, pady=20, command=clear_button)

# Adding "special" buttons such as clear , mul,() etc.


# Adding buttons to the screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_clear.grid(row=1, column=0)
button_add.grid(row=1, column=1)
button_sub.grid(row=1, column=2)

button_0.grid(row=5, column=0)
#button_equal.grid(row=5, column=1, columnspan=2)

# Adding Text widget


# Adding buttons functionality to each one



# if __name__ == '__main__':
root.mainloop()
