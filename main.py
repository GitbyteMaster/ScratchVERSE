import os
import getpass

val = ""
def curl(obj):
    os.system(f"curl {obj} > /Users/$USER/Desktop/ScratchVERSE/getcurl")
curl("https://api.scratch.mit.edu")
if open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/getcurl","r").read() == "":
    print("\nScratchVerse can't connect to the Internet or Scratch API. Please try again later.")
else:
    print("Login to ScratchVerse:\n====================")
    username = input("Username: ")
    password = input("Password: ")
    if open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/userinfo.txt","r").read() == "":
        curl(f"https://api.scratch.mit.edu/users/{username}")
        if not open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/getcurl","r").read() == "":
            val = open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/getcurl","r").read()
            n = val.index("\"bio\":")+6
            i = ""
            while not val[n+1] == "\"":
                n += 1
                i = f"{i}{val[n]}"
            open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/userinfo.txt", "w+").write(f"{username}\n{i}")
    print("\nLoading ScratchVERSE..")
    open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/home.svg", "w").write("")
    val = open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/home-top.svg", "r").read()
    n = 0
    i = "<"
    while not n+1 == val.index("USER"):
        n += 1
        i = f"{i}{val[n]}"
    i = f"{i}{username}"
    n += 4
    while not n == len(val)-1:
        n += 1
        i = f"{i}{val[n]}"
    curl(f"https://api.scratch.mit.edu/users/{username}")
    if not"{\"code\":\"ResourceNotFound\"," in open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/getcurl","r").read():
        open(f"/Users/{getpass.getuser()}/Desktop/ScratchVERSE/home.svg", "r+").write(i)
        os.system("open /Users/$USER/Desktop/ScratchVERSE/home.svg")
    else:
        print("\nThis user doesn't exist.")
