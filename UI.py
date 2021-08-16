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


but_1 = Button(root, text="1", padx=40, pady=20, command=add_button)
but_2 = Button(root, text="2", padx=40, pady=20, command=add_button)
but_3 = Button(root, text="3", padx=40, pady=20, command=add_button)
but_4 = Button(root, text="4", padx=40, pady=20, command=add_button)
but_5 = Button(root, text="5", padx=40, pady=20, command=add_button)
but_6 = Button(root, text="6", padx=40, pady=20, command=add_button)
but_7 = Button(root, text="7", padx=40, pady=20, command=add_button)
but_8 = Button(root, text="8", padx=40, pady=20, command=add_button)
but_9 = Button(root, text="9", padx=40, pady=20, command=add_button)
but_0 = Button(root, text="0", padx=40, pady=20, command=add_button)
but_add = Button(root, text="+", padx=39, pady=20, command=add_button)
#but_sub = Button(root, text="-", padx=40, pady=20, command=add_button)
#but_mul = Button(root, text="x", padx=40, pady=20, command=add_button)
but_sum = Button(root, text="=", padx=91, pady=20, command=add_button)
#but_precent = Button(root, text="%", padx=40, pady=20, command=add_button)
#but_dot = Button(root, text=".", padx=40, pady=20, command=add_button)
but_clr = Button(root, text="Clear", padx=79, pady=20, command=add_button)



# Adding "special" buttons such as clear , mul,() etc.


# Adding buttons to the screen
but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)

but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)
#but_mul.grid(row=2, column=3)

but_0.grid(row=4, column=0)
but_clr.grid(row=4, column=1,columnspan=3)
but_add.grid(row=5, column=0)
but_sum.grid(row=5, column=1,columnspan=3)

#but_sub.grid(row=5, column=2)

#but_precent.grid(row=4, column=0)
#but_dot.grid(row=4, column=2)



# Adding special buttons

# Adding Text widget


# Adding buttons functionality to each one



#


# if __name__ == '__main__':
root.mainloop()
