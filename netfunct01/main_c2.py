#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
# Importing Python3 Crayons
import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.yellow("Handshaking")}. .. ... connecting with {ip}') # fstring with Yellow
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'{crayons.red("Attempting to sending command -->")} {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

def devicereboot(devicecmd): # devicereboot==dict
    for ip2 in devicecmd.keys(): #looping thru same list as commandpush function
#        print(ip2)
        print(f'\nConnecting to ... {ip2}    REBOOTING NOW')
#        for turd in devicecmd[ip]:
#            print(f'This bitch is about to blow...'{crayons.red({turd}
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"\n\nWelcome ...\nto the \n{crayons.blue('Network')} \n{crayons.green('Device')} \n{crayons.yellow('Command')} \n{crayons.cyan('Pusher')}") # welcome message
#    print(f"Welcome to the {crayons.blue('Network')} device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd) # call function to reboot switches
# call our main function
main()

