import time
import random

list_random = []
list_check = []

how_seconds = int(input("Enter seconds: "))

for i in range(0, 10):
    list_random.append(random.randint(1, 100))
    print(list_random[i])

time.sleep(how_seconds)

for i in range(0, 10):
    check_number = int(input("Enter number: "))
    list_check.append(check_number)

if list_random == list_check:
    print("you are winner")
else:
    print("no")
