#https://judge.softuni.org/Contests/Practice/Index/1658#1
rest = int(input())
availb_rest_m = 127
availb_work_m = 63
norm_m = 30000
work_d = 365 - rest
play_time_m = (work_d * 63) + (rest * 127)

if play_time_m > norm_m:
    z = play_time_m - norm_m
    x = z // 60
    y = z % 60
    print(f"Tom will run away\n{x} hours and {y} minutes more for play")

if play_time_m < norm_m:
    z = norm_m - play_time_m
    x = z // 60
    y = z %  60
    print(f"Tom sleeps well\n{x} hours and {y} minutes less for play")