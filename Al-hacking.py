from __future__ import print_function
try:
    from googlesearch import search
except ImportError:
    print("")

import sys
import time

if sys.version[0] in "2":
    print ("\n[:(] AL-SEARCH is not supported for Python 2. Use Python 3 to continue!! \n")
    print ("\n[:)]  THANKS FOR USING AL-SEARCH!! ;)\n\n")
    exit()

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

banner = (""" 
     █████╗ ██╗             ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
    ██╔══██╗██║             ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╚══██║
    ███████║██║     ███████╗███████╗█████╗  ███████║██████╔╝██║     ███████║
    ██╔══██║██║     ╚══════╝╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
    ██║  ██║███████╗        ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝        ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝v1.0""")

for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  4lbH4cker
                Github:  https://github.com/4lbH4cker""")
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\t[:)]: Hello, I hope you enjoy this tool!! \n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)

try:
    data = input("\n[:|] Do you want this tool to save the searches in a txt file? ( Y (yes) / N (no) ): ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[:(] User interruption occurred..!\033[0m")
        time.sleep(0.5)
        print ("\n\n\t\033[:)]: Hello, I hope you enjoy this tool!!\n\n")
        time.sleep(0.5)
        sys.exit(1)

def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()

if data.lower().startswith("y"):
    l0g = input("[:)] Enter a name for your file!!: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[:)] Saving has been skipped...!!")
    print ("\n" + "  " + "»" * 78 + "\n")

def dorks():
    try:
        dork = input("\n[:)] What do you want AL-SEARCH to look for!!: ")
        amount = input("[:)] How many webpages do you want to display??: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[:)] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            if l0g != "":
                logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[:(] User interruption occurred..!\033[0m")
            time.sleep(0.5)
            print ("\n\n\t\033[:)]: I hope you enjoy this tool!!\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Everything clear... Exiting...")
    print ("\n\t\t\t\t\033[34mAL-SEARCH\033[0m")
    print ("\n\n\t\033[:)]: I hope you enjoy this tool!!\n\n")
    sys.exit()

#Main 
if __name__ == "__main__":
    dorks()