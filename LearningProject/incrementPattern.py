from bokeh.plotting import figure, output_file, show
import json
from collections import Counter


for i in range(1,5):
    for j in range(i,5):
        print(j, end=" ")
    print()


output_file("Birthday_Month_Histogram_using_Bokeh_Libs.html")

months = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]

num_to_string ={
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
}

with open('/home/syed/Documents/PyDocs/birthday.json', 'r') as birth_doc:
    birthdays = json.load(birth_doc)

birthday_months = []

for bd_month in birthdays.values():
    month = int(bd_month.split('/')[1])
    act_mon = num_to_string.get(month)
    birthday_months.append(act_mon)

birthday_months = Counter(birthday_months)
mon = list(birthday_months.keys())
count = list(birthday_months.values())
print(mon)

pic = figure(x_range=months)
pic.vbar(x=mon, top=count, width=0.5)
show(pic)
