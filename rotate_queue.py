import numpy as np

def rotate_2d_point(point, angle_x, angle_y):
    rotation_x = np.array([np.cos(angle_x),-np.sin(angle_x)[np.sin(angle_x), np.cos(angle_x)]])
    rotation_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                           [0, 1],
                           [-np.sin(angle_y), 0, np.cos(angle_y)]])
    return rotation_y @ rotation_x @ point