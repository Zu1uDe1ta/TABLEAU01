

# 6.2.1: Print functions.

def print_points(name, age, total_points):
    print('{} is {}'.format(name, age))
    print('{} made {} points'.format(name, total_points))

user_name = 'Sam'
user_age = 22
regular_time_points = 22
overtime_points = 5

print_points(user_name, user_age, regular_time_points + overtime_points)