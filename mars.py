import sys,time,random
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
playername = str(input("What is your name? "))
print('')
print_slow('Welcome to the Martian Trail, %s.\n\n' % playername)
time.sleep(1) # delays for 1 seconds

print_slow("In this game, you are going to plan and control a mission to Mars. \n\n")
time.sleep(1) # delays for 1 seconds
print_slow("How many rockets do you want to launch? ")
rocketcount = int(input(""))
print('')
time.sleep(1) # delays for 1 seconds
print_slow("Cool.  %s rockets. \n" % rocketcount)
print_slow("The end. \n" % rocketcount)
