
keep_playing = True

print("Welcome to Is It Prime? \n")

while keep_playing:
    num = int(input("Enter a number: "))

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num//i, "is", num)
                print("Try again\n")
        else:
            print(num, "is a prime number")
            play_again = input(
                "Would you like to try another number? Type 'y' is Yes or 'n' if No\n")
            if play_again.lower() == "n":
                keep_playing = False

    else:
        print(num, "is not a prime number")
