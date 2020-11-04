import random
import string
import secrets
import requests
from bs4 import *
from threading import *

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

# n = 100
# ind = -1
# nums = [45, 65, 78, 87, 98, 123, 234, 567, 5678]
#
# is_in_list(nums, 5678)

fun = [[0 for col in range(3)] for row in range(3)]
print(fun)
for i in range(9):

    # user_ip = input('please select a square to tick(in format row,col): ').split(',')
    # row = int(user_ip[0])
    # col = int(user_ip[1])
    # fun[row][col] = 'X' if i % 2 == 0 else 'O'
    # print(fun)
    print(i+1)


