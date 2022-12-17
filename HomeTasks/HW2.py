nubrer_or_word = input()

if nubrer_or_word.isdigit():
    print("It's numer.")
    if int(nubrer_or_word) % 2 == 0:
        print("This even numer")
    else:
        print("This not even numer")
else:
    print(f"This word have {len(nubrer_or_word)} etters.")