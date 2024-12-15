from tkinter import Tk, Label, Entry, Button, Frame
from functools import partial
win = Tk()
win.title("Ganda")
win.geometry("500x350+650+280")
win.config(bg="#FCD6F0")
Label(win, text="Python GUI: Basic Calculator v1", font=("Century Gothic", 16), bg="#FCD6F0", fg="#8E0C4D").grid(row=0, column=0, columnspan=3, pady=10)
Label(win, text="First Number:", font=("Century Gothic", 12), bg="#FCD6F0").grid(row=1, column=0, sticky="e", padx=10)
Label(win, text="Second Number:", font=("Century Gothic", 12), bg="#FCD6F0").grid(row=2, column=0, sticky="e", padx=10)
entry1 = Entry(win, width=10, font=("Century Gothic", 14), bg="#F59FCB")
entry1.grid(row=1, column=1, padx=5, pady=5)
entry2 = Entry(win, width=10, font=("Century Gothic", 14), bg="#F59FCB")
entry2.grid(row=2, column=1, padx=5, pady=5)
result_label = Label(win, text="00", font=("Century Gothic", 16, "bold"), bg="white", width=12, relief="sunken")
result_label.grid(row=2, column=2, padx=20, pady=5)
result_text = Label(win, text="Result:", font=("Century Gothic", 12), bg="#FCD6F0")
result_text.grid(row=1, column=2, padx=20, pady=5)
def calculate(op):
    try:
        n1, n2 = float(entry1.get()), float(entry2.get())
        results = {"+": (n1 + n2, "Sum"), "-": (n1 - n2, "Difference"), "*": (n1 * n2, "Product"), "/": (n1 / n2, "Quotient"),
                   "//": (n1 // n2, "Floor Qoutient"), "^": (n1 ** n2, "Power"), "%": (n1 % n2, "Remainder")}
        res, txt = results[op]
        result_label.config(text=f"{res:.2f}")
        result_text.config(text=txt)
    except:
        result_label.config(text="Error")
        result_text.config(text="")
ops = [("+", 0, 0), ("-", 0, 1), ("*", 0, 2), ("/", 1, 0), ("%", 1, 1), ("//", 1, 2), ("^", 2, 1)]
frame = Frame(win, bg="#FCD6F0")
frame.grid(row=3, column=0, columnspan=3, pady=20)
for op, r, c in ops:
    Button(frame, text=op, font=("Century Gothic", 14, "bold"), width=8, bg="#A40773", command=partial(calculate, op)).grid(row=r, column=c, padx=10, pady=10)
win.mainloop()
