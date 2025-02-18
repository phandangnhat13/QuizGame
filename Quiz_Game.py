import gspread
import random
from datetime import datetime
from termcolor import colored, cprint
import sys
import os
import time


gc = gspread.service_account("secret_key.json")
sh = gc.open("Countries and Capitals")
wk = sh.worksheet("Data")

#print(wk.cell(2, 1).value)
#print(wk.acell("A2").value)
#print(wk.get("A2:A10"))
#wk.update(range_name="A4", values=[["Democratic Republic of the Congo"]])
#wk.update(range_name="D1", values=[["=SUM(C2:C)"]], raw=False)
#wk.update(range_name="A241:C241", values=[["Data Country", "Fact", "1"]])

#num_rows = len(wk.col_values(1))
#print(num_rows)

#random_row = random.randint(2, num_rows)
#print(random_row)

#country = wk.cell(random_row, 1).value
#capital = wk.cell(random_row, 2).value
#print(f"Country: {country}, Capital: {capital}")

tests = int(input(colored("How many tests do you want to do? >>", "magenta")))
tests_start = tests
points = 0
today = datetime.today()
day = today.strftime("%Y-%m-%d")
time_hm = today.strftime("%H:%M")
# num_rows = len(wk.col_values(1))
num_rows = 10

logs = sh.worksheet("Logs")
id = logs.acell("A2").value or 0
logs.insert_row([int(id) + 1, day, time_hm, tests], 2)


def get_random():
    while True:
        random_row = random.randint(2, num_rows)
        if wk.cell(random_row, 6).value != str(day):
            return random_row
while tests > 0:
    os.system("cls")
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2K")
    cprint(f'Test left 👉 {tests} | Points 👉 {points} | Correct 👉 {round(points/tests_start*100, 2)}%',
           "cyan", "on_blue", attrs=["bold"])
    tests -= 1
    random_row = get_random()
    country = wk.cell(random_row, 1).value
    capital = wk.cell(random_row, 2).value

    no_of_tests = wk.cell(random_row, 4).value or 0
    correct = wk.cell(random_row, 5).value or 0
    wk.update_cell(random_row, 6, str(day))
    wk.update_cell(random_row, 4, int(no_of_tests) + 1)

    cprint((f"What is the capital of {country!r}? : "), "magenta")
    answer = input(">> ")
    if answer == capital:
        cprint(("✔ Correct. \u2776 point"), "green")
        points += 1
        wk.update_cell(random_row, 5, int(correct) + 1)
    else:
        cprint(f"❌ Wrong. Correct answer is ", "magenta", end="")
        cprint(f"{capital}", "red", attrs=["bold", "underline"])
    time.sleep(1)

logs.update_cell(2, 5, points)


def summary():
    os.system("cls")
    score = "points" if points > 1 else "point"
    c_asterisk = "red"
    c_background = "on_blue"
    c_border = "on_green"
    cprint("*"*50,
           c_asterisk, c_border, attrs=["bold"])
    cprint("*",
           c_asterisk, c_border, attrs=["bold"], end="")
    cprint(" "*48,
           c_asterisk, c_background, attrs=["bold"], end="")
    cprint("*",
           c_asterisk, c_border, attrs=["bold"])
    cprint("*", c_asterisk, c_border, attrs=["bold"], end="")
    cprint(f'🏆 You got {points} {score} 🏆. Correct {round(points/tests_start*100, 2)}%'.center(46),
           "magenta", c_background, attrs=["bold"],  end="")
    cprint("*", c_asterisk, c_border, attrs=["bold"])
    cprint("*",
           c_asterisk, c_border, attrs=["bold"], end="")
    cprint(" "*48,
           c_asterisk, c_background, attrs=["bold"], end="")
    cprint("*",
           c_asterisk, c_border, attrs=["bold"])
    cprint("*"*50,
           c_asterisk, c_border, attrs=["bold"])


summary()