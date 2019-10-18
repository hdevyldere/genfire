import os
os.path.append('.','..')

import numpy as np
from opticaltomography.opticsutil import ImageRotation


def slice( fft_space, Euler_angle_ranges):

    slice_errors = np.empty(Euler_angle_ranges.shape)
    obj = ImageRotation(fft_space.shape, axis=0, pad=False, pad_value=0, flag_gpu_inout=False, flag_inplace=True)

    for phi in Euler_angle_ranges[0]:
        obj.axis = 0
        obj._rotate3D(fft_space,phi)
        for theta in Euler_angle_ranges[1]:
            obj.axis = 1
            obj._rotate3D(fft_space, theta)
            for psi in Euler_angle_ranges[2]:
                obj.axis = 0
                obj._rotate3D(fft_space, psi)

                error(obj,slice_errors,phi,theta,psi)


def error(obj,slice_errors,phi,theta,psi)
