import random

# Create a list of uppercase and lowercase letters
words = []
for i in range(26):
    words.append(chr(65 + i))  # Uppercase letters (A-Z)
    words.append(chr(97 + i))  # Lowercase letters (a-z)

# Function to generate a random password
def generate_password(length, words):
    password = ""
    for i in range(length):
        index = random.randint(0, 51)  # Random index between 0 and 51
        password += words[index]
    return password

# Input length and generate the password
length = int(input("Enter the length of the password: "))
password = generate_password(length, words)
print(f'The randomly generated password is {password}')
