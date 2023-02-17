# # months = ["i", "j", "k", "l", "m"]
# # # for x in months:
# # for i in range(0, 5):
# #     # print(f"{x} = {i}")
# #     print(i, months[i])
# date = input("Enter a date: ")
# if date == "january".casefold():
#     period = 0
# elif date == "february".casefold():
#     period = 1
# elif date == "march".casefold():
#     period = 2
# elif date == "april".casefold():
#     period = 3
# elif date == "may".casefold():
#     period = 4
# elif date == "june".casefold():
#     period = 5
# elif date == "july".casefold():
#     period = 6
# elif date == "august".casefold():
#     period = 7
# elif date == "september".casefold():
#     period = 8
# elif date == "october".casefold():
#     period = 9
# elif date == "november".casefold():
#     period = 10
# elif date == "december".casefold():
#     period = 11
#
# print(period)
# dates = period - 1
# my_list = ["try_again", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
# date = my_list[dates]
# print(date)


# details = {
#     "may": {
#         "name": [],
#         "salary": [],
#         "password": [],
#         "email": [],
#         "phone": [],
#         "occupation": [],
#         "kid": [],
#         "plan": [],
#         "marital": [],
#         "tax_status": [],
#     },
#
#     "june": {
#         "name": "Oma Onyia",
#         "salary": "20000000",
#         "password": "nmesoma",
#         "email": "nmesoma@gmail.com",
#         "phone": "09012345678",
#         "occupation": "Python Developer",
#         "kid": "2",
#         "plan": "monthly",
#         "marital": "single",
#         "tax_status": "not paid",
#
#
#     }
# }
# for k_values in details:
#     print(k_values)
# if "fingers" not in "june":
#     print("pay for july")
#     # if k_values["tax_status"] == "paid":
#     #     print("paid for new month")
#     #     break
#     # else:
#     #     print("Pay for previous month")
#     #     break
#
#
# details = {
#     "august": {
#         "name": "Oma",
#         "salary": "200000",
#         "password": "dfghjm",
#         "email": "name@gmail.com",
#         "phone": "08099722221",
#         "occupation": "Doctor",
#         "kid": "1",
#         "plan": "monthly",
#         "marital": "married",
#         "tax": "21000.0",
#         "tax_status": "paid",
#         "serial_no": 1
#     },
#
#     "january": {
#         "name": "fj",
#         "salary": "40000",
 #         "password": "123",
#         "email": "fghkkl",
#         "phone": "098765432",
#         "occupation": "ippio",
#         "kid": "0",
#         "plan": "monthly",
#         "marital": "single",
#         "tax": "4000.0",
#         "tax_status": "paid",
#         "serial_no": 1
#     }
# }
# #
# # print(len(details))
#
# import random
# ran = random.randint(0, 100000000000000)
# print(ran)
# for key.values() in details:
#         key["name"  + str(ran)]
date = input("Enter a date: ")
months = ["january".casefold(), "february".casefold(), "march".casefold(), "april".casefold(),
          "may".casefold(), "june".casefold(), "july".casefold(), "august".casefold(), "september".casefold(),
          "october".casefold(), "november".casefold(), "december".casefold()]
# for i in range(0, 11):
#     print
if date in months:
    dates = months.index(date)
    print(dates)
    period = dates-1
    periods = months[period]
    print(periods)
database = \
    {
        "january": [
            {
                "name": "oma",
                "fame": "oma",
                "bame": "oma",
                "qame": "oma",
                "pame": "oma",
                "lame": "oma"
            }
        ],
        "february": [
            {
                "name": "oma",
                "fame": "oma",
                "bame": "oma",
                "qame": "oma",
                "pame": "oma",
                "lame": "oma"
            }
        ],
        "march": [
            {
                "name": "oma",
                "fame": "oma",
                "bame": "oma",
                "qame": "oma",
                "pame": "oma",
                "lame": "oma"
            }
        ],
        "april": [
            {
                "name": "peace",
                "fame": "oma",
                "bame": "oma",
                "qame": "oma",
                "pame": "oma",
                "lame": "oma"
            }
        ]
    }
username = input("Enter your name: ")
for elem in database[periods]:
    for k, v in elem.items():
        if k == "name":
            value = username
            # print(value)
for i in range(0, 12):
    while i < dates:
        dat = months[i]
        # print(dat)
        # print(database[dat])
        break

for elem in database:
    for ents in database[elem]:
        for k, v in ents.items():
            if k == "name":
                val = v
            if val == username:
                print("You have paid for ", elem)
                break
            else:
                print("You have not paid for ", elem)
                break