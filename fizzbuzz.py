def main():
    """
    The “Fizz-Buzz test” is an interview question designed to help filter out the 99.5% of programming
    job candidates who can’t seem to program their way out of a wet paper bag.
    Write a program that prints the numbers from 1 to 100, followed by a new line. But for multiples of
    three print Fizz instead of the number and for the multiples of five print Buzz. For numbers which
    are multiples of both three and five print FizzBuzz.
    Each number or word should be separated by a space"""
    x = 0
    while x <= 100:
        x += 1

        if x % 3 == 0 and x % 5 != 0:
            print('fizz')

        elif x % 5 == 0 and x % 3 != 0:
            print('buzz')

        elif x % 5 == 0 and x % 3 == 0:
            print('fizzbuzz')
        else:
            print(x, end=", ")


if __name__ == "__main__":
    main()