# importing time module
import time

# creating rate_rhythm method with the main logic
def rate_rhythm(target_time, actual_time):
    """calculating difference between user input rhythms , using target and actual time and giving """
    difference = abs((target_time - actual_time) / actual_time) * 100
    if difference <= 8:
        return "Great!"
    elif difference <= 16:
        return "Okay!"
    else:
        return "Miss!"

# now the system will get data about how many rounds and seconds, system should run
# speed variable holds the value of seconds user tests their speed
while True:
    try:
        speed = int(input("Choose rhythm speed (1, 2 or 3): "))
        # checking if the user input is 1,2 or 3
        if speed == 1 or speed == 2 or speed == 3:
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3")
    # handles the exception if user enters string
    except ValueError:
        print("Invalid choice. Enter 1, 2 or 3")

#round variable holds the count of rounds user want to try
while True:
    try:
        rounds = int(input("Chose number of rounds (5 to 50): "))
        # check if the user input is between 5 and 50
        if 5 <= rounds <= 50:
            break
        else:
            print("Please enter an integer between 1 and 50!")
    # this exception will handle the error if user inputs string as input
    except ValueError:
        print("Please enter an integer as count of rounds")

# displaying user about the game using their inputs
print(f"Okay, this test will last {rounds} rounds and you are aiming for a {speed} second rhythm.")

# creating an empty array to store user input times
listOfInputs = []

input("press enter to begin")

# record the time of starting first round using time library
startTime = time.time()

for currentRound in range(1, rounds + 1):
    # display user the number of rounds
    print(f"Round {currentRound} of {rounds}")
    input("press enter to record")
    # recording the current time when user inputs enter
    currentTime= time.time()
    # measuring rhythm of the round using the difference between startTime and currentTime
    # round the value to two decimal values
    rhythmTime = round(currentTime - startTime, 2)
    # getting the result of rhythm using rate_rhythm function
    roundResult = rate_rhythm(speed, rhythmTime)
    # display results of the current round
    print(f"{rhythmTime}s - {roundResult}\n")
    # append(insert) results data into the list
    listOfInputs.append(rhythmTime)
    # updating the value of starting time of the next iteration
    startTime = time.time()

# this part will display once user enters click
input("Test complete! Press enter to see your results.")

# updating variable values using minimum, maximum and average values of the list
minimumRhythm = min(listOfInputs)
averageRhythm = sum(listOfInputs) / len(listOfInputs)
maximumRhythm = max(listOfInputs)

# displaying user the details about response times
print("\nResults:")
print(f"  Fastest Response: {round(minimumRhythm, 2)} {rate_rhythm(speed,minimumRhythm)}")
print(f"  average Response: {round(averageRhythm, 2)} {rate_rhythm(speed,averageRhythm)}")
print(f"  slowest Response: {round(maximumRhythm, 2)} {rate_rhythm(speed,maximumRhythm)} \n")

print("All Results: ")

# display all the response time in table
print(f"{'Round':<6} {'Response':<10} {'Difference':<15}")
print(f"{'-' * 5:<6} {'-' * 8:<10} {'-' * 11:<15}")
for roundNumber, roundResponseTime in enumerate(listOfInputs):
    # getting the difference between actual time and user given time and rounding it to 2 decimal values
    rhythmDiff = round(abs(roundResponseTime - speed),2)
    if roundResponseTime < speed:
        message = f"{rhythmDiff} early"
    elif roundResponseTime > speed:
        message = f"{rhythmDiff} late"
    else:
        message ="spot on"
    # printing out each attempt with time in the table
    print(f"{roundNumber:<6} {roundResponseTime:<10.2f} {message:<15}")

print("\n---Thank you for using Rhythm Tester---")