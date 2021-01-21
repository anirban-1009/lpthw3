from sys import argv

script = argv
filename = "ex15_sample.txt"
txt = open(filename)

print(f"here is your file {filename}:")
print(txt.read())
print("\n\n\n")



print("Type the filename")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())