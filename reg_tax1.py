import os.path
import tkinter as reg_tax
import json
from tkinter import messagebox
registration = reg_tax.Tk()
registration.title("Registration")
registration.geometry("600x500")


def register():
    plan = payment_plan.get()
    kid1 = int(kids.get())
    salary_s = salary.get()
    tax = 0
    marital_s = marital.get()

    if marital_s == "single" and not kid1:
        tax = int(salary_s) * 10/100 if plan == "monthly" else (int(salary_s) * 12) * 10 / 100

    elif marital_s == "single" and kid1:
        tax = (int(salary_s) * 6/100) if plan == "monthly" else ((int(salary_s) * 12) * 6 / 100)

    elif marital_s == "married" and not kid1:
        tax = int(salary_s) * 8/100 if plan == "monthly" else (int(salary_s) * 12) * 8 / 100

    elif marital_s == "married" and kid1:
        if plan == "monthly":
            tax = ((float(salary_s) * 10/100) + (1000 * kid1))
        else:
            tax = (((float(salary_s) * 12) * 10 / 100) + (1000 * kid1))

    tax_entry.insert("end", str(tax))

    details = {}
    period = date.get()
    details[period] = {}

    details[period]["name"] = name.get()
    details[period]["salary"] = salary.get()
    details[period]["password"] = password.get()
    details[period]["email"] = email.get()
    details[period]["phone"] = phone_number.get()
    details[period]["occupation"] = work.get()
    details[period]["kid"] = kids.get()
    details[period]["plan"] = plan
    details[period]["marital"] = marital.get()
    details[period]["tax"] = tax_entry.get()

    file_name = 'monthly.json' if plan == "monthly" else "yearly.json"
    if not os.path.exists(file_name):
        create_file = open(file_name, 'w')
        create_file.write("{}")
        create_file.close()

    with open(file_name, 'r') as reader:
        database = json.load(reader)
        if not(database and period in database.keys()):
            database[period] = [details[period]]
        elif database[period]:
            database[period].append(details[period])

        with open(file_name, 'w') as create:
            json.dump(database, create, indent=4)

    messagebox.showinfo("tax", f"Thanks for registering, your tax is {tax}")

    salary.delete(0, "end")
    name.delete(0, "end")
    password.delete(0, "end")
    email.delete(0, "end")
    kids.delete(0, "end")
    phone_number.delete(0, "end")
    work.delete(0, "end")
    payment_plan.delete(0, "end")
    date.delete(0, "end")
    marital.delete(0, "end")
    tax_entry.delete(0, "end")


def back():
    registration.destroy()
    import main


name_label = reg_tax.Label(registration, text="Name", bg="black", fg="white", padx=10, pady=5, width=16)
name_label.grid(row=0, column=0)

name = reg_tax.Entry(registration, bg="white", fg="black", width=40)
name.grid(row=0, column=1)

password_label = reg_tax.Label(registration, text="password", bg="black", fg="white", padx=10, pady=10, width=16)
password_label.grid(row=1, column=0)

password = reg_tax.Entry(registration, bg="white", fg="black", width=40, show='\u2022')
password.grid(row=1, column=1)

email_label = reg_tax.Label(registration, text="Email", bg="black", fg="white", padx=10, pady=10, width=16)
email_label.grid(row=2, column=0)

email = reg_tax.Entry(registration, bg="white", fg="black", width=40)
email.grid(row=2, column=1)

phone_label = reg_tax.Label(registration, text="Phone number", bg="black", fg="white", padx=10, pady=10, width=16)
phone_label.grid(row=3, column=0)

phone_number = reg_tax.Entry(registration, bg="white", fg="black", width=40)
phone_number.grid(row=3, column=1)

occupation_label = reg_tax.Label(registration, text="Present occupation", bg="black",
                                 fg="white", padx=10, pady=10, width=16)
occupation_label.grid(row=4, column=0)

work = reg_tax.Entry(registration, bg="white", fg="black", width=40)
work.grid(row=4, column=1)

salary_label = reg_tax.Label(registration, text="Salary paid", bg="black",
                             fg="white", padx=10, pady=10, width=16)
salary_label.grid(row=5, column=0)

salary = reg_tax.Entry(registration, bg="white", fg="black", width=40)
salary.grid(row=5, column=1)

kids_label = reg_tax.Label(registration, text="No. of kids", bg="black",
                           fg="white", padx=10, pady=10, width=16)
kids_label.grid(row=6, column=0)

kids = reg_tax.Entry(registration, bg="white", fg="black", width=40)
kids.grid(row=6, column=1)

plan_label = reg_tax.Label(registration, text="Plan: Monthly or Yearly", bg="black",
                           fg="white", padx=10, pady=10, width=16)
plan_label.grid(row=7, column=0)

payment_plan = reg_tax.Entry(registration, bg="white", fg="black", width=40)
payment_plan.grid(row=7, column=1)

date_label = reg_tax.Label(registration, text="Date: month or year", bg="black",
                           fg="white", padx=10, pady=10, width=16)
date_label.grid(row=8, column=0)

date = reg_tax.Entry(registration, bg="white", fg="black", width=40)
date.grid(row=8, column=1)

marital_label = reg_tax.Label(registration, text="Marital status", bg="black",
                              fg="white", padx=10, pady=10, width=16)
marital_label.grid(row=9, column=0)

marital = reg_tax.Entry(registration, bg="white", fg="black", width=40)
marital.grid(row=9, column=1)

tax_label = reg_tax.Label(registration, text="Tax", bg="black", fg="white",
                          padx=10, pady=10, width=16)
tax_label.grid(row=11, column=0)

tax_entry = reg_tax.Entry(registration, bg="white", fg="black", width=40)
tax_entry.grid(row=11, column=1)

register_button = reg_tax.Button(registration, text="Register", bg="white", fg="black", font=1, command=register)
register_button.grid(row=10, column=1)

back_button = reg_tax.Button(registration, text="Back", bg="white", fg="black", command=back, font=1)
back_button.grid(row=13, column=1)

registration.mainloop()
