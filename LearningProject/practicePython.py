import random
import string
import secrets
import requests
from bs4 import *
from threading import *
import json
from collections import Counter
from bokeh.plotting import figure, output_file, show

def character_input(name, age, show):
    diff = 100 - age
    print(show * "You'll be 100 on other ", diff, " Years \n")

def divisors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return factors

def list_overlap(lst1, lst2):
    commons = []
    for num in lst1:
        if num in lst2:
            commons.append(num)

    return list(set(commons))

def palindrome_string(text):
    exp_text = text.lower()[::-1]
    if text.lower() == exp_text:
        print('it is palindrome')
    else:
        print('not palindrome')
def list_ends(lst):
    ends = []
    ends.append(lst[0])
    ends.append(lst[len(lst)-1])
    print(ends)

def password_generator(pass_length):
    pass_char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(pass_char) for _ in range(pass_length))

def decode_webpage(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('h2'):
        print(link.text)

def decode_webpage_2(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    dir = '/home/syed/Documents/PyDocs/'
    with open(dir+'file_to_save.txt', 'w') as open_file:
        for text in soup.find_all('p'):
           open_file.write('\n\n'+ text.text)

def reverse_word_order(text):
    return ' '.join(text.split()[::-1])

def element_search(ordered_list, element_to_search):
    if element_to_search  in ordered_list:
        return True
    return False

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def read_file(file_dir):
    counter_dict = {}
    with open(file_dir, 'r') as file:
        line = file.readline()
        while line:
            line = line.split('/')[2]
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = file.readline()

    return counter_dict
def file_to_list_of_ints(file_dir):
    nums_list = []
    with open(file_dir, 'r') as file:
        num = file.readline()
        while num:
            nums_list.append(int(num))
            num = file.readline()
    return nums_list

def is_in_list(list, n):
    list = sorted(list)
    lower = 0
    up = len(list) - 1
    guess = 0

    while lower <= up:
        mid = (lower + up) // 2
        guess += 1
        if list[mid] == n:
            print('found at ', mid)
            print(guess)
            break
        elif list[mid] < n:
            lower = mid + 1
        else:
            up = mid - 1

# decode_webpage('https://www.nytimes.com/')
# decode_webpage_2('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')

# text = input('Enter a text')
# result = reverse_word_order(text)
# print(result)

# class hello(Thread):
#     def gen(self):
#         for i in range(10):
#             print("gent", i)
#
# class hi(Thread):
#     def gun(self):
#         for i in range(10):
#             print("dice", i)
#
# t1 = hello()
# t2 = hi()
#
# t1.start()
# t1.gen()
# t2.start()
# t2.gun()
num = [2,3,23,5,3,5,323,21,42,54,23,65,744,33]
print(sum(num))
mul = 1
for ele in num:
    mul *= ele
print(mul)
print(max(num))
print(min(num))
print(set(num))
print( 'not empty' if len(num)>0 else 'empty')
print(num.copy())
str_lst = ['abc', 'xyz', 'aba', '1221', 'reer', 'jj', 'kewyertk']
count = 0
for txt in str_lst:
    if len(txt) >= 2:
        if txt[0] == txt[(len(txt)-1)]:
            count+=1
print(count)
tup_lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)
print(sort_list_last(tup_lst))

bd_dict = {
    "abbu": "20/08/1968",
    "ammi": "26/10/1974",
    "firoz": "05/02/1995",
    "afrid": "12/03/1997",
    "arshad": "23/05/1999"
}
# while True:
#     bd_per = input("Who's birthday do you want to look up?: ").lower()
#     print("{}'s birthday on {}"
#         .format(bd_per, bd_dict.get(bd_per, r'DD/MM/YYYY')))

with open('/home/syed/Documents/PyDocs/birthday.json', 'w') as file:
    json.dump(bd_dict, file)
with open('/home/syed/Documents/PyDocs/birthday.json','r') as bd_doc:
    bd = json.load(bd_doc)
bd_per = input("Who's birthday do you want to look up?: ").lower()
print("{}'s birthday on {}"
        .format(bd_per, bd.get(bd_per, r'DD/MM/YYYY')))

months = []

num_to_string = {
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

for month in bd.values():
    bd_month = int(month.split('/')[1])
    months.append(num_to_string.get(bd_month))
print(Counter(months))
# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)