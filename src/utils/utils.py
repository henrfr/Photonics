import numpy as np

def rot(angle):
    return np.asarray([[np.cos(angle), -np.sin(angle)],
                       [np.sin(angle), np.cos(angle)]])

def rotate_vector(vec, angle):
    return np.matmul(rot(angle), vec)

def rotate_matrix(mat, angle):
    return np.round(np.matmul(rot(-angle), np.matmul(mat, rot(angle))), decimals=4)   

class LinearPolarization():
    
    def __init__(self, angle=0):
        self.jones = np.array([1,0])

        if angle:
            self.jones = rotate_vector(self.jones, angle)

    def get_angle_to_x_axis(self):
        if not self.jones[1]:
            return 0
        else:
            return np.arctan(self.jones[0]/self.jones[1])

    def get_jones_vector(self):
        return self.jones

class QuarterWavePlate():

    def __init__(self, angle=0):
        self.angle = angle
        self.jones = np.asarray([[1, 0],
                                 [0, 1j]])
        
        if angle:
            self.jones = rotate_matrix(self.jones, angle)
    def get_jones_vector(self):
        return self.jones

class LinearPolarizer():

    def __init__(self, angle=0):
        self.angle = angle
        self.jones = np.asarray([1,0])

        if angle:
            self.jones = rotate_vector(self.jones, angle)

