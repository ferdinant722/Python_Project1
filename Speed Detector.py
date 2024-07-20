def check_speed(speed):
    speed_limit = 70
    demerit_point_threshold = 5
    suspension_points = 12

    if speed <= speed_limit:
        print("Ok")
    else:
        demerit_points = (speed - speed_limit) 
        if demerit_points > suspension_points:
            print("License suspended")
        else:
            print(f"Points: {demerit_points}")

try:
    speed = int(input('Enter speed: '))
    check_speed(speed)
except ValueError:
    print("Please enter a valid speed as an integer.")