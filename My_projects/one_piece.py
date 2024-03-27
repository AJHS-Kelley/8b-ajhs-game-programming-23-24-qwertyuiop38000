print("Welcome to the One Piece calculator!")
print("This calculator will tel you how long you've spent watching One Piece and how long you have left.")
Name = input("What is your name?\n")
Char = input("What is your favorite crewmate of the Straw Hats? type the name as the crew calls them. For example, it wouldn't be roronoa zoro, it would be zoro as the crew calls him.\n")
Char = Char.lower()
if Char == "ussop":
    exit
elif Char == "nami":
    exit
elif Char == "robin":
    exit
elif Char == "franky":
    exit
elif Char == "jimbei":
    exit
elif Char == "luffy":
    exit
elif Char == "zoro":
    exit
elif Char == "sanji":
    exit
elif Char == "brook":
    exit
elif Char == "chopper":
    exit
else:
    print("You put the wrong name")
count = int(input("How many episodes have you watched?\n"))
skip = input("Do you skip the intro, recap, and the outro? Y for yes and N for no.\n")
if skip == "Y":
    skip = True
elif skip == "N":
    skip = False
else:
    print("invalid input")
    quit
episodeTime = 0
if skip == True:
    episodeTime = 20
else:
    episodeTime = 23
time = episodeTime * count
time_minutes = time%60
time_hours = int(time/60)
time_days = int(time_hours/24)
time_hours = time_hours - time_days * 24
print(f"you have watched for {time_days} days, {time_hours} hours, and {time_minutes} minutes.")
episodes = 1096
episodes_left = episodes - count
time2 = episodeTime * episodes_left
time_minutes2 = time2%60
time_hours2 = int(time2/60)
time_days2 = int(time_hours2/24)
time_hours2 = time_hours2 - time_days2 * 24
print(f"you have {time_days2} days left, {time_hours2} hours left, and {time_minutes2} minutes left.")
print(24 * 13)