
# =================
# practice send function as argument in another function
# =================

def loud(l_text):
    return "\n[ " + l_text.upper() + " ]"


def quiet(q_text):
    return "\n[ " + q_text.lower() + " ]"


def the_text(a_function):               # after this is called, it is going to ask user for input / text
    input_text = input("Enter a text: ").capitalize()
    if input_text.isdigit():            # just to make sure user input is not digit
        return "\n[ Invalid input - string only ]"

    else:
        this_text = a_function(input_text)  # any function that user want the text to be displayed will be called here
        return this_text


print("\n== Say something... ==")
print("1. LOUDLY")
print("2. quietly")
print("e. Exit")
choice = input("choice: ").lower()       # make user input to lower case to make while-loop condition simpler

while choice != 'e':
    if choice == '1':
        print("")
        print(the_text(loud))           # the_text function in this case is in higher order / will be called first

    elif choice == '2':
        print("")
        print(the_text(quiet))

    else:
        print("\n[ Invalid choice ]")

    print("\n== Say something ==")
    print("1. Loudly")
    print("2. Quietly")
    print("e. Exit")
    choice = input("choice: ").lower()

print("\n== Exit Program ==")
