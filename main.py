import sys

#Get book filename and what we're doing
mode = sys.argv[1]
book = sys.argv[2]

#Output whole book
def read(book):
	with open(f"books/{book}") as f:
		file = f.read()
		print(file)

def main():
	with open(f"books/{book}") as f:
		file = f.read()
		if mode == "words":
			print(f"Word count: {len(file.split())}")
		elif mode == "read":
			read(book)
		else:
			print("Useage is \"python3 main.py MODE BOOK.txt\"")
main()
