import sys

#Get book filename and what we're doing
mode = sys.argv[1]
book = sys.argv[2]

#Output whole book
def read(book):
	with open(f"books/{book}") as f:
		file = f.read()
		print(file)

def letters(file):
	letter_list = {}
	not_letters = (
		",", " ", ".", "%", "*", "'", "(",
		 ")", "\n", "-", "_", "?", "$", "/",
		 "\"", "[", "]", ";", ":", "!", "@",
		 "#", "1", "2", "3", "4", "5", "6",
		 "7", "8", "9", "0"
	)
	for words in file:
		for letter in words:
			lower_letter = letter.lower()
			if lower_letter not in not_letters:
				if lower_letter in letter_list:
					letter_list[lower_letter] += 1
				else:
					letter_list[lower_letter] = 1
	print(letter_list)

def main():
	with open(f"books/{book}") as f:
		file = f.read()
		if mode == "words":
			print(f"Word count: {len(file.split())}")
		elif mode == "letters":
			letters(file)
		elif mode == "read":
			read(book)
		else:
			print("Useage is \"python3 main.py MODE BOOK.txt\"")

main()
