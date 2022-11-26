from matplotlib import pyplot as plt
from matplotlib import style, figure
import pandas as pd
import numpy as np
import csv

black_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
class Number:
    def __init__(self, num):
        self.num = num
        self.even = 0
        self.odd = 0
        self.red = 0
        self.black = 0
        self.low = 0
        self.high = 0
        self.first_twlv = 0
        self.sec_twlv = 0
        self.third_twlv = 0
        self.first_col = 0
        self.sec_col = 0
        self.third_col = 0
        
        # 0 
        if self.num < 1:
            pass
        else:
            #even or odd
            if self.num%2 == 0:
                self.even = 1
            else:
                self.odd = 1

            #red or black
            if self.num in black_list:
                self.black = 1
            else:
                self.red = 1

            #low or high
            if self.num <= 18:
                self.low = 1
            elif self.num >=19:
                self.high = 1
            
            #cols
            if self.num%3==1:
                self.first_col = 1
            elif self.num%3==2:
                self.sec_col = 1
            else:
                self.third_col = 1

            #twlvs
            if 1 < self.num < 13:
                self.first_twlv = 1
            elif 13 <= self.num < 25:
                self.sec_twlv = 1
            else:
                self.third_twlv = 1



csv_file = pd.read_csv('numbers.csv')


def create_csv():
    nums = np.random.randint(-1, 37, size=10000)
    with open('numbers.csv', 'w', newline='') as f:
        fieldnames = []
        a = Number(nums[0])
        for k in a.__dict__.keys():
            fieldnames.append(k)
        wf = csv.DictWriter(f, fieldnames=fieldnames)
        wf.writeheader()
        for num in nums:
            x = Number(num)
            wf.writerow(vars(x))

def add_label(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])

def straight_up():
    with open('numbers.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        straight_up = {}
        for row in data:
            num = int(row['num'])
            if num not in straight_up:
                straight_up[num] = 0
            straight_up[num] +=1
    straight_up_sorted = {k: straight_up[k] for k in sorted(straight_up)}

    style.use('fivethirtyeight')
    bins = np.arange(-1, 37)
    plt.bar(list(straight_up_sorted.keys()), list(straight_up_sorted.values()))
    add_label(list(straight_up_sorted.keys()), list(straight_up_sorted.values()))
    plt.xlabel('numbers')
    plt.ylabel('amount')
    plt.xticks(bins)
    plt.show()

def red_black(csv_file):
    style.use('fivethirtyeight')
    
    red_sum = csv_file['red'].sum()
    plt.bar("red", red_sum, color="#FF0000", width=0.8)
    plt.text("red", red_sum, red_sum)

    black_sum = csv_file['black'].sum()
    plt.bar("black", black_sum, color="black", width=0.8)
    plt.text("black", black_sum, black_sum)
    
    plt.title('Red vs Black')
    plt.tight_layout()
    plt.show()

def even_odd(csv_file):
    style.use('fivethirtyeight')

    even_sum = csv_file['even'].sum()
    plt.bar("even", even_sum, color="#FF0000", width=0.8)
    plt.text("even", even_sum, even_sum)

    odd_sum = csv_file['odd'].sum()
    plt.bar("odd", odd_sum, color="#444444", width=0.8)
    plt.text("odd", odd_sum, odd_sum)
    
    plt.title('even vs odd')
    plt.tight_layout()
    plt.show()

def low_high(csv_file):
    style.use('fivethirtyeight')

    low_sum = csv_file['low'].sum()
    plt.bar("low", low_sum, color="#FF0000", width=0.8)
    plt.text("low", low_sum, low_sum)

    high_sum = csv_file['high'].sum()
    plt.bar("high", high_sum, color="#444444", width=0.8)
    plt.text("high", high_sum, high_sum)
    
    plt.title('low vs high')
    plt.tight_layout()
    plt.show()

def twelve(csv_file):
    style.use('fivethirtyeight')
    first_twlv_sum = csv_file['first_twlv'].sum()
    plt.bar("first_twlv", first_twlv_sum, color="#FF0000", width=0.8)
    plt.text("first_twlv", first_twlv_sum, first_twlv_sum)

    sec_twlv_sum = csv_file['sec_twlv'].sum()
    plt.bar("sec_twlv", sec_twlv_sum, color="#444444", width=0.8)
    plt.text("sec_twlv", sec_twlv_sum, sec_twlv_sum)

    third_twlv_sum = csv_file['third_twlv'].sum()
    plt.bar("third_twlv", third_twlv_sum, color="#444444", width=0.8)
    plt.text("third_twlv", third_twlv_sum, third_twlv_sum)

    plt.title('Twelves')
    plt.tight_layout()
    plt.show()

def columns(csv_file):
    style.use('fivethirtyeight')
    first_col_sum = csv_file['first_col'].sum()
    plt.bar("first_col", first_col_sum, color="#FF0000", width=0.8)
    plt.text("first_col", first_col_sum, first_col_sum)

    sec_col_sum = csv_file['sec_col'].sum()
    plt.bar("sec_col", sec_col_sum, color="#444444", width=0.8)
    plt.text("sec_col", sec_col_sum, sec_col_sum)

    third_col_sum = csv_file['third_col'].sum()
    plt.bar("third_col", third_col_sum, color="#444444", width=0.8)
    plt.text("third_col", third_col_sum, third_col_sum)

    plt.title('Twelves')
    plt.tight_layout()
    plt.show()



create_csv()
straight_up()
red_black(csv_file)
even_odd(csv_file)
low_high(csv_file)
twelve(csv_file)
columns(csv_file)

