import sys
sys.path.append('/home/hannah/repos/PhaseContrastTomographySolver')

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import operators as op
from utilities import ImageRotation

obj = np.load('test_obj.npy').astype('float')
obj = torch.from_numpy(obj)
phi = np.linspace(-10,10,4)
Euangranges = [phi,phi,phi]

def slice( fft_space, orig_Euler_angle, Euler_angle_ranges):

    # Create an empty array for the errors to be stored
    #slice_errors = np.empty(Euler_angle_ranges.shape)
    #initialize object
    # middle = np.floor(obj_rot.dim[0] / 2)
    obj = fft_space
    if obj is None:
        obj = op.r2c(torch.zeros(fft_space.shape).cuda())
    else:
        if not obj.is_cuda:
            obj = obj.cuda()
        if len(obj.shape) == 3:
            obj = op.r2c(obj)

    # Initialize an ImageRotation object
    obj_rotation = ImageRotation(obj.shape, axis=0, pad=False, pad_value=0, dtype = torch.float32, device = torch.device('cuda'))

    # Rotate to approx. starting angle of incoming projections
    obj = obj_rotation.forward(obj,orig_Euler_angle[0])
    obj_rotation.axis = 1
    obj = obj_rotation.forward(obj,orig_Euler_angle[1])
    obj_rotation.axis = 2
    obj = obj_rotation.forward(obj,orig_Euler_angle[2])

    phi0, theta0, psi0 = [0,0,0]
    for phi in Euler_angle_ranges[0]:
        obj_rotation.axis = 0
        obj = obj_rotation.forward(obj, phi - phi0 )
        phi0 = phi
        for theta in Euler_angle_ranges[1]:
            obj_rotation.axis = 1
            obj = obj_rotation.forward(obj, theta - theta0 )
            theta0 = theta
            for psi in Euler_angle_ranges[2]:
                obj_rotation.axis = 0
                obj = obj_rotation.forward(obj, psi - psi0 )
                psi0 = psi
                show_obj(obj)

               # error(obj,projection,slice_errors,middle,phi,theta,psi)


def error(obj,projection,slice_errors,middle,phi,theta,psi):
    slice_errors[phi,theta,psi] = np.sum(np.abs(bj[middle,:,:] - projection)) # Way too simple of a error measurement
    return slice_errors

def show_obj(obj):
    plt.figure()
    print(obj.shape)
    objj = obj.cpu()
    print(objj.shape)
    objj = objj.numpy()
    plt.imshow(objj.mean(axis=2))
    plt.show()

