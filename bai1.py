f = open("files.txt", "w")
for num in range(1, 30000001):
    if num % 15 == 0:
        f.write("FizzBuzz\n")
    elif num % 5 == 0:
        f.write("Fizz\n")
    elif num % 3 == 0:
        f.write("Buzz\n")
    else:
        f.write(str(num) + "\n")

f.close()
