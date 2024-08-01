#!usr/bin/env python3

# By running this script anybody can change mode from monitor to managed or vice versa

import subprocess    # This Library is used to run commands of present OS uing python

def getMode()->str:
    Standardoutput = subprocess.run(["sudo","iw","dev"],capture_output=True,text=True).stdout.split("\n\t\t")
    # Firstly runing the command and taking the output using stdout function than making list of output attributes by spliting
    for line in Standardoutput: # Extracting the type info from list
        temp = line.split(" ")
        if temp[0] == 'type':
            Current_mode = temp[1]     # Type could be either managed or monitor
            break
    return Current_mode

def changeMac(Current_mode):
    subprocess.run(["sudo","ifconfig","wlan0","down"])
    if Current_mode == 'managed':        # Based on the present state wlan0 changing mode accordingly
        subprocess.run(["sudo","airmon-ng","check","kill"])
        subprocess.run(["sudo","iwconfig", "wlan0", "mode", "monitor"])
    else:
        subprocess.run(["sudo","iwconfig","wlan0","mode","managed"])
        subprocess.run(["sudo","systemctl","restart","NetworkManager"])   # It's important to restart the network manager as it's become disable after airmon kill

    subprocess.run(["sudo","ifconfig","wlan0","up"])


if __name__ == "__main__":
    Current_mode = getMode()
    print("Current mode is:",Current_mode)
    ans = input("Do you want to change? type Y?N-->")
    if ans == 'Y' or ans == 'y':                # Taking user intraction
        changeMac(Current_mode)
        print("Mode changed succesfully!!")
    elif ans == 'N' or ans == 'n':
        print("Mode not changed")
        exit()
    else:
        print("Invalid input \n Kindly re-run to program with correct inputs\n\t Correct inputs are Y/N or y/n")
        exit()

