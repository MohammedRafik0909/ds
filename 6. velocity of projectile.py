import numpy as np
time = np.array([0,1,2,3,4])
vert_pos = np.array([0,15,25,50,75])

time_diff = np.diff(time)
vert_diff = np.diff(vert_pos)
vel =  vert_diff/time_diff
print("time interval :",time)
print("\nVertical posistion :",vert_pos)
print("\nchange in time:",time_diff)
print("\nchange in vertical posistion:",vert_diff)
print("\n average velocity:",vel)
