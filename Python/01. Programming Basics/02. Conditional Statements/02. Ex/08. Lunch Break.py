# https://judge.softuni.org/Contests/Compete/Index/2414#7
import math

name_of_sitcom = str(input())
duration_of_sitcom = int(input())
duration_of_break = int(input())

time_for_lunch = duration_of_break / 8
time_for_relax = duration_of_break / 4

time = time_for_lunch + time_for_relax + duration_of_sitcom

if duration_of_break >= time:
    time_left = duration_of_break - time
    print(f"You have enough time to watch {name_of_sitcom} and left with {math.ceil(time_left)} minutes free time.")

elif duration_of_break < time:
    time_needed = time - duration_of_break
    print(f"You don't have enough time to watch {name_of_sitcom}, you need {math.ceil(time_needed)} more minutes.")