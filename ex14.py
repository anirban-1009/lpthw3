from sys import argv

first, second = argv
prompt = '>'

print(f"Hi {second}, I'm {first}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {second}?")
likes = input(prompt)

print(f"Where do you live {second}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")