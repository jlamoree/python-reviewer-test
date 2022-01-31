def main():
    ask_again = True
    operations_count = 0
    while ask_again:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        result = perform_division(a, b)
        print(result)
        operations_count += 1
        ask_again = input("Do you want to perform another operation? Enter yes or no: ")
        if ask_again == 'yes':
            ask_again = True
        else:
            ask_again = False
            print(f"You performed {operations_count} operations, bye!")


def perform_division(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError as e:
        return "Nope. Can't divide by zero."


main()
