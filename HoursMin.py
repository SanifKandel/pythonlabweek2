#Given the integer the number of min that passed since midnight - how many hours and min are displayed on the 24 hr
#clock import time. The program should print two numbers the number of hours ( between 0 and 23) and the number of
#minutes (between 0 and 59).

"""userInput = int(input("Enter the no of min that has passed since midnight (In Min):"))
checklogic = True
while checking == True:
    checklogic = False
if userInput > 60:
    intHour = 0
    userInput -= 60
elif user
    """
N = int(input("Enter the no of min that has passed since midnight (In Min):"))
hours = (N//60)
minutes = (N%60)
print (f"The hours is {hours}")
print (f"The minutes is {minutes}")
print(f"Its {hours}:{minutes} now")