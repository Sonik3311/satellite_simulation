import numpy as np

SOLVER = 'ODE'
#ODE : good big orbits, no info (good for real world satellites)
#PHYS: VERY SLOW with big orbits, lots of info (good for messing around)

G_FACTOR = 11 #don't touch
if SOLVER == "ODE":
    #Change if your solver is ODE
    M = 5.972 * 10**24 # Planet Mass
    R = 6371000 # Planet radius
    r = 437 * 10**3 #satellite height
    SCALE = 11.25**6 #How much shold the simulation be scaled down (x/scale = point in 10m range from center)
    VELOCITY = 7654 #Satellite speed
    
    POSITION = 1 # isn't used by ODE solver
    ATMOSPHERE = 10  # isn't used by ODE solver
    A_DENSITY = 1 # isn't used by ODE solver
    LOOP_STOP = False # isn't used by ODE solver
else:
    #Change if your solver is PHYS
    M = 10000 # planet mass
    R = 3 #don't touch, causes visual bugs if you change it
    VELOCITY = np.array([0.00,0.0045,0.00], dtype=np.float32) # satellite initial velocity
    POSITION = np.array([4,0,0]) # satellite initial position
    ATMOSPHERE = 1 # atmosphere height
    A_DENSITY = 0.0 # the density of the athmosphere
    LOOP_STOP = True # Should solver stop calculations when the satellite completed a full loop? (turn off when atmosphere is enabled)

    SCALE = 1 # isn't used by PHYS solver
    r = 1 # isn't used by PHYS solver


