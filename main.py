from datetime import date
import datetime
import os
import sys

now = datetime.datetime.now() #Set today's date

class Date:
    def __init__(self, x):
        for i in range(0, len(x)):
            if (x[i] == '/'):
                slashpos = i
                break
        self.month = int (x[:slashpos:])
        self.day = int (x[(slashpos + 1)::])

def convert_month(x):
    calendar = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]
    return (calendar[x - 1])

def convert_date(x):
    if (x == 1):
        return str(x) + "st"
    elif (x == 2):
        return str(x) + "nd"
    elif (x == 3):
        return str(x) + "rd"
    else:
        return str(x) + "th"

def daysApart(birth):
    #Returns the amount of days apart from the two dates passed in
    #birth should be the Date of the birthday that is being tested
    x = date(now.year, now.month, now.day)
    y = date(now.year, birth.month, birth.day)
    dif = y - x
    if (dif.days < 0):
        y = date(now.year + 1, birth.month, birth.day)
        dif = y - x

    return dif.days

def main():
    print ()

    script_dir = os.path.dirname(__file__) #Absolute dir the script is in
    rel_path = "birthdays.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as b: #Take in birthdays
        birthdays = b.readlines()
    birthdays = [x.strip() for x in birthdays]
    for i in range(0, len(birthdays)): #Removes years from dates
        birthdays[i] = birthdays[i][:-5]
    for i in range(0, len(birthdays)): #Format birthdays
        birthdays[i] = Date(birthdays[i])

    script_dir = os.path.dirname(__file__) #Absolute dir the script is in
    rel_path = "names.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as n: #Take in names
        names = n.readlines()
    names = [x.strip() for x in names] #Format names

    distance = [] #Holds the amount of days each birthday is from today
    for i in range(0, len(birthdays)):
        distance.append(daysApart(birthdays[i]))

    final = [0]
    for i in range(1, len(distance)):
        if (distance[i] == distance[final[0]]):
            final.append(i)
        elif (distance[i] < distance[final[0]]):
            final = [i]

    if (distance[final[0]] == 0):
        for i in range(0, len(final)):
            print("Today is " + names[final[i]] + "'s birthday!")
    else:
        for i in range(0, len(final)):
            print("The next birthday is " + names[final[i]] + "'s on " +
            convert_month(birthdays[final[i]].month) + " " +
            convert_date(birthdays[final[i]].day) + ".")

    b.close()
    n.close()
    return 0

if __name__ == "__main__":
    main()
