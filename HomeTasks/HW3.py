#TASK 1
text = input('Enter the text: ')

for letter in text:
    if letter.isdigit():
        if int(letter) % 2 == 0:
            print(f"{letter} even numer")
        else:
            print(f"{letter} not even numer")
    elif letter.isalpha():
        if 'A' <= letter <= 'Z':
            print (f"{letter} big letter")
        else :
            print(f"{letter} small letter")
    else:
        print (f"{letter} it's symbol")


# TASK 2
x = 'I love Python'
import time

for _ in x:
    time.sleep(4.2)
    print(x)

