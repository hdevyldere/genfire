import numpy as np
import matplotlib.pyplot as plt

def create_obj():
    shape = [101,101,101]
    obj = np.zeros(shape,int16)

    shape2 = [51,51,51]
    obj2 = np.ones(shape2,int16)
    obj2[9:40,9:40,:] = 0
    obj2[9:40,:,9:40] = 0
    obj2[:,9:40,9:40] = 0
    obj2[25,0:25,25] = 1

    obj[24:75,24:24:75] = obj2

    return obj

