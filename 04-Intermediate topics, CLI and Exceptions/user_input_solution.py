def get_float():
    while True:
        try:
            num = float(input("Give me a number: "))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
    return num

num = get_float()
print("This is the number you have given me: {:.2f}".format(num))
