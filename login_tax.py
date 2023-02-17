import tkinter as login
import json
from tkinter import messagebox
login_t = login.Tk()
login_t.title("Login")
login_t.geometry("600x500")


def enter():
    username = username_entry.get()
    password1 = password_entry.get()
    plan = plan_entry.get()
    date = date_entry.get()
    period = 0
    periods = 0
    years = ["2020", "2021", "2022", "2023"]
    for i in range(0, 3):
        if date in years:
            dates = years.index(date)
            period = dates - 1
            periods = years[period]
    months = ["january".casefold(), "february".casefold(), "march".casefold(), "april".casefold(),
              "may".casefold(), "june".casefold(), "july".casefold(), "september".casefold(),
              "october".casefold(), "november".casefold(), "december".casefold()]
    for i in range(0, 12):
        if date in months:
            dates = months.index(date)
            period = dates - 1
            periods = months[period]

    file_name = "monthly.json" if plan == "monthly" else "yearly.json"
    with open(file_name, 'r') as reader:
        database = json.load(reader)

        for elem in database[periods]:
            for k, v in elem.items():
                if k == "name":
                    value = username
                    for x, z in elem.items():
                        if x == "password":
                            value1 = password1

        if value == username and value1 == password1:
            for w, e in elem.items():
                if w == "tax":
                    value2 = e
            messagebox.showinfo("Tax", f"Welcome, your tax is {value2}")
            details = {}
            details[date] = {}

            details[date]["name"] = username_entry.get()
            details[date]["password"] = password_entry.get()
            details[date]["plan"] = plan_entry.get()
            details[date]["tax"] = value2

            with open(file_name, 'r') as create:
                database = json.load(create)
                database[date].append(details[date])

            with open(file_name, 'w') as create:
                json.dump(database, create, indent=4)
            messagebox.showinfo("Paid", "Successfully Paid")
        else:
            messagebox.showerror("Error", "Password or Username not correct")

        # if (value == username and value1 == password1) and (username and password1) not in periods:
        #     messagebox.showerror("Error", f"You have not paid for {periods}")


def back():
    login_t.destroy()
    import main


username_label = login.Label(login_t, text="Name", bg="black", fg="white", padx=10, pady=5, width=10)
username_label.grid(row=0, column=0)

username_entry = login.Entry(login_t, bg="white", fg="black", width=40)
username_entry.grid(row=0, column=1)

password_label = login.Label(login_t, text="Password", bg="black", fg="white", padx=10, pady=5, width=10)
password_label.grid(row=1, column=0)

password_entry = login.Entry(login_t, bg="white", fg="black", width=40)
password_entry.grid(row=1, column=1)

plan_label = login.Label(login_t, text="Plan", bg="black", fg="white", padx=10, pady=5, width=10)
plan_label.grid(row=2, column=0)

plan_entry = login.Entry(login_t, bg="white", fg="black", width=40)
plan_entry.grid(row=2, column=1)

date_label = login.Label(login_t, text="Date to pay", bg="black", fg="white", padx=10, pady=5, width=10)
date_label.grid(row=3, column=0)

date_entry = login.Entry(login_t, bg="white", fg="black", width=40)
date_entry.grid(row=3, column=1)

login_button = login.Button(login_t, text="Login", bg="white", fg="black", font=1, command=enter)
login_button.grid(row=4, column=1)

back_button = login.Button(login_t, text="Back", bg="white", fg="black", font=1, command=back)
back_button.grid(row=5, column=1)

login_t.mainloop()
