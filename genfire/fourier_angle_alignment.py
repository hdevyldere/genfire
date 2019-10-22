import os
os.path.append('.','..')

import numpy as np
from opticaltomography.opticsutil import ImageRotation


def slice( fft_space, orig_Euler_angle, projection, Euler_angle_ranges):

    # Create an empty array for the errors to be stored
    slice_errors = np.empty(Euler_angle_ranges.shape)
    middle = np.floor(obj.shape[0] / 2)

    # Initialize an ImageRotation object
    obj = ImageRotation(fft_space.shape, axis=0, pad=False, pad_value=0, flag_gpu_inout=False, flag_inplace=True)

    # Rotate to approx. starting angle of incoming projections
    obj._rotate3D(fft_space,orig_Euler_angles[0])
    obj.axis = 1
    obj._rotate3D(fft_space,orig_Euler_angles[1])
    obj.axis = 2
    obj._rotate3D(fft_space,orig_Euler_angles[2])

    for phi in Euler_angle_ranges[0]:
        obj.axis = 0
        obj._rotate3D(fft_space,phi)
        for theta in Euler_angle_ranges[1]:
            obj.axis = 1
            obj._rotate3D(fft_space, theta)
            for psi in Euler_angle_ranges[2]:
                obj.axis = 0
                obj._rotate3D(fft_space, psi)

                error(obj,projection,slice_errors,middle,phi,theta,psi)


def error(obj,projection,slice_errors,middle,phi,theta,psi):
    slice_errors(phi,theta,psi) = np.sum(np.abs(bj[middle,:,:] - projection)) # Way too simple of a error measurement
    return slice_errors
