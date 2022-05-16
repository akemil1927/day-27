from tkinter import *


def convert():
    miles = float(miles_input.get())
    Km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{Km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=500, height=300)

# Entry
miles_input = Entry(width=7)
# print(input.get())
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)


# Button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)





window.mainloop()