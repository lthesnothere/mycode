#!/usr/bin/env python3
# Display useful interface information.

# Import Libraries:
import netifaces

# Print the known interfaces
def display_interfaces()
print('Type an interface from the following list:')
print(netifaces.interfaces())


for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
#    print(netifaces.ifaddresses(i))
#    print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
    try:
        print('MAC:  ', end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP:   ', end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Could not collect adaptor information') #Prints an error message.
