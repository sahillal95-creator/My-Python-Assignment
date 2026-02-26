import tkinter as tk

# -----------------------------
# Global Variables
# -----------------------------
first_number = None
operation = None
reset_screen = False

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# -----------------------------
# Display Screen
# -----------------------------
entry = tk.Entry(root, font=("Arial", 22), borderwidth=5,
                 relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)


# -----------------------------
# Number Button Function
# -----------------------------
def button_number(num):
    global reset_screen

    if reset_screen:
        entry.delete(0, tk.END)
        reset_screen = False

    entry.insert(tk.END, str(num))


# -----------------------------
# Decimal Button
# -----------------------------
def button_decimal():
    current = entry.get()
    if "." not in current:
        entry.insert(tk.END, ".")


# -----------------------------
# Operation Button
# -----------------------------
def button_operation(op):
    global first_number, operation, reset_screen

    try:
        first_number = float(entry.get())
        operation = op
        reset_screen = True
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# -----------------------------
# Equal Button
# -----------------------------
def button_equal():
    global first_number, operation, reset_screen

    try:
        second_number = float(entry.get())

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                raise ZeroDivisionError
            result = first_number / second_number
        else:
            result = second_number

        entry.delete(0, tk.END)
        entry.insert(0, result)
        reset_screen = True

    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Cannot divide by 0")
        reset_screen = True
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        reset_screen = True


# -----------------------------
# Clear Button
# -----------------------------
def clear():
    global first_number, operation
    first_number = None
    operation = None
    entry.delete(0, tk.END)


# -----------------------------
# Button Layout
# -----------------------------
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:

    if text.isdigit():
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        command=lambda t=text: button_number(t))

    elif text == ".":
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        command=button_decimal)

    elif text in "+-*/":
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        command=lambda t=text: button_operation(t))

    elif text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        command=button_equal)

    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 18),
                        command=clear)

    btn.place(x=10 + col * 80, y=100 + row * 70, width=70, height=60)

# -----------------------------
# Run Application
# -----------------------------
root.mainloop()