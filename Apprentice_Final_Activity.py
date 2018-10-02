"""Write a program with a menu that has the following options:
Accept and store a string
Basic Calculator 
Print the previously stored string
Compare 2 numbers to determine the larger
Remove a selected letter from a string """
import operator

saved_string = ""


def remove_letter():  # Remove a selected letter from a string
    base_string = str(raw_input("Enter a string: "))
    letter_remove = str(raw_input("Enter a letter: "))  # takes any size string
    letter_remove = letter_remove[0]
    string_length = len(base_string)
    location = 0

    while location < string_length:  # by reference (rather than by value)
        if base_string[location] == letter_remove:
            base_string = base_string[:location] + base_string[location + 1 : :]
            string_length -= 1
        location += 1

    print("Result: %s" % base_string)
    return


def num_compare():  # Compare 2 numbers to determine the larger

    num1 = int(raw_input("Enter first number "))
    num2 = int(raw_input("Enter second number "))

    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print("The numbers are equal")

    return


def print_string():  # Print a the previously stored string
    print(saved_string)
    return


def calculator():  # Basic Calculator
    sign_dict = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.div,
    }

    num1 = int(raw_input("Input first number "))
    sign = str(raw_input("Action: "))
    num2 = int(raw_input("Input second number "))

    print(sign_dict[sign](num1, num2))

    return


def accept_and_store():  # Accept and store a string
    global saved_string
    saved_string = str(raw_input("Enter a string: "))
    return


def main():  # menu goes here
    opt_list = [accept_and_store, calculator, print_string, num_compare, remove_letter]

    while True:
        print("SELECT AN OPTION")
        print("1\tAccept and Store")
        print("2\tCalculator")
        print("3\tPrint stored string")
        print("4\tNumber Comparison")
        print("5\tLetter Removal")
        opt_choice = int(raw_input("Make a selection "))
        opt_choice -= 1
        opt_list[opt_choice]()

    return


main()
