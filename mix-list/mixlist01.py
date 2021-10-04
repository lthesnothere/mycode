#!/usr/bin/env python3
# Define List
my_list = [ "192.168.0.5", 5060, "UP" ]
# Print the first item in the list
print("The first item in the list (IP): " + my_list[0] )
# Print the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )
# Print the last item in the list
print("The last item in the list (state): " + my_list[2] )

## Challenge 01
print()
print("This is the Challenge section below")
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# Print the IP addresses from list 'iplist'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
