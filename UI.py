from tkinter import *
import tkinter.ttk as ttk

# Creating the app`s window
root = Tk()
root.wm_title("Calculator")
sum_display = Entry(root, width=35, borderwidth=5)
sum_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Adding buttons widget of the app
def add_button():
    return


button_1 = Button(root, text="1", padx=40, pady=20, command=add_button)
button_2 = Button(root, text="2", padx=40, pady=20, command=add_button)
button_3 = Button(root, text="3", padx=40, pady=20, command=add_button)
button_4 = Button(root, text="4", padx=40, pady=20, command=add_button)
button_5 = Button(root, text="5", padx=40, pady=20, command=add_button)
button_6 = Button(root, text="6", padx=40, pady=20, command=add_button)
button_7 = Button(root, text="7", padx=40, pady=20, command=add_button)
button_8 = Button(root, text="8", padx=40, pady=20, command=add_button)
button_9 = Button(root, text="9", padx=40, pady=20, command=add_button)
button_0 = Button(root, text="0", padx=40, pady=20, command=add_button)
button_add = Button(root, text="+", padx=40, pady=20, command=add_button)
button_sub = Button(root, text="-", padx=40, pady=20, command=add_button)



# Adding buttons to the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)

# Adding Text widget


# Adding buttons functionality



#


# if __name__ == '__main__':
root.mainloop()