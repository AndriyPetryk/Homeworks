x = input()

if x.isdigit():
    print("It's numer.")
    if int(x) % 2 == 0:
        print("This even numer")
    else:
        print("This not even numer")
else:
    print("This word have" + ' ' + str(len(x)) + ' ' + 'letters.')