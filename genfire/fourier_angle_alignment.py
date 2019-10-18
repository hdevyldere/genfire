import numpy as np

def slice( fft_space, Euler_angle_ranges):

    slice_errors = np.empty(Euler_angle_ranges.shape)

    for phi in Euler_angle_ranges[0]:
        for theta in Euler_angle_ranges[1]:
            for psi in Euler_angle_ranges[2]:
                rotate()
