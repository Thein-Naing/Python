# Lessons from Vinsloev Academy 

import hashlib

def crackhash(inputPass):
    try:
        passFile = open("password", "r")
    except:
        print("Could not find file")

    for password in passFile:
        encPass = password.encode("utf-8")
        digest = hashlib.md5(encPass.strip()).hexdigest()
        if digest == inputPass:
            print("Password Found" + password)
if __name__ == "__main__":
        crackhash("1a1dc91c907325c69271ddf0c944bc72")
