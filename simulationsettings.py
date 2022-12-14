import numpy as np



G_FACTOR = 11 # 6... * 10 ** -G_FACTOR      #ISS Data, use with ODE
M = 1000000 #Planet Mass                    #5.972 * 10 ** 24
R = 3 #Planet Radius                        #6371000
r = 1 #Satellite height                     #473000

SCALE = 10**0 #How much to scale system down (i plot everything in range less than 10m, but calculating orbits in thousands of km)
VELOCITY = 6000 # speed, uncomment velocity below to use with PHYS
POSITION = np.array([4,0,0]) #used for PHYS, position of the sattelite (sphere visualizer radius is 3 units)

SOLVER = 'PHYS' 
#ODE : good big orbits, no info (используйтя для +- точного соотношения орбиты и земли)
#PHYS: VERY SLOW with big orbits, a lot of info (need to scale down simulation size like 10000km orbit radius -> 10m orbit radius so there are not a lot of calculations)



#///OPTIONS FOR PHYS SOLVER///#
# UNCOMMENT WHAT IS COMMENTED WITH """ AND CHANGE ONLY WHEN PHYS SOLVER IS SELECTED
VELOCITY = np.array([0,0.05,0.02], dtype=np.float32)

#recomendations: PHYS - R = 3, r >= 1, M +- = 100000, поиграйтесь с массой, сложно угадать нужные значения
#                ODE : Leave as is
