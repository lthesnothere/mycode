#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = "You must specify a time of day between 0 & 24."
message_1 = 'Your bedtime is scheduled for '+ 

# wrap connection in a float() to accept decimals as numbers
bedtime = float(input("What time do you go to bed?"))

# if input value was higher or equal to 25
if bedtime > 24:
    message_1 = 'There are not that many hours in a day. '+ message
elif bedtime >= 23:
    message_1 = message_1 + 'That is pretty late.'
elif bedtime >= 21:
    message_1 = message_1 + 'You must be an early riser.'
else:
    message_1 = message_1 + 'That is a strange sleep habit.'
print(message_1)
