from tkinter import *

window = Tk()
window.title("Miles to Km converter")
#window.minsize(width=350, height=200)
window.config(padx=20, pady=20)


# LABEL
is_equal_label = Label(text="is equal to:", font=("Arial", 12, "bold"))
is_equal_label.grid(column=0, row=1)

# LABEL 2
answer_label = Label(text=0, font=("Arial", 12, "bold"))
answer_label.grid(column=1, row=1)

# LABEL 3
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# LABEL 4
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# ENTRY
input = Entry(width=20)
input.grid(column=1, row=0)


# BUTTON
def convert():
    miles = float(input.get())
    km = round(miles * 1.60934, 2)
    answer_label.config(text=km)


calculate = Button(text="Calculate", command=convert, font=("Arial", 12, "bold"))
calculate.grid(column=1, row=2)


window.mainloop()