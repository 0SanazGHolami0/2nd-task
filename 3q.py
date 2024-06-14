d = 0.1
def Calculate_Magic_Numbers(a, b, count_, d):
    for i in range(1, count_ + 1):
        print(d * (b - a) * a)
        d += 0.001

starts = int(input(""))
end = int(input(""))
count_ = int(input("How many? "))
Calculate_Magic_Numbers(starts, end, count_, d)

#-------------------------------------------------

import random
from time import perf_counter

def exam_numbers():
    cout_t = []
    cout_f = []

    p = perf_counter()

    while True:
        n = random.randint(0, 16)
        print(bin(n))
        a = input("your guess: ")

        if a == n:
            cout_t.append("True")
        else:
            cout_f.append("False")
        
        q = perf_counter()
        if q - p >= 20:
            break
    return cout_t, cout_f

print(exam_numbers())


#--------------------------------------------

import string

def check_pass(li):
    lower_ = string.ascii_lowercase
    upper_ = string.ascii_uppercase
    symbols_ = "~!@#$%^&*()_+=-><|"

    for i in li:
        if len(i[1]) == 8:
            for x in i[1]:
                if x in upper_:
                    B = True
            if B == True:
                for x in i[1]:
                    if x in lower_:
                        C = True
            if C == True:
                for x in i[1]:
                    if x in symbols_:
                        print(i[1])
                        break                

li_karbar = []
while True:
    w1 = input("\nenter both with a split in the middle: ")
    if w1 == ("exit"):
        break
    w2 = w1.split(" ")
    w3 = tuple(w2)
    print(w3)
    li_karbar.append(w3)

print(li_karbar)
check_pass(li_karbar)




