result = []

for number in range(1,101):

    if number % 15 == 0:

        result.append("FizzBuzz")

    elif number % 3 == 0:

        result.append("Fizz")

    elif number % 5 == 0:

        result.append("Buzz")

    else:
        result.append(number)

print(result)
