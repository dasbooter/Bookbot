import sys

def output(book):
	with open(f"books/{book}") as f:
		file = f.read()
		print(file)

output(sys.argv[1])
