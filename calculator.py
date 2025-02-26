from tkinter import *

# Create root (base) window
root = Tk()
# Set width and height of base window
root.geometry("424x412")
root.resizable(0, 0)  # To prevent from resizing the window

root.title("Calculator")

# Global expression variable
expression = ""

# Button click function
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# clear button function
def button_clear():
    global expression
    expression = ""
    input_text.set(expression)

#   equal button function
def button_equal():
    global expression
    result = str(eval(expression))  # 'eval': This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


# 'StringVar()' is used to get the instance of input field
input_text = StringVar()

# Create a frame for the input field
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)

# Create an input field inside the frame
input_field = Entry(input_frame, font=("arial", 18, "bold"), textvariable=input_text,
                    width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # internal padding to increase the height of input field

# Create another frame for button below the input frame
buttons_frame = Frame(root, width=312, height=272.5, bg="grey")
buttons_frame.pack()

# First row
clear = Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: button_clear())
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="news")

divide = Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: button_click("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

# Second row
seven = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(9))
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

# Third row
four = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(6))
six.grid(row=2, column=2, padx=1, pady=1)

minus = Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click("-"))
minus.grid(row=2, column=3, padx=1, pady=1)

# Fourth row
one = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(3))
three.grid(row=3, column=2, padx=1, pady=1)

plus = Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click("+"))
plus.grid(row=3, column=3, padx=1, pady=1)

# Fifth row
zero = Button(buttons_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click(0))
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="news")

point = Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_click("."))
point.grid(row=4, column=2, padx=1, pady=1)

equals = Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: button_equal())
equals.grid(row=4, column=3, padx=1, pady=1)

# Start event loop
root.mainloop()
