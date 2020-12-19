# https://www.codewars.com/kata/56484848ba95170a8000004d/train/python

def gps(s, x):
    velocities = []
    for dist_stamp in range(1, len(x)):
        if (x[dist_stamp] - x[dist_stamp - 1] <= 1):
            velocities.append(0)
        velocities.append(((x[dist_stamp] - x[dist_stamp - 1]) * 3600) / s)

    max = 0
    for vel in velocities:
        if (vel > max):
            max = vel
    return max // 1


