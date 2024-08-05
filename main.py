import sys

#Global variables
#mode = sys.argv[2]
book = sys.argv[1]
letter_list = {}
not_letters = (
	",", " ", ".", "%", "*", "'", "(",
	 ")", "\n", "-", "_", "?", "$", "/",
	 "\"", "[", "]", ";", ":", "!", "@",
	 "#", "1", "2", "3", "4", "5", "6",
	 "7", "8", "9", "0"
)

#Prints selection menu
def print_menu(menu, selected_index):
    for i, option in enumerate(menu):
        if i == selected_index:
            print(f"> {option}")
        else:
            print(f"  {option}")

#Print count of individual letters
def letters(file):
	for words in file:
		for letter in words:
			lower_letter = letter.lower()
			if lower_letter not in not_letters:
				if lower_letter in letter_list:
					letter_list[lower_letter] += 1
				else:
					letter_list[lower_letter] = 1
	print(letter_list)

def main(book):
    try:
        with open(f"books/{book}") as f:
            file = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{book}' was not found.")
        return

    menu = ["Read", "How many Words?", "How many Letters?", "Exit"]
    current_index = 0

    while True:
        print("\n" * 100)  # Clear the screen by printing newlines
        print_menu(menu, current_index)

        print("\nUse 'w' to move up, 's' to move down, and 'enter' to select.")

        # Get user input
        key = input().strip().lower()

        if key == "w" and current_index > 0:
            current_index -= 1
        elif key == "s" and current_index < len(menu) - 1:
            current_index += 1
        elif key == "":
            if current_index == 0:  # Read
                print(file)
                break
            elif current_index == 1:  # How many Words?
                word_count = len(file.split())
                print(f"Word count: {word_count}")
                input("Press Enter to continue...")
            elif current_index == 2:  # How many Letters?
                letters(file)
                input("Press Enter to continue...")
            elif current_index == 3:  # Exit
                print("Exiting...")
                break
        else:
            print("Invalid input. Use 'w', 's', or ENTER.")
            input("Press Enter to continue...")

main(sys.argv[1])
