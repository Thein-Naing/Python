import random
import pyautogui
import string

# You can add symbols and all other characters in chars.
# chars = "abcdefghijklmnopqrstuvwxyz0123456789"

chars = string.printable
chars_list = list(chars)

password = pyautogui.password("Enter your password: ")

guess_password = ""

while (guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<==================" + str(guess_password) + "==================>")

    if (guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break
