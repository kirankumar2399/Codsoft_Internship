import random

# Define the possible characters for the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter the length of the password: "))

# Generate a password of the specified length using random characters
password = ""
for i in range(length):
  password += random.choice(characters)

# Display the password on the screen
print("Your password is:", password)
