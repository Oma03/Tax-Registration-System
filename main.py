import tkinter as tax
tps = tax.Tk()
tps.title("Tax Payment System")
tps.geometry("600x200")
tps.config(bg="black")


def press():
    tps.destroy()
    import reg_tax1


def skip():
    tps.destroy()
    import login_tax


frame = tax.LabelFrame(tps, padx=5, pady=5)
frame.pack(padx=10, pady=10)

frame1 = tax.LabelFrame(tps, padx=5, pady=5, border=0, background="black")
frame1.pack(padx=10)

frame2 = tax.LabelFrame(tps, padx=5, pady=5, border=0, background="black")
frame2.pack(padx=10)

text_label = tax.Label(frame, text="Welcome", bg="black",
                       fg="thistle", font=("Vladimir Script", 30), width=70)
text_label.pack()

text_label1 = tax.Label(frame1, text="Are you a new user?", font=("Cambria", 15),
                        bg="black", fg="white")
text_label1.pack()

button_yes = tax.Button(frame2, text="Yes", font=1, bg="white", fg="black", command=lambda: press())
button_yes.grid(row=0, column=0)

button_no = tax.Button(frame2, text="No", font=1, bg="white", fg="black", command=lambda: skip())
button_no.grid(row=0, column=1)

tps.mainloop()
