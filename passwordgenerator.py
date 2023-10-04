# Lessons from Vinsloev Academy 

import random
import string

def generate_password(length=12):
    # Define characters to use in the password
      characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters
      password = ''.join(random.choice(characters) for _ in range(length))

      return password

if __name__ == "__main__":
      password_length = int(input("Enter the desired password length"))
      if password_length < 6:
          print("Password length must be at least 6 character" )
      else:
          desired_password = generate_password(password_length)
          print("generated Password:", desired_password)
